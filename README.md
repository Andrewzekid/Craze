# Craze
Craze Wordle Solver, Using filtering to iteratively find the correct answer.
Craze takes in a guess, information about what letters are yellow and green, and from a list of all possible wordle words, picks the next best guess.

Version 1.1 (:white_check_mark:):
===================================
Performance: <span style="color: red;">5-6 guesses.</span>
- [X] Load list of words
- [X] Take input of a guess and data about yellow and green letters :tada:
- [X] Function to calculate the score for a candidate guess, representing how good that guess is
- [X] Filter list of words to based on information about what is yellow and green
- [X] Return best guess from a list of guesses

## Version 1.2 (✅):

> [!NOTE]
> Performance of this version was around 3-4 guesses
- [X] Filter list of candidate words to exclude greyed out letters
- [X] Discourage guesses that have two or more of the same letter

> [!IMPORTANT]
> Patch fix 1.21 Fixed bug of 1 yellow letter and 1 black letter causing program to glitch out

Todo:
----
- [X] Filter list of candidate words to exclude greyed out letters
- [X] Discourage guesses that have two or more of the same letter
- [ ] Improve performance, currently around 4-5 guesses on average (See metric, greyed and fix word list)
- [ ] Update metric we’ll use to evaluate each guess: [predicted number of remaining words after that guess.](https://medium.com/@gordonbchen/wordle-solver-a1a531d22085)
- [ ] Fix word list, current word list is: [current word list](https://gist.github.com/dracos/dd0668f281e685bad51479e5acaadb93)
- [ ] Reinforcement learning implementation (In far far future)
- [ ] Incorporate probability that words come up into score calculation
- [ ] [#1 ](https://github.com/Andrewzekid/Craze/issues/1)https://github.com/Andrewzekid/Craze/issues/1


