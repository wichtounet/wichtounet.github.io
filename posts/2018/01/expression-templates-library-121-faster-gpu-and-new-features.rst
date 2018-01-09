Happy new year to all my dear readers!

It has been a while since I've posted on this blog. I've had to serve three
weeks in the army and then I had two weeks vacation. I've been actively working
on budgetwarrior with a brand new web interface! More on that later ;)

Today, I'm happy to release the version 1.2.1 of my Expression Templates Library
(ETL) project. This is a minor version but with significantly better GPU support
and a few new features and bug fixes so I decided to release it now.

Faster GPU support
++++++++++++++++++

Last year, I `implemented the support for the detection of advanced GPU patterns in ETL <https://baptiste-wicht.com/posts/2017/11/advanced-gpu-patterns-optimization-in-etl.html>`_.

This will significantly reduce the number of CUDA kernel calls that are being
launched. For instance, each of the following expressions will be evaluated
using a single GPU kernel:

.. code:: C++

   yy = 1.1 * x + y
   yy = x + 1.1 * y
   yy = 1.1 * y + 1.2 * y
   yy = 1.1 * x * y
   yy = x / (1.1 * y)

This makes some operation significantly faster.

Moreover, I've reduced a lot the numbers of device synchronization in the
library. Especially, I've removed almost all synchronization from the
etl-gpu-blas sub library. This means that synchronization is mostly only done
when data needs to go back to the CPU. For machine learning, this means at the
end of the epoch to compute the final error. This makes a HUGE difference in
time, I didn't realize before that I was doing way too much synchronization.

With these two changes, I've been able to attain *state of the art training performance on GPU* with my Deep Learning Library (DLL) project!

Moreover, I've now added for random number generations on the GPU and for
shuffle operations as well.

New Features
++++++++++++

I've also added a few new features recently. They were especially added to
support new features in DLL.

Matrices and vectors can now be normalized in order to have zero-mean and
unit-variance distribution. You can also merge matrices together. For now, there
is no GPU support, so this will use CPU anyway. I plan to fix that later.

In addition to bias_batch_mean that I added before, I also added bias_batch_var
now with the variance in place of the mean. This is mainly used for Batch
Normalization in machine learning, but it may have some other usages. The GPU
support has been added as well directly.

And the last feature is the support for embedding and the gradients of
embedding. Again this is totally related to machine learning, but can be very
useful as well. I haven't add the time to develop the GPU version so far, but
this will come as well.

Performance
+++++++++++

Nothing fancy on the CPU performance side, I only added vectorization for
hyperbolic versions. This makes *tanh much faster on CPU*.

Bug Fixes
+++++++++

I fixed quite a few bugs in this version, which is one of the main reason
I released it:

1. When using large fast_matrix and aliasing was detected, there was a big chance of stack overflow occurring. This is now fixed by using a dynamic temporary.
1. Some assignables such sub_view did not perform any detection for aliasing. This is now fixed and aliasing is detected everywhere.
1. fast_dyn_matrix can now be correctly used with *bool*
1. The use of iterators was not always ensuring correct CPU/GPU consistency. This is now correctly handled.
1. The 4D convolution in GPU were not using the correct flipping
1. Fix small compilation bug with sub_matrix and GPU

What's next ?
+++++++++++++

I don't really know what will be in the next release. This should be the release
1.3. One possible idea would be to improve and review the support for sparse
matrix which is more than  poor as of now. But I'm not really motivated to
work on that :P Moreover, I'm now *actively* working on the next release of
budgetwarrior which will probably still come this month.

I'm also still hesitating in switching to C++17 for the library to make it
faster to compile. And also to clean some parts of the code. I would be able to
remove quite some SFINAE with the new *if constexpr*, but I'm afraid this will
make the library to difficult to use since it would need at least GCC 7 or clang
3.9.

Download ETL
============

You can download ETL `on Github <https://github.com/wichtounet/etl>`_. If you
only interested in the 1.2.1 version, you can look at the
`Releases pages <https://github.com/wichtounet/etl/releases>`_ or clone the tag
1.2.1. There are several branches:

* *master* Is the eternal development branch, may not always be stable
* *stable* Is a branch always pointing to the last tag, no development here

For the future release, there always will tags pointing to the corresponding
commits. You can also have access to previous releases on Github or via the
release tags.

The documentation is still a bit sparse. There are a few examples and the Wiki,
but there still is work to be done. If you have questions on how to use or
configure the library, please don't hesitate.

Don't hesitate to comment this post if you have any comment on this library or
any question. You can also open an Issue on Github if you have a problem using
this library or propose a Pull Request if you have any contribution you'd like
to make to the library.

Hope this may be useful to some of you :)
