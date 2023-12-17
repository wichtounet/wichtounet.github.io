In the last few months, I have been working on refreshing my Expression Templates Library (ETL) project with modern
C++. I am happy to report that I have now finished the refresh. It took me longer than I expected and I also had less
time than I expected. But I am very happy about the result. 

The main change in etl is the use of concepts. Expression Templates are making heavy use of SFINAE. And I was able to
replace every single usage of SFINAE with concepts. I was also able to replace many assertions with concepts instead. 

In most cases, I am using concepts instead of the `typename` declaration. For instance

.. code:: cpp

	template <typename A, typename M, cpp_enable_iff(is_4d<A>)>
	static void apply(A&& in, M&& m, size_t c1, size_t c2, size_t c3) {

becomes

.. code:: cpp

	template <etl_4d A, typename M>
	static void apply(A&& in, M&& m, size_t c1, size_t c2, size_t c3) {

This makes the declaration much simpler to read. In some cases, I had to use `requires`. For instance, here is the old definition of sub_view: 

.. code:: cpp

	template <typename T, bool Aligned>
	struct sub_view<T, Aligned, std::enable_if_t<!fast_sub_view_able<T>>> final {

and here is the new one: 

.. code:: cpp

	template <typename T, bool Aligned>
	requires(!fast_sub_view_able<T>)
	struct sub_view<T, Aligned> final {

This also explains the requirements much better than using SFINAE. In most cases, concepts should be faster to compile
than the old enable-if stuff. However, I have not yet had time to measure that.

I also made many small cleanups to the code, but they are probably not worth discussing. 

AVX-512
-------

What is worth discussing is that I finally added support for AVX-512 into etl. Before, I was waiting until Intel would
give AVX-512F support to desktop CPU, but this is still not the case unfortunately. So I rented a VPS with AVX-512F
support. 

AVX512-F is able to process 512b vector operations at once, twice more than AVX-2. This makes it twice faster in theory.
I have completed the support in etl and did some extra testing as well. I wish I had a machine where to test that on
a regular basis (the VPS is pretty expensive to keep running). If I start working a lot on this project again, I will
consider having a Xeon CPU at hone.

FP16 and BF16
-------------

Another thing I had been wanting to work on for many years is FP16 operations on GPU. FP16 is a floating point type with
only 16b instead of the standard 32b for `float`. With my new computer and new versions of CUDA, I now got a working
system to do FP16. 

So, I implemented support for many FP16 operations on my `etl-gpu-blas` project that is used by `etl` to provide GPU
operations. Thanks to operator overloading in CUDA, there is really nothing complicated about doing that.

Doing so, I also added support for BF16. This is another half-precision floating point type, but the mantissa and
exponent part are different, apparently better tuned for machine learning. The support is more or less the same in CUDA,
only a different type.

Currently, it is only used in etl-gpu-blas, not yet in DLL. Indeed, the problem with FP16 and BF16 is that there is no
CPU support, so it is not as easy to use. I plan to improve that support in the future so that I can use it on DLL
without even going to the CPU.

Next steps
----------

Another thing I want to explore in the future is FP8, which is a quarter-precision floating point. However, FP8 can only
be used for some tensor operations, through the use of tensor cores. So, I will likely only use it through CUDNN
for convolution operations.

Finally, I also want to explore INT8 for neural networks. INT8 is easy to do on both CPU and GPU, but you cannot replace
all types in a neural network with INT8, a certain level of quantization is necessary and storage should still be done
in INT16 and INT32. But, that's not for tomorrow.

The next immediate projec is to refresh the code of dll, with C++23. Then, I want to run some more benchmarks and see
what are my next steps to make dll faster on CPU and GPU.
