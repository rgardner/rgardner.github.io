---
layout: project
title: BSH
---

In college, one of my favorite projects was to implement a command line shell
in C in my Computer Systems Organization class, aimed at teaching processes,
signals, and a bit of programming language theory. After the class ended, I
continued the project as [bsh][bsh-c]. This gave me the opportunity to
practice writing data structures, e.g. circular buffers and linked lists.
This project was also a good practice space for cross-platform development
(macOS and Linux support), documentation (via [doxygen][doxygen]), and
[CMake][cmake].

Later in college, I learned about the [Rust][rust] programming language and
re-wrote the program in Rust as [bsh-rs][bsh-rs]. Rust's standard library and
higher level abstractions enabled me to quickly implement many builtin
commands, so I spent more time writing a robust parser and fixing issues in
upstream crates (see [Goals section of the README][bsh-rs-goals]).

[bsh-c]: https://github.com/rgardner/bsh
[bsh-rs]: https://github.com/rgardner/bsh-rs
[bsh-rs-goals]: https://github.com/rgardner/bsh-rs#goals
[cmake]: https://cmake.org/
[doxygen]: https://github.com/doxygen/doxygen
[rust]: https://www.rust-lang.org/
