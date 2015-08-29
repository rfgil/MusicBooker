# -*- coding: utf-8 -*-
import os
import gettext

# https://wiki.maemo.org/Internationalize_a_Python_application

APP_NAME = "MusicBooker"

# We need to choose the language. We will provide a list, and gettext
# will use the first translation available in the list
languages = os.environ.get('LANG', '').split(':')
languages += ['en_US']

mo_location = 'i18n'

gettext.install(True, localedir=None)
gettext.find(APP_NAME, mo_location)
gettext.textdomain(APP_NAME)
gettext.bind_textdomain_codeset(APP_NAME, "UTF-8")

language = gettext.translation(APP_NAME, mo_location, languages=languages, fallback=True)
