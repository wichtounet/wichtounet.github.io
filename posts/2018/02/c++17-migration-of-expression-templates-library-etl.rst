I've finally decided to migrate my Expression Templates Library (ETL) project to
C++17. I've talking about doing that for a long time and I've released several
releases without doing the change, but the next version will be a C++17 library.
The reason why I didn't want to rush the change was that this means the library
needs a very recent compiler that may not be available to everybody. Indeed,
after this change, the ETL library now needs at least GCC 7.1 or Clang 4.0.

I've already made some previous experiments in the past. For instance,
`by using if constexpr, I've managed to speed up compilation by 38% <https://baptiste-wicht.com/posts/2017/09/how-i-made-deep-learning-library-38-faster-to-compile-optimization-and-cpp17-if-constexpr.html>`_ and I've also written an article about `the fold expressions introduced in C++17 <https://baptiste-wicht.com/posts/2015/05/cpp17-fold-expressions.html>`_. But I haven't migrated a full library yet. This is now done with ETL. In this article, I'll try to give some example of improvements by using C++17.

This will only cover the C++17 features I'm using in the updated ETL library,
I won't cover all of the new C++17 features.

if constexpr
############

The most exciting new thing in C++17 for me is the :code:`if constexpr`
statement. This is a really really great thing. In essence, it's a normal
:code:`if` statement, but with one very important difference. The statement that
is not taken (the :code:`else` if the condition is true, or the :code:`if
constexpr` if the condition is false) is *discarded*. And what is interesting
is what happens to *discarded* statements:

1) The body of a *discarded* statement does not participate in return type
   deduction.
2) The discarded statement is not instantiated
3) The discarded statement can *odr-use* a variable that is not defined

Personally, I'm especially interested by points 1 and 2. Let's start with an
example where point 1 is useful. In ETL, I have a make_temporary function. This
function either forwards an ETL container or creates a temporary container from
an ETL expression. This is based on a compile-time traits. The return type of
the function is the not the same in both cases. What you did in those case
before C++17, is use SFINAE and make two functions:

.. code:: cpp

    template <typename E, cpp_enable_iff(is_dma<E>)>
    decltype(auto) make_temporary(E&& expr) {
        return std::forward<E>(expr);
    }

    template <typename E, cpp_enable_iff(!is_dma<E>)>
    decltype(auto) make_temporary(E&& expr) {
        return force_temporary(std::forward<E>(expr));
    }

One version of the function will forward and the other version will force
a temporary and the return type can be different since these are two different
functions. This is not bad, but still requires two functions where you only want
to write one. However, in C++17, we can do much better using :code:`if constexpr`:

.. code:: cpp

    template <typename E>
    decltype(auto) make_temporary(E&& expr) {
        if constexpr (is_dma<E>) {
            return std::forward<E>(expr);
        } else {
            return force_temporary(std::forward<E>(expr));
        }
    }

I think this version is really superior to the previous one. We only have one
function and the logic is much clearer!

Let's now see an advantage of the point 2. In ETL, there are two kinds of
matrices, matrices with compile-time dimensions (fast matrices) and matrices
with runtime dimensions (dynamic matrices). When they are used, for instance for
a matrix-multiplication, I use static assertions for fast matrices and runtime
assertions for dynamic matrices. Here is an example for the validation of the
matrix-matrix multiplication:

.. code:: cpp

    template <typename C, cpp_disable_iff(all_fast<A, B, C>)>
    static void check(const A& a, const B& b, const C& c) {
        static_assert(all_2d<A,B,C>, "Matrix multiplication needs matrices");
        cpp_assert(
            dim<1>(a) == dim<0>(b)         //interior dimensions
                && dim<0>(a) == dim<0>(c)  //exterior dimension 1
                && dim<1>(b) == dim<1>(c), //exterior dimension 2
            "Invalid sizes for multiplication");
        cpp_unused(a);
        cpp_unused(b);
        cpp_unused(c);
    }

    template <typename C, cpp_enable_iff(all_fast<A, B, C>)>
    static void check(const A& a, const B& b, const C& c) {
        static_assert(all_2d<A,B,C>, "Matrix multiplication needs matrices");
        static_assert(
            dim<1, A>() == dim<0, B>()         //interior dimensions
                && dim<0, A>() == dim<0, C>()  //exterior dimension 1
                && dim<1, B>() == dim<1, C>(), //exterior dimension 2
            "Invalid sizes for multiplication");
        cpp_unused(a);
        cpp_unused(b);
        cpp_unused(c);
    }

