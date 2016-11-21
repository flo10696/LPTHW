from sys import exit
from random import randint

class Scene(object):

    def __init__(self):
        pass

    def enter(self, name, bag):
        print "This scene is not definded."
        exit(1)


class CaveEntry(Scene):

    def enter(self, name, bag):
        self.bag = bag
        self.name = name
        print "Wecome %s" %name
        print "You are right now standing in front of a huge cave."
        print "You have a bag where you can store tools or stuff that"
        print "you find on your way to the gold of Glorietta."
        print "To see what you have in your bag simply type bag"
        print "When you type something please only"
        print "use small characters."
        print "There are lianas all over the entry."
        print "What do you do?"
        action = raw_input("> ")

        while action == "bag":

            bag.show()
            action = raw_input("> ")

        if action == "use axe":
            print "You can cut the lianas and enter the cave."

            return 'cave', self.name

class Cave(Scene):

    def enter(self, name, bag):
        self.bag = bag
        self.name = name
        print "Well done %s, you are now standing in a big cave."
        print "You can barely see something because it is very dark."
        print "What do you do?"
        action = raw_input("> ")

        while action == "bag":

            bag.show()
            action = raw_input("> ")

        counter  = 0
        while action != "look around":
            if counter < 5:
                print "Maybee try to do something else!"
                action = raw_input("> ")
                counter = counter + 1
            else:
                print "You could try to look around ;)"
                action  = raw_input("> ")

        if action == "look around":
            print "You found a torch and put it in your bad!"
            self.bag.add("torch")

        print "And now?"




class BallRun(Scene):

    def enter(self, name, bag):
        pass

class PuzzleRoom(Scene):

    def enter(self, name, bag):
        pass

class TreasureRoom(Scene):

    def enter(self, name, bag):
        pass

class Death(Scene):

    def enter(self, name, bag):
        pass
