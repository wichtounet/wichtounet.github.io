I'm very proud to announce the release of the first version of Deep Learning
Library (DLL) 1.0. DLL is a neural network library with a focus on speed and
ease of use.

I started working on this library about 4 years ago for my Ph.D. thesis.
I needed a good library to train and use Restricted Boltzmann Machines (RBMs)
and at this time there was no good support for it. Therefore, I decided to write
my own. It now has very complete support for the RBM and the Convolutional RBM
(CRBM) models. Stacks of RBMs (or Deep Belief Networks (DBNs)) can be pretrained
using Contrastive Divergence and then either fine-tuned with mini-batch gradient
descent or Conjugate Gradient or used as a feature extractor. Over the years,
the library has been extended to handle Artificial Neural Networks (ANNs) and
Convolutional Neural Networks (CNNs). The network is also able to train regular
auto-encoders. Several advanced layers such as Dropout or Batch Normalization
are also available as well as adaptive learning rates techniques such as
Adadelta and Adam. The library also has integrated support for a few datasets:
MNIST, CIFAR-10 and ImageNet.

This library can be used using a C++ interface. The library is fully
header-only. It requires a C++14 compiler, which means a minimum of clang 3.9 or
GCC 6.3.

In this post, I'm going to present a few examples on using the library and give
some information about the performance of the library and the roadmap for the
project.

.. TEASER_END

Examples
########

MNIST MLP

MNIST CNN

How to build
Some notes about the performance triggers
...

Performance
###########

What's next ?
#############

Embedding

RNN

Download DLL
############
