It has been too long again since I wrote here. But with family, my other blog and work, I did not get a chance to write here for a while.

Today is going to be a short update. I recently updated my main projects to use C++26. There is not much I can use at this point, but I have upgraded my compilers to GCC-15 and Clang-20 so that I can access most things. I will probably do some minor updates of the code in the coming weeks/months to see what I can add. What I am really waiting for is the concepts and the meta-programming, which are not yet in the base compilers. These two features are really going to make a huge difference on how we write C++ code.

In the last two months, I have started learning some Rust. Since I believe the best way to learn a language is by writing code, I quickly got into coding. I have ported a (small) part of my ETL and DLL libraries to Rust. I came to the point where I can train a simple Dense Neural Network on MNIST and it works. Of course, I also tried to make it as fast as possible. Currently, it is relatively close to at about 30% slower than ETL on a CPU and without MKL.

Overall, Rust is an interesting language. Its borrow checker and strong compiler contracts are definitely making the code safer. On the other hand, it also makes the code very strict. And some things that are very easy to write in C++ become very difficult to write in Rust. 

Here are some of the issues I found with Rust:

1. The generics are very limited. Compared to the level of meta-programming we can do in C++ with templates, the comparison does not even start. Everything must be tied to Traits (a bit like concepts in this case) and we can't specialize code based on the type.
2. The SIMD library is also quite limited. I am currently using the `portable-simd` library from nightly Rust and it gets the job done. But we are again limited to the common interface between integers and floating points since we cannot specialize and unfortunately, some of the things are not defined for both. For instance, I could not get FMA in my code and I cannot easily tune the size of the vectors to the types.
3. Because of the borrow-checker, we are also not allowed to do some expressions where we mix mutable and immutable references, like `x = b * x + d` (x is once mutable and once immutable), so we either need to do two operations (slow) or do some inplace wrappers instead of relying on expressions (ugly
4. Currently, there is a lot of overhead to the parallelism I used (through `rayon`). Compared to simply using a simple thread pool, this is quickly much more complicated and apparently much more overhead. I am using much higher thresholds for parallelizing operations in my Rust library than I am in C++.

I should still mention that this was probably not the best project to start in Rust since C++ excels at templates while Rust does not. But it was fun. And it was not that difficult for me to quickly get into Rust. But it will take a longer time to become an expert.

While I enjoy writing Rust, I do enjoy writing C++ much more, so I really hope I can keep on writing C++ for a long time.

What about you? Anybody tried Rust?
