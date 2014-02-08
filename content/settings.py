#!/usr/bin/env python
# -*- coding: utf-8 -*-

AUTHOR = u'Eoin Hurrell'
SITENAME = u'Eoin Hurrell'
SITEURL = ''

TIMEZONE = 'Europe/Dublin'
DEFAULT_LANG = u'en'

GITHUB_URL = 'http://github.com/ultimatehurl'
DISQUS_SITENAME = "eoinhurrellsblog"
EMAIL = "eoin.hurrell@gmail.com"

# Additional
# GOOGLE_ANALYTICS = "UA-34295039-1"
# DOMAIN = "eoinhurrell.com"

# Twitter Cards
TWITTER_CARDS = True
TWITTER_NAME = "ultimatehurl"

THEME = '../skeleton-theme'
PATH = ''
OUTPUT_PATH = '../../output'

PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
LOCALE = 'en_IE'
DEFAULT_DATE_FORMAT = '%d-%m-%y'
DEFAULT_PAGINATION = 5


# FEEDS
FEED_ALL_ATOM = "feeds/all.atom.xml"
TAG_FEED_ATOM = "feeds/tag/%s.atom.xml"


# Social widget
SOCIAL = (('Github', GITHUB_URL),)


ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{slug}/index.html"

# global metadata to all the contents
#DEFAULT_METADATA = (('yeah', 'it is'),)

# static paths will be copied under the same name
STATIC_PATHS = ['images']  # , 'CNAME']

# A list of files to copy from the source to the destination
#FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),)


#Plugin details
PLUGIN_PATH = '../plugins/'
PLUGINS = ['liquid_tags.notebook', 'liquid_tags.include_code',
           'liquid_tags.img', 'liquid_tags.video']

CODE_DIR = 'code'
NOTEBOOK_DIR = 'notebooks'
EXTRA_HEADER = open('../_nb_header.html').read().decode('utf-8')

EXTRA_PATH_METADATA = {
    #'/CNAME': {'path': '/CNAME'},
    #'extra/robots.txt': {'path': 'robots.txt'},
    }
