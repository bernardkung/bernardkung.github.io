---
layout: post
title: Javascript Crash Course Day 1
date: 2020-04-19
---

Started working through the HackReactor/Galvanize Software Engineering Basic Prep today.
One of the things I did to chart a course was to go through and request syllabi for a bunch of different bootcamps and compare to determine what to study. HackReactor didn't have a syllabus, but it did require an admission test, and more importantly, provided a free crash course to prep. 

## Thoughts on Similarities

It's pretty helpful. I'm shooting through it pretty quickly because of my experience with Python, and somewhat guiltily, VBA too. In terms of variables and operators it's basically the same as Python, although the Number data type in Javascript vs the int, float, and complex is a change. Stranger still is that there's both parseInt() and parseFloat() functions.
I did learn about the *= and /= operators. Not sure how I skipped over that in Python, but it makes sense in hindsight.

Otherwise, concepts like Python Lists = Javascript Arrays, but Javascript Objects are definitely not analaguous. What they do remind me a lot of are VBA Variants. But other ideas like how Python dictionaries make a lot of the key-value behavior that a JS Object can handle make sense. The syntax of explicitly declaring variables reminds me a lot of VBA as well.

Just some quick thoughts, it's pretty straightforward for now.

## A Spontaneous Project

Oh, I also slapped together a [quick Python script](https://github.com/bernardkung/bernardkung.github.io/blob/master/create_post.py) for creating these blog posts. Basically it just prompts the user to enter a title, and it'll automatically reformat since I also need a variation with the date appended, the markdown file format appended, and the spaces replaced with dashes. It'll create a file in the required location, and put in the required heading. 