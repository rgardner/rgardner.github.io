---
layout: project
title: Virtual Painting
---

In Fall 2018, Nicole and I collaborated on a "Virtual Painting" photo booth
experience for her Master's Thesis. From [the README][readme]:

> Be who you want to be! Virtual Painting is a fun photo booth experience
> where you can take a selfie and then construct a new identity. This project
> is intended to be deployed in an exhibition environment, so it automatically
> resets back to the photo booth screen after 15 seconds of inactivity.

<https://github.com/rgardner/Virtual-Painting>

## Architecture

Virtual Painting is written in C# and uses the [Model-view-viewmodel](mvvm)
architectural pattern. The core photo booth experience is implemented as a
state machine using the [Stateless](stateless) library.

[mvvm]: https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93viewmodel
[stateless]: https://github.com/dotnet-state-machine/stateless

[readme]: https://github.com/rgardner/Virtual-Painting#readme
