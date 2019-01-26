---
layout: post
title: Raspberry Pi Console Cable
tags: [nikola, raspberry-pi]
---

Where have you been all my life.

That's how this cable makes me feel. Let me show you a magical cable that
allows you to log into the Raspberry Pi shell from your computer, be it
Windows, Mac, or Linux. If you are connecting to a Raspberry Pi 1 model, then
this is all you need. For the Raspberry Pi 2, you will need an external power
supply to power the Raspberry Pi, as the console cable does not supply enough
power.

<!-- more -->

![Raspberry Pi Console
Cable](https://learn.adafruit.com/system/assets/assets/000/003/119/original/learn_raspberry_pi_console_cable.jpg?1396791620)

That's it. Four pins on one side, a standard USB 2.0 plug on the other end.
After at most 5 minutes of software installation, you can now connect the
console cable to your computer and Raspberry Pi and voilà, you can now log in
to your Raspberry Pi on your laptop.

I won't go into much detail here on how to get this amazing setup working with
your hardware, the [Adafruit
tutorial](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-5-using-a-console-cable/overview)
on this topic does a much better job.  But what I will say, is that after
installing the drivers and connecting the console cable to my Raspberry Pi and
laptop, I only have to run the command:

```
screen /dev/cu.usbserial 115200
```

to connect to my Raspberry Pi from my Mac.

After a semester and a half of pain in my energy research because of networking
issues and having to find the rest of the computer - keyboard, mouse, display,
and cables - this little cable is a godsend.

Here are some cases where the cable is already helping me:
- I set up a new Raspberry Pi without a keyboard and monitor.
- I misconfigured the network interface on the Raspberry Pi and couldn't
  connect via SSH, so console cable to the rescue!

I am a big fan of Adafruit, so [here's a link to buy it from
them](https://www.adafruit.com/products/954). You can also find similar cables
across the net, but YMMV. While you don't need this cable to use the Raspberry
Pi, it allows me to fix problems faster and get on with my research.
