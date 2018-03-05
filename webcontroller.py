"""
Spotify Web Controller Interface (connects to the API used by the Play button)
6 January 2017, Benjamin Shanahan.

Unfortunately, this web controller interface only provides play and pause capabilities.
This is too limited for our purposes, but we can use it to queue up new songs / playlists!
It will also open Spotify on the Desktop, which is useful!

Modified from: https://github.com/cgbystrom/spotify-local-http-api
"""

import ssl
from string import ascii_lowercase
from random import choice
import urllib
import urllib2
import json
import time


class WebController:

    def __init__(self):
        # Default port that Spotify Web Helper binds to.
        self.PORT = 4370
        self.DEFAULT_RETURN_ON = ["login", "logout", "play", "pause", "error", "ap"]
        self.ORIGIN_HEADER = {"Origin": "https://open.spotify.com"}
        # I had some troubles with the version of Spotify"s SSL cert and Python 2.7 on Mac.
        # Did this monkey dirty patch to fix it. Your milage may vary.
        def new_wrap_socket(*args, **kwargs):
            kwargs["ssl_version"] = ssl.PROTOCOL_SSLv3
            return orig_wrap_socket(*args, **kwargs)
        orig_wrap_socket, ssl.wrap_socket = ssl.wrap_socket, new_wrap_socket
        # get OAuth and CSRF tokens from Spotify Web Helper
        self.open_spotify_client()
        self.oauth_token = self.get_oauth_token()
        self.csrf_token = self.get_csrf_token()

    def get_json(self, url, params={}, headers={}):
        if params:
            url += "?" + urllib.urlencode(params)
        request = urllib2.Request(url, headers=headers)
        return json.loads(urllib2.urlopen(request).read())

    def generate_local_hostname(self):
        """Generate a random hostname under the .spotilocal.com domain"""
        subdomain = "".join(choice(ascii_lowercase) for x in range(10))
        return subdomain + ".spotilocal.com"

    def get_url(self, url):
        return "https://%s:%d%s" % (self.generate_local_hostname(), self.PORT, url)

    def get_version(self):
        return self.get_json(get_url("/service/version.json"), params={"service": "remote"}, headers=self.ORIGIN_HEADER)

    def get_oauth_token(self):
        return self.get_json("http://open.spotify.com/token")["t"]

    def get_csrf_token(self):
        # Requires Origin header to be set to generate the CSRF token.
        return self.get_json(self.get_url("/simplecsrf/token.json"), headers=self.ORIGIN_HEADER)["token"]

    def get_status(self, return_after=59, return_on=None):
        if return_on is None: return_on = self.DEFAULT_RETURN_ON
        params = {
            "oauth": self.oauth_token,
            "csrf": self.csrf_token,
            "returnafter": return_after,
            "returnon": ",".join(return_on)
        }
        return self.get_json(self.get_url("/remote/status.json"), params=params, headers=self.ORIGIN_HEADER)

    def pause(self, pause=True):
        params = {
            "oauth": self.oauth_token,
            "csrf": self.csrf_token,
            "pause": "true" if pause else "false"
        }
        self.get_json(self.get_url("/remote/pause.json"), params=params, headers=self.ORIGIN_HEADER)

    def unpause(self):
        self.pause(pause=False)

    def play(self, spotify_uri):
        params = {
            "oauth": self.oauth_token,
            "csrf": self.csrf_token,
            "uri": spotify_uri,
            "context": spotify_uri,
        }
        self.get_json(self.get_url("/remote/play.json"), params=params, headers=self.ORIGIN_HEADER)

    def next(self):
        params = {
            "oauth": self.oauth_token,
            "csrf": self.csrf_token,
            "next": "true"
        }
        self.get_json(self.get_url("/remote/next.json"), params=params, headers=self.ORIGIN_HEADER)

    def open_spotify_client(self):
        return self.get_json(self.get_url("/remote/open.json"), headers=self.ORIGIN_HEADER)