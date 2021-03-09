# This Code Is A Base For A Spammer.

from os import system, name
import pyautogui
import time

def clear(): 
    if name == 'nt': 
        _ = system('cls')

def startCount():
    startCountdown = 5
    while(startCountdown != 0):
        print(startCountdown)
        time.sleep(1)
        startCountdown -= 1
    

def InputValueSpam():
        spam = str(input("Enter A Text To Be Spammed: "))
        spamCount = int(input("Enter The Amount Of Time To Spam: "))
        Count = 0
        print("\n")
        startCount()
        
        while Count < spamCount:
                print("\n")
                pyautogui.typewrite(spam + '\n')
                Count = Count + 1 
            

def InfiniteSpam():
        spam = str(input("Enter A Text To Be Spammed: "))
        startCount()
        print()
        while True:
                pyautogui.typewrite(spam + '\n')                
        

while True:
        clear()
        print("Spammer v0.1:")
        print("1. Custom Spam Value")
        print("2. Infinite")
        print("3. Exit")

        print()

        x = int(input("Which Type Of Spam Do You Prefer: "))
        
        print()

        if x == 1:
                InputValueSpam()
        elif x == 2:
                InfiniteSpam()
        elif x == 3:
                break
        else:
                print("Wrong Value.")



        


