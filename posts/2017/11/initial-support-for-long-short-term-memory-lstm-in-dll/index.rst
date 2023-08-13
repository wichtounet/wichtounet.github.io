I'm really happy to announce that I just merged support for

Long Short Term Memory
(LSTM) cells into my Deep Learning Library (DLL) machine learning framework. Two
weeks ago, `I already merged suport for Recurrent Neural network (RNN) <https://baptiste-wicht.com/posts/2017/11/initial-support-for-recurrent-neural-network-rnn-in-dll.html>`_.

It's nothing fancy yet, but forward propagation of LSTM and basic
Backpropagation Through Time (BPTT) are now supported. It was not really
complicated to implemenet the forward pass but the backward pass is much
complicated for an LSTM than for a RNN. It took me quite a long time to figure
out all the gradients formulas and the documentation on that is quite scarce.

For now, still only existing classification loss is supported for RNN and LSTM.
As I said last time, I still plan to add support for sequence-to-sequence loss
in order to be able to train models able to generate characters. However, I don't
know when I'll be able to work on that. Now that I've got the code for LSTM,
I should be able to implement a GRU cell and NAS cell quite easily I believe.

For example, here is a simple LSTM used on MNIST for classification:

.. code:: cpp

    #include "dll/neural/dense_layer.hpp"
    #include "dll/neural/lstm_layer.hpp"
    #include "dll/neural/recurrent_last_layer.hpp"
    #include "dll/network.hpp"
    #include "dll/datasets.hpp"

    int main(int /*argc*/, char* /*argv*/ []) {
        // Load the dataset
        auto dataset = dll::make_mnist_dataset_nc(dll::batch_size<100>{}, dll::scale_pre<255>{});

        constexpr size_t time_steps      = 28;
        constexpr size_t sequence_length = 28;
        constexpr size_t hidden_units    = 100;

        // Build the network

        using network_t = dll::dyn_network_desc<
            dll::network_layers<
                dll::lstm_layer<time_steps, sequence_length, hidden_units, dll::last_only>,
                dll::recurrent_last_layer<time_steps, hidden_units>,
                dll::dense_layer<hidden_units, 10, dll::softmax>
            >
            , dll::updater<dll::updater_type::ADAM>      // Adam
            , dll::batch_size<100>                       // The mini-batch size
        >::network_t;

        auto net = std::make_unique<network_t>();

        // Display the network and dataset
        net->display();
        dataset.display();

        // Train the network for performance sake
        net->fine_tune(dataset.train(), 50);

        // Test the network on test set
        net->evaluate(dataset.test());

        return 0;
    }

The network is quite similar to the one used previously with an RNN, just
replace rnn with lstm and that's it. It starts with LSTM layer, followed by
a layer extracting the last time step and finally a dense layer with a softmax
function. The network is trained with Adam for 50 epochs. You can change the
activation function , the initializer for the weights and the biases and number
of steps for BPTT truncation.

Here is the result I got on my last run:

