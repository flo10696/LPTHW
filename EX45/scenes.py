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

        while "bag" in action:

            bag.show()
            action = raw_input("> ")

        if action == "use axe":
            print "You can cut the lianas and enter the cave."
            self.bag.remove("axe")

            return 'cave', self.name, self.bag

        elif "go" or "run" in action:
            print "Only an idiot runs against a wall."
            print "Maybe you should think about that..."
            print "Because you are dead now."
            return 'death', self.name, self.bag

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
                print "Maybe try to do something else!"
                action = raw_input("> ")
                counter = counter + 1

                if "go" in action:
                    print "Because you did not see anything"
                    print "you ran against a rock and died!"
                    return 'death'

                while "bag" in action:

                    bag.show()
                    action = raw_input("> ")


                if "wait" in action:
                    print "You can wait when you are dead!"
                    print "You coward."
            elif "look around" not in action:
                print "You could try to look around ;)"
                action  = raw_input("> ")

        if "look around" in action:
            print "You found a torch and three rocks and put it in your bad!"
            self.bag.add("torch")
            self.bag.add("rock light")
            self.bag.add("rock medium")
            self.bag.add("rock heavy")

        print "And now?"
        action == raw_input("> ")

        while "bag" in action:

            bag.show()
            action = raw_input("> ")

        if "lit torch" in action:
            print "With the torch you can see some meters"
            print "into the cave and you go forward."
            print ""



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
