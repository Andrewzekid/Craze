import numpy as np

def heuristic(corpus,guess,greens,yellows):
    """
    Find a list of words that should be considered from next
    Args:
        corpus: list of words
        guess: previous guess
        greens: list containing indexes of what letters in the guess was green
        yellows: list containing indexes of what letters in guess was yellow
    Returns:
        target_list (list): list of guesses to be considered
    """
    #Get the green and yellow letters in the previous guess
    green_letters = [guess[i] for i in greens]
    yellow_letters = [guess[j] for j in yellows]
    
    target_list = []
    scores_list = []
    
    #remove the current guess from the corpus
    corpus = corpus
    corpus.remove(guess)
    target_list = corpus
    
    if len(green_letters) > 0:
        #Filter all green letters
        for i in range(len(greens)):
            current_green_letter = green_letters[i]
            current_green_index = greens[i]
            #Filter all words that have the green letter in them at the same position
#             print(corpus)
            target_list = [word for word in target_list if current_green_letter in word and word[current_green_index] == current_green_letter]
            
    if len(yellow_letters) > 0:
#         print(target_list)
        for i in range(len(yellows)):
            current_yellow_letter = yellow_letters[i]
            current_yellow_index = yellows[i]
            #Filter all words that have the yellow letter in them but not at the same position
            target_list = [word for word in target_list if current_yellow_letter in word and word[current_yellow_index] != current_yellow_letter]

    blacks = {0,1,2,3,4} - set(greens) - set(yellows)
    print(blacks,greens,yellows)
    black_letters = [guess[i] for i in blacks]
    #Index of all black letters
    #Black = NOT IN THIS POSITION OR NOT IN THIS WORD.
    #First of all, filter out the not in this positions. THen filter out not in this words.
    black_letters_and_position = [{letter:idx} for idx,letter in enumerate(black_letters)] #[{"R":0},{"A":1},"T":2}
    #Get how many times each letter occurs in a string
    black_counts_dict = {letter:0 for letter in set(black_letters)}

    for letter in black_letters:
        black_counts_dict[letter] += 1
    

    

    print(f"Dictionary of black letters and their positions: {black_letters_and_position}. Counts: {black_counts_dict}")
    #This letter is not in this position
    if len(black_letters) > 0:
        #More than 1 black letter
        for i in range(len(blacks)):
            current_black_letter_and_position = black_letters_and_position[i]
            current_black_letter = str(list(current_black_letter_and_position.keys())[0])
            current_black_position = int(list(current_black_letter_and_position.values())[0])
            print(f"Excluding current black letter: {current_black_letter} which is at position {current_black_position}")
            print(target_list)
            target_list = [word for word in target_list if word[current_black_position] != current_black_letter]
        print(f"New target_list is: {target_list}")
        
        #This letter is not in this word. I.e: [{"R":2},{"V":1}] - two rs are black and one v is black filter out words with 1 v and 2 rs.
        for letter,count in black_counts_dict.items():
            print(f"Exluding words with {count} {letter}'s")
            #I.e: if there is not two Rs in this, then exclude words with 3rs, 4rs, 5rs and 2rs
            target_list = [word for word in target_list if not(word.count(letter) >= count)]
        print(f"New target_list is: {target_list}")
    #Find how many black letters there can be
        #For every word, if it has one or more of the black 


    return target_list

def score(candidate,guess,greens,yellows):
    """
    Calculate how good a candidate guess is
    Args:
        candidate (str): candidate guess to be considered
        guess (str): previous guess
        greens (list[int]): list containing indexes of what letters were green 
        yellows (list[int]): list containing indexes of what letters were yellow
    Returns:
        score (0-1) of how good the guess is
    """
    #Greens and yellows contain indexes of greens and yellows
    green_letters_in_candidate = [guess[i] for i in greens if guess[i] in candidate]
    yellow_letters_in_candidate = [guess[j] for j in yellows if guess[j] in candidate]
    duplicates = 0
    copy = candidate
    for letter in copy:
        #Remove that letter
        copy = copy.replace(letter,"",1)
        if letter in copy:
            #Duplicate
            duplicates = duplicates + 1

    #Initialize score
    score = 0
    
    #Score calculations
    score += (30 * len(green_letters_in_candidate))
    score += (10 * len(yellow_letters_in_candidate))
    score -= (duplicates * 10)
    
    score /= 150
    print(f"Score for {candidate} is {score}!")
    return score

def return_best_guess(target_list,guess,greens,yellows):
    """
    Given a list of candidate words to be considered, return the best candidate guess
    Args:
        target_list: list of candidate guesses to be considered
        guess: previous guess
        greens: list containing indexes of what letters in the previous guess were green
        yellows: list containing indexes of what letters in the previous guess were yellow
    """
    scores = [score(candidate,guess,greens,yellows) for candidate in target_list]
#     print(scores)
    return target_list[np.argmax(scores)]