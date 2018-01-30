#http://www.pythonforbeginners.com/feedparser/using-feedparser-in-python
## CTRL + SHIFT + B 

import feedparser

rssFeeds = [
	"http://www.reddit.com/r/python/.rss",
	"http://www.reddit.com/r/python/.rss",
	"http://www.reddit.com/r/python/.rss"
]

for feed in rssFeeds:
	d = feedparser.parse(feed)

	for post in d.entries:
		print (post.title + ": " + post.link + "\n")