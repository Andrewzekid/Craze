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
    
    if len(green_letters) > 0:
        #Filter all green letters
        target_list = corpus
        for i in range(len(greens)):
            current_green_letter = green_letters[i]
            current_green_index = greens[i]
            #Filter all words that have the green letter in them at the same position
#             print(corpus)
            target_list = [word for word in target_list if current_green_letter in word and word[current_green_index] == current_green_letter]
            
    if len(yellow_letters) > 0:
        if target_list == []:
            #No greens so create target list
            target_list = corpus
#         print(target_list)
        for i in range(len(yellows)):
            current_yellow_letter = yellow_letters[i]
            current_yellow_index = yellows[i]
            #Filter all words that have the yellow letter in them but not at the same position
            target_list = [word for word in target_list if current_yellow_letter in word and word[current_yellow_index] != current_yellow_letter]
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
    
    #Initialize score
    score = 0
    
    #Score calculations
    score += (30 * len(green_letters_in_candidate))
    score += (10 * len(yellow_letters_in_candidate))
    score /= 150
    
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