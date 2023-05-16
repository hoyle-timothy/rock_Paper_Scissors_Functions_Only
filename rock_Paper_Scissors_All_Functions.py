import random

#rnd increments the number of rounds a player has played
rnd = 0
#hwin initializes the number of times the player has won
hwin = 0
#cwin initializes the number of times the computer has won
cwin = 0

def setup(human,computer,x): #this line is the function definition. It takes 3 arguments; human (number of times the player has won) computer (computer wins) and x (number of rounds played)
    '''sets up the game by greeting the user and asking them whether or not they would like to play. Also lets them choose whether or not to continue playing'''
    if x == 0: #x increments the number of rounds the game has been played, and displays the below message if a round has NOT been played
        choice = input("Hello, would you like to play rock, paper, scissors? 'y' or 'n': ").lower()#this line asks the user if they would like to play and takes player input
        while not choice in ('y','n','N'): #this line is input validation, testing the user input to ensure the user has typed a valid response of either 'y' or 'n'
            choice = input("invalid choice. Please type 'y' or 'n': ").lower() #this displays a message to the user if they entered an invalid input, and asks them to input a valid response
        if choice == 'y': #this line catches the input if the user chooses to play
            mainfunc(human,computer,x) #this line calls the actual game function, called 'mainfunc()'
        elif choice == 'n': #this line catches the input if the user does NOT want to play
            print("Thanks anyway, have a good day.") #this line displays a message for the user if the user has decided NOT to play
    elif x > 0: #x is the variable holding the round incrementer. If one round has already been played, then this elif statement will run
        choice = input("Would you like to play again? 'y' or 'n': ") #this line asks the user if they would like to play again
        while not choice in ('y','Y','n','N'): #this line is input validation, testing the user input to ensure the user has typed a valid response of either 'y' or 'n'
            choice = input("invalid choice. Please type 'y' or 'n': ") #this displays a message to the user if they entered an invalid input, and asks them to input a valid response
        if choice == 'y' or choice == 'Y': #this line catches the input if the user chooses to play again
            print("Awesome. Let's play again") #this line displays a message to the player, letting them know that they are about to play again
            mainfunc(human,computer,x) #this line calls the actual game function, called 'mainfunc()'
        elif choice == 'n' or choice == 'N': #this line catches the input if the user does NOT want to play again
            print("Thanks anyway, have a good day.") #this line displays a message for the user if the user has decided NOT to play again


def mainfunc(hscore,cscore,x): #this line is the function definition. It takes 3 arguments; hscore (number of times the player has won) cscore (computer wins) and x (number of rounds played)
    '''main function of the game. It takes the player's selection, the computer's selection, and calls the appropriate function based on player and computer's selection'''
    hchoice = input("Please choose and type rock, paper or scissors: ") #this line asks the player to select rock, paper or scissors
    while not hchoice in ('rock','paper','scissors'): #this line is input validation, ensuring the user has input a valid selection
        hchoice = input("invalid choice. Please type rock, paper or scissors: ") #if the player types an invalid input, this line runs and asks them to input a valid selection
    
    cchoice = random.choice(['rock','paper','scissors']) #this line tells the computer to randomely select rock, paper or scissors
    
    if hchoice == cchoice: #this line handles an outcome where the player and the computer select the same option
        draw(hscore,cscore,hchoice,cchoice,x) #this line calls the 'draw' function, which handles situations where the game has ended in a 'draw'
    
    elif hchoice == 'rock' and cchoice == 'paper': #this line handles an outcome where the player chose 'rock' and the computer selected 'paper'
        computerwin(hscore,cscore,hchoice,cchoice,x) #calls the function 'computerwin' and passes the current player score, computer score, their respective choices, and the number of rounds played
    
    elif hchoice == 'rock' and cchoice == 'scissors': #this line handles an outcome where the player chose 'rock' and the computer selected 'scissors'
        humanwin(hscore,cscore,hchoice,cchoice,x) #calls the function 'humanwin' and passes the current player score, computer score, their respective choices, and the number of rounds played
    
    elif hchoice == 'paper' and cchoice == 'rock': #this line handles an outcome where the player chose 'paper' and the computer selected 'rock'
        humanwin(hscore,cscore,hchoice,cchoice,x) #calls the function 'humanwin' and passes the current player score, computer score, their respective choices, and the number of rounds played
    
    elif hchoice == 'paper' and cchoice == 'scissors': #this line handles an outcome where the player chose 'paper' and the computer selected 'scissors'
        computerwin(hscore,cscore,hchoice,cchoice,x) #calls the function 'computerwin' and passes the current player score, computer score, their respective choices, and the number of rounds played
    
    elif hchoice == 'scissors' and cchoice == 'paper': #this line handles an outcome where the player chose 'scissors' and the computer selected 'paper'
        humanwin(hscore,cscore,hchoice,cchoice,x) #calls the function 'humanwin' and passes the current player score, computer score, their respective choices, and the number of rounds played
    
    elif hchoice == 'scissors' and cchoice == 'rock': #this line handles an outcome where the player chose 'scissors' and the computer selected 'rock'
        computerwin(hscore,cscore,hchoice,cchoice,x) #calls the function 'computerwin' and passes the current player score, computer score, their respective choices, and the number of rounds played
  
#draw() function outlines how to handle a situation where both the computer and the player select the same object  
def draw(human,computer,hchoice,cchoice,x):
    print(f"It's a draw! You chose \"{hchoice}\" and the computer chose \"{cchoice}\"")
    x += 1
    print(f'Player wins: {human}')
    print(f'Computer wins: {computer}\n')
    setup(human,computer,x)
   
#humanwin() function outlines how to handle a situation where the player wins the round  
def humanwin(human,computer,hchoice,cchoice,x):
    print(f"You win! The computer chose \"{cchoice}\" and you chose \"{hchoice}\"")
    human += 1
    x += 1
    print(f'Player wins: {human}')
    print(f'Computer wins: {computer}\n')
    setup(human,computer,x)
    
#computerwin() function outlines how to handle a situation where the computer wins the round  
def computerwin(human,computer,hchoice,cchoice,x):
    print(f"You lose. The computer chose \"{cchoice}\" and you chose \"{hchoice}\"")
    computer += 1
    x += 1
    print(f'Player wins: {human}')
    print(f'Computer wins: {computer}\n')
    setup(human,computer,x)

setup(hwin,cwin,rnd) #this line calls the initial function, 'setup', to start the game. It passes the number of player wins, computer wins, and rounds played

            