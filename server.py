#!/usr/bin/env python
#-*- coding:utf-8 -*-
import tornado.ioloop
from settings import settings
from urls.handler import urls
application = tornado.web.Application(urls,**settings)

if __name__ == '__main__':
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
