import sys
import translation_watson
import gui

class Controller():

    def __init__(self):


        self.app = gui.QApplication(sys.argv)
        self.gui = gui.Gui(self)
        self.translator = translation_watson.Translator()
        self.gui.initUI()


        sys.exit(self.app.exec_())

    def translate(self, readText):
        self.app.processEvents()

        for x in range(0,11):
            
            self.gui.update(x, self.translator.translateInput(x+1, readText))
            self.app.processEvents()
