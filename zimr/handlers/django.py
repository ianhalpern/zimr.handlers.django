from __future__ import absolute_import
import os, sys
from functools import partial
import zimr.handlers.wsgi

# reference /usr/lib/pymodules/python2.6/django/core/management/commands/runserver.py

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
from django.core.servers.basehttp import AdminMediaHandler, WSGIServerException

application = AdminMediaHandler( django.core.handlers.wsgi.WSGIHandler(), '' )

connection_handler = partial( zimr.handlers.wsgi.connection_handler, application )
