---
layout: post
title: C++ Function Try Block
tags: [cpp]
---

Most of my code reviews are for C++ code and every so often, a commit or review
comment reminds me of a nuanced C++ feature I need to study more closely.
Recently, it was a teammate leaning on the [function try
block][cpp-function-try], a feature I usually avoid because it behaves
differently depending on where you use it.

A function try block lets you wrap an entire constructor, destructor, or free
function in `try { ... } catch { ... }`, giving you access to parameters when an
exception is thrown before the body even runs. On paper that sounds simple, but
the rules change just enough between constructors, destructors, and regular
functions that it's easy to shoot yourself in the foot.

This post is the field notes from that review: when the feature helps, the traps
I bumped into, and why I still reach for it only when there's no cleaner option.

<!-- more -->

## Constructors

The main selling point of the function try block is that it allows you to
handle exceptions thrown during the initialization of member variables in a
constructor that otherwise could not be caught by the class author.

```cpp
class my_class {
 public:
  my_class(std::string str) try : str_{str} {
    // A catch block here would not catch exceptions thrown by the member
    // initializer list, in this example, the std::string copy constructor.
  } catch (const std::exception& e) {
    // You can log, modify the exception, throw a different exception, or abort
    // the program, but you cannot use a return statement (compiler error).
    // The constructor parameters are available here, which is especially useful
    // for logging.
  }  // implicit "throw;" here

 private:
  std::string str_;
};
```

In real production code, I've seen this feature used for logging. Another valid
use case is to throw a different exception, e.g. at an API boundary.

The implicit `throw;` at the end of the catch block is a bit of a gotcha. It
makes sense if you consider that the constructor is expected to fully initialize
the object, and an exception thrown during construction would leave the object
in a partially constructed state.

## Destructors

The implicit behavior varies for constructors, destructors, and regular
functions, and to me, makes it too complicated to generally recommend using
outside of constructors and macros (more on that later).

| Function Type               | Implicit Behavior                                              | Explicit Return Statement Allowed |
| --------------------------- | -------------------------------------------------------------- | --------------------------------- |
| Constructor                 | `throw;`                                                       | No (illegal, compiler error)      |
| Destructor                  | `throw;`                                                       | Yes                               |
| Void-returning function     | `return;`                                                      | Yes                               |
| Non-void returning function | `return;`, (undefined behavior, may generate compiler warning) | Yes                               |

One of the other use cases I thought of for the function try block is to make it
easier to implement a `noexcept` function without having to indent the entire
function body. And for regular functions, this **is** the implicit behavior if
the end of the catch block is reached. But for destructors, where the
consequence of not catching an exception is aborting the program, the implicit
behavior of the function try block is to rethrow the exception, just like
constructors. Though unlike constructors, you can use an explicit `return;`
statement to suppress it, which makes sense because the object is already fully
destructed and the caller can't continue to use it (unlike a constructor).
Maybe the reason that destructors implicitly `throw;` is because the function
doesn't have a return type and can't signal that it violated its postcondition,
requiring the catch handler to explicitly spell out via `return;` that it
handled the exception.

Example:

```cpp
class function_try_dtor {
 public:
  ~function_try_dtor() noexcept try {
  } catch (...) {
    // handle exception
    return;
  }
};
```

While Clang recognizes this as correctly implementing the `noexcept`
specification, MSVC still emits a warning:

```
warning C4297: 'function_try_dtor::~function_try_dtor': function assumed not to throw an exception but does
<source>(7): note: destructor or deallocator has a (possibly implicit) non-throwing exception specification
```

Because of this, I recommend implementing `noexcept` destructors with normal
try-catch blocks inside the destructor body.

To wrap up constructors and destructors, another gotcha is that accessing member
variables in the catch handler is undefined behavior. In practice, Clang emits a
warning, but MSVC does not.

## Regular Functions

For regular functions, the implicit behavior if the end of the catch block is
reached is to return, which is useful for implementing a `noexcept` function.
But, if the function has a non-void return type, it's undefined behavior if the
catch block ends without an explicit return or throwing an exception. Clang and
MSVC both emit a warning for this case.

