I've improved a lot the display of my Deep Learning Library (DLL). I know this
is generally not the most important point in a machine learning framework, but
the first impression being important. Therefore, I decided it was time to get
a nicer output in the console for training networks.

A network or a dataset can be displayed using the :code:`display()` function.
I've added a :code:`display_pretty()` function to them to display it more
nicely. I've also added the :code:`dll::dump_timers_nice()` function to do the
same for :code:`dll::dump_timers()`.

I've also improved the display for the results of the batches during training.
Now, the display is updated every 100ms and it also displays the current
estimated time until the end of the epoch. With that, the user should have
a much better idea on what's going on during training, especially when training
networks when the epochs are taking a long time to complete.

Here is a full output of the training of fully-connected network on MNIST
(`mnist_mlp.cpp <https://github.com/wichtounet/dll/blob/master/examples/src/mnist_mlp.cpp>`):

.. code:: bash

       ------------------------------------------------------------
       | Index | Layer                | Parameters | Output Shape |
       ------------------------------------------------------------
       | 0     | Dense(SIGMOID) (dyn) |     392000 | [Bx500]      |
       | 1     | Dropout(0.50)(dyn)   |          0 | [Bx500]      |
       | 2     | Dense(SIGMOID) (dyn) |     125000 | [Bx250]      |
       | 3     | Dropout(0.50)(dyn)   |          0 | [Bx250]      |
       | 4     | Dense(SOFTMAX) (dyn) |       2500 | [Bx10]       |
       ------------------------------------------------------------
                      Total Parameters:     519500

       --------------------------------------------
       | mnist | Size  | Batches | Augmented Size |
       --------------------------------------------
       | train | 60000 | 600     | 60000          |
       | test  | 10000 | 100     | 10000          |
       --------------------------------------------

      Train the network with "Stochastic Gradient Descent"
          Updater: NADAM
             Loss: CATEGORICAL_CROSS_ENTROPY
       Early Stop: Goal(error)

      With parameters:
                epochs=50
            batch_size=100
         learning_rate=0.002
                 beta1=0.9
                 beta2=0.999

      epoch   0/50 batch  600/ 600 - error: 0.04623 loss: 0.15097 time 3230ms
      epoch   1/50 batch  600/ 600 - error: 0.03013 loss: 0.09947 time 3188ms
      epoch   2/50 batch  600/ 600 - error: 0.02048 loss: 0.06565 time 3102ms
      epoch   3/50 batch  600/ 600 - error: 0.01593 loss: 0.05258 time 3189ms
      epoch   4/50 batch  600/ 600 - error: 0.01422 loss: 0.04623 time 3160ms
      epoch   5/50 batch  600/ 600 - error: 0.01112 loss: 0.03660 time 3131ms
      epoch   6/50 batch  600/ 600 - error: 0.01078 loss: 0.03546 time 3200ms
      epoch   7/50 batch  600/ 600 - error: 0.01003 loss: 0.03184 time 3246ms
      epoch   8/50 batch  600/ 600 - error: 0.00778 loss: 0.02550 time 3222ms
      epoch   9/50 batch  600/ 600 - error: 0.00782 loss: 0.02505 time 3119ms
      epoch  10/50 batch  600/ 600 - error: 0.00578 loss: 0.02056 time 3284ms
      epoch  11/50 batch  600/ 600 - error: 0.00618 loss: 0.02045 time 3220ms
      epoch  12/50 batch  600/ 600 - error: 0.00538 loss: 0.01775 time 3444ms
      epoch  13/50 batch  600/ 600 - error: 0.00563 loss: 0.01803 time 3304ms
      epoch  14/50 batch  600/ 600 - error: 0.00458 loss: 0.01598 time 3577ms
      epoch  15/50 batch  600/ 600 - error: 0.00437 loss: 0.01436 time 3228ms
      epoch  16/50 batch  600/ 600 - error: 0.00360 loss: 0.01214 time 3180ms
      epoch  17/50 batch  600/ 600 - error: 0.00405 loss: 0.01309 time 3090ms
      epoch  18/50 batch  600/ 600 - error: 0.00408 loss: 0.01346 time 3045ms
      epoch  19/50 batch  600/ 600 - error: 0.00337 loss: 0.01153 time 3071ms
      epoch  20/50 batch  600/ 600 - error: 0.00297 loss: 0.01021 time 3131ms
      epoch  21/50 batch  600/ 600 - error: 0.00318 loss: 0.01103 time 3076ms
      epoch  22/50 batch  600/ 600 - error: 0.00277 loss: 0.00909 time 3090ms
      epoch  23/50 batch  600/ 600 - error: 0.00242 loss: 0.00818 time 3163ms
      epoch  24/50 batch  600/ 600 - error: 0.00267 loss: 0.00913 time 3229ms
      epoch  25/50 batch  600/ 600 - error: 0.00295 loss: 0.00947 time 3156ms
      epoch  26/50 batch  600/ 600 - error: 0.00252 loss: 0.00809 time 3066ms
      epoch  27/50 batch  600/ 600 - error: 0.00227 loss: 0.00773 time 3156ms
      epoch  28/50 batch  600/ 600 - error: 0.00203 loss: 0.00728 time 3158ms
      epoch  29/50 batch  600/ 600 - error: 0.00240 loss: 0.00753 time 3114ms
      epoch  30/50 batch  600/ 600 - error: 0.00263 loss: 0.00864 time 3099ms
      epoch  31/50 batch  600/ 600 - error: 0.00210 loss: 0.00675 time 3096ms
      epoch  32/50 batch  600/ 600 - error: 0.00163 loss: 0.00628 time 3120ms
      epoch  33/50 batch  600/ 600 - error: 0.00182 loss: 0.00611 time 3045ms
      epoch  34/50 batch  600/ 600 - error: 0.00125 loss: 0.00468 time 3140ms
      epoch  35/50 batch  600/ 600 - error: 0.00183 loss: 0.00598 time 3093ms
      epoch  36/50 batch  600/ 600 - error: 0.00232 loss: 0.00711 time 3068ms
      epoch  37/50 batch  600/ 600 - error: 0.00170 loss: 0.00571 time 3057ms
      epoch  38/50 batch  600/ 600 - error: 0.00162 loss: 0.00530 time 3115ms
      epoch  39/50 batch  600/ 600 - error: 0.00155 loss: 0.00513 time 3226ms
      epoch  40/50 batch  600/ 600 - error: 0.00150 loss: 0.00501 time 2987ms
      epoch  41/50 batch  600/ 600 - error: 0.00122 loss: 0.00425 time 3117ms
      epoch  42/50 batch  600/ 600 - error: 0.00108 loss: 0.00383 time 3102ms
      epoch  43/50 batch  600/ 600 - error: 0.00165 loss: 0.00533 time 2977ms
      epoch  44/50 batch  600/ 600 - error: 0.00142 loss: 0.00469 time 3009ms
      epoch  45/50 batch  600/ 600 - error: 0.00098 loss: 0.00356 time 3055ms
      epoch  46/50 batch  600/ 600 - error: 0.00127 loss: 0.00409 time 3076ms
      epoch  47/50 batch  600/ 600 - error: 0.00132 loss: 0.00438 time 3068ms
      epoch  48/50 batch  600/ 600 - error: 0.00130 loss: 0.00459 time 3045ms
      epoch  49/50 batch  600/ 600 - error: 0.00107 loss: 0.00365 time 3103ms
      Restore the best (error) weights from epoch 45
      Training took 160s

      Evaluation Results
         error: 0.01740
          loss: 0.07861
      evaluation took 67ms

       -----------------------------------------------------------------------------
       | %        | Timer                         | Count  | Total     | Average   |
       -----------------------------------------------------------------------------
       | 100.000% | net:train:ft                  | 1      | 160.183s  | 160.183s  |
       | 100.000% | net:trainer:train             | 1      | 160.183s  | 160.183s  |
       |  99.997% | net:trainer:train:epoch       | 50     | 160.178s  | 3.20356s  |
       |  84.422% | net:trainer:train:epoch:batch | 30000  | 135.229s  | 4.50764ms |
       |  84.261% | sgd::train_batch              | 30000  | 134.971s  | 4.49904ms |
       |  44.404% | sgd::grad                     | 30000  | 71.1271s  | 2.3709ms  |
       |  35.453% | sgd::forward                  | 30000  | 56.7893s  | 1.89298ms |
       |  32.245% | sgd::update_weights           | 90000  | 51.6505s  | 573.894us |
       |  32.226% | sgd::apply_grad:nadam         | 180000 | 51.6211s  | 286.783us |
       |  28.399% | dense:dyn:forward             | 180300 | 45.4903s  | 252.303us |
       |  17.642% | dropout:train:forward         | 60000  | 28.2595s  | 470.99us  |
       |  13.707% | net:trainer:train:epoch:error | 50     | 21.957s   | 439.14ms  |
       |  12.148% | dense:dyn:gradients           | 90000  | 19.4587s  | 216.207us |
       |   4.299% | sgd::backward                 | 30000  | 6.88546s  | 229.515us |
       |   3.301% | dense:dyn:backward            | 60000  | 5.28729s  | 88.121us  |
       |   0.560% | dense:dyn:errors              | 60000  | 896.471ms | 14.941us  |
       |   0.407% | dropout:backward              | 60000  | 651.523ms | 10.858us  |
       |   0.339% | dropout:test:forward          | 60000  | 542.799ms | 9.046us   |
       |   0.161% | net:compute_loss:CCE          | 60100  | 257.915ms | 4.291us   |
       |   0.099% | sgd::error                    | 30000  | 158.33ms  | 5.277us   |
       -----------------------------------------------------------------------------

I hope this will make the output of the machine learning framework more useful.

All this support is now in the **master** branch of the DLL project if you want
to check it out. You can also check out the example online:
`mnist_mlp.cpp <https://github.com/wichtounet/dll/blob/master/examples/src/mnist_mlp.cpp>`_

You can access the project `on Github <https://github.com/wichtounet/dll>`_.
