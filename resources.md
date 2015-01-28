---
layout: resource
title: Resources
---

Here I am documenting a collection of resources that I've found helpful over
the years. These can be related to life in NYU and NYC, they can be about
software development and computer science research, fun books I've read -
anything!

Because this is Git, anyone out there can contribute back to these easily! See
that "Fork me on GitHub" ribbon at the top of the page? That's your queue to
peak behind the covers and edit anything you find here. You can even make all
the changes on GitHub without having to download anything to your computer!
Though you should totally learn Git and Version Control.

{% for resource in site.resources %}
  <a href="{{ resource.url }}">{{ resource.title }}</a>
{% endfor %}
