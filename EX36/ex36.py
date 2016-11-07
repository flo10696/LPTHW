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
            gotz_room(gotz_passed, nishant_passed, jonathan_passed)
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
                gotz_room(gotz_passed, nishant_passed, jonathan_passed)
            elif door == "4" and passed != True:
                print "This door is locked!"
            elif door == "4" and passed == True:
                holy_room()
            else:
                print "Choose a door or you will fail and will never get back here!"




def gotz_room(gotz_passed, nishant_passed, jonathan_passed):
    if gotz_passed == False:
        if nishant_passed == False and jonathan_passed == False:
            print "You first have to passed the other two Rooms."
        elif nishant_passed == False and jonathan_passed == True:
            print "You have to pass nishants challenge first"
        elif nishant_passed == True and jonathan_passed == False:
            print "You have to pass jonathans challenge first"
        else:
            print "You have now entered a room which is very chaotic."
            print "Everywhere are big stacks of paper."
            print "And Gotz, the professor, is sittin in the middle of the room and is trying to process the stacks."
            print "He is sorrounded by MacBooks and Smartphones that are trying to distract him"
            print "You have to convince him to correct your exam from the first semester right now!"
            print "because if he does not do it you wont get your Bachelor degree."
            print "What do you want to say to him?:"
            print "1: If you do it right now you get a crate of beer"
            print "2: You get into ragemode and shout at him"
            print "3: You have no idea what to say and go home to cry"

            while True:
                answer_gotz = raw_input("> ")
                if answer_gotz == "1":
                    print "I would do everything for a beer right now. Your exam is done in /n 3...2...1... DONE!"
                    gotz_passed = True
                elif answer_gotz == "2":
                    print "Just caaaaaaaaalm down and relax."
                elif answer_gotz == "3":
                    print "Do not cry! It is okay!"
                    print "It does not work!"

                else:
                    print "I have no idea what you meant! Try again!"



    else:
        print "You can now enter the fourth room. Do you want to?"
        enter_room = raw_input("> ")

        if enter_room == True:
            holy_room()
        else :
            print "I don't care what you want to!"
            holy_room()


def jonathan_room(jonathan_passed):
    if jonathan_passed == False:
        print "You hear loud techno music and see a guy standing behind his MacBook."
        print "He is typing chaoticly on it."
        print "You want to tell him about your arduino project."
        print "But first you have to get his attention!"
        print "How would you do that?"
        print "1: Show him your big relay and tell him that it is only 20 bugs."
        print "2: Show him that you made the LED to fade."
        print "3: Unpower his MacBook."

        while jonathan_passed == False:
            answer_jonathan = raw_input("> ")

            if answer_jonathan == "1":
                print "He suddenly stops to play with his computer and listens to you."
                print "You made it. Congratulation!"
                jonathan_passed = True
            elif answer_jonathan == "2":
                print "That is nothing interesting for him. He keeps on playing."
                print "TRY AGAIN!"
            elif answer_jonathan == "3":
                print "You idiot! A Macbook also runs without power supply!"
                print "TRY AGAIN!"
            else:
                print "I have no idea what you mean!"

        passed = True
        print "There are four doors:"
        print "But the fourt door is locked. Which door do you want to enter?"

        while True:
            door = raw_input("> ")
            if door == "1":
                start_room(True, gotz_passed, jonathan_passed)
            elif door == "2":
                nishant_room(nishant_passed)
            elif door == "3":
                gotz_room(gotz_passed, nishant_passed, jonathan_passed)
            elif door == "4" and passed != True:
                print "This door is locked!"
            elif door == "4" and passed == True:
                holy_room()
            else:
                print "Choose a door or you will fail and will never get back here!"

    else:
        print "You can now enter another room."
        while True:
            door = raw_input("> ")
            if door == "1":
                start_room(True, gotz_passed, jonathan_passed)
            elif door == "2":
                nishant_room(nishant_passed)
            elif door == "3":
                gotz_room(gotz_passed, nishant_passed, jonathan_passed)
            elif door == "4" and passed != True:
                print "This door is locked!"
            elif door == "4" and passed == True:
                holy_room()
            else:
                print "Choose a door or you will fail and will never get back here!"


def holy_room():
    print "You made it into the holy room."
    print "In the middle of the room you see your bachelor degree flying."
    exit(0)

start_room(False, False, False)
