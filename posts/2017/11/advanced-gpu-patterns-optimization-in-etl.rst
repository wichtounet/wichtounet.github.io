The GPU performance of my Expression Templates Library (ETL) is pretty good when
most of the time is spent inside expensive operations such as Matrix-Matrix
Multiplication or convolutions. However, when most of the time is spent in
linear kernels, performance is not great because this will invoke a lot of CUDA
kernels. Indeed, the way it is done is that each sub expressions compute its
result in a temporary GPU vector (or matrix) and these temporaries are passed
through the expressions. For instance, this expression:

.. code:: C++

    yy = 1.1 * x + 1.2 * y

will be executed on the GPU as something like this:

.. code:: C++

    t1 = 1.1 * x
    t2 = 1.2 * y
    yy = t1 + t2

that will results in three GPU kernels being invoked. In the CPU case, the
complete expression will be executed as one CPU kernel, that is constructed with
Expression Templates. Unfortunately, a CUDA kernel cannot be constructed in the
same way since the CUDA compiler does not support general template
metaprogramming. That's why I've implemented by using small kernels for each
expression.

Fortunately, we can do better with a bit more meta-programming. Indeed, there
are some patterns that are repeated a lot and that easily be implemented in CUDA
kernels. I've started detecting a few of these patterns and for each of them
a single CUDA kernel is executed. For instance, each of the following
expressions can be executed with a single kernel:

.. code:: C++

   yy = 1.1 * x + y
   yy = x + 1.1 * y
   yy = 1.1 * y + 1.2 * y
   yy = 1.1 * x * y
   yy = x / (1.1 * y)

This results in significantly performance improvement for these expressions!

I have tested these new improvements in my Deep Learning Library (DLL) project
(not yet merged) and it resulted in **25% faster momentum computation** and
**17% faster Nesterov Adam (NADAM)**.

I'm going to continue to investigate which kernels need to be made faster for
DLL and try to improve the overall performance. Currently, the GPU performance
of DLL is very good for large convolutional networks, but could be improved for
small fully-connected networks. Indeed, in that case, quite some time is spent
outside the matrix-matrix multiplication and inside serial expressions for which
GPU could be improved. Once I'm done with my optimizations, I'll probably post
again on the blog with the latest results.

All these new optimizations are now in the **master** branch of the ETL
project if you want to check it out. You can access the project
`on Github <https://github.com/wichtounet/etl>`_.
