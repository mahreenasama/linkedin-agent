# post_generator.py

import feedparser

rss = feedparser.parse(
    "https://spring.io/blog.atom"
)

latest = rss.entries[0]
title = latest.title
link = latest.link

post = f"""
🚀 Interesting Spring update today:
{title}
I found this topic particularly interesting because it shows how the Spring ecosystem continues evolving.
Read more:
{link}
#Java #SpringBoot #Microservices
"""
print(post)
``
