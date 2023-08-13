I'm happy to announce that I just merged support for Recurrent Neural Networks
(RNNs) into my Deep Learning Library (DLL) machine learning framework.

It's nothing fancy yet, but forward propagation of RNN and basic Backpropagation
Through Time (BPTT) are now supported. For now, only existing classification
loss is supported for RNN. I plan to add support for sequence-to-sequence loss
in order to be able to train models able to generate characters, but I don't
know when I'll be able to work on that. I also plan to add support for other
types of cells such as LSTM and GRU (maybe NAS) in the future.

For example, here is a simple RNN used on MNIST:

.. code:: cpp

    #include "dll/neural/dense_layer.hpp"
    #include "dll/neural/recurrent_layer.hpp"
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
                dll::recurrent_layer<time_steps, sequence_length, hidden_units, dll::last_only>,
                dll::recurrent_last_layer<time_steps, hidden_units>,
                dll::dense_layer<hidden_units, 10, dll::softmax>
            >
            , dll::updater<dll::updater_type::ADAM>      // Adam
            , dll::batch_size<100>                       // The mini-batch size
        >::network_t;

        auto net = std::make_unique<network_t>();

        // Display the network and dataset
        net->display();

        // Train the network for performance sake
        net->fine_tune(dataset.train(), 50);

        // Test the network on test set
        net->evaluate(dataset.test());

        return 0;
    }

The network starts with recurrent layer, followed by a layer that extracts only
the last layer and finally a dense layer with a softmax function. The recurrent
layer has support to change the activation function, change the initializer for
the two weights matrices of the RNN and the number of steps for BPTT truncation.

Here is a possible result:

.. code::

    Network with 3 layers
        RNN(dyn): 28x28 -> TANH -> 28x100
        RNN(last): 28x100 -> 100
        Dense(dyn): 100 -> SOFTMAX -> 10
    Total parameters: 13800
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

    Epoch   0/50 - Classification error: 0.11635 Loss: 0.39999 Time 4717ms
    Epoch   1/50 - Classification error: 0.11303 Loss: 0.36994 Time 4702ms
    Epoch   2/50 - Classification error: 0.06732 Loss: 0.23469 Time 4702ms
    Epoch   3/50 - Classification error: 0.04865 Loss: 0.17091 Time 4696ms
    Epoch   4/50 - Classification error: 0.05957 Loss: 0.20437 Time 4706ms
    Epoch   5/50 - Classification error: 0.05022 Loss: 0.16888 Time 4696ms
    Epoch   6/50 - Classification error: 0.03912 Loss: 0.13743 Time 4698ms
    Epoch   7/50 - Classification error: 0.04097 Loss: 0.14509 Time 4706ms
    Epoch   8/50 - Classification error: 0.03938 Loss: 0.13397 Time 4694ms
    Epoch   9/50 - Classification error: 0.03525 Loss: 0.12284 Time 4706ms
    Epoch  10/50 - Classification error: 0.03927 Loss: 0.13770 Time 4694ms
    Epoch  11/50 - Classification error: 0.03315 Loss: 0.11315 Time 4711ms
    Epoch  12/50 - Classification error: 0.05037 Loss: 0.17123 Time 4711ms
    Epoch  13/50 - Classification error: 0.02927 Loss: 0.10042 Time 4780ms
    Epoch  14/50 - Classification error: 0.03322 Loss: 0.11027 Time 4746ms
    Epoch  15/50 - Classification error: 0.03397 Loss: 0.11585 Time 4684ms
    Epoch  16/50 - Classification error: 0.02938 Loss: 0.09984 Time 4708ms
    Epoch  17/50 - Classification error: 0.03262 Loss: 0.11152 Time 4690ms
    Epoch  18/50 - Classification error: 0.02872 Loss: 0.09753 Time 4672ms
    Epoch  19/50 - Classification error: 0.02548 Loss: 0.08605 Time 4691ms
    Epoch  20/50 - Classification error: 0.02245 Loss: 0.07797 Time 4693ms
    Epoch  21/50 - Classification error: 0.02705 Loss: 0.08984 Time 4684ms
    Epoch  22/50 - Classification error: 0.02422 Loss: 0.08164 Time 4688ms
    Epoch  23/50 - Classification error: 0.02645 Loss: 0.08804 Time 4690ms
    Epoch  24/50 - Classification error: 0.02927 Loss: 0.09739 Time 4715ms
    Epoch  25/50 - Classification error: 0.02578 Loss: 0.08669 Time 4702ms
    Epoch  26/50 - Classification error: 0.02785 Loss: 0.09368 Time 4700ms
    Epoch  27/50 - Classification error: 0.02472 Loss: 0.08237 Time 4695ms
    Epoch  28/50 - Classification error: 0.02125 Loss: 0.07324 Time 4690ms
    Epoch  29/50 - Classification error: 0.01977 Loss: 0.06635 Time 4688ms
    Epoch  30/50 - Classification error: 0.03635 Loss: 0.12140 Time 4689ms
    Epoch  31/50 - Classification error: 0.02862 Loss: 0.09704 Time 4698ms
    Epoch  32/50 - Classification error: 0.02463 Loss: 0.08158 Time 4686ms
    Epoch  33/50 - Classification error: 0.02565 Loss: 0.08771 Time 4697ms
    Epoch  34/50 - Classification error: 0.02278 Loss: 0.07634 Time 4718ms
    Epoch  35/50 - Classification error: 0.02105 Loss: 0.07075 Time 4697ms
    Epoch  36/50 - Classification error: 0.02770 Loss: 0.09358 Time 4711ms
    Epoch  37/50 - Classification error: 0.02627 Loss: 0.08805 Time 4742ms
    Epoch  38/50 - Classification error: 0.02282 Loss: 0.07712 Time 4708ms
    Epoch  39/50 - Classification error: 0.02305 Loss: 0.07661 Time 4697ms
    Epoch  40/50 - Classification error: 0.02243 Loss: 0.07773 Time 4700ms
    Epoch  41/50 - Classification error: 0.02467 Loss: 0.08234 Time 4712ms
    Epoch  42/50 - Classification error: 0.01808 Loss: 0.06186 Time 4691ms
    Epoch  43/50 - Classification error: 0.02388 Loss: 0.07917 Time 4681ms
    Epoch  44/50 - Classification error: 0.02162 Loss: 0.07508 Time 4699ms
    Epoch  45/50 - Classification error: 0.01877 Loss: 0.06289 Time 4735ms
    Epoch  46/50 - Classification error: 0.02263 Loss: 0.07969 Time 4764ms
    Epoch  47/50 - Classification error: 0.02100 Loss: 0.07207 Time 4684ms
    Epoch  48/50 - Classification error: 0.02425 Loss: 0.08076 Time 4752ms
    Epoch  49/50 - Classification error: 0.02328 Loss: 0.07803 Time 4718ms
    Restore the best (error) weights from epoch 42
    Training took 235s
    Evaluation Results
       error: 0.03000
        loss: 0.12260
    evaluation took 245ms

Nothing fancy, but this example is not necessarily optimized.

All this support is now in the **master** branch of the DLL project if you want
to check it out. You can also check out the example online:
`mnist_rnn.cpp <https://github.com/wichtounet/dll/blob/master/examples/src/mnist_rnn.cpp>`_

You can access the project `on Github <https://github.com/wichtounet/dll>`_.
