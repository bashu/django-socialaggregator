# -*- coding: utf-8 -*-

class BaseAggregator(object):
    connector = None

    def __init__(self):
        self.init_connector()

    def init_connector(self):
        pass

    def search(self, query):
        pass
