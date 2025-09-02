from random import randint
import time
import pyttsx3
import speech_recognition as sr

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate',150)
    engine.say(text)
    engine.runAndWait()

print("Welcome to the perfect guess game")
speak("Welcome to the perfect guess game")
computer=randint(0,100)
player=-1
guesses=0
speak("How do you want to play the game. Type 'a' if you want a bot to play for you. Type 'b' if yu want to play on your own")
n=input("How do you want to play the game. Type 'a' if you want a bot to play for you.Type 'b' if yu want to play on your own: ")

if(n=='a'):
    print("You have chosen a bot to play for you")
    speak("You have chosen a bot to play for you")

    print("The bot will guess a number between 0 to 100")
    speak("The bot will guess a number between 0 to 100")
    while(player!=computer):
        guesses+=1
        player=randint(0,100)
        time.sleep(0.7)

        if(player>computer):
            print(f"You have chosen {player}. Wrong guess, choose lower number please")

        elif(player<computer):
            print(f"You have chosen {player}. Wrong guess, choose higher number please")
    
        elif(player==computer):
            print(f"Correct guess.The correct number is {computer}")

        elif(player<0):
            print("Invalid number. Please choose an number between 0 to 100")

    if(guesses==1):
        print(f"You have guessed the number in {guesses} attempt")
        speak(f"You have guessed the number in {guesses} attempt")
    else:
        print(f"You have guessed the number in {guesses} attempts")
        speak(f"You have guessed the number in {guesses} attempts")

if(n=='b'):
    print("You have chosen to play by yourself")
    while(player!=computer):
        guesses+=1
        player=int(input("Enter the number you have chosen: "))

        if(player>computer):
           print(f"You have chosen {player}. Wrong guess, choose lower number please")

        elif(player<computer):
            print(f"You have chosen {player}. Wrong guess, choose higher number please")
    
        elif(player==computer):
            print(f"Correct guess.The correct number is {computer}")

        elif(player<0):
            print("Invalid number. Please choose an number between 0 to 100")

    if(guesses==1):
        print(f"You have guessed the number in {guesses} attempt")
        speak(f"You have guessed the number in {guesses} attempt")
    else:
        print(f"You have guessed the number in {guesses} attempts") 
        speak(f"You have guessed the number in {guesses} attempts")

speak("Thank you for playing the game")
print("Thank you for playing the game")

speak("Do you want to play again? Type 'yes' or 'no'")
n2=input("Do you want to play again? Type 'yes or 'no: ")

if(n2.lower()=="yes"):
    print("Let us play again")
    speak("Let us play again")