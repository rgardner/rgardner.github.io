---
layout: resource
title: Python
---

I love the Python programming language. Python is cross-platform, open-source,
and has a wide array of use cases:

- small utilities
- data analysis
- web scraping
- websites and web apps

and probably most importantly, it is an excellent teaching language.

For people new to programming in general and Python specifically, I recommend
the [Intro to Computer Science by](https://www.udacity.com/course/cs101) course
from [Udacity](https://www.udacity.com/)

While this course was great for learning the syntax and logic with the
language, I hadn't learned how to run actual Python code on my computer (only
through their web interface). When I came back to Python after my forays in
Java, Bash, and Ruby, I learned from [Learn Python the Hard
Way](http://learnpythonthehardway.org/).

Websites and forums like [Project Euler](https://projecteuler.net/) and
[Reddit's Daily Programmer](http://www.reddit.com/r/dailyprogrammer) were great
for learning more about programming in general and Python language fundamentals
specifically.

The [r/python](https://www.reddit.com/r/programming) subreddit is a great
resource for those who want to read more about the language and the ecosystem
in general. As always, forums like [Hacker News](https://news.ycombinator.com/)
and [r/programming](https://www.reddit.com/r/programming) are excellent
resources because they expose you to many different parts of programming,
Computer Science, and the intersections of those with the rest of the world.

Tools I use to develop Python applications:

- Code formatter: [Black](https://github.com/psf/black)
  - Current go to formatter. I previously used [yapf](https://github.com/google/yapf),
    but I like that Black is managed by the Python Software Foundation and it is
    easier to use in CI (`black --check .`)
- Static analysis: [mypy](https://github.com/python/mypy)
  - Optional static type checking. Using Python's type annotations, the `mypy`
    command line tool warns you of type violations, e.g. passing an int to a
    function that expects a string.
- Static analysis: [pylint](https://www.pylint.org/)
- Testing: [pytest](https://docs.pytest.org/en/latest/)
