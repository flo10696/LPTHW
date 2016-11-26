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
        print "Wecome %s" %self.name
        print "You are right now standing in front of a huge cave."
        print "You have a bag where you can store tools or stuff that"
        print "you find on your way to the gold of Glorietta."
        print "To see what you have in your bag simply type bag"
        print "When you type something please only"
        print "use small characters."
        print "There are lianas all over the entry."
        print "What do you do?"
        action = "x"

        while "use axe" not in action:
            action = raw_input("> ")
            if "bag" in action:
                self.bag.show()

            if action == "use axe":
                print "You can cut the lianas and enter the cave."
                self.bag.remove("axe")
                return 'cave', self.name, self.bag

            if "run" in action:
                print "Only an idiot runs against a wall."
                print "Maybe you should think about that..."
                print "Because you are dead now."
                return 'death', self.name, self.bag

            else:
                "I have no idea what you mean"

        if action == "use axe":
            print "You can cut the lianas and enter the cave."
            self.bag.remove("axe")
            return 'cave', self.name, self.bag

class Cave(Scene):

    def enter(self, name, bag):
        self.bag = bag
        self.name = name
        print "Well done %s, you are now standing in a big cave." %self.name
        print "You can barely see something because it is very dark."
        print "What do you do?"
        action = "x"

        counter  = 0
        while "look around" not in action:
            action = raw_input("> ")
            if counter < 5:
                if "bag" in action:
                    self.bag.show()

                else:
                    print "Maybe try to do something else!"
                    counter = counter + 1

                if "go" in action:
                    print "Because you did not see anything"
                    print "you ran against a rock and died!"
                    return 'death', self.name, self.bag

                if "bag" in action:

                    self.bag.show()


                if "wait" in action:
                    print "You can wait when you are dead!"
                    print "You coward."

            elif "look around" not in action:
                print "You could try to look around ;)"

        if "look around" in action:
            print "You found a torch and three rocks and put it in your bad!"
            self.bag.add("torch")
            self.bag.add("rock light")
            self.bag.add("rock medium")
            self.bag.add("rock heavy")

        print "And now?"
        action = "x"

        while "lit torch" not in  action:
            action = raw_input("> ")
            if "bag" in action:

                self.bag.show()

            elif "light torch" in action:
                print "With the torch you can see some meters"
                print "into the cave and you go forward."
                print "You accidentially step on a latch"
                print "which releases a huge stone from above your head."
                print "This stone is now pursuiting you"
                print "with increasing speed."
                self.bag.remove("torch")
                return 'ballRun', self.name, self.bag

            elif "rock" in action:
                self.bag.remove("small rock")
                print "You throw a rock inside the cave and release"
                print "a huge stone which is behind you."
                print "It is pursuiting you and you start to run"
                print "but because you can't see anything you"
                print "you strumble over the rock you have thrown."
                print "You die."

                return 'death', self.name, self.bag

            else:
                print "I have no idea what you are trying to do here!"



        if "light torch" in action:
            print "With the torch you can see some meters"
            print "into the cave and you go forward."
            print "You accidentially step on a latch"
            print "which releases a huge stone from above your head."
            print "This stone is now pursuiting you"
            print "with increasing speed."
            self.bag.remove("torch")
            return 'ballRun', self.name, self.bag



class BallRun(Scene):

    def enter(self, name, bag):
        self.bag = bag
        self.name = name
        print "You are fleeing from the huge Ball which is following you."
        print "What do you do to stop the Ball?"
        action = "x"

        while "rock heavy" not in action:
            action = raw_input("> ")

            if "bag" in action:
                self.bag.show()

            elif "rock heavy" in action:
                self.bag.remove("rock heavy")
                print "You throw the big rock from your bag."
                print "It lands behind you and can stop the huge rock at that position."
                print "After you relaxed a bit from the running you notice"
                print "a big altar in front of you."
                return 'puzzleRoom', self.name, self.bag

            elif "rock medium" in action:
                pass
            elif "rock small" in action:
                pass
            elif "run" in action:
                pass
            else:
                pass


class PuzzleRoom(Scene):

    def enter(self, name, bag):
        self.bag = bag
        self.name = name
        print "A key lays on the top of the altar and you recognize that"
        print "it is laying on a balanced spot."
        print "What do you do?"
        action = "x"

        while "rock medium" not in action:
            action = raw_input("> ")

            if "bag" in action:
                self.bag.show()

            elif "rock medium" in action:
                print "You exchange the key with the medium rock."
                print "Because it is the same weight nothing happens"
                print "and you can take the key and put it in your bag."
                self.bag.add("key")
                self.bag.remove("rock medium")

                return 'treasureRoom', self.name, self.bag

            elif "rock small" in action:
                print "You try to exchange the key with"
                print "the small rock. But the small rock"
                print "is not heavy enough and because of that"
                print "a mechanism starts that shoots 42 poisioned"
                print "arrows at you that all hit you."

                return 'death', self.name, self.bag

            else:
                print "I have no idea what that means."


class TreasureRoom(Scene):
    def enter(self, name, bag):
        self.name = name
        self.bag = bag
        print "Congratulations you are not standing"
        print "In front of a huge door."
        print "What do you do?"

        action = "x"

        while "key" not in action:
            action = raw_input("> ")

            if "bag" in action:
                self.bag.show()

            elif "rock small" in action:
                print "You throw the small rock against the door,"
                print "it hits it and is returned right back to you."
                print "It hits your head - you die."

                return 'death', self.name, self.bag

            elif "key" in action:
                print "You put the key into the lock."
                print "And you can turn it."
                print "QQQQIIIIIIEEETZ"
                print "You can open it."
                print "You get into the room and find the treasure:"
                print "It's a toy ape with a little drum on which it is playing."

                return 'finish', self.name, self.bag

            else:
                print "I have no idea what you mean."


class Finish(Scene):

    def enter(self, name, bag):
        print "Congratulations %s. You finished this adventure" %name

class Death(Scene):

    def enter(self, name, bag):
        scenarios = ["You Idiot! You are dead.",
                    "Woooow, you are dead.",
                    "Congratulations! - wait - you are dead. Alright no congrats!",
                    "Yeah, thats not what you wanted right?",
                    "Ooooooooops",
                    "An End can also be a beginning - just try again."]

        print scenarios[randint(0, 5)]
        exit(1)
