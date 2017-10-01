.. image:: /images/logo.png
   :align: center
   :alt: ETL Logo

I'm happy to announce the version 1.2 of my Expression Templates Library (ETL):
ETL 1.2, two months after `I released the version 1.1 <https://baptiste-wicht.com/posts/2017/08/expression-templates-library-etl-11.html>`_.
This version does not have a lot of new features, but the GPU support is now
complete and has a lot of changes in the internal code.

GPU Support
===========

Before, only algorithms such as 4D convolution or matrix-matrix multiplication
were computed in the GPU and lots of operations were causing copies between CPU
and GPU version. Now, the support for basic operations has also been completed
and therefore, expressions like this:

.. code:: cpp

   C = sigmoid(2.0 * (A + B)) / sum(A)

Can be computed entirely on GPU.

Each matrix and vector containers have a secondary GPU memory space.  During the
execution, the status of both space is being managed and when necessary, copies
are made between two spaces. In the best case, there should only be initial
copies to the GPU and then everything should be done on the GPU.

If you have an expression such as :code:`c = a + b * 2`, it can be entirely computed
on GPU, however, it will be computed in two GPU operations such as:

.. code:: cpp

   t1 = b * 2
   c = a + t1

This is not perfect in terms of performance but this will be done without any
copies between CPU and GPU memory. I plan to improve this system with a bit more
complex operations to avoid too many GPU operations, but there will always be
more operations than in CPU where this can easily be done in one go.

There are a few expressions that are not computable on the GPU, such as random
generations. A few transformations are also not fully compatible with GPU.
Moreover, if you access an element with operators :code:`[]` or :code:`()`, this
will invalidate the GPU memory and force an update to the CPU memory.

GPU operations are not implemented directly in ETL, there are coming from
various libraries. ETL is using NVIDIA CUDNN, CUFFT and CUDNN for most
algorithms. Moreover, for other operations, I've implemented a libraries with
simple GPU operations: ETL-GPU-BLAS (EGBLAS). You can have a look at
`egblas <https://github.com/wichtounet/etl-gpu-blas>`_ if you are interested.

My Deep Learning Library (DLL) project is based on ETL and its performances are
mostly dependent on ETL's performances. Now that ETL fully supports GPU, the
GPU performance of DLL is much improved. You may remember a few weeks ago
I posted `very high CPU performance of DLL <https://baptiste-wicht.com/posts/2017/08/dll-blazing-fast-neural-network-library.html>`_.
Now, I've run again the tests to see the GPU performance with DLL. Here is the
performance for training a small CNN on the MNIST data set:

.. image:: /images/etl_12_dll_gpu_mnist.png
   :align: center
   :alt: Performances for training a Convolutional Neural Network on MNIST

As you can see, the performances on GPU are now excellent. DLL's performances
are on par with Tensorflow and Keras!

The next results are for training a much larger CNN on ImageNet, with the time
necessary to train a single batch:

.. image:: /images/etl_12_dll_gpu_imagenet.png
   :align: center
   :alt: Performances for training a Convolutional Neural Network on Imagenet

Again, using the new version of ETL inside DLL has led to excellent performance.
The framework is again on par with TensorFlow and Keras and faster than all the
other frameworks. The large difference between DLL and Tensorflow and Keras is
due to the inefficiency of reading the dataset in the two frameworks, so the
performance of the three framework themselves are about the same.

Other Changes
=============

The library also has a few other new features. Logarithms of base 2 and base 10
are now supported in complement to the base e that was already available before.
Categorical Cross Entropy (CCE) computation is also available now, the CCE loss
and error can be computed for one or many samples. Convolutions have also been
improved in that you can use mixed types in both the image and the kernel and
different storage order as well. Nevertheless, the most optimized version
remains the version with the same storage order and the same data type.

* *Feature* Default selection of algorithms by default
* *Feature* Improve support for complex numbers and etl::complex

* *Performance* Improved performance of using parallel BLAS

* *Misc* Full cleanup of the traits
* *Misc* Use of variable templates (C++14) for the traits
* *Misc* Improved support for clang
* *Misc* Reduced compilation time for non-tests / non-benchmark code
* *Misc* Reduce durations of the tests
* *Misc* Preliminary C++17 if constexpr support


Finally, a few bugs have been fixed. There was a slight bug in the Column-Major
matrix-matrix multiplication kernel. Binary operations with different types in
the left and right hand sides was also problematic with vectorization. The last
bug was about GPU status in case ETL containers were moved.

Download ETL
============

TODO
