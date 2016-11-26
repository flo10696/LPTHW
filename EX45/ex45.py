
from sys import exit
from random import randint
import scenes
import bag



class Engine(object):

    def __init__(self, scene_map, pBag):
        self.scene_map = scene_map
        self.bag = pBag

    def play(self):
        print "Hello! Welcome to this adventure!"
        print "Bevore we start: What's your name?"
        self.name = raw_input("> ")
        print "All right %s! Let's start our journey!" %self.name
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finish‚')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter(self.name, self.bag)
            self.bag = next_scene_name[2]
            self.name = next_scene_name[1]
            next_scene_name = next_scene_name[0]
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter(self.name, self.bag)


class Map(object):

    sceneList = {
        'entry' : scenes.CaveEntry(),
        'cave' : scenes.Cave(),
        'ballRun' : scenes.BallRun(),
        'puzzleRoom' : scenes.PuzzleRoom(),
        'treasureRoom' : scenes.TreasureRoom(),
        'death' : scenes.Death(),
        'finish' : scenes.Finish(),
    }

    def __init__(self, start_scene):
        self.start = start_scene

    def next_scene(self, scene_name):
        return self.sceneList.get(scene_name)

    def opening_scene(self):
        Val = self.next_scene(self.start)
        return Val

aBag = bag.Bag()
aMap = Map('entry')
game = Engine(aMap, aBag)
game.play()
