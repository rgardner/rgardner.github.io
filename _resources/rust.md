---
layout: resource
title: Rust
---

## Introduction

[Rust](https://www.rust-lang.org/) is a programming language focused on
performance and memory safety. It offers similar runtime performance to C and
C++, but prevents buffer overflows and data races without a garbage collector
through stronger compile-time checks.

```rust
fn main() {
    println!("Hello, world!");
}
```

You can try out Rust with zero setup in the [playground](https://play.rust-lang.org/).

## Learning Resources

### Getting Started

If you are first starting out with Rust, I recommend reading
["The Rust Programming Language" book][rust-book] available online. I read the
first edition and most of the second edition and it covers everything you
need to get started and understand the fundamentals. It contains example
projects to work through as well as comparisons to other languages. The
["Learn"][rust-learn] page on the official Rust website contains other
resources in case reading a book is not your thing.

### Next Steps

Once you've learned the fundamentals of Rust, there are tons of resources to
explore writing different types of programs.

If you want to write a simple command line interface (CLI) program, the Rust
CLI Working Group put together [a small book][rust-cli]. It recommends crates
(aka libraries) to write ergonomic and well-documented CLIs, as well as
crates for testing.

While you are writing your Rust programs, the Rust compiler will provide tons
of feedback :) Every compiler error has additional information, including
correct/incorrect examples, to help you better understand the error. e.g.
`rustc --explain E0382`. In addition, I strongly recommend setting up
[clippy][clippy] as soon as possible on your projects. It guides you to
writing idiomatic and performant APIs through static analysis on your Rust
projects.

If you are looking for example code in various domains (e.g. error handling,
file handling, threads), [Rust by Example][rust-by-example] contains dozens
(if not hundreds) of small snippets and example programs.

Rust has become popular for writing [WebAssembly][wasm] (wasm) web applications
because Rust has a rich library ecosystem and does not have a garbage
collector. The ["Rust And WebAssembly" Book][rust-wasm] teaches you
everything you need to know to get started writing Rust wasm web apps by
walking you through an interactive [Conway's Game of Life][conway] tutorial
built in Rust compiled to wasm with a TypeScript-based UI.

Rust competes with C++ and Go for writing fast I/O-bound applications. Rust's
async ecosystem has matured tremendously in 2020 after the stabilization of
async/await. [Tokio][tokio] is arguably the most popular async framework and
has a great [tutorial][tokio-tutorial] to help you learn the ins and outs of
using Tokio to write multi-threaded Rust code.

If you want to publish your own *crate*, look over the [Rust API
Guidelines][rust-api]. It covers tips for making your code easier to use and
debug in other programs, including writing effective documentation and
versioning your APIs.

### Advanced

If you want to learn more about Rust's Package manager, cargo,
["The Cargo Book"][cargo-book] explains the `Cargo.toml` file format,
[workspaces][cargo-workspaces], [profiles][cargo-profiles],
[build scripts][cargo-build-scripts], and more.

["The Rust Performance Book"][rust-perf] contains mostly Rust-specific
performance tips.

## Reference

### Tooling

To quickly add, remove, and upgrade dependencies, I use [Cargo Edit][cargo-edit].
Fun fact, I wrote the original implementation of `cargo rm`.

I use [Visual Studio Code][vscode] as my preferred editor for writing Rust
applications. The [Rust Analyzer][rust-analyzer] extension is a must and provides
fantastic intellisense, editor hints for running individual tests, auto imports,
parameter hints, and more. Seriously, VS Code + Rust Analyzer is an amazing
combination. I also use the [crates][vscode-crates] extension to show me
outdated dependencies when viewing `Cargo.toml` files in VS Code.

### Crates

* [StructOpt](https://github.com/TeXitoi/structopt)

[cargo-book]: https://doc.rust-lang.org/cargo/index.html
[cargo-build-scripts]: https://doc.rust-lang.org/cargo/reference/build-scripts.html
[cargo-edit]: https://github.com/killercup/cargo-edit
[cargo-profiles]: https://doc.rust-lang.org/cargo/reference/profiles.html
[cargo-workspaces]: https://doc.rust-lang.org/cargo/reference/workspaces.html
[clippy]: https://github.com/rust-lang/rust-clippy
[conway]: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
[rust-analyzer]: https://marketplace.visualstudio.com/items?itemName=matklad.rust-analyzer
[rust-api]: https://rust-lang.github.io/api-guidelines/
[rust-book]: https://doc.rust-lang.org/book/
[rust-by-example]: https://doc.rust-lang.org/rust-by-example/index.html
[rust-cli]: https://rust-cli.github.io/book/index.html
[rust-learn]: https://www.rust-lang.org/learn
[rust-perf]: https://nnethercote.github.io/perf-book/title-page.html
[rust-wasm]: https://rustwasm.github.io/docs/book/
[tokio-tutorial]: https://tokio.rs/tokio/tutorial
[tokio]: https://tokio.rs/
[vscode-crates]: https://marketplace.visualstudio.com/items?itemName=serayuzgur.crates
[vscode]: https://code.visualstudio.com/
[wasm]: https://webassembly.org/
