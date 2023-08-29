
from __future__ import absolute_import, unicode_literals

# from .celery import app as celery_app__all__ = ['celery_app']
# import  mainapp

from .celery import app as celery_app


__all__ = ('celery_app',)