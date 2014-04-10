import unittest
from feed import *
 
class TestFeed(unittest.TestCase):
    # def setUp(self):

    # def tearDown(self):

    def test_from_file(self):
        feed = Feed('data/2014-04-05_16-54.atom')
        self.assertEqual(len(feed.articles),89)
        
    def test_duplicate_articles(self):
        feed = Feed('data/2014-04-05_16-54.atom')
        feed.add_feed('data/2014-04-05_16-54.atom')
        self.assertEqual(len(feed.articles),89)