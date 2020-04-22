---
layout: post
title: galvanize prep (module 0 finished)
date: 2020-04-21
---

Finished up Module 0 of the [Galvanize prep course](https://www.galvanize.com/web-development/prep). Pretty late, so I just wanted to jot down some closing thoughts.

So far I've been able to get away with not watching a lot of the videos. A lot of the concepts I'm familiar with, it's just a matter of learning new names and new syntax. For some reason, when I declare a for loop, I keep using a comma instead of a semicolon, but ONLY on the last one. Two semicolons, and then a mistake comma- every time. 

On reflection, the syntax is a lot like declaring function parameters. Declaring a function and declaring a for loop both use () braces, but in the former parameters are separated by commas, and in the latter statements are separated by semicolons. I suspect the issue is how it's being parsed, where the for loop () braces are parsed as sequential statements, and [maybe I'm right](https://stackoverflow.com/questions/15485735/use-of-commas-versus-semicolons).

Ideas like the semicolons are also a little more formal than Python. Stylistically, I'm trying to be rigorous in including them instead of relying on the Automatic Semicolon Insertion. Although on further reflection, it's interesting how the design choices in this respect have translated to one feeling more "formal". Because in fact, I suspect that the use of semicolons in JS means that indenting purely sylistic. Whereas in Python, doing away with the braces and the semicolons means that indenting lines are necessary for code to parse correctly. This I was not able to confirm with a 30 second google search, ~a 30s goog if you will~ (nevermind, bleh).

I definitely feel like I'm just easing into things though, and I'd love to get cracking both on new concepts, and learning new things to actually start building things.

The other thing on my list to check out is more open-source project, just to get some exposure to the kinds of professional, production-level codebases, so I can start setting my expectations to what I should be able to accomplish.