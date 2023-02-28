<a href="https://oscar-defelice.github.io" target="_blank"><img src="https://user-images.githubusercontent.com/49638680/98257151-9f5e5800-1f7f-11eb-9f42-479a4fc6cf24.png" height="125" align="right" /></a>

# Recommender Systems

This is the repository for the Recommender Systems course.

<p align="center">
  <img width="776" alt="image" src="https://user-images.githubusercontent.com/49638680/204351915-373011d3-75ac-4e21-a6df-99cd1c552f2c.png">
</p>

## Introduction

Recommender systems or _recommender engines_ are a set of algorithms that have in common the idea of _suggesting_ a "product" to a user.

It is difficult to determine when this ancient idea was transferred to the IT field, but we know that it has profoundly changed the way we relate to the digital world. Just think of Google, Amazon, Netflix, YouTube, etc., all of these companies base their successes on particular recommendation systems that are particularly efficient.

The extensive use of these systems has contributed greatly to the emergence of the phenomenon known as the " information bubbles"[[1]](#1).
Indeed, the increasing presence of people on social networks and their tendency to inform themselves through these channels has produced important social and political effects, as shown for example in [[2]](#2) or [[3]](#3).

Other problems with the use of recommender systems have emerged when it has been found that these systems can lead to increased levels of anxiety and depression in predisposed individuals [[4]](#4) and generally ruin the online experience, or how they make it much easier for fake news [[5]](#5) and conspiracy theories [[6]](#6) to spread.

Of course, there are not only negative consequences of using these systems.
Many companies have been able to publicize themselves online more effectively (the advertisements being targeted to the "right" users) and at the same time the average user during his online presence has been able to see only products of his interest.

Studies are underway on the possibility of building personalized therapies for each patient, with definitely promising results [[7]](#7).

In conclusion, recommender systems are probably among the applications of machine learning whose study is most useful not only to the professional but also to the ordinary citizen, given their enormous influence in shaping today's society.
For these reasons, understanding and studying how these systems work is important and interesting.

We refer you to the various modules and the lecture index (see below) for timely details; in the meantime, we _recommend_ good learning and good work!

---

## Installation

I strongly recommend creating a virtual environment to isolate package dependencies.
Depending on the operating system, there are various guides and tutorials on how to do this. [Here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) I point to a cross-platform one.

The recommended version of Python is `3.7` (or higher).

Once you have set up your environment, at your favorite command prompt, run

```bash
pip install -r requirements.txt
```

this will install the packages and libraries needed for the course in the appropriate versions.

## Interacting with online notebooks

The free _Binder_ service, allows you to access an already configured environment and run notebooks. Just click on the badge below to start the environment.

<p align="center">
<a href = "https://mybinder.org/v2/gh/DeepLearningItalia/Recommender-Systems-Course/HEAD?urlpath=lab" target="_blank"> <img src="https://mybinder.org/badge_logo.svg"> </a>
</p>

## Table of Contents of lectures

[Here](src/README.md) you can find a more detailed index of the various modules.

---

## Your lecturer

### [Oscar de Felice](https://oscar-defelice.github.io/)

<a href="https://oscar-defelice.github.io/" target="_blank" rel="that's me!">![Oscar](https://oscar-defelice.github.io/images/OscarAboutMe.png)</a>

I am a theoretical physicist and programming and AI enthusiast.

I write articles on Medium (very unsystematically), you can read them [here](https://oscar-defelice.medium.com/).
I also have a [github profile](https://github.com/oscar-defelice) where I put my personal and open-source projects.

📫 [Contact me!](mailto:oscar.defelice@gmail.com)

[![github](https://img.shields.io/badge/GitHub-100000?style=plastic&logo=github&logoColor=white)](https://github.com/oscar-defelice)
[![Website](https://img.shields.io/badge/oscar--defelice-oscar-orange?style=plastic&logo=netlify&logoColor=informational&link=oscar-defelice.github.io)](https://oscar-defelice.github.io)
[![Twitter Badge](https://img.shields.io/badge/-@OscardeFelice-1ca0f1?style=plastic&labelColor=1ca0f1&logo=twitter&logoColor=white&link=https://twitter.com/oscardefelice)](https://twitter.com/OscardeFelice)
[![Linkedin Badge](https://img.shields.io/badge/-oscardefelice-blue?style=plastic&logo=Linkedin&logoColor=white&link=https://linkedin.com/in/oscar-de-felice-5ab72383/)](https://linkedin.com/in/oscar-de-felice-5ab72383/)

## Other courses

Here you can find more material about other lectures and courses on Machine Learning topics.

1. [Introduction to Data Science](https://oscar-defelice.github.io/DSAcademy-lectures) 🧮
2. [Statistical Learning](https://oscar-defelice.github.io/ML-lectures) 📈
3. [Deep Learning](https://oscar-defelice.github.io/DeepLearning-lectures) 🦾
4. [Time Series](https://oscar-defelice.github.io/TimeSeries-lectures) ⌛
5. [Computer Vision Hands-On](https://oscar-defelice.github.io/Computer-Vision-Hands-on) 👀️

## References

<a id="1">[1]</a>
Van Alstyne, Marshall; Brynjolfsson, Erik (March 1997).
["Electronic Communities: Global Village or Cyberbalkans?"](http://web.mit.edu/marshall/www/papers/CyberBalkans.pdf)

<a id="2">[2]</a>
Hern (2017).
["How social media filter bubbles and algorithms influence the election"](https://www.theguardian.com/technology/2017/may/22/social-media-election-facebook-filter-bubbles)

<a id="3">[3]</a>
Baer, Drake (2017).
["The ‘Filter Bubble’ Explains Why Trump Won and You Didn’t See It Coming"](http://nymag.com/scienceofus/2016/11/how-facebook-and-the-filter-bubble-pushed-trump-to-victory.html)

<a id="4">[4]</a>
Lazar, Shira (June 1, 2011).
["Algorithms and the Filter Bubble Ruining Your Online Experience?"](http://www.huffingtonpost.com/shira-lazar/algorithms-and-the-filter_b_869473.html)

<a id="5">[5]</a>
Meredith, Sam (10 April 2018).
["Facebook-Cambridge Analytica: A timeline of the data hijacking scandal"](https://www.cnbc.com/2018/04/10/facebook-cambridge-analytica-a-timeline-of-the-data-hijacking-scandal.html)

<a id="6">[6]</a>
Catalina Albeanu (17 November 2016).
["Bursting the filter bubble after the US election: Is the media doomed to fail?"](https://www.journalism.co.uk/news/bursting-the-filter-bubble-after-the-us-election/s2/a692918/)

<a id="7">[7]</a>
Felix Gräßer, Stefanie Beckert, Denise Küster, Jochen Schmitt, Susanne Abraham, Hagen Malberg, and Sebastian Zaunseder (2017).
["Therapy Decision Support Based on Recommender System Methods"](https://www.hindawi.com/journals/jhe/2017/8659460/)
