word = input('Please enter a word for your opponent: ')

wrongGuesses = 7
guessed = False
correctLetters = ''
wrongLetters = ''
blanks = ''

for letter in word:
    blanks = blanks+'_ '

print(blanks)
print('You have', wrongGuesses, 'wrong guesses left.')

while guessed is False and wrongGuesses > 0:

    print('Correct Letters Guessed: ', correctLetters)
    print('Wrong Letters Guessed: ', wrongLetters)
    guess = input('What letter would you like to guess?')

    newLetter = True
    for letter in wrongLetters:
        if guess == letter:
            newLetter = False
    for letter in correctLetters:
        if guess == letter:
            newLetter = False

    if newLetter is False:
        print("I'm sorry, you already guessed that letter.")
    else:
        blanks = ''
        validLetter = False

        for letter in word:
            if letter == guess:
                validLetter = True

        if validLetter == True:
            correctLetters = correctLetters + guess
            print('Correct!', 'The letter', guess, 'is in the word.')
        else:
            wrongLetters = wrongLetters + guess
            wrongGuesses = wrongGuesses - 1
            print("I'm sorry,", guess, "is not in the word.")
            print('You have', wrongGuesses, 'wrong guesses left.')

        lettersGuessedCorrect = 0
        for letter in word:
            letterInWord = False
            for ltr in correctLetters:
                if letter == ltr:
                    letterInWord = True
                    lettersGuessedCorrect = lettersGuessedCorrect + 1
            
            if letterInWord is True:
                blanks = blanks + letter + ' '
            else:
                blanks = blanks + '_ '

        print(blanks)

        if len(word) == lettersGuessedCorrect:
            print('You have guessed the word! You had', wrongGuesses, 'wrong guesses left.')
            guessed = True
if wrongGuesses == 0:
    print('Too bad! the word was:', word)
    print("I'm sorry, you lose.")
else:
    print('Congratulations! You win!')

print('Please play again!')