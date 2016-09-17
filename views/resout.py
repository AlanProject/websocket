#!/usr/bin/env python
#-*- coding:utf-8 -*-
#auther = Alan
import subprocess
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class ActiveCommand(object):
    def __init__(self,q, **kwargs):
        self.command = kwargs.get('command')
        self.queue = q

    def active_command(self):
        s = subprocess.Popen(self.command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
        while True:
            buff = s.stdout.readline()
            self.queue.put(buff)
            if buff == "" and s.poll() != None:
                break
