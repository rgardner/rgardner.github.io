---
layout: post
title: Memory Jogger Update
tags: [personal, tech]
---

[Memory Jogger](https://github.com/rgardner/memory-jogger) is a program I wrote
to help me find interesting articles and videos I had saved in
[Pocket](https://getpocket.com). I wrote about it previously [in this post]({%
post_url 2020-07-12-announcing-memory-jogger %}). It started as a program to
send me daily email digests of items I had previously saved that were related to
current events (via Google Trends data).

<!-- more -->

Mostly it was to help me prioritize reading some of the thousands of unread
items that I've saved over the years.  But I also thought that it would make
current events more meaningful by reading historical context and commentary.
Sometimes it worked as you'd expect, for example, when Hamilton came out on
Disney+, it reminded me of the original New York Times article from when the
play came out in 2015. Unique words like "Pokemon" also returned relevant
results. But other times, the articles and videos in the daily email digest were
completely unrelated to the Google Trends results.

This is mostly expected. I used the
[tf-idf](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) algorithm I learned about
in my first internship to implement search. tf-idf helps when search terms
contain a mix of common and unique words, e.g. "Pokemon" is rare, but "The" is
very common, so "The Pokemon Game" would weight articles that contain Pokemon
higher than articles just about games (assuming "Pokemon" is less common than
"game" in the document collection).

But the problem wasn't the search relevance, it was how I use email. I try as
hard as possible to keep inbox zero, using Gmail inbox sections to triage emails
based on "Needs Action/Reply", "Awaiting Reply", "Scheduled", and the rarely
used "Delegated." But where do these email digests fit in? They don't! I don't
need a longer to-do list. Instead, I want "pull", not "push". Review these items
when I have time, but without the guilt and annoyance of push notifications and
"unread" messages. I thought for surfacing "trending" articles an email digest
was the right UI, but I didn't think about how these emails would actually fit
into my life.

For a positive surprise, I found I clicked on the irrelevant items as often as
the relevant ones. Even if the articles in the digest were completely unrelated
to what was trending at the time (same words, but different context), it was
still fun to read items I had saved years ago. Or, I knew I didn't care about
that item and could just archive or delete it.

So, in 2021, I've been using Memory Jogger completely differently. Instead of an
email digest that sends me notifications and adds to my to-do list, I wrote an
interactive program to just return random items from my Pocket, with commands to
quickly archive/delete/skip items. This interactive program interacts with the
email digest program via subprocesses and sharing a SQLite DB.

Sometimes, I don't even use the interactive program. I just load the database in
[DB Browser for SQLite](https://sqlitebrowser.org/) and then execute the
subprocesses manually, e.g.

```bash
memory_jogger saved-items archive --item-id <id> 
```

or even better, create an alias and then just run `mja <id>` or `mjd <id>`.

I've been slowly cleaning up my Pocket and have enjoyed reading the articles and
watching the videos. No notifications, no "unread count", no search algorithm,
just sync, SQLite, and RNG to guide me.
