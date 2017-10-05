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

If you have been following my blog lately, you already may have seen part of
this information, but I wanted to emphasize it here. I've been doing a lot of
work on the performance of the library. TODO...

What's next ?
#############

I do not know exactly what the next version of DLL will contain, but I know the
direction in which I'm going to develop.

I would really like to be able to use DLL to classify text. In first time,
I plan to add support for learning embeddings from text and be able to use CNN
on top of the embeddings. Doing that, I also plan to add support to be able to
merge several CNN layers together, so that I can use various filter sizes.
Hopefully, this should not take too long. In a second time, I really want to
integrate support for Recurrent Neural Networks (RNNs) into the framework. In
a first time, only simple CNN cell, but then I want to add support for LSTM and
GRU cells. This will definitely take some time, but I really want to do it
completely in order to fully understand what's going on inside such networks.

Documentation

Examples

Performance
GPU

Compilation time

Download DLL
############
