import os
from unittest import TestCase
import trakt


class TraktTestCase(TestCase):
    def test_setup(self):
        trakt.tv.setup(apikey='APIKEY', username='USER', password='PWD')
        self.assertEqual(os.getenv('TRAKT_APIKEY'), 'APIKEY')
        self.assertEqual(os.getenv('TRAKT_USERNAME'), 'USER')
        self.assertEqual(os.getenv('TRAKT_PASSWORD'), 'f73e110427648014568f7144031a6d48060eab0a')

    def test_reset(self):
        trakt.tv.setup(apikey='APIKEY', username='USER', password='PWD')
        trakt.tv.reset()
        for var in ('TRAKT_APIKEY', 'TRAKT_USERNAME', 'TRAKT_PASSWORD'):
            self.assertEqual(os.getenv(var), None)
