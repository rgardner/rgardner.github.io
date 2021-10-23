---
layout: resource
title: Chrome Developer Tools Tips
---

<https://www.youtube.com/watch?v=2zmUSoVMyRU>

1. Use JQuery selector
  - Use `document.querySelector` and `document.querySelectorAll` to find
    elements by selector (without JQuery)
  - `document.querySelectorAll` is aliased by `$$`
2. To not lose console session when refreshing page, right click console and
  select "Preserve log upon navigation"
3. `document.body.contentEditable = true` allows us to change anything on the
  document.
4. `console.log('Window',window)` to log the object to the console.
5. To look at events for element, use `getEventListeners(element)` to find all
  the different event listeners.
6. call `monitorEvents(element)` to log all events of element to console
  - key events, mouse events, etc.
  - use `monitorEvents(element, 'click')` to only get click events
  - the event can only be an array
  - `unmonitorEvents(element)` to stop logging all events
7. use `console.time('name_of_timer')` that can starts timers
  - `console.timeEnd('name_of_timer')` to stop timer
8. use `console.groupCollapsed('Name')` to group console prints together
  - use `console.groupEnd()` to stop the group
9. use `console.table(myArray)` to create object table for array
10. use `$_` to access last result of console
11. use `clear()` to clear console; `ctl-L`
12. get stack via `console.trace()`
13. use `console.count('name')` to count the number of times this gets hit
14. use `profile('function')` to start profiling and `profileEnd('function')`
  to stop profiling
15. use `dir(element)` to list all of the properties of the object
16. use `inspect(element)` to immediately go to the element in the elements
  area of the debugging tools
17. use `$0` to get last selected element, `$1` for second to last, all the way
  up to `$4`
