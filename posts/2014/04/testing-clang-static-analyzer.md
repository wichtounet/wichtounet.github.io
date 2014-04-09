I recently started a bit of work on my compiler (eddic) again. I started by adapting it to build on CLang with libc++. There was some minor adaptions to make it compile, but nothing really fancy. It now compiles and runs fine on LLVM/Clang 3.4 with the last version of libc++. I'm gonna use some features of C++14 in it and I plan to refactor some parts to make it more *STL-correct*. I also plan to use only CLang on eddic right now, since C++14 support of GCC is not released right now. 

I decided it was a good time to try again the CLang static analyzer. 

## Installation

If, like me, you're using Gentoo, the static analyzer is directly installed with the *sys-devel/clang* package, unless you disabled the *static-analyzer* USE flag. 

If your distribution does not ship the static analyzer directly with CLang, you'll have to install it manually. To install, I advise you to follow the [Official Installations instruction](http://clang-analyzer.llvm.org/installation.html). 