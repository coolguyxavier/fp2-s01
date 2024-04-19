# - FP2-S01 - External Files Summative - #
# - Xzavier Mooosmin - #
# - 04/09/2024 - #
 
 
# - The Purpose of this Program - #
# I am hoping that my program that I plan to code somehow helps people understand a topic.
# A topic on usernames and numbers in a dictionary
# like a highscore board
# A topic on easily reading and writing into a file
# The project I plan on doing is allowing the user to both read and add their own usernames

# - Developer Notes - #
# i might just be overdoing it, i dunno
# yeah im overdoing it
# swhyte says simple program so im keeping it simple

# - Imports - #
from time import sleep
    
# - Functions - #

def main():
    run = 1
    while run == 1:
        user_choice = input("You want to read or write?\n1 - Read\n2 - Write\n>").lower()
        if user_choice == "1" or user_choice == "read":
            readfile()
            
        elif user_choice == "2" or user_choice == "write":
            print("Prepare to add to the file.")
            appendfile()
        
        elif user_choice == "3" or user_choice == "quit":
            run = 0
def readfile():
    print("Here's all the scores.")
    highscores = open('scores.txt', 'r') # opens the .txt file and saves it as highscores
    lines = highscores.readlines() # reads all the lines and saves it as lines
    
    for line in lines:
        print(line) # prints each line seperately
        sleep(0.5) # ensures that its easy to follow
    
    firstpos = (lines[1])
    print("The user in First place is:", firstpos)    
    
    highscores.close() # closes once done  

def appendfile():
    add_name = input("What name are you going to add?\n>")
    
    add_score = input("What score do they have?\n>")
    
    highscores = open('scores.txt', 'a') # opens file
    
    highscores.write("\n" + add_name + "-" + add_score) # on a new line at the bottom, add together the user's name and score choice
    
    highscores.close() # closes file
    
    print("Your username and score was added to the .txt file.")
    
# - Main Code - #
print("Want to know highscores?")
sleep(1)
print("Too bad, you're gonna know them anyways.")
sleep(2)
main()
sleep(2)

print("Bye bye!")
