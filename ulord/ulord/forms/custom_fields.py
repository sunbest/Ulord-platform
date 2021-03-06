# -*- coding: utf-8 -*-
# @Date    : 2018/5/18
# @Author  : Shu
# @Email   : httpservlet@yeah.net
from wtforms import Field
from wtforms.widgets import TextInput

class TagListField(Field):
    widget = TextInput()

    def _value(self):
        return self.data if self.data else ""

    def process_formdata(self, valuelist):
        if valuelist:
            self.data = [x.strip() for x in valuelist if x]
        else:
            self.data = []