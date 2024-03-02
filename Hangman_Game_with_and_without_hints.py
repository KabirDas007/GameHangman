#if you want a hint, enter '*' when asked for an alphabet

import string
import random

WORDLIST_FILENAME = 'words.txt'


def load_words():
    print('Loading wordlist from file...')
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("     ", len(wordlist), 'words loaded')

    return wordlist

def choose_word(wordlist):
    return random.choice(wordlist)

wordlist = load_words()
#print(wordlist)

def is_word_guessed(secret_word,letters_guessed):
# this function is used in the while loop to decide if the secret word has been guessed or not
# based on the letters guessed by the user
    flag = 0
    for e in secret_word:
        if e in letters_guessed:
            pass
        else:
            flag = 1
            break
    if flag ==1:
        return False
    else:
        return True
        

import string        
def get_available_letters(letters_guessed):
# shows the letters that havent been guessed so far and hence are valid future guesses

    avl_lett = string.ascii_lowercase[:]

    for e in avl_lett:
        if e in letters_guessed:
            n = avl_lett.find(e)
            avl_lett = avl_lett[:n]+avl_lett[n+1:]
    return(avl_lett)
    
def get_guessed_word(secret_word,letters_guessed):
# shows the state of the game: the letters that have been guessed correctly appear at their respective places in the secret word, and others are shown as  '_ '
    
    display_string = ''
    for e in secret_word:
        if e in letters_guessed:
            display_string = display_string + e
        else:
            display_string += '_ '
    return display_string


def matching_with_gaps(myword ,otherword):
# tells if a word is a possible choice for the secret word based on the letters in the secret word revealed so far
    myword = myword.replace(' ','')         #removing the space to correct the number of letters in myword.
    dl = []                                 #dl = discovered letters  for example secret word = boobs, and myword = 'b_ _ bs', then dl = ['b','s']

    if len(myword) != len(otherword):
        return False
    for e in myword:
        if e !='_' and e not in dl:
            dl.append(e)
    #print(dl)

    rll = []                                # rrl = revealed letters indexes in the secret word 'boobs': ex rll = [0,3,4]
    bll = []                                #bll = blank letters indices ex bll = [1,2]

    for i in range(len(myword)):
        if myword[i] != '_':
            rll.append(i)
        else:
            bll.append(i)
    #print(rll)
    #print(bll)

    for i in rll:
        if myword[i] == otherword[i]:               # code to check if the revealed letters in the words matches with the letters in the other word at the same indices
            flag1 = 0
        else:
            flag1 = 1
            break
    
    for i in bll:                                   # code to ensure that the other word does not contain discovered letters at places other than revealed indices,
                                                        # as that will mean that it can not be the secret word.
            if otherword[i] not in dl:
                flag2 = 0
            else:
                flag2 = 1
                break

    if flag2 == 0 and flag1 == 0:
        return True
    else:
        return False
    
def show_possible_matches(myword):
    lp = []          #list of possibilities
    for e in wordlist:
        if matching_with_gaps(myword,e):
            lp.append(e)
    #print(lp)
    return lp


    
def Hangman(secret_word):
    #print(secret_word)
    warning = 3
    number_guesses = 6
    letters_guessed = []                    #letters already guesed by the player
    #secret_word = choose_word(wordlist)
    print('I am thinking of a word that is', len(secret_word), ' letters long.')
    print('my choosen word is:',secret_word,'but pretend that you didnt see this word')
    vowels = ['a','e', 'i','o','u']
    while not is_word_guessed(secret_word, letters_guessed) and number_guesses>0:
        print('Available letters:', get_available_letters(letters_guessed))
        print('list of used letters used so far is:',letters_guessed)

        next_letter = input('Enter an alphabet:')
        if next_letter == '*':
            if len(letters_guessed) >0:
                myword = get_guessed_word(secret_word,letters_guessed)
                #print('myword is',myword)
                print(show_possible_matches(myword))
            else:
                print('cant seek help without trying')
        elif  str.isalpha(next_letter):
            next_letter = str.lower(next_letter)
            print(next_letter)   

            #print(letters_guessed)
            if next_letter in letters_guessed:
                if warning>0:
                    warning -= 1
                    print('That letter has already been guessed,you have ',warning, 'warnings left')
                else:
                    number_guesses -= 1
                
            if next_letter in secret_word:
                if next_letter not in letters_guessed:
                    letters_guessed.append(next_letter)
                    print('Good Guess!!')

            if next_letter not in secret_word and next_letter not in letters_guessed:
                if next_letter not in vowels:
                    number_guesses -= 1
                else:
                    number_guesses -= 2
                print('Oops! That letter not in my word')    
                letters_guessed.append(next_letter)
            print(letters_guessed)
        else:
            if warning>0:
               warning -= 1

            else:
               number_guesses -=1
            print('Oops! That is not a valid letter. You have', warning , 'warnings left')
        print('number of Guesses: ', number_guesses)
        print(get_guessed_word(secret_word, letters_guessed))
        print('______________________________________________________')
    if number_guesses <= 0:
            print('My friend! you lost. But its just a game.')
            print('The word I guessed  was: ', secret_word)
    else:
        if is_word_guessed(secret_word, letters_guessed):
            l = []
            for e in secret_word:
                if e not in l:
                    l.append(e)
            score =number_guesses*len(l)
            print('Congratulations!, your score is:', score)
    
if __name__ == '__main__':
    secret_word = choose_word(wordlist)
    Hangman(secret_word)

