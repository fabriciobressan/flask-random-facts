#!/usr/bin/env python3
import random
HANGMAN_PICS = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   0   |
       |
       |
      ===''', '''
   +---+
   0   |
   |   |
       |
      ===''', '''
   +---+
   0   |
  /|   |
       |
      ===''', '''
   +---+
   0   |
  /|\  |
       |
      ===''', '''
   +---+
   0   |
  /|\  |
  /    |
      ===''', '''
   +---+
   0   |
  /|\  |
  / \  |
  / \  |
      ===''']

words = 'alvorada amanha amor amplo anseio aqui areia arte assobio atemporal atitude atraves azul bela bem brisa calma calor caminho cancao ceu chuva cidade clara corda dente doce epoca escuro espaco estrela estudar familia felicidade flor forca gesto harmonia historia ideia ilha jardim jovem lagoa leveza livre longe luz mar memoria momento monte mundo musica nascer natureza nuvem onda outono paz poesia porquê praia presente primavera rio rosa ser silencio sol sombra terra tempo trilha verdade vento vida visao viver voz voo'.split()

def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()
    
    print('Letras erradas: ', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()
        
    blanks = '_' * len(secretWord)
          
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=' ')
    print()
          
def getGuess(alreadyGuessed):
    while True:
        print('Escolha uma letra.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Por favor digite apenas uma letra.')
        elif guess in alreadyGuessed:
            print('Você já adivinhou esta letra. Escolha outra.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Por favor digite uma LETRA.')
        else:
            return guess
        
def playAgain():
    print('Você quer jogar novamente? (sim ou não)')
    return input().lower().startswith('s')

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)
    
    guess = getGuess(missedLetters + correctLetters)
    
    if guess in secretWord:
        correctLetters = correctLetters + guess
        
        foundAllLetters = True 
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Aew! A palavra secreta é "' + secretWord + '"! Você acertou!')
            gameIsDone = True 
    else:
        missedLetters = missedLetters + guess
        
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print(' Acabaram-se suas chances!\nDepois de ' + str(len(missedLetters)) + ' palpites errados e ' + str(len(correctLetters)) + ' palpites corretos, a palavra era "' + secretWord + '"')
            gameIsDone = True 
            
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
