One week ago, zapcc 1.0 was released and it showed much faster than the other
compilers in terms of compile time. This can be seen when
`I tested it on my Expression Templates Library (ETL) <http://baptiste-wicht.com/posts/2017/03/release-zapcc-10-fast-cpp-compiler.html>`_. It was almost four
times faster than clang 3.9 and about 2.5 times faster than GCC.

The ETL library is quite heavy to compile, but still reasonable. This is not the
case for my Deep Learning Library (DLL) where compiling all the test cases takes
a very long time. I have to admit that I have been going overboard with
templates and such and I have now to pay the price. In practice, this is not
a huge problem since only one or two neural networks will be compiled, but in
the test cases, there are hundreds of them and this is a huge pain. Anyway,
enough with the ramble, I figured it would be very good to test zapcc on it and
see what I can gain from using it.

Results
+++++++

However, I soon realized that I would have more issues than I thought. The first
problem is the memory consumed by zapcc. Indeed, it is based on clang and
I always had problem with huge memory consumption from clang on this library and
zapcc has even bigger memory consumption because some information is cached
between runs. When zapcc goes over the memory limit, it simply wipes out its
caches. This means, all the gain for the next compilation will be lost.

When I tried compiling using several threads, it soon used all my memory and
crashed. The same occurs with clang but I can still compile with 3 or 4 threads
without too much issues on this computer. The same also occurs but it can still
handle 4 or 5 threads (depending on the order of the compilation units).

The tests are performed on my desktop computer at work, which is not really
good... I have 12Go (I had to ask for extra...) of RAM and an old Sandy Bridge
processor, at least I have an SSD (also had to ask for extra).

I started with testing with only one compiler thread. For zapcc, I set the
maximum memory limit to 8Go. Even with such a limit, the zapcc server restarted
more than 10 times during the compilation of the 84 test cases. After this
first, I increased the number of threads to two for each compiler, using 4Go
limit for zapcc. Even with two threads, I was unable to finish a compilation
with zapcc. Moreover, a big problem with that is that the servers are not killed
when there is no no more memory, they just hang and use all the memory of the
computer which is really inconvenient for server processes. When this happens
with clang or gcc, the compiler simply crashes and the memory is released. Since
zapcc is not able to work with more than one thread on this computer, the
results are taken from one thread. I was also surprised to be able to compile
the library with clang and four threads, this was not possible before clang-3.9.

+----------------------------+-------------+-------------+------------+------------+
| Compiler                   |   -j1       |   -j2       |   -j3      |   -j4      |
+============================+=============+=============+============+============+
| gcc-4.9.3                  | 2250.95     | 1256.36     | 912.67     | 760.84     |
+----------------------------+-------------+-------------+------------+------------+
| gcc-5.3.0                  | 2305.37     | 1279.49     | 918.08     | 741.38     |
+----------------------------+-------------+-------------+------------+------------+
| clang-3.9                  | 2047.61     | **1102.93** | **899.13** | **730.42** |
+----------------------------+-------------+-------------+------------+------------+
| zapcc-1.0                  | **1483.73** | 1483.73     | 1483.73    | 1483.73    |
+----------------------------+-------------+-------------+------------+------------+
|   Difference against Clang | -27.55%     | +25.69%     | +39.37%    | +50.77%    |
+----------------------------+-------------+-------------+------------+------------+
|   Speedup VS GCC-5.3       | -35.66%     | +13.75%     | +38.09%    | +50.03%    |
+----------------------------+-------------+-------------+------------+------------+
|   Speedup VS GCC-4.9       | -34.08%     | +15.30%     | +38.50%    | +48.75%    |
+----------------------------+-------------+-------------+------------+------------+

If we look at the results with only one thread, we can see that there still are
some significant improvements when using zapcc, but nowhere need as good as what
was seen in the compilation of ETL. Here, the compilation is reduced by 34%
compared to gcc and 27% compared to clang. This is not bad, since it is faster
than the other compilers, but I would have expected better speedups. We can see
that g++-4.9 is slightly faster than g++-5.3, but this is not really
a significant difference. I'm actually very surprised to find that clang is
faster than g++ on this experiment. On ETL, it is always very significantly
slower and before, it was also significantly slower on DLL. I was so used to
this state, that I stopped using it on this project.  I may have to reconsider
my position.

Let's look at the results with more than two threads. Even with two threads,
every compiler is faster than zapcc. Indeed, zapcc is slower than Clang by 25%
and slower than GCC by about 15%. If we use more threads, the other compilers
are becoming even faster and the slowdowns of zapcc are more important. When
using four threads, zapcc is about 48% slower than gcc and about 50% slower than
clang. This is really showing one big downside of zapcc that has a very large
memory consumption. When it is used to compile really heavy template code, it is
failing early. And even when there is enough memory, the speedups are not as
great as for relatively simpler code.

Some may argue that this is not a fair comparison since zapcc does not have the
same numbers of threads. However, considering it is the best zapcc can do on
this machine, I would argue that this is a fair comparison in this limited
setting. If we were to have a big machine for compilation, which I don't have at
work, the zapcc results would likely be more interesting, but in this specific
limited case, it shows that zapcc suffers from its high memory consumption. It
should also be taken into account that this experiment was done with almost
nothing else running on the machine (no browser for instance) to have as much
memory as possible available for the compilers. This is not a common use case.
Most of the days, when I compile something, I have my browser open, which makes
a large difference in memory available, and several other applications.j

This experiment made me realize that the compilation times for this library were
quickly going crazy. Most of the time, the complete test suite is only compiled
on my Continuous Integration machine at home which has a much processor and much
more RAM. Therefore, it is relatively fast since it uses more threads to
compile.  Nevertheless, this is not a good point that the unit tests takes so
much time to compile. I plan to split the test cases in several sets. Because,
currently the unit tests are compiled with the performance tests and other
various tests. I'll probably end up generating three executables. This will help
greatly during development. Moreover, I also have a technique to decrease the
compilation time by erasing some parameters. This is already ready, but has
currently a runtime overhead that I will try to remove and use this technique
everywhere to get back to something reasonable. I'll also try to see if I can
find obvious compilation bottlenecks in the code.

Conclusion
++++++++++

To conclude, while zapcc brings some very interesting compilation speedups in
some cases like in my ETL library, it also has some downsides, namely
**huge memory consumption**. This memory consumption may prevent the use of several
compiler threads and render zapcc much less interesting than other compilers.

When trying to compile my DLL library on a machine with 12Go of RAM with two
zapcc threads, it was impossible to make it complete. While zapcc was faster
with one thread than the other compilers, they were able to use up to four
threads and in the end **zapcc was about twice slower than clang**.

I knew that zapcc memory consumption was very large, but I would have not have
expected something so critical. Another feature that would be interesting in
zapcc would be to set a max memory hard limit for the server instead of simply
a limit on the cache they are able to keep in memory. This would prevent hanging
the complete computer.

For now, I'll continue using clang on this DLL project and use zapcc only on my
ETL project. I'll also focus on improving the compilation time on this project
and make it reasonable again.
