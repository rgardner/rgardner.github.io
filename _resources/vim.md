---
layout: resource
title: Vim
---

Vim is a text editor. It is modal, meaning it has multiple modes that each have
their own keymappings and commands. At first this will seem limiting, but with
a little time and patience it will start to feel natural.

I first learned Vim when I had to work on the [Spartan] Python package as part
of a summer research job during college. The code only worked on the school's
Linux cluster and I wanted to quickly ramp up without having to install a GUI
on my workstation (and remote in) or figure out how to use Sublime and rsync.

[Spartan]: https://github.com/spartan-array/spartan

## Install

Your machine probably already comes with Vim, but I still like to upgrade to
the latest versions.

```sh
$ brew install macvim  # macOS
$ sudo apt-get install vim  # Ubuntu/Debian
```

## Customization

To customize Vim, you modify the settings and add your own functions in
`~/.vimrc`. My vimrc can be found in my [dotfiles repo].

[dotfiles repo]: https://github.com/rgardner/dotfiles/blob/main/link/.vimrc

## Plugins for other editors and IDEs

Note, I don't have experience with Emacs (yet), but have used Vim emulation in
all of the other editors and IDEs in this list.

- Atom
  + [Vim Mode]
- Emacs
  + [Evil]
- Visual Studio
  + [VsVim]
- Sublime
  + [Vintage]
- Eclipse
  + [Vrapper]
- JetBrains (e.g. PyCharm, RubyMine, IntelliJ)
  + [IdeaVim]


[Vim Mode]: https://github.com/atom/vim-mode
[Evil]: http://www.emacswiki.org/emacs/Evil
[VsVim]: https://visualstudiogallery.msdn.microsoft.com/59ca71b3-a4a3-46ca-8fe1-0e90e3f79329
[Vintage]: https://www.sublimetext.com/docs/2/vintage.html
[Vrapper]: http://vrapper.sourceforge.net/home/
[IdeaVim]: https://plugins.jetbrains.com/plugin/164
