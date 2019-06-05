# -*- coding: utf-8 -*-
# from django.test import TestCase
import sys,os
print('Python %s on %s' % (sys.version, sys.platform))
import django;
print('Django %s' % django.get_version())
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
sys.path.extend(['E:\\pythonproject\\framework_py', 'D:\\JetBrains\\PyCharm\\helpers\\pycharm', 'D:\\JetBrains\\PyCharm\\helpers\\pydev'])
if 'setup' in dir(django):
    django.setup()
# Create your tests here.

from django.conf import settings
print(settings.__dict__)
