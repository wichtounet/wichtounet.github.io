I've been recently reminded that a long time ago I was doing a series of
tutorial on C++11 Concurrency. For some reason, I haven't continued these
tutorials.  The next post in the series was supposed to be about Futures, so I'm
finally going to do it :)

Here are the links to the current posts of the C++11 Concurrency Tutorial:

* `Part 1: Start Threads <https://baptiste-wicht.com/posts/2012/03/cpp11-concurrency-part1-start-threads.html>`_
* `Part 2: Protect Shared Data <https://baptiste-wicht.com/posts/2012/03/cp11-concurrency-tutorial-part-2-protect-shared-data.html>`_
* `Part 3: Advanced Locking and condition variables <https://baptiste-wicht.com/posts/2012/04/c11-concurrency-tutorial-advanced-locking-and-condition-variables.html>`_
* `Part 4: Atomic Types <https://baptiste-wicht.com/posts/2012/07/c11-concurrency-tutorial-part-4-atomic-type.html>`_

In this post, we are going to talk about futures, more precisely
`std::future<T>`. What is a future ? It's a very nice and simple mechanism
to work with asynchronous tasks. It also has the advantage of decoupling you
from the threads themselves, you can do multithreading without using
`std::thread`. The future itself is a structure pointing to a result that
will be computed in the future. How to create a future ? The simplest way is to
use `std::async` that will create an asynchronous task and return
a `std::future`.

Let's start with the simplest of the examples:

.. code:: c++

    #include <thread>
    #include <future>
    #include <iostream>

    int main(){
        auto future = std::async(std::launch::async, [](){
            std::cout << "I'm a thread" << std::endl;
        });

        future.get();

        return 0;
    }

Nothing really special here. `std::async` will execute the task that we
give it (here a lambda) and return a `std::future`. Once you use the
`get()` function on a future, it will wait until the result is available
and return this result to you once it is. The `get()` function is then
blocking. Since the lambda, is a void lambda, the returned future is of type
`std::future<void>` and `get()` returns `void` as well. It is
very important to know that you cannot call `get` several times on the
same future. Once the result is consumed, you cannot consume it again! If you
want to use the result several times, you need to store it yourself after you
called `get()`.

Let's see with something that returns a value and actually takes some time
before returning it:

.. code:: c++

    #include <thread>
    #include <future>
    #include <iostream>
    #include <chrono>

    int main(){
        auto future = std::async(std::launch::async, [](){
            std::this_thread::sleep_for(std::chrono::seconds(5));
            return 42;
        });

        // Do something else ?

        std::cout << future.get() << std::endl;

        return 0;
    }

This time, the future will be of the time `std::future<int>` and thus
`get()` will also return an `int`. `std::async` will again
launch a task in an asynchronous way and `future.get()` will wait for the
answer. What is interesting, is that you can do something else before the call
to future.

But `get()` is not the only interesting function in `std::future`.
You also have `wait()` which is almost the same as `get()` but does
not consume the result. For instance, you can wait for several futures and then
consume their result together. But, more interesting are the
`wait_for(duration)` and `wait_until(timepoint)` functions. The
first one wait for the result at most the given time and then returns and the
second one wait for the result at most until the given time point. I think that
`wait_for` is more useful in practices, so let's discuss it further.
Finally, an interesting function is `bool valid()`. When you use
`get()` on the future, it will consume the result, making `valid()
returns `false`. So, if you intend to check multiple times for a future,
you should use `valid()` first.

One possible scenario would be if you have several asynchronous tasks, which is
a common scenario. You can imagine that you want to process the results as fast
as possible, so you want to ask the futures for their result several times. If
no result is available, maybe you want to do something else. Here is a possible
implementation:

.. code:: c++

    #include <thread>
    #include <future>
    #include <iostream>
    #include <chrono>

    int main(){
        auto f1 = std::async(std::launch::async, [](){
            std::this_thread::sleep_for(std::chrono::seconds(9));
            return 42;
        });

        auto f2 = std::async(std::launch::async, [](){
            std::this_thread::sleep_for(std::chrono::seconds(3));
            return 13;
        });

        auto f3 = std::async(std::launch::async, [](){
            std::this_thread::sleep_for(std::chrono::seconds(6));
            return 666;
        });

        auto timeout = std::chrono::milliseconds(10);

        while(f1.valid() || f2.valid() || f3.valid()){
            if(f1.valid() && f1.wait_for(timeout) == std::future_status::ready){
                std::cout << "Task1 is done! " << f1.get() << std::endl;
            }

            if(f2.valid() && f2.wait_for(timeout) == std::future_status::ready){
                std::cout << "Task2 is done! " << f2.get() << std::endl;
            }

            if(f3.valid() && f3.wait_for(timeout) == std::future_status::ready){
                std::cout << "Task3 is done! " << f3.get() << std::endl;
            }

            std::cout << "I'm doing my own work!" << std::endl;
            std::this_thread::sleep_for(std::chrono::seconds(1));
            std::cout << "I'm done with my own work!" << std::endl;
        }

        std::cout << "Everything is done, let's go back to the tutorial" << std::endl;

        return 0;
    }

The three tasks are started asynchronously with `std::async` and the
resulting `std::future` are stored. Then, as long as one of the tasks is
not complete, we query each three task and try to process its result. If no
result is available, we simply do something else. This example is important to
understand, it covers pretty much every concept of the futures.

One interesting thing that remains is that you can pass parameters to your task
via `std::async`. Indeed, all the extra parameters that you pass to
`std::async` will be passed to the task itself. Here is an example of
spawning tasks in a loop with different parameters:

.. code:: c++

    #include <thread>
    #include <future>
    #include <iostream>
    #include <chrono>
    #include <vector>

    int main(){
        std::vector<std::future<size_t>> futures;

        for (size_t i = 0; i < 10; ++i) {
            futures.emplace_back(std::async(std::launch::async, [](size_t param){
                std::this_thread::sleep_for(std::chrono::seconds(param));
                return param;
            }, i));
        }

        std::cout << "Start querying" << std::endl;

        for (auto &future : futures) {
          std::cout << future.get() << std::endl;
        }

        return 0;
    }

Pretty practical :) All The created `std::future<size_t>` are stored in
a `std::vector` and then are all queried for their result.

Overall, I think `std::future` and `std::async` are great tool that
can simplify your asynchronous code a lot. They allow you to make pretty
advanced stuff while keeping the complexity of the code to a minimum.

I hope this long-due post is going to be interesting to some of you :)
The code for this post is available `on Github <https://github.com/wichtounet/articles/tree/master/src/threads/part5>`_

I do not yet know if there will be a next installment in the series. I've
covered pretty much everything that is available in C++11 for concurrency. I may
cover the parallel algorithms of C++17 in a following post. If you have any
suggestion for the next post, don't hesitate to post a comment or contact me
directly by email.
