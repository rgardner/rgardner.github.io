---
layout: project
title: Projects
---

I have had the opportunity to work on a lot of cool projects. This page is my
chance to explain what I've learned, what interests me, and what direction I am
headed.

{% for project in site.projects %}
  {% if project.title %}
    <a href="{{ project.url }}">{{ project.title }}</a>
  {% endif %}
{% endfor %}
