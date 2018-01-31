import configparser
import feedparser
import PTN
import json

config = configparser.ConfigParser()
config.read('../config.ini')

def getRssFeeds():
	configRssList = config['DEFAULT']['RSSFEEDS'].split('\n')
	rssFeeds = list(filter(None, configRssList)) # Remove empty lines
	return rssFeeds


def retrieveAll():
	rssFeeds = getRssFeeds()
	for feed in rssFeeds:
		d = feedparser.parse(feed)

		for post in d.entries:
			#print (post.title + ": " + post.link + "\n")
			torrentName = post.title
			metadata = PTN.parse(torrentName)
			print (post.title)
			print (metadata['title'] + ' (' + str(metadata['year']) + ')')
			#print (json.dumps(metadata))
			print ()


retrieveAll()

# {"id":"fgdf-324234-fgdgfg-GUID1","imdbId":"tt123jkfd2","title":"Red Dawn","year":"2010","genre":["action","drama"],"length":160,"trailer":"http://youtube.com/jSdFFnd","torrentUrl":"http://torrent.link/example.torrent","torrentFiles":["sample.mkv","Red.Dawn.2016.mkv","Red.Dawn.2016.srt"],"origin":[{"name":"Rapidcaws","url":"http://examples.com/list.rss"}]}