Again, we use SFINAE to distinguish the two different cases. In that case, we
cannot use a normal :code:`if` since the value of the dimensions cannot be taken
at compile-time for dynamic matrices, more precisely, some templates cannot be
instantiated for dynamic matrices. As for the cpp_unused, we have to use for the
static version because we don't use them and for the dynamic version because
they won't be used if the assertions are not enabled. Let's use :code:`if constexpr` to avoid having two functions:

.. code:: cpp

    template <typename C>
    static void check(const A& a, const B& b, const C& c) {
        static_assert(all_2d<A,B,C>, "Matrix multiplication needs matrices");

        if constexpr (all_fast<A, B, C>) {
            static_assert(dim<1, A>() == dim<0, B>()         //interior dimensions
                              && dim<0, A>() == dim<0, C>()  //exterior dimension 1
                              && dim<1, B>() == dim<1, C>(), //exterior dimension 2
                          "Invalid sizes for multiplication");
        } else {
            cpp_assert(dim<1>(a) == dim<0>(b)         //interior dimensions
                           && dim<0>(a) == dim<0>(c)  //exterior dimension 1
                           && dim<1>(b) == dim<1>(c), //exterior dimension 2
                       "Invalid sizes for multiplication");
        }

        cpp_unused(a);
        cpp_unused(b);
        cpp_unused(c);
    }

Since the *discarded* won't be instantiated, we can now use a single function!
We also avoid some duplications of the first static assertion of the unused
statements. Pretty great, right ? But we can do better with C++17. Indeed, it
added a nice new attribute :code:`[[maybe_unused]]`. Let's see what this gives
us:

.. code:: cpp

    template <typename C>
    static void check([[maybe_unused]] const A& a, [[maybe_unused]] const B& b, [[maybe_unused]] const C& c) {
        static_assert(all_2d<A,B,C>, "Matrix multiplication needs matrices");

        if constexpr (all_fast<A, B, C>) {
            static_assert(dim<1, A>() == dim<0, B>()         //interior dimensions
                              && dim<0, A>() == dim<0, C>()  //exterior dimension 1
                              && dim<1, B>() == dim<1, C>(), //exterior dimension 2
                          "Invalid sizes for multiplication");
        } else {
            cpp_assert(dim<1>(a) == dim<0>(b)         //interior dimensions
                           && dim<0>(a) == dim<0>(c)  //exterior dimension 1
                           && dim<1>(b) == dim<1>(c), //exterior dimension 2
                       "Invalid sizes for multiplication");
        }
    }

No more need for :code:`cpp_unused` trick :) This attribute tells the compiler
that a variable or parameter can be sometimes unused and therefore does not lead
to a warning for it. Only one thing that is not great with this attribute is
that it's too long, 16 characters. It almost double the width of my check
function signature. Imagine if you have more parameters, you'll soon have to use
several lines. I wish there was a way to set an attribute for all parameters
together or a shortcut. I'm considering whether to use a short macro to use in
place of it, but haven't yet decided.

Just a note, if you have :code:`else if` statements, you need to set them as
:code:`constexpr` as well! This was a bit weird for me, but you can figure it as
if the condition is :code:`constexpr`, then the :code:`if` (or :code:`else if`)
is :code:`constexpr` as well.

Overall, I'm really satisfied with the new `if constexpr`! This really makes the
code much nicer in many cases, especially if you abuse metaprogramming like
I do.

