#-*- coding=utf-8 -*-
import threading
from analysis.language import Language
from analysis.twitter.statistics import TweetAnalyser
from stream.twitter import Stream

class TwitterCrawler(threading.Thread):
    def run(self):
        #Stream.run(TweetAnalyser.stats)
        print hello

TwitterCrawler().start()
