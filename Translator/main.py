import sys
import translation_watson
import gui

def main():


    app = gui.QApplication(sys.argv)
    ex = gui.Gui()
    translator = translation_watson.Translator()

    ex.update(0, translator.translateInput(3, "What time is it?"))

    #for x in range(0,11):
    #    ex.update(x, translator.translateInput(x+1, "What time is it?"))

    sys.exit(app.exec_())

main()
