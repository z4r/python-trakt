import os
TRAKT_RESPONSE = os.path.join(os.path.dirname(__file__), 'response')


def get_trakt_body(filename):
    with open(os.path.join(TRAKT_RESPONSE, filename)) as fp:
        body = fp.read()
    return body
