---
layout: resource
title: Resources
---

Here I am documenting a collection of resources that I've found helpful over the
years. Most of them are software related, but some are about NYC and NYU, fun
books I've read - anything!

Because this is Git, anyone out there can contribute back to these easily! See
that "Fork me on GitHub" ribbon at the top of the page? That's your cue to peak
behind the covers and edit anything you find here. You can even make all the
changes on GitHub without having to download anything to your computer! Though
you should totally learn Git and Version Control.

<ul>
{% for resource in site.resources %}
  <li><a href="{{ resource.url }}">{{ resource.title }}</a></li>
{% endfor %}
<ul>
