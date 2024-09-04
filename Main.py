import time
import random
import sys, subprocess
import math
import DeckBuild
import Extras

easy = {
    "bankerS1": "you must have some nice friends, you have 1000 credits. "
}
intermediate = {
    "bankerS1": "heres your company-mandated credits. \n *she tosses a bag to you with 500 credits*"
}
hard = {
    "bankerS1": "you're pathetic, I think i might keep some of these for myself... \n*she takes some coins out of a pouch and hands you the measly 250 credits*"
}
impossible = {

}
trueD = {

}
difficulty = "Error"
o = " "
name = ""
def startUp():
    i = input("|--Press Enter to Continue--|")
    subprocess.run('clear', shell=True)
    print("|-----ULTIMATE GAMBLING-----|")
    print("|===========================|")
    global difficulty
    while difficulty == "Error":
        difficulty = input("Select your difficulty: \n A.) Easy \n B.) Intermediate \n C.) Hard \n D.) Impossible \n Select Difficulty -->")
        if difficulty.upper() == "A":
            difficulty = easy
        elif difficulty.upper() == "B":
            difficulty = intermediate
        elif difficulty.upper() == "C":
            difficulty = hard
        elif difficulty.upper() == "D":
            difficulty = impossible
        else:
            print("Error, please try again")
            difficulty = "Error"
            i = input("|--Press Enter to Continue--|")
            subprocess.run('clear', shell=True)
    subprocess.run('clear', shell=True)
    Extras.scanPrint("Warden: Hello? Hello?")
    time.sleep(1)
    Extras.scanPrint("Warden: Good, you're awake.")
    time.sleep(1)
    Extras.scanPrint("Warden: Hurry up and go get your funds.")
    i = input("|--Press Enter to Continue--|")
    subprocess.run('clear', shell=True)
    while True:
        o = input("Options: \n A.) Follow the Warden \n B.) Search your room \n C.) Break your right wrist \n Select option -->")
        if o.upper() == "A":
            Extras.scanPrint("You leave your rusting cell...")
            break
        if o.upper() == "B":
            Extras.scanPrint("You find nothing but dust...")
        if o.upper() == "C":
            Extras.scanPrint("The pain is harsh but berable for now...")
        i = input("|--Press Enter to Continue--|")
        subprocess.run('clear', shell=True)
    Extras.scanPrint("You look back to see the 6 jail cells, 3 of them empty including yours...")
    i = input("|--Press Enter to Continue--|")
    subprocess.run('clear', shell=True)
    Extras.scanPrint("The banker sits in their barred office, siting lazily as if bored...")
    time.sleep(1)
    Extras.scanPrint("Banker: Name?")
    time.sleep(1)
    global name
    name = input("Whats your name? \n --> ")
    print()
    Extras.scanPrint(f"well \"{name},\" {difficulty["bankerS1"]}")








DeckBuild.makeDeck()
startUp()