from unittest import TestCase
import datetime
from httpretty import httprettified, HTTPretty
import trakt
from trakt.api import AbstractApi
from trakt.api import *
from trakt.errors import TraktException
from trakt.tests import get_trakt_body


class ApiTestCase(TestCase):
    @httprettified
    def test_get(self):
        HTTPretty.register_uri(
            HTTPretty.GET,
            'http://api.trakt.tv/shows/updated.json/TRAKTAPIKEY',
            body=get_trakt_body('invalid_apikey.json'),
        )
        self.assertRaises(TraktException, AbstractApi._get, 'shows/updated')
        self.assertEqual(len(HTTPretty.latest_requests), 1)

    @httprettified
    def test_get_auth(self):
        HTTPretty.register_uri(
            HTTPretty.GET,
            'http://api.trakt.tv/shows/updated.json/TRAKTAPIKEY',
            body=get_trakt_body('invalid_apikey.json'),
        )
        trakt.tv.setup(username='USER', password='PWD')
        self.assertRaises(TraktException, AbstractApi._get, 'shows/updated')
        self.assertEqual(len(HTTPretty.latest_requests), 1)
        self.assertEqual(
            HTTPretty.last_request.headers['Authorization'],
            'Basic VVNFUjpmNzNlMTEwNDI3NjQ4MDE0NTY4ZjcxNDQwMzFhNmQ0ODA2MGVhYjBh'
        )
        trakt.tv.reset()


class ShowsTestCase(TestCase):
    @httprettified
    def test_trending(self):
        HTTPretty.register_uri(
            HTTPretty.GET,
            'http://api.trakt.tv/shows/trending.json/TRAKTAPIKEY',
            body=get_trakt_body('shows/trending.json'),
        )
        response = Shows.trending()
        self.assertEqual(response[0]['title'], 'The Big Bang Theory')
        self.assertEqual(len(HTTPretty.latest_requests), 1)

    @httprettified
    def test_updated(self):
        HTTPretty.register_uri(
            HTTPretty.GET,
            'http://api.trakt.tv/shows/updated.json/TRAKTAPIKEY/1363933987',
            body=get_trakt_body('shows/updated.json'),
        )
        response = Shows.updated(1363933987)
        self.assertEqual(len(response['shows']), 8)
        self.assertEqual(len(HTTPretty.latest_requests), 1)


class CalendarTestCase(TestCase):
    @httprettified
    def test_shows(self):
        HTTPretty.register_uri(
            HTTPretty.GET,
            'http://api.trakt.tv/calendar/shows.json/TRAKTAPIKEY/20110421/2',
            body=get_trakt_body('calendar/shows.json'),
        )
        response = Calendar.shows(date=datetime.date(year=2011, month=04, day=21), days=2)
        self.assertEqual(response[0]['date'], '2011-04-21')
        self.assertEqual(len(HTTPretty.latest_requests), 1)

    @httprettified
    def test_shows_nodate(self):
        HTTPretty.register_uri(
            HTTPretty.GET,
            'http://api.trakt.tv/calendar/shows.json/TRAKTAPIKEY',
            body=get_trakt_body('calendar/shows.json'),
        )
        response = Calendar.shows(days=2)
        self.assertEqual(response[0]['date'], '2011-04-21')
        self.assertEqual(len(HTTPretty.latest_requests), 1)

    @httprettified
    def test_premieres(self):
        HTTPretty.register_uri(
            HTTPretty.GET,
            'http://api.trakt.tv/calendar/premieres.json/TRAKTAPIKEY/20110421/2',
            body=get_trakt_body('calendar/shows.json'),
        )
        response = Calendar.premieres(date=datetime.date(year=2011, month=04, day=21), days=2)
        self.assertEqual(response[0]['date'], '2011-04-21')
        self.assertEqual(len(HTTPretty.latest_requests), 1)

    @httprettified
    def test_premieres_nodate(self):
        HTTPretty.register_uri(
            HTTPretty.GET,
            'http://api.trakt.tv/calendar/premieres.json/TRAKTAPIKEY',
            body=get_trakt_body('calendar/shows.json'),
        )
        response = Calendar.premieres(days=2)
        self.assertEqual(response[0]['date'], '2011-04-21')
        self.assertEqual(len(HTTPretty.latest_requests), 1)


class ServerTestCase(TestCase):
    @httprettified
    def test_time(self):
        HTTPretty.register_uri(
            HTTPretty.GET,
            'http://api.trakt.tv/server/time.json/TRAKTAPIKEY',
            body=get_trakt_body('server/time.json'),
        )
        response = Server.time()
        self.assertEqual(response['timestamp'], 1363960739)
        self.assertEqual(len(HTTPretty.latest_requests), 1)


class SearchTestCase(TestCase):
    @httprettified
    def test_shows(self):
        HTTPretty.register_uri(
            HTTPretty.GET,
            'http://api.trakt.tv/search/shows.json/TRAKTAPIKEY/big+bang+theory',
            body=get_trakt_body('search/shows.json'),
        )
        response = Search.shows('big bang theory')
        self.assertEqual(response[0]['title'], 'The Big Bang Theory')
        self.assertEqual(len(HTTPretty.latest_requests), 1)


class ShowTestCase(TestCase):
    @httprettified
    def test_episode(self):
        HTTPretty.register_uri(
            HTTPretty.GET,
            'http://api.trakt.tv/show/episode/summary.json/TRAKTAPIKEY/261690/1/1',
            body=get_trakt_body('show/episode.json'),
        )
        response = Show.episode(title=261690, season=1, episode=1)
        self.assertEqual(response['show']['title'], 'The Americans (2013)')
        self.assertEqual(len(HTTPretty.latest_requests), 1)

    @httprettified
    def test_related(self):
        HTTPretty.register_uri(
            HTTPretty.GET,
            'http://api.trakt.tv/show/related.json/TRAKTAPIKEY/261690',
            body=get_trakt_body('show/related.json'),
        )
        response = Show.related(title=261690)
        self.assertEqual(response[0]['title'], 'Game of Thrones')
        self.assertEqual(len(HTTPretty.latest_requests), 1)

    @httprettified
    def test_season(self):
        HTTPretty.register_uri(
            HTTPretty.GET,
            'http://api.trakt.tv/show/season.json/TRAKTAPIKEY/261690/1',
            body=get_trakt_body('show/related.json'),
        )
        response = Show.season(title=261690, season=1)
        self.assertEqual(len(response), 10)
        self.assertEqual(len(HTTPretty.latest_requests), 1)

    @httprettified
    def test_seasons(self):
        HTTPretty.register_uri(
            HTTPretty.GET,
            'http://api.trakt.tv/show/seasons.json/TRAKTAPIKEY/261690',
            body=get_trakt_body('show/seasons.json'),
        )
        response = Show.seasons(title=261690)
        self.assertEqual(response[0]['episodes'], 13)
        self.assertEqual(len(HTTPretty.latest_requests), 1)

    @httprettified
    def test_summary(self):
        HTTPretty.register_uri(
            HTTPretty.GET,
            'http://api.trakt.tv/show/summary.json/TRAKTAPIKEY/261690',
            body=get_trakt_body('show/summary.json'),
        )
        response = Show.summary(title=261690)
        self.assertEqual(response['title'], 'The Americans (2013)')
        self.assertEqual(len(HTTPretty.latest_requests), 1)
