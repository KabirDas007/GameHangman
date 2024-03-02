# GameHangman
Code to play the wordgame known as hangman with computer.
<br>
If unfamiliar with the rules of the game please read https://en.wikipedia.org/wiki/Hangman_(game).
<br> 
Game Rules: 
1. The user starts with 3 warnings and 6 guesses.
2. If the user inputs anything besides an alphabet (symbols, numbers), tells the
user that they can only input an alphabet.  
  	a. If the user has one or more warning left, the user should lose one 
	warning. Tells the user the number of remaining warnings.<br>
  	b. If the user has no remaining warnings, they should lose one guess.
3. If the user inputs a letter that has already been guessed, prints a message
telling the user the letter has already been guessed before.<br>
	a. If the user has one or more warning left, the user should lose one 
	warning. Tells the user the number of remaining warnings.<br>
	b. If the user has no warnings, they should lose one guess.
4. If the user inputs a letter that hasn’t been guessed before and the letter is in 
the secret word, the user loses no​ guesses. 
5. Consonants:​ If the user inputs a consonant that hasn’t been guessed and the
consonant is not in the secret word, the user loses one​ guess if it’s a 
consonant.
6. Vowels:​ If the vowel hasn’t been guessed and the vowel is not in the secret
​​​​​​ word, the user loses two​ guesses. Vowels are a, e, i, o, and u. y does not 
count as a vowel.<br>

Game Termination: 
1. The game should end when the user constructs the full word or runs out of 
guesses.  
2. If the player runs out of guesses before completing the word, tell them they
lost and reveal the word to the user when the game ends.  
6
3. If the user wins, print a congratulatory message and tell the user their score.  
4. The total score is the number of guesses_remaining once the user has
guessed the secret_word times the number of unique letters in secret_word.  
Total score = guesses_remaining* number unique letters in secret_word


Hints:
If user guesses the special character * the computer will find all the words
from its loaded list that might match your current guessed word, and print out each of 
them. Of course, we don’t recommend trying this at the first step, since this will print
out a very large number of words!  But if you are getting close to an answer and
are running out of guesses, this might help. Number of guesses wont be deducted.