You may remember that I've `coded a version of static if in the past with C++14 <https://baptiste-wicht.com/posts/2015/07/simulate-static_if-with-c11c14.html>`_ in the past. This was able to solve point 2, but not point 1 and was much uglier. Now we have a good solution to it. I've replaced two of these in the current code with the new :code:`if constexpr`.

Fold expressions
################

For me, fold expressions is the second major feature of C++17. I wont' go into
too much details here, since
`I've already talked about fold expression in the past <https://baptiste-wicht.com/posts/2015/05/cpp17-fold-expressions.html>`_
. But I'll show two examples of refactorings I've been able to do with this.

Here was the size() function of a static matrix in ETL before:

.. code:: cpp

    static constexpr size_t size() {
       return mul_all<Dims...>;
    }

The Dims parameter pack from the declaration of fast_matrix:

.. code:: cpp

    template <typename T, typename ST, order SO, size_t... Dims>
    struct fast_matrix_impl;

And the mul_all is a simple helper that multiplies each value of the variadic
parameter pack:

.. code:: cpp

    template <size_t F, size_t... Dims>
    struct mul_all_impl final : std::integral_constant<size_t, F * mul_all_impl<Dims...>::value> {};

    template <size_t F>
    struct mul_all_impl<F> final : std::integral_constant<size_t, F> {};

    template <size_t F, size_t... Dims>
    constexpr size_t mul_all = mul_all_impl<F, Dims...>::value;

Before C++17, the only way to compute this result at compilation time was to use
template recursion, either with types or with constexpr functions. I think this
is pretty heavy only for doing a multiplication sum. Now, with fold expressions,
we can manipulate the parameter pack directly and rewrite our size function:

.. code:: cpp

    static constexpr size_t size() {
        return (Dims * ...);
    }

This is much better! This clearly states that each value of the parameter should
be multiplied together. For instance :code:`1,2,3` will become :code:`(1*2)*3`.

Another place where I was using this was to code a traits that tests if a set of
boolean are all true at compilation-time:

.. code:: cpp

    template <bool... B>
    constexpr bool and_v = std::is_same<
        cpp::tmp_detail::bool_list<true, B...>,
        cpp::tmp_detail::bool_list<B..., true>>::value;

I was using a nice trick here to test if all booleans are true. I don't remember
where I picked it up, but it's quite nice and very fast to compile.

This was used for instance to test that a set of expressions are all
single-precision floating points:

.. code:: cpp

    template <typename... E>
    constexpr bool all_single_precision = and_v<(is_single_precision<E>)...>;

Now, we can get rid of the and_v traits and use directly the parameter pack
directly:

.. code:: cpp

    template <typename... E>
    constexpr bool all_single_precision = (is_single_precision<E> && ...);

I think using fold expressions results in much clearer syntax and better code
and it's a pretty nice feature overall :)

As a note here, I'd like to mention, that you can also use this syntax to call
a function on each argument that you have, which makes for much nicer syntax as
well and I'll be using that in DLL once I migrate it to C++17.

Miscellaneous
#############

There are also a few more C++17 features that I've used to improve ETL, but that
have a bit less impact.

A very nice feature of C++17 is the support for structured bindings. Often you
end up with a function that returns several parts of information in the form of
a pair or a tuple or even a fixed-size array. You can use an object for this,
but if you don't, you end up with code that is not terribly nice:

.. code:: cpp

    size_t index;
    bool result;
    float alpha;
    std::tie(index, result, alpha) = my_function();

It's not terribly bad, but in these cases, you should be be hoping for something
better. With c++17, you can do better:

.. code:: cpp

    auto [index, result, alpha] = my_function();

Now you can directly use auto to deduce the types of the three variables at once
and you can get all the results in the variables at once as well :) I think this
is really nice and can really profit some projects. In ETL, I've almost no use
for this, but I'm going to be using that a bit more in DLL.

Something really nice to clean up the code in C++17 is the ability to declared
nested namespaces in one line. Before, you have a nested namespace
etl::impl::standard for instance, you would do:

.. code:: cpp

    namespace etl {
    namespace impl {
    namespace standard {

    // Someting inside etl::impl::standard

    } // end of namespace standard
    } // end of namespace impl
    } // end of namespace etl

