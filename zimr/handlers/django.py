from __future__ import absolute_import
import os, sys
from functools import partial
import zimr.handlers.wsgi

# reference /usr/lib/pymodules/python2.6/django/core/management/commands/runserver.py
if 'DJANGO_SETTINGS_MODULE' not in os.environ:
	os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
from django.core.servers.basehttp import AdminMediaHandler, WSGIServerException

_application = AdminMediaHandler( django.core.handlers.wsgi.WSGIHandler(), '' )

def application( environ, start_response ):
	# django SCRIPT_NAME fix
	environ['PATH_INFO'] = environ['SCRIPT_NAME'] + environ['PATH_INFO']
	environ['SCRIPT_NAME'] = ''
	return _application( environ, start_response )

connection_handler = partial( zimr.handlers.wsgi.connection_handler, application )