I have seen a few functions that use function try blocks to handle exceptions,
e.g. by logging and suppressing the exception. In my own code, I prefer to just
indent the entire function body and use a normal try-catch block, or introduce
a separate helper function to avoid mixing logic and error handling in the same
function.

```cpp
void private_api();

void function_try() try {
  private_api();
} catch (const std::exception& e) {
  // handle exception
}

void inner_try() try {
  try {
    private_api();
  } catch (const std::exception& e) {
    // handle exception
  }
}
```

For non-void functions, I think it also makes it clearer that the function with
the try-catch block in the function body is still responsible for returning a
value.

Which do you find more readable?

Where I've seen the benefits of this feature outweigh the complexity is for
handling exceptions consistently at an API boundary. For example:

```cpp
[[noreturn]] void rethrow_current_exception() {
  try {
    throw;
  } catch (const std::exception& e) {
    // log, modify, throw a different exception, or abort the program
  }
}

#define FOO_API_BEGIN try
#define FOO_API_END catch (...) { rethrow_current_exception(); }

void foo_api() FOO_API_BEGIN {
}
FOO_API_END
```

If these macros were instead used within the function body, the entire function
would need to be indented, which seems unnecessary, or they would immediately
call into a helper function, which adds more reading/debugging overhead and
potential for bugs. A drawback of these macros is that contributors need to be
educated on their use, but an advantage is that it's clearer to see that
functions using these macros are handling exceptions consistently.

## Conclusion

I generally avoid using the function try block because of the complexity and the
potential for undefined behavior. I think it's more readable to use a normal
try-catch block, but will use it for constructors and macros when it's the best
tool for the job.

I hope you've found this post a useful supplement to the
[cppreference page][cpp-function-try] for summarizing the differences in
implicit behavior and allowed explicit behavior, as well as practical use cases
and gotchas.

## Appendix: Rust Approach

I use Rust for hobby projects and I often find it interesting to compare how
Rust addresses these problems. In Rust, there aren't constructors, just regular
functions that return a new instance of the `struct` or a `Result` with an
error. The fields of the `struct` are initialized in the function body and the
function must explicitly handle any errors.

```rust
struct MyStruct {
    num: i32,
}

impl MyStruct {
    fn new(str: &str) -> Result<Self, Box<dyn std::error::Error>> {
        let num = str.parse()?;
        Ok(Self { num })
    }
}
```

Here `MyStruct::new` propagates the error from `str.parse` to the caller via
the `?` operator. Values are moved into the `struct` fields and unlike C++
move is implemented by the compiler, so it's not possible to write a throwing
move.

That just leaves destructors. In Rust, the `Drop` trait can be used to add
custom code within the destructor.

```rust
pub trait Drop {
    // Required method
    fn drop(&mut self);
}
```

As you can see, the `drop` method can't return anything, so there's no way to
signal that the destructor failed. As a convention, implementors of `Drop::drop`
suppress any errors that occur, but callers interested in manually handling the
error can explicitly call a separate method that returns a `Result`. An example
of this in the standard library is
[`std::fs::File`](https://doc.rust-lang.org/stable/std/fs/struct.File.html) and
its `sync_all` method. And compared to C++, implementations of `Drop::drop` can
still reference the fields of the `struct` without undefined behavior. It's
important to note that panicking in `drop()`
[can lead to surprising behavior](https://doc.rust-lang.org/std/ops/trait.Drop.html#panics),
so it's generally avoided. Another gotcha is that `Drop::drop` is synchronous
and today async cleanup doesn't have a standard solution ([1][rust-async-cleanup]).

Compared to C++, I find Rust's approach to this problem more consistent and
easier to reason about because it's more explicit and more consistent across
different types of functions.

[cpp-function-try]: https://en.cppreference.com/w/cpp/language/try.html#Function_try_block
[rust-async-cleanup]: https://without.boats/blog/asynchronous-clean-up/
