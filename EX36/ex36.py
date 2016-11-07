from sys import exit

passed = False

nishant_passed = False
gotz_passed = False
jonathan_passed = False

nishant_text = """
For your topic you would really have to take into account that the women have been underestiminated in coputerscience
in the book "When computers were women" it is pointed out really good that women have been a major part in the development of computers
and also that the tasks that computers do today were excecuted by women. And Women were also called computers and so on and so forth.
Do not use Wikipedia as a source because like somebody pointed out in whatever it is not really reliable
for example are many women not listed on Wikipedia because nobody wrote about them an so on and so forth.
There is a little village in India near to the chinese border where the people started to write in mandarin letters because
the smartphones werent able to deal with the dialect that is spoken there.
You should also think about what Facebook does with it's free internet project and so on and so forth
For your topic you would really have to take into account that the women have been underestiminated in coputerscience
in the book "When computers were women" it is pointed out really good that women have been a major part in the development of computers
and also that the tasks that computers do today were excecuted by women. And Women were also called computers and so on and so forth.
Do not use Wikipedia as a source because like somebody pointed out in whatever it is not really reliable
for example are many women not listed on Wikipedia because nobody wrote about them an so on and so forth.
There is a little village in India near to the chinese border where the people started to write in mandarin letters because
the smartphones werent able to deal with the dialect that is spoken there.
You should also think about what Facebook does with it's free internet project and so on and so forth
For your topic you would really have to take into account that the women have been underestiminated in coputerscience
in the book "When computers were women" it is pointed out really good that women have been a major part in the development of computers
and also that the tasks that computers do today were excecuted by women. And Women were also called computers and so on and so forth.
Do not use Wikipedia as a source because like somebody pointed out in whatever it is not really reliable
for example are many women not listed on Wikipedia because nobody wrote about them an so on and so forth.
There is a little village in India near to the chinese border where the people started to write in mandarin letters because
the smartphones werent able to deal with the dialect that is spoken there.
You should also think about what Facebook does with it's free internet project and so on and so forth
For your topic you would really have to take into account that the women have been underestiminated in coputerscience
in the book "When computers were women" it is pointed out really good that women have been a major part in the development of computers
and also that the tasks that computers do today were excecuted by women. And Women were also called computers and so on and so forth.
Do not use Wikipedia as a source because like somebody pointed out in whatever it is not really reliable
for example are many women not listed on Wikipedia because nobody wrote about them an so on and so forth.
There is a little village in India near to the chinese border where the people started to write in mandarin letters because
the smartphones werent able to deal with the dialect that is spoken there.
You should also think about what Facebook does with it's free internet project and so on and so forth
For your topic you would really have to take into account that the women have been underestiminated in coputerscience
in the book "When computers were women" it is pointed out really good that women have been a major part in the development of computers
and also that the tasks that computers do today were excecuted by women. And Women were also called computers and so on and so forth.
Do not use Wikipedia as a source because like somebody pointed out in whatever it is not really reliable
for example are many women not listed on Wikipedia because nobody wrote about them an so on and so forth.
There is a little village in India near to the chinese border where the people started to write in mandarin letters because
the smartphones werent able to deal with the dialect that is spoken there.
You should also think about what Facebook does with it's free internet project and so on and so forth
For your topic you would really have to take into account that the women have been underestiminated in coputerscience
in the book "When computers were women" it is pointed out really good that women have been a major part in the development of computers
and also that the tasks that computers do today were excecuted by women. And Women were also called computers and so on and so forth.
Do not use Wikipedia as a source because like somebody pointed out in whatever it is not really reliable
for example are many women not listed on Wikipedia because nobody wrote about them an so on and so forth.
There is a little village in India near to the chinese border where the people started to write in mandarin letters because
the smartphones werent able to deal with the dialect that is spoken there.
You should also think about what Facebook does with it's free internet project and so on and so forths


Did you understand everything or should I repeat it for you?
Yes or No?
"""


def start_room(nishant_passed, gotz_passed, jonathan_passed):
    print "You are in a big, bright room with many people"
    print "They are all talking in Denglish and you do not understand a whole sentence."
    print "There are four doors but the fourth is locked."
    print "Which door do you want to open?"

    while True:
        door = raw_input("> ")
        if door == "1":
            nishant_room(nishant_passed)
        elif door == "2":
            jonathan_room(jonathan_passed)
        elif door == "3":
            gotz_room(gotz_passed)
        elif door == "4" and passed != True:
            print "This door is locked!"
        elif door == "4" and passed == True:
            holy_room()
        else:
            print "Choose a door or you will fail and will never get back here!"


def nishant_room(nishant_passed):
    if nishant_passed != True:
        print "You are in a room with very loud indian music."
        print "An indian looking person is sitting inbetween a mountain of donuts and donut boxes."
        print "In front of him is a big Notebook."
        print "You see that he is writing a big post on his Facebook page."
        print "You can also see that his name is Nashint"
        print "He is one of your professors and you have to ask him about his opinion about your topic for your exam."
        print "What do you ask him?"

        question = raw_input("> ")

        if "brief" in question or "short" in question:
            nishant_answer(True)
        else:
            nishant_answer(False)
    else:
        nishant_answer(True)



def nishant_answer(short):
    if short == False:
        print nishant_text
        while True:
            repeat = raw_input("> ")
            if repeat == "Yes":
                nishant_answer(False)
            elif repeat == "No":
                nishant_answer(True)
            else:
                print "I have no idea what you said!"

    else:
        print "I think your topic is good. Work on that and read 400 pages until tomorrow"
        print "Congratulation! You passed this Challenge!"
        passed = True
        print "There are four doors:"
        print "But the fourt door is locked. Which door do you want to enter?"



        while True:
            door = raw_input("> ")
            if door == "1":
                start_room(True, gotz_passed, jonathan_passed)
            elif door == "2":
                jonathan_room(jonathan_passed)
            elif door == "3":
                gotz_room(gotz_passed)
            elif door == "4" and passed != True:
                print "This door is locked!"
            elif door == "4" and passed == True:
                holy_room()
            else:
                print "Choose a door or you will fail and will never get back here!"




def gotz_room(gotz_passed):
    print "test"

def jonathan_room(jonathan_passed):
    print "test"

def holy_room():
    print "Test"

start_room(False, False, False)
