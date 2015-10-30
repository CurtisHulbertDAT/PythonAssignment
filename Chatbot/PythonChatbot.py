from stop_words import get_stop_words

stop_words = get_stop_words('en')
stop_words = get_stop_words('english')

response = raw_input ("Hello there human. What is your name? ")
print ("Hello " + response)
response = raw_input("are you OK? ")
if (response.find("yes") > -1):
	print ("good")
else:
	print ("sorry to hear that")
response = raw_input("Can I ask you a question?")
if (response.find("yes") > -1):
	print ("Brilliant! here is the first question")
else:
	print ("Not to worry then. Goodbye.")

print ("Here is your first question")

import random

questions = ["what is the capital of France?", "What is the main ingredient in bolognaise?", "How many days in a week?"]

def shuffle(questions):
    if len(Question) >0:
        random.shuffle(questions)
        win = questions.pop()
        print("the question is: %s" % win)
    else:
        print ("I dont have anymore questions to ask")
begin = raw_input (questions)
if (response.find ("Paris","Tomato","7") >-1):
    print ("Well done that's correct")
else:
    print ("Oops. That's wrong I'm afraid")
begin = raw_input ("did you enjoy the quiz?")
if (response.find ("yes") >-1):
    print ("Good too hear. I enjoyed playing")
else:
     print ("Damn. I guess I'll need some better questions next time :/")
        