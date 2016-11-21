from sys import exit
from random import randint

class Bag(object):

    def __init__(self):
        self.content = ['Axe']

    def add(self, tool):
        self.content.append(tool)

    def remove(self, tool):
        self.content.remove(tool)

    def show(self):
        for tools in self.content:
            print tools
