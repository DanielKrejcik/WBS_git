import random   #importing random numbers
print("Welcome to Hangman. This is a game where you are supposed to find out a given word by guessing its letters. You win if you guess all letters or provide the solution with less than six mistakes.")
diff = input("Please select your difficulty: Prompt '1' for easy, '2' for difficult and '3' for 2-players-mode")
#!pip install english-words
#from english_words import english_words_alpha_set  # importing english dictionary via pip
#wordlist = list(english_words_alpha_set) #defining list where we can draw a random word from
oword = str(0)
if diff == 3:
    oword = input("Player 1: Please prompt a word of your choice and make sure Player 2 is not looking on your screen or keyboard.") #The word/sentence Player 2 is about to find if we chose 2-Player-Mode.
    if oword.isalpha() is not True:
        oword = input("Please make sure to use only latin letters in your word. Prompt a new word")
#else: #in single player will take a random word from given list
 #   rnd = random.randrange(1, len(wordlist)) #creating a random number from intervall 1 to len(wordlist), to make sure every word can be chosen
  #  oword = wordlist[rnd-1] #rnd-element from wordlist starting @index = 0
word = oword.upper()
hidden = ("_ " * (len(word)))[:-1] #Creating a string, where all characters of the word are replaced by "_" and separated by" " ending with "_"
count = 6 #After six missed calls our hangman is dead, so we need an initial counter.
gamescount = 0
if diff == 3:
    if gamecount % 2 != 0:
        print("Get ready Player 2!")
    else:
        print("Get ready Player 1!")
print("In the next line you find a number of '_' corresponding to the lenght of the wanted word. Whenever you want to leave the game, prompt 'end'.")
print(hidden) #show number of characters with "_" separated with empty spaces
listedletters = list(word) #putting all letters in a list for easier handling, since i was not able to get the desired printed outputs the while working with strings
print(f"You have {count} wrong answers left")
while True: 
    oguess = input("Guess a letter! Or try a solution.")
    if oguess.isalpha() is True:
        guess = oguess.upper()
        if len(guess) == 1: #player just guessed a single character
            if guess in listedletters: #is the guessed letter part of the wanted word (the list of letters)?
                print("Good call!")
                for char in listedletters: #loop through the list
                    indexlist = [] #creating an empty list for later usage
                    if char == guess: #if-condition for correct guessed letter
                        pos = listedletters.index(char) #getting the position of each single character correctly guessed while looping through the list
                        listedletters[pos]= False #renaming the list entry in order to "get rid of it"
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
                gamescount = gamescount + 1
                break #ending the won game
            elif count == 0: #our hangman died because of too many failed guesses
                print(f"You have lost. The solution is {word}. Better luck next time.")
                gamescount = gamescount + 1
                break #ending the lost game
        if len(guess) > 1: #player tried to give a solution
            if guess == word: #player gave the correct solution
                print(f"Congratulations! You have won, {word} is the correct answer.")
                gamescount = gamescount + 1
                break
            elif guess == "end":#if we want to end the game, before our hangman is dead
                break
            else: #player gave wrong solution
                count = count -1 #wrong solution means one step closer to death for the hangman
                print("Try again. This is not the right solution.")
                print(hidden)
                print(f"You have {count} wrong answers left")
    else:
        print("Please prompt a letter from the latin alphabet.")        