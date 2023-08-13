eddic is a compiler I'm writing in C++. This compiler is made for EDDI. It is a programming language I invented especially for this compiler. The language is still basic, but it's close to C in its syntax.

## The language

EDDI was first an interpreted language, but I decided to switch to a compiled language in order to learn Linux assembly code. For now, the generated assembly is not really optimized, but I will try to improve it in the same time as my assembly skills.

At this time, the EDDI language supports:

* several types: int, char, bool, strings and structures
* templates
* variables
* Mathematical expressions with +-\*/% operators
* string concatenations
* conditional branches if, else, else if
* boolean expressions for branches and loops
* loops: for, foreach and while
* arrays, both global and local
* function calls
* function overloading
* arrays
* ...

For now, the generated code is 32 bits or 64 bits.

## Building

A compiler supporting the new standard, C++11, is necessary to build the compiler. The compilation has been tested on GCC 4.7 and CLang 3.1 and greater versions. You need Boost 1.47.0 installed on your computer to build this project.

You have to use CMake to build the compiler:

```bash
$ git clone git://github.com/wichtounet/eddic.git
$ cd eddic
$ cmake .
$ make
```

## Usage

You can compile an EDDI source file using the compiler easily. For example, with one of the provided sample:

```bash
$ cd eddic
$ ./bin/eddic samples/asm.eddi
```

That will create a "a.out" file in the current folder. You can then run this file as any other executable on your computer:

```bash
./a.out
```

## Compilation model

The compilation of EDDI Source file to assembly code is made in several phases. You can have a [description of the architecture](https://github.com/wichtounet/eddic/wiki/Architecture) on the wiki.

## More information about the EDDI compiler

The EDDI compiler is available on GitHub under the Boost Software License 1.0: [eddic](https://github.com/wichtounet/eddic).

The ChangeLog of each version of eddic is available [on Github](https://github.com/wichtounet/eddic/blob/develop/ChangeLog).

[All the posts about the EDDI compiler](http://www.baptiste-wicht.com/tag/eddi/)