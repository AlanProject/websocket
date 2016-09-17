#!/usr/bin/env python
#-*- coding:utf-8 -*-
from views.views import *
urls = [
  (r'/',MianHandler),
  (r'/story/(\d+)', StoryHandler),
  (r'/admin/', AdminHandler),
  (r'/send/', SendHandler),
]
