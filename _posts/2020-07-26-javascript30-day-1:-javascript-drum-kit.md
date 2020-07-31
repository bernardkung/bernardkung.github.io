---
layout: post
title: Javascript30 Day 1 - Javascript Drum Kit
date: 2020-07-26
---

##[Page Link](http://www.bkung.com/projects/01/drumkit.html)

## Introduction

I've been looking for projects to work on since finishing up Colt Steele's [Web Developer Bootcamp](https://www.udemy.com/course/the-web-developer-bootcamp/) course on Udemy, and I came across [Javascript30](javacript30.com)- a set of 30 free exercises in CSS and vanilla JS. 

## Starter

Starter file includes a basic webpage showing divs with the keys A-L (as laid out on a keyboard) and a corresponding sound for each. The goal is to play the corresponding sound and highlight the corresponding div when its corresponding key is pressed. The HTML was already structured in two sets of divs: one set of div tags to display the keys on the page, and one set of audio tags with the audio for each key. Both the div tags and the audio tags had "data-key" attributes equal to their corresponding key.

## Process

My general strategy was to detect a keypress event, then play a sound, and finally flash the div.
Luckily Colt had covered keypress events in his course, but I was rusty on a lot of stuff. First was a quick review of how to select elements in the DOM using JS. This meant both a general review of how to actually do this (i.e querySelector, getElementById, etc.), this covered the basics of selecting by name, id, and class; but I had never had to select by these HTML5 "data-" attributes. This involved learning more about querySelectorAll to select attributes, and then unusually the syntax inside as well. To select "data-key" equal to 65, it uses a single "=" as opposed to the "===" that is typical to JS. 

After some learning, this was fairly straightforward. Set an eventListener to detect keypress, and based off that I would need to play the audio and highlight the key.

Playing the audio was also something new- Colt Steele had covered making a Patatap clone very similar to this project, but audio had been handled through Howler.js. So it was off to studying how to play audio through vanilla JS, which involved a lot of trial and error to get the syntax right as I tabbed back-and-forth with the Mozilla Developer Network Web Docs.

Finally, there was quite a bit of challenge with the highlighting. Part of this was inexperience with the layout of the course. It's not clearly delineated in the video when the explanation ends and the solution explanation begins so I had stopped too early.  Luckily, I had a look through the provided CSS and noticed that a "highlight" class was already provided, and was explained in the video. It was fairly straightforward after that to set the "keypress" event to both play the audio and apply the "highlight" class.

However, the highlight is only a momentary flash, so I had to remove the "highlight" class. My solution was to set a simple setTimeout(), which I had worked with before. Basically I just removed the "highlight" class half a second after it was applied.

In review of the provided solution, I learned a few new things. One was animations: in the provided solution, the key div has a transition style applied in its CSS which I had overlooked. An eventListener was added to watch for the end of the transition to then trigger the removal of the class. So I learned about transforms, the transition style, and both about a new specific eventListener as well as to be more open-minded about what eventListener was actually capable of listening for.


## Things Learned

- Using querySelectorAll to select for attributes, as well as selecting for specific attributes.
- Playing audio
- Transform and transition CSS styles.
- Expanded understanding of what eventListener is capable of.

