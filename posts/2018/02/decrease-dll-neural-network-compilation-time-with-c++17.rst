Just last week, `I've migrated my Expression Templates Library (ETL) library to C++17 <https://baptiste-wicht.com/posts/2018/02/c%2B%2B17-migration-of-expression-templates-library-etl.html>`_,
it is now also done in my Deep Learning Library (DLL) library. In ETL, this
resulted in a *much nicer code overall*, but no real improvement in compilation
time.

The objective of the migration of DLL was two-fold. First, I also wanted to
simplify some code, especially with :code:`if constexpr`. But I also especially
wanted to try to reduce the compilation time. In the past,
`I've already tried a few changes with C++17 <https://baptiste-wicht.com/posts/2017/09/how-i-made-deep-learning-library-38-faster-to-compile-optimization-and-cpp17-if-constexpr.html>`_, with good results on the compilation of the entire test suite.
While this is very good, this is not very representative of users of the library.
Indeed, normally you'll have only one network in your source file not several.
The new changes will especially help in the case of many networks, but less in
the case of a single network per source file.

This time, I decided to test the compilation on the examples. I've tested the
eight official examples from the DLL library:

0) mnist_dbn: A fully-connected Deep Belief Network (DBN) on the MNIST data set
   with three layers
1) char_cnn: A special CNN with embeddings and merge and group layers for text
   recognition
2) imagenet_cnn: A 12 layers Convolutional Neural Network (CNN) for Imagenet
3) mnist_ae: A simple two-layers auto-encoder for MNIST
4) mnist_cnn: A simple 6 layers CNN for MNIST
5) mnist_deep_ae: A deep auto-encoder for MNIST, only fully-connected
6) mnist_lstm: A Recurrent Neural Network (RNN) with Long Short Term Memory
   (LSTM) cells
7) mnist_mlp: A simple fully-connected network for MNIST, with dropout
8) mnist_rnn: A simple RNN with simple cells for MNIST

This is really representative of what users can do with the library and I think
it's a much better for compilation time.

For reference, you can find `the source code of all the examples online <https://github.com/wichtounet/dll/tree/master/examples/src>`_.

Results
+++++++

Let's start with the results. I've tested this at different stages of the
migration with clang 5 and GCC 7.2. I tested the following steps:

1) The original C++14 version
2) Simply compiling in c++17 mode (-std=c++17)
3) Using the C++17 version of the ETL library
4) Upgrading DLL to C++17 (without ETL)
5) ETL and DLL in C++17 versions

I've compiled each example independently in release_debug mode. Here are the
results for G++ 7.2:

.. table::
    :align: center

    +-------------------+--------+--------+--------+--------+--------+--------+--------+--------+--------+
    | Example           |    0   | 1      | 2      | 3      | 4      | 5      | 6      | 7      | 8      |
    +===================+========+========+========+========+========+========+========+========+========+
    | C++14             | 37.818 | 32.944 | 33.511 | 15.403 | 29.998 | 16.911 | 24.745 | 18.974 | 19.006 |
    +-------------------+--------+--------+--------+--------+--------+--------+--------+--------+--------+
    | -std=c++17        | 38.358 | 32.409 | 32.707 | 15.810 | 30.042 | 16.896 | 24.635 | 19.134 | 19.027 |
    +-------------------+--------+--------+--------+--------+--------+--------+--------+--------+--------+
    | ETL C++17         | 36.045 | 31.000 | 30.942 | 15.322 | 28.840 | 16.747 | 24.151 | 18.208 | 18.939 |
    +-------------------+--------+--------+--------+--------+--------+--------+--------+--------+--------+
    | DLL C++17         | 35.251 | 32.577 | 32.854 | 15.653 | 29.758 | 16.851 | 24.606 | 19.098 | 19.146 |
    +-------------------+--------+--------+--------+--------+--------+--------+--------+--------+--------+
    | Final C++17       | 32.289 | 31.133 | 30.939 | 15.232 | 28.753 | 16.526 | 24.326 | 18.116 | 17.819 |
    +-------------------+--------+--------+--------+--------+--------+--------+--------+--------+--------+
    | Final Improvement | 14.62% | 5.49%  | 7.67%  | 1.11%  | 4.15%  | 2.27%  | 1.69%  | 4.52%  | 6.24%  |
    +-------------------+--------+--------+--------+--------+--------+--------+--------+--------+--------+

The difference by just enabling c++17 is not significant. On the other hand,
some significant gain can be obtained by using the C++17 version of ETL,
especially for the DBN version and for the CNN versions. Except for the DBN
case, the migration of DLL to C++17 did not bring any significant advantage.
When everything is combined, the gains are more important :) In the best case,
the example is 14.6% faster to compile.