.. code::

    ------------------------------------------------------------
    | Index | Layer                | Parameters | Output Shape |
    ------------------------------------------------------------
    | 0     | LSTM (TANH) (dyn)    |      51200 | [Bx28x100]   |
    | 1     | RNN(last)            |          0 | [Bx100]      |
    | 2     | Dense(SOFTMAX) (dyn) |       1000 | [Bx10]       |
    ------------------------------------------------------------
                  Total Parameters:      52200

    --------------------------------------------
    | mnist | Size  | Batches | Augmented Size |
    --------------------------------------------
    | train | 60000 | 600     | 60000          |
    | test  | 10000 | 100     | 10000          |
    --------------------------------------------

    Network with 3 layers
        LSTM(dyn): 28x28 -> TANH -> 28x100
        RNN(last): 28x100 -> 100
        Dense(dyn): 100 -> SOFTMAX -> 10
    Total parameters: 52200
    Dataset
    Training: In-Memory Data Generator
                  Size: 60000
               Batches: 600
    Testing: In-Memory Data Generator
                  Size: 10000
               Batches: 100

    Train the network with "Stochastic Gradient Descent"
        Updater: ADAM
           Loss: CATEGORICAL_CROSS_ENTROPY
     Early Stop: Goal(error)

    With parameters:
              epochs=50
          batch_size=100
       learning_rate=0.001
               beta1=0.9
               beta2=0.999

    epoch   0/50 batch  600/ 600 - error: 0.07943 loss: 0.28504 time 20910ms
    epoch   1/50 batch  600/ 600 - error: 0.06683 loss: 0.24021 time 20889ms
    epoch   2/50 batch  600/ 600 - error: 0.04828 loss: 0.18233 time 21061ms
    epoch   3/50 batch  600/ 600 - error: 0.04407 loss: 0.16665 time 20839ms
    epoch   4/50 batch  600/ 600 - error: 0.03515 loss: 0.13290 time 22108ms
    epoch   5/50 batch  600/ 600 - error: 0.03207 loss: 0.12019 time 21393ms
    epoch   6/50 batch  600/ 600 - error: 0.02973 loss: 0.11239 time 28199ms
    epoch   7/50 batch  600/ 600 - error: 0.02653 loss: 0.10455 time 37039ms
    epoch   8/50 batch  600/ 600 - error: 0.02482 loss: 0.09657 time 23127ms
    epoch   9/50 batch  600/ 600 - error: 0.02177 loss: 0.08422 time 41766ms
    epoch  10/50 batch  600/ 600 - error: 0.02453 loss: 0.09382 time 29765ms
    epoch  11/50 batch  600/ 600 - error: 0.02575 loss: 0.09796 time 21449ms
    epoch  12/50 batch  600/ 600 - error: 0.02107 loss: 0.07833 time 42056ms
    epoch  13/50 batch  600/ 600 - error: 0.01877 loss: 0.07171 time 24673ms
    epoch  14/50 batch  600/ 600 - error: 0.02095 loss: 0.08481 time 20878ms
    epoch  15/50 batch  600/ 600 - error: 0.02040 loss: 0.07578 time 41515ms
    epoch  16/50 batch  600/ 600 - error: 0.01580 loss: 0.06083 time 25705ms
    epoch  17/50 batch  600/ 600 - error: 0.01945 loss: 0.07046 time 20903ms
    epoch  18/50 batch  600/ 600 - error: 0.01728 loss: 0.06683 time 41828ms
    epoch  19/50 batch  600/ 600 - error: 0.01577 loss: 0.05947 time 27810ms
    epoch  20/50 batch  600/ 600 - error: 0.01528 loss: 0.05883 time 21477ms
    epoch  21/50 batch  600/ 600 - error: 0.01345 loss: 0.05127 time 44718ms
    epoch  22/50 batch  600/ 600 - error: 0.01410 loss: 0.05357 time 25174ms
    epoch  23/50 batch  600/ 600 - error: 0.01268 loss: 0.04765 time 23827ms
    epoch  24/50 batch  600/ 600 - error: 0.01342 loss: 0.05004 time 47232ms
    epoch  25/50 batch  600/ 600 - error: 0.01730 loss: 0.06872 time 22532ms
    epoch  26/50 batch  600/ 600 - error: 0.01337 loss: 0.05016 time 30114ms
    epoch  27/50 batch  600/ 600 - error: 0.01842 loss: 0.07049 time 40136ms
    epoch  28/50 batch  600/ 600 - error: 0.01262 loss: 0.04639 time 21793ms
    epoch  29/50 batch  600/ 600 - error: 0.01403 loss: 0.05292 time 34096ms
    epoch  30/50 batch  600/ 600 - error: 0.01185 loss: 0.04456 time 35420ms
    epoch  31/50 batch  600/ 600 - error: 0.01098 loss: 0.04180 time 20909ms
    epoch  32/50 batch  600/ 600 - error: 0.01337 loss: 0.04687 time 30113ms
    epoch  33/50 batch  600/ 600 - error: 0.01415 loss: 0.05292 time 37393ms
    epoch  34/50 batch  600/ 600 - error: 0.00982 loss: 0.03615 time 20962ms
    epoch  35/50 batch  600/ 600 - error: 0.01178 loss: 0.04830 time 29305ms
    epoch  36/50 batch  600/ 600 - error: 0.00882 loss: 0.03408 time 38293ms
    epoch  37/50 batch  600/ 600 - error: 0.01148 loss: 0.04341 time 20841ms
    epoch  38/50 batch  600/ 600 - error: 0.00960 loss: 0.03701 time 29204ms
    epoch  39/50 batch  600/ 600 - error: 0.00850 loss: 0.03094 time 39802ms
    epoch  40/50 batch  600/ 600 - error: 0.01473 loss: 0.05136 time 20831ms
    epoch  41/50 batch  600/ 600 - error: 0.01007 loss: 0.03579 time 29856ms
    epoch  42/50 batch  600/ 600 - error: 0.00943 loss: 0.03370 time 38200ms
    epoch  43/50 batch  600/ 600 - error: 0.01205 loss: 0.04409 time 21162ms
    epoch  44/50 batch  600/ 600 - error: 0.00980 loss: 0.03674 time 32279ms
    epoch  45/50 batch  600/ 600 - error: 0.01068 loss: 0.04133 time 38448ms
    epoch  46/50 batch  600/ 600 - error: 0.00913 loss: 0.03478 time 20797ms
    epoch  47/50 batch  600/ 600 - error: 0.00985 loss: 0.03759 time 28885ms
    epoch  48/50 batch  600/ 600 - error: 0.00912 loss: 0.03295 time 41120ms
    epoch  49/50 batch  600/ 600 - error: 0.00930 loss: 0.03438 time 21282ms
    Restore the best (error) weights from epoch 39
    Training took 1460s

    Evaluation Results
       error: 0.02440
        loss: 0.11315
    evaluation took 1000ms


Again, nothing fancy yet, but this example has not been optimized for
performance nor for accuracy.

I also made a few changes to the RNN layer. I added support for biases and
improved the code as well for performance and readability.

All this support is now in the **master** branch of the DLL project if you want
to check it out. You can also check out the example online:
`mnist_lstm.cpp <https://github.com/wichtounet/dll/blob/master/examples/src/mnist_lstm.cpp>`_

You can access the project `on Github <https://github.com/wichtounet/dll>`_.

Currently I'm working on the GPU performance again. The performance of some is
still not as good as I want it to be, especially complex operation like used in
Adam and Nadam. Currently, there are many calls to GPU BLAS libraries and
I want to try to extract some more optimized patterns. Once it's done, I'll post
more on that later on the blog.
