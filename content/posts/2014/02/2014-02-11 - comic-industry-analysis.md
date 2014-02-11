Title: Crisis on Infinite Datapoints Part 1
Slug: crisis-on-infinite-datapoints-part1
Date: 2014-02-11
Category: Comics
Tags: comics, data science 
Author: Eoin Hurrell
Summary: Part 1 of an analysis into the comic industry
I was interested in learning more about the comics industry, so I collected any data I could find on it. I assembled a dataset from the last twenty years of comics, drawing in their monthly sales and rankings from [Comichron](http://ww.comichron.com) and the details of their creators from [ComicVine](http://comicvine.com). 

This dataset has a huge number of stories to tell, encoded in it are the successful careers of many many talented people, the popularity of many story arcs and details of how the industry trades. In this first blog post I explore the most popular titles in comics.

#Part 1 - Popularity Overview

Comics have always had a following. Fans love reading their favourite characters and following their favourite story arcs. This sort of popularity shows an established fanbase, and usually leads to people outside of comics learning the names of characters like Spider-Man or Batman.

Popularity in comics can mean selling a lot, but that's only one dimension. Really popularity is part sales, part consistency. For a comic to truly be popular it must go to a second run, or just perform well month-on-month. In short it must appear high in the bestselling rankings more frequently than other titles, to show people are reading, getting their friends to read, and following the series. 

To begin my analysis of popularity I choose to look at trade paperbacks in particular, mostly because that's where full stories are found. Phrases like "I'll wait for the trade" are common enough that I dove right in to examine what was popular, and measured the number of times a title appeared on the bestseller list and ranked them in descending order. Here are the top ten:

###The Top 10 Frequent Bestseller Trade Titles
* 1 - Walking Dead Vol. 1 Days Gone Bye
* 2 - Watchmen
* 3 - Walking Dead Vol. 3 Safety Behind Bars
* 4 - Walking Dead Vol. 2 Miles Behind Us
* 5 - Walking Dead Vol. 4 Hearts Desire
* 6 - Batman Dark Knight Returns
* 7 - Y The Last Man Vol. 1 Unmanned
* 8 - Fables Vol. 1 Legends In Exile
* 8 - Walking Dead Vol. 5 Best Defense
* 9 - Walking Dead Vol. 6 Sorrowful Life
* 9 - Walking Dead Vol. 8 Made To Suffer
* 10 - Batman The Killing Joke Special Ed HC
* 10 - Civil War
* 10 - Walking Dead Vol. 9 Here We Remain

So, it's clear is that The Walking Dead is a bit of a phenomenon. Hugely successful in the trades (eight volumes appear on the top 10 frequent bestseller list), it even outsells Watchmen. Granted our 20 year study doesn't cover Watchmen's launch and does cover The Walking Dead's, but that's still an impressive claim. Also interesting to note is the fact that only one entry on the list, Y The Last Man, hasn't (yet) had some attempt to work characters into other media, while all the other have had films, games and television shows come out of their popularity.

Since The Walking Dead is a long-running series of trades with many volumes I wanted to see the attrition rate of readers, that is where do people stop reading, how many reading a volume are likely to read the next? So here are the number of readers for each volume.

![The Walking Dead Attrition Rate](/images/comics/the_walking_dead_attrition.png)

Unsurprisingly each volume's sales are less than or equal to the previous volume's, i.e. people tend not to start reading in the middle in large numbers, except for volume 9, which for some reason has a big sales spike. Looking into it, volume 9 was released January 1, 2009 and wasn't the most current volume when the TV show was announced (that would be volume 11 or 12). It may be that people heard of the TV show and decided to start from a volume or two before current to catch up. Whatever the reason, we can also see the first volume is vastly more popular than any other (which I'm given to understand is common, people try out a single volume), with diminishing returns before it begins to level out. It's clear The Walking Dead has a large, vocal following, but as with much creative work it's also clear it's not for everyone.

Of course trades aren't the bread and butter of the comic industry, single issues are, so I looked at single issues on the frequent bestseller list:

###The Top 10 Frequent Bestseller Single Issue Titles
* 1 -  Amazing Spider-Man
* 2 - Batman
* 3 - Spawn
* 3 - Uncanny X-Men
* 4 - Wolverine
* 5 - Action Comics
* 6 - Detective Comics
* 6 - Green Lantern
* 7 - Wonder Woman
* 8 - Superman
* 9 - Hellblazer
* 10 - Fantastic Four

So, this is where Marvel and DC, the Big Two come into their own. It seems to be a dead even Marvel/DC split for popular single issues, and The Walking Dead is nowhere in sight! Image still turn up, with Spawn appearing as the third most popular comic of the last twenty years. Considering how well Spider-Man and Batman have been doing in the mainstream the Spawn movie is an even worse tragedy. 


Popularity is an important thing. In this post I looked at popular work in the trades and single issues, and showed the attrition rates of the most popular trade. This was just a basic overview, but one question still to ask is how does popularity affect sales? 

![How Rank Affect Sales](/images/comics/average_sales_by_rank_overall.png)

As I show here there is a huge difference between the average sales at rank 1 and at rank 10 each month. The next part of this series will explore sales data.
