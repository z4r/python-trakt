================================
Python interface to trakt.tv API
================================

.. image:: https://api.travis-ci.org/z4r/python-trakt.png?branch=master
   :target: http://travis-ci.org/z4r/python-trakt

.. image:: https://coveralls.io/repos/z4r/python-trakt/badge.png?branch=master
    :target: https://coveralls.io/r/z4r/python-trakt

This package provides a module to interface with the `trakt.tv`_ `API`_.

.. contents::
    :local:

.. _installation:

Installation
============
Using pip::

    $ pip install git+https://github.com/z4r/python-trakt

.. _usage:

trakt API usage
===============
::

    import trakt
    trakt.tv.setup(apikey=<YOUR_APIKEY>)
    trakt.tv.search.shows('walking dead')

You can perform auth request
::

    import trakt
    trakt.tv.setup(apikey=<YOUR_APIKEY>, username=<USER>, password=<PWD>)
    trakt.tv.show.episode('the-walking-dead', 1, 1)

.. _license:

License
=======

This software is licensed under the ``Apache License 2.0``. See the ``LICENSE``
file in the top distribution directory for the full license text.

.. _references:

References
==========
* `trakt.tv`_
* `API`_

.. _trakt.tv: http://trakt.tv
.. _API: http://trakt.tv/api-docs