In C++17, you can do:

.. code:: cpp

    namespace etl::impl::standard {

    // Someting inside etl::impl::standard

    } // end of namespace etl::impl::standard

I think it's pretty neat :)

Another very small change is the ability to use the typename keyword in place of
the class keyword when declaring template template parameters. Before, you had
to declare:

.. code:: cpp

    template <template <typename> class X>

now you can also use:

.. code:: cpp

    template <template <typename> typename X>

It's just some syntactic sugar, but I think it's quite nice.

The last improvement that I want to talk about is one that probably very few
know about but it's pretty neat. Since C++11, you can use the :code:`alignas(X)`
specifier for types and objects to specify on how many bytes you want to align
these. This is pretty nice if you want to align on the stack. However, this
won't always work for dynamic memory allocation. Imagine this struct:

.. code:: cpp

    struct alignas(128)  test_struct  { char data; };

If you declare an object of this type on the stack, you have the guarantee that
it will be aligned on 128 bytes. However, if you use :code:`new` to allocate it
on the heap, you don't have such guarantee. Indeed, the problem is that 128 is
greater than the maximum default alignment. This is called an over-aligned type.
In such cases, the result will be aligned on the max alignment of your system.
Since C++17, :code:`new` supports aligned dynamic memory allocation of
over-aligned types. Therefore, you can use a simple :code:`alignas` to allocate
dynamic over-aligned types :) I need this in ETL for matrices that need to be
aligned for vectorized code. Before, I was using a larger array with some
padding in order to find an aligned element inside, but that is not very nice,
now the code is much better.

Compilation Time
################

I've done a few tests to see how much impact these news features have on
compilation time. Here, I'm doing benchmark on compiling the entire test suite
in different compilation mode, I enabled most compilation options (all GPU and
BLAS options in order to make sure almost all of the library is compiled).

Since I'm a bit short on time before going to vacation, I've only gathered the
results with g++. Here are the results with G++ 7.2.0

+------------+-------+---------+---------------+
|            | debug | release | release_debug |
+------------+-------+---------+---------------+
| C++14      | 862s  | 1961s   | 1718s         |
+------------+-------+---------+---------------+
| C++17      | 892s  | 2018s   | 1745s         |
+------------+-------+---------+---------------+
| Difference | +3.4% | +2.9%   | +1.5%         |
+------------+-------+---------+---------------+

Overall, I'm a bit disappointed by these results, it's around 3% slower to
compile the C++17 version than the C++14 version. I was thinking that this would
a least be as fast to compile as before. It seems that currently with G++ 7.2,
:code:`if constexpr` are slower to compile than the equivalent SFINAE functions.
I didn't do individual benchmarks of all the features I've migrated, therefore,
it may not be coming from :code:`if constexpr`, but since it's the greatest
change by far, it's the more likely candidate. Once I'll have a little more
time, after my vacations, I'll try to see if that is also the case with clang.

Keep in mind that we are compiling the test suite here. The ETL test suite is
using the manual selection mode of the library in order to be able to test all
the possible implementations of each operation. This makes a considerable
difference in performance. I expect better compilation time when this is used in
automatic selection mode (the default mode). In the default mode, a lot more
code can be disabled with :code:`if constexpr`. I will test this next with the
DLL library which I will also migrate to C++17.

Conclusion
##########

This concludes this report on the migration of my ETL library from C++14 to
C++17. Overall, I'm really satisfied with the improvement of the code, it's much
better. I'm a bit disappointed by the slight increase  (around 3%) in
compilation time, but it's not dramatic either. I'm still hoping that once it's
used in DLL, I will see a decrease in compilation, but we'll see that when I'll
be done with the migration of DLL to C++17 which may take some time since I'll
have two weeks vacation in China starting Friday.

The new version is available only through the *master* branch. It will be
released as the 1.3 version probably when I integrate some new features, but in
itself will not be released as new version. You can take a look in the
`Github etl repository <https://github.com/wichtounet/etl>`_ if you are interested.
