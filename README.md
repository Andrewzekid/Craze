# Craze
Craze Wordle Solver, Using filtering to iteratively find the correct answer.
Craze takes in a guess, information about what letters are yellow and green, and from a list of all possible wordle words, picks the next best guess.

Version 1.1 (:white_check_mark:):
===================================
- [X] Load list of words
- [X] Take input of a guess and data about yellow and green letters :tada:
- [X] Function to calculate the score for a candidate guess, representing how good that guess is
- [X] Filter list of words to based on information about what is yellow and green
- [X] Return best guess from a list of guesses

Todo:
----
- [ ] Filter list of candidate words to exclude greyed out letters
- [ ] Discourage guesses that have two or more of the same letter
- [ ] Improve performance, currently around 4-5 guesses on average
- [ ] Update metric we’ll use to evaluate each guess: [predicted number of remaining words after that guess.](https://medium.com/@gordonbchen/wordle-solver-a1a531d22085)
We’ll calculate the predicted remaining words after a guess by taking the sum of (the number of remaining words after a set of colors) weighted (aka multiplied) by (the probability of getting that set of colors) over all combinations of colors.
- [ ] Fix word list, current word list is: [current word list](https://gist.github.com/dracos/dd0668f281e685bad51479e5acaadb93)
- [ ] Reinforcement learning implementation (In far far future)


