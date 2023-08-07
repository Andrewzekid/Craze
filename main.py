from utils import *
from score import *
#Issues - word list not accurate
#Not discounting grey letters
#Using the same letter twice? discourage

#Get all wordle words
corpus = get_input("valid-wordle-words.txt")

#Main loop
found = False
#While a word has not been found
target_list = corpus
    
while found != True:

    #Get users input and results
    guess = input("What is your guess: ")
    green = input("What position (1-5) were the greens at? Separate your answers with spaces, I.e 1 2 5: ")
    yellow = input("What position (1-5) were the yellows at? separate your answers with spaces, I.e 3 4: ")
    
    #Process inputs and turn all into a list of integers [1,2,5] [3,4]
    if green != "":
        green = [idx - 1 for idx in list(map(int,green.split(" ")))]
    else:
        green = []
    
    if yellow != "":
        yellow = [idx - 1 for idx in list(map(int,yellow.split(" ")))]
    else:
        yellow = []
    
    print(f"Guess {guess} got greens at {green} (green letters are {[guess[idx] for idx in green]}) and yellows at {[guess[idx] for idx in yellow]}!")
    
    if len(green) == 5:
        #Get out if done
        print("Found!")
        found = True
        break
    
    #Find candidate list of words -> Narrow target list down each time
    target_list = heuristic(target_list,guess,green,yellow)
    next_guess = return_best_guess(target_list,guess,green,yellow)
    assert next_guess != None and next_guess != "", f"Next guess is none or empty string! targetlist: {target_list[:5]}"
    print(f"Target list updated to {target_list[:5]} and next guess is {next_guess}!")
    print("======================================================")
    

    