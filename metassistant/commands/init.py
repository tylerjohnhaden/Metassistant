import subprocess

import os
from argparse import Namespace

import metassistant
from .app import app

settings_injection = """\n
\"\"\"****************************************************************\"\"\"
\"\"\" This section of the settings.py file was added by Metassistant \"\"\"

import sys

# required to access metassistant package
sys.path.insert(0, os.path.join(BASE_DIR, os.pardir, os.pardir))
import metassistant

# set templates to Metassistant's apps directory
TEMPLATES[0]['APP_DIRS'] = False
TEMPLATES[0]['DIRS'] = [os.path.join(BASE_DIR, os.pardir, 'apps')]

# set static to Metassistant's static directory
STATICFILES_DIRS = [os.path.join(BASE_DIR, os.pardir, 'static')]

# based on Metassistant's configuration, will listen on localhost and or public IPv4 ports
# todo: add link to information
ALLOWED_HOSTS.extend(metassistant.settings(ALLOWED_HOSTS=ALLOWED_HOSTS))

# based on Metassistant's configuration, will update Django with active apps
INSTALLED_APPS.extend(metassistant.settings(INSTALLED_APPS=INSTALLED_APPS))

\"\"\"****************************************************************\"\"\""""

urls_injection = """\n
\"\"\"************************************************************\"\"\"
\"\"\" This section of the urls.py file was added by Metassistant \"\"\"

from django.conf.urls import include

import metassistant

urlpatterns.extend(include(u) for u in metassistant.urls())

\"\"\"************************************************************\"\"\""""


def init(args):
    try:
        import django as _
    except ModuleNotFoundError:
        return '''You need to install the "django" module.
This may be accomplished by running "pip install django".
If this doesn\'t work, follow this link to Django\'s documentation on installation.
https://www.djangoproject.com/download/'''

    try:
        if 0 != subprocess.call('cd {0} && django-admin startproject metaproject'.format(metassistant.PATH),
                                shell=True):
            raise ValueError
    except Exception:
        return 'There was an error when running "django-admin startproject metaproject".'

    # todo: make this cleaner
    # check installation
    if not os.path.exists(os.path.join(metassistant.PATH, 'metaproject')):
        return '''I am not sure why the directory "metaproject" was not created, 
even though "django-admin" returned successfully.'''

    if not os.path.exists(os.path.join(metassistant.PATH, 'metaproject', 'metaproject', 'settings.py')):
        return '''I am not sure why the file "settings.py" was not created, 
even though "django-admin" returned successfully.'''

    # inject Metassistant settings
    with open(os.path.join(metassistant.PATH, 'metaproject', 'metaproject', 'settings.py'), 'a') as settings_file:
        settings_file.write(settings_injection)

    if not os.path.exists(os.path.join(metassistant.PATH, 'metaproject', 'metaproject', 'urls.py')):
        return '''I am not sure why the file "urls.py" was not created, 
even though "django-admin" returned successfully.'''

    # inject Metassistant urls
    with open(os.path.join(metassistant.PATH, 'metaproject', 'metaproject', 'urls.py'), 'a') as settings_file:
        settings_file.write(urls_injection)

    # create apps directory
    os.mkdir(os.path.join(metassistant.PATH, os.pardir, 'apps'))

    return 'All good'
