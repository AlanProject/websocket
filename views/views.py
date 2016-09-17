#!/usr/bin/env python
#-*- coding:utf-8 -*-
from tornado import web
from tornado import websocket
from resout import ActiveCommand
import Queue
import json
import time,sys
reload(sys)
sys.setdefaultencoding('utf-8')
def on_message(ws,message):
    return message

class MianHandler(web.RequestHandler):
    def get(self):
        self.write('hello word')

class AdminHandler(web.RequestHandler):
    def get(self):
        self.render('admin.html')
    def post(self):
        arg = self.request.arguments
        for i in range(10):
            i = str(i)
            self.write(i)

            # self.flush()
            time.sleep(1)
class SendHandler(websocket.WebSocketHandler):
    clients = set()

    def open(self):
        SendHandler.clients.add(self)
        self.stream.set_nodelay(True)

    def on_message(self, message):
        message = json.loads(message)
        q = Queue.Queue()
        obj = ActiveCommand(q,**message)
        obj.active_command()

        while q.qsize() > 0:
            tmp_data = q.get()
            self.write_message(json.dumps({"res":tmp_data}))

        # 服务器主动关闭
        self.close()
        if self in self.clients:
            SendHandler.clients.remove(self)

    def on_close(self):
        # 客户端主动关闭
        if self in self.clients:
            SendHandler.clients.remove(self)



class StoryHandler(web.RequestHandler):
    def get(self,story_id):
        self.write('You Request Story %s'%story_id)
