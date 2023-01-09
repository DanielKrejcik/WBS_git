import random   #importing random numbers
# !pip install english-words -- doesnt seem to work anymore. needs some research to find a replacement!
from english_words import english_words_alpha_set  # importing english dictionary via pip
wordlist = list(english_words_alpha_set) #defining list where we can draw a random word from
oword = input("Please prompt a word of your choice or press Enter to draw a random word.") #The word/sentence we are about to find if we chose to do so.
if len(oword) < 1: #if no word is prompted we will take a random word from given list
    rnd = random.randrange(1, len(wordlist)) #creating a random number from intervall 1 to len(wordlist), to make sure every word can be chosen
    oword = wordlist[rnd-1] #rnd-element from wordlist starting @index = 0
diff = int(input("Select your difficulty: 1 for beginners and 2 for expert"))
word = oword.upper()
hidden = ("_ " * (len(word)))[:-1]
llist = list(word)  #putting all letters in a list for easier handling, since i was not able to get the desired printed outputs the while working with strings
if diff == 1:
    if len(word) >= 8:
        rlist = random.sample(range(1, len(word)), 2)
        for r in rlist:
            hint = llist[r-1].upper()
            for char in llist:
                ilist = []
                if char == hint:
                    pos = llist.index(char)
                    llist[pos]= False
                    ilist.append(pos)
                    for index in ilist:
                        hidden = hidden[:index*2]+hint+" "+hidden[(index+1)*2:]
    else:
        rnd = random.randrange(1, len(word))
        hint = llist[rnd-1].upper()
        for char in llist:
            ilist = []
            if char == hint:
                pos = llist.index(char)
                llist[pos]= False
                ilist.append(pos)
                for index in ilist:
                    hidden = hidden[:index*2]+hint+" "+hidden[(index+1)*2:]
else:
    hidden = ("_ " * (len(word)))[:-1] #Creating a string, where all characters of the word are replaced by "_" and separated by" " ending with "_"
count = 6 #After six missed calls our hangman is dead, so we need an initial counter.
print("Welcome to Hangman. You are supposed to find the word from before. In order to do that, you may guess its letters before you try to find a solution. In the next line you find a number of '_' corresponding to the lenght of the wanted word. If you want to leave the game, prompt 'end'.")
print(hidden) #show number of characters with "_" separated with empty spaces
print(f"You have {count} wrong answers left")
while True: 
    oguess = input("Guess a letter! Or try a solution.")
    guess = oguess.upper()
    if len(guess) == 1: #player just guessed a single character
        if guess in llist: #is the guessed letter part of the wanted word (the list of letters)?
            print("Good call!")
            for char in llist: #loop through the list
                indexlist = [] #creating an empty list for later usage
                if char == guess: #if-condition for correct guessed letter
                    pos = llist.index(char) #getting the position of each single character correctly guessed while looping through the list
                    llist[pos]= False #renaming the list entry in order to "get rid of it"
                    indexlist.append(pos) #new list for storing the indices of the found letters
                    for index in indexlist: #looping through that list in order to
                        hidden = hidden[:index*2]+guess+" "+hidden[(index+1)*2:] #modify the "_ _ _ _" with the correct letters at the right position (*2 since i always have empty spaces between the characters in that string)
            print(hidden) # print out the modified "hidden"-string
        else: #taking care of uncorrect player-suggestions
            count = count - 1 #hangman gets one step closer to death each time the player gives a wrong suggestion
            print("This letter is not included. Please try again.")
            print(hidden)
            print(f"You have {count} wrong answers left")
        if hidden.replace(" ", "") == word:#players has guessed all characters correctly, removing the empty spaces from the "hidden"-string and check if it is equal to the wanted word
            print(f"Congratulations! You have won, {word} is the correct answer.")
            break #ending the won game
        elif count == 0: #our hangman died because of too many failed guesses
            print(f"You have lost. The solution is {word}. Better luck next time.")
            break #ending the lost game
    if len(guess) > 1: #player tried to give a solution
        if guess == word: #player gave the correct solution
            print(f"Congratulations! You have won, {word} is the correct answer.")
            break
        elif guess == "end":#if we want to end the game, before our hangman is dead
            break
        else: #player gave wrong solution
            count = count -1 #wrong solution means one step closer to death for the hangman
            print("Try again. This is not the right solution.")
            print(hidden)
            print(f"You have {count} wrong answers left")