---
layout: post
title: Javascript30 Day 2 - JS and CSS Clock
date: 2020-07-27
---

## [Page Link](http://www.bkung.com/projects/02/clock.html)

## Introduction

Given a starter HTML page pre-styled with a clock face and three clock hand divs, create a simple clock using just vanilla JS and CSS.

## Process

My initial plan was to select each clockhand div in JS, set their initial position based on the current time, and then rotate each hand based on their time.

Selecting each clockhand div was fairly straightforward by doing a getElementsByClassName since each clockhand div had a unique class. This seemed open and shut, but it turns out it always returns a list of DOM elements- so I subset the list. Alternatively, I could use querySelector as per the solution file provided.

Setting their initial position required getting the time. This involved reading around the MDN Web Docs for date functions, but was fairly straightforward. Set a date variable, and then from that extract the hour, minute, and second using the getHours(), getMinutes(), and getSeconds() functions respectively.

The next part of this involved translating the time to a relative clock position. I wrote a simple function to translate an integer, identified as either an hour, minute, or second, to a respective angle in the circle. 

To actually tick the clock, I ended up referring to the solution. The end result was very similar to day 1 involving the use of transforms- in this case a cubic-bezier transform-timing-function as well as a transition timing to create a physical clock "tick" animation. A lot of inexperience here, as I didn't even know where to begin tackling animation despite day 1.

Finally, in the midst of doing this in conjunction with the solution file it became apparent that I didn't need to set an initial position of the clock hands, and then update it. I simply needed to run a setInterval function every second and update each clock hand position.

## Things I Learned

- More about animations were the top. It's clear that I need to tackle more of the JS and CSS that work with animations.
- Basics of working with dates and times in JS.
