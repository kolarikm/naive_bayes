import sys

"""
print "Hello, goodbye!"

var = raw_input("Please enter something: ")
print "You entered", var
"""

def loop():
    while True:
        print "Please make a selection:"
        print "1: Base Classifier\n2: Predictor\n0: Exit"
        choice = raw_input("-> ")
        if choice == "1":
            execfile("test.py")
        if choice == "2":
            print "Chose 2!"
        if choice == "0":
            print "Goodbye!"
            break

loop()

sys.exit