Let's see if it's the same with clang++ 5.0:

.. table::
    :align: center

    +-------------------+--------+--------+--------+--------+--------+--------+--------+--------+--------+
    | Example           | 0      | 1      | 2      | 3      | 4      | 5      | 6      | 7      | 8      |
    +===================+========+========+========+========+========+========+========+========+========+
    | C++14             | 40.690 | 34.753 | 35.488 | 16.146 | 31.926 | 17.708 | 29.806 | 19.207 | 20.858 |
    +-------------------+--------+--------+--------+--------+--------+--------+--------+--------+--------+
    | -std=c++17        | 40.502 | 34.664 | 34.990 | 16.027 | 31.510 | 17.630 | 29.465 | 19.161 | 20.860 |
    +-------------------+--------+--------+--------+--------+--------+--------+--------+--------+--------+
    | ETL C++17         | 37.386 | 33.008 | 33.896 | 15.519 | 30.269 | 16.995 | 28.897 | 18.383 | 19.809 |
    +-------------------+--------+--------+--------+--------+--------+--------+--------+--------+--------+
    | DLL C++17         | 37.252 | 34.592 | 35.250 | 16.131 | 31.782 | 17.606 | 29.595 | 19.126 | 20.782 |
    +-------------------+--------+--------+--------+--------+--------+--------+--------+--------+--------+
    | Final C++17       | 34.470 | 33.154 | 33.881 | 15.415 | 30.279 | 17.078 | 28.808 | 18.497 | 19.761 |
    +-------------------+--------+--------+--------+--------+--------+--------+--------+--------+--------+
    | Final Improvement | 15.28% | 4.60%  | 4.52%  | 4.52%  | 5.15%  | 3.55%  | 3.34%  | 3.69%  | 5.25%  |
    +-------------------+--------+--------+--------+--------+--------+--------+--------+--------+--------+

First of all, as I have seen time after time, clang is still slower than GCC.
It's a not a big difference, but still significant. Overall, the gains are a bit
higher on clang than on GCC, but not by much. Interestingly, the migration of
DLL to C++17 is less interesting in terms of compilation time for clang. It
seems even to slow down compilation on some examples. On the other hand, the
migration of ETL is more important than on GCC.

Overall, every example is faster to compile using both libraries in C++17, but
we don't have spectacular speed-ups. With clang, we have speedups from 3.3% to
15.3%. With GCC, we have speedup  from 1.1% to 14.6%. It's not very high, but
I'm already satisfied with these results.

C++17 in DLL
++++++++++++

Overall, the migration of DLL to C++17 was quite similar to that of ETL. You can
take a look at my `previous article <https://baptiste-wicht.com/posts/2018/02/c%2B%2B17-migration-of-expression-templates-library-etl.html>`_
if you want more details on C++17 features I've used.

I've *replaced a lot of SFINAE functions* with :code:`if constexpr`. I've also
replaced a lot of :code:`statif_if` with :code:`if constexpr`. There was a large
number of these in DLL's code. I also enabled all the :code:`constexpr` that
were commented for this exact time :)

I was also thinking that I could replace a lot of meta-programming stuff with
*fold expressions*. While I was able to replace a few of them, most of them were
harder to replace with fold expressions. Indeed, the variadic pack is often
hidden behind another class and therefore the pack is not directly usable from
the network class or the group and merge layers classes. I didn't want to start
a big refactoring just to use a C++17 feature, the current state of this code is
fine.

I made some use of structured bindings as well, but again not as much as I was
thinking. In fact, a lot of time, I'm assigning the elements of a pair or tuple
to existing variables not declaring new variables and unfortunately, you can
only use structured bindings with :code:`auto` declaration.

Overall, the *code is significantly better now*, but there was less impact than
there was on ETL. It's also a smaller code base, so maybe this is normal and my
expectations were too high ;)

Conclusion
++++++++++

The trunk of DLL is now a C++17 library :) I think this improve the quality of
the code by a nice margin! Even though, there is still some work to be done to
improve the code, especially for the DBN pretraining code, the quality is quite
good now. Moreover, the switch to C++17 made the compilation of neural networks
using the DLL library *faster to compile*, from 1.1% in the worst case to 15.3% in
the best case! I don't know when I will release the next version of DLL, but it
will take some time. I'll especially have to polish the RNN support and add
a sequence to sequence loss before I will release the 1.1 version of DLL.

I'm quite satisfied with C++17 even if I would have liked a bit more features to
play with! I'm already a big fan of :code:`if constexpr`, this can make the code
much nicer and fold expressions are much more intuitive than their previous
recursive template counterpart.

I may also consider migrating some parts of the cpp-utils library, but if I do,
it will only be through the use of conditionals in order not to break the other
projects that are based on the library.
