‚from sys import exit
from random import randint

class Bag(object):

    def __init__(self):
        self.content = ['axe']

    def add(self, tool):
        self.content.append(tool)

    def remove(self, tool):
        self.content.remove(tool)

    def show(self):
        if self.content != []:
            for tools in self.content:
                print tools

        else:
            print "Your bag is empty!"
