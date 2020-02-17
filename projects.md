---
layout: resource
title: Projects
---

Here is a curated list of projects that I enjoyed working on and/or
contributing to:

<ul>
{% for project in site.projects %}
<li><a href="{{ project.url }}">{{ project.title }}</a></li>
{% endfor %}
</ul>
