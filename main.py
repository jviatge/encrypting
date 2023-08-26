import os
import string

def genAlphabet():
    return string.ascii_lowercase + " #.!"

def casearCrypt(message, key, param):

    listChar = genAlphabet()
    messageEcrypt = ""
    binary = bin(key)[2:]

    if key % len(listChar) == 0:
        return "erreur : clé inutile"

    i = 1
    if param == 0:
        x = 0
    else:
        x = 1
 
    for word in message:
        
        i = i + 1

        if binary[i % len(binary)] == x:
            index = listChar.find(word) + key
        else:
            index = listChar.find(word) - key    
        
        messageEcrypt += listChar[index % len(listChar)]
    
    return messageEcrypt

def clear(): return os.system('clear')

choice = ""

while choice != 0:

    clear()

    print("-------------------------------------")
    print("------- Welcome SataCrypteur --------")
    print("-------------------------------------")
    print("")

    print("(1) New message | (2) Decrypt message | (h) help")
    print("(0) Quit ----------------------------")
    print("")

    choice = int(input("choice: "))

    if choice == 1:

        clear()
        print("----------- New message -------------")
        print("")
        message = str(input("Your message: "))
        print("")
        key = int(input("Your key (only number): "))

        clear()
        print("----------- Your message -------------")
        print(" ")
        print(casearCrypt(message, key, 1))
        print(" ")
        print("With the key:", key)
        print(" ")
        print("-------------------------------------")
        input("Press a key for continue... ")
        
    if choice == 2:

        clear()
        print("--------- Decrypt message -----------")
        print("")
        message = str(input("Your message: "))
        print("")
        key = int(input("Your key (only number): "))

        clear()
        print("----------- Your message -------------")
        print(" ")
        print(casearCrypt(message, -key, 0))
        print(" ")
        print("-------------------------------------")
        input("Press a key for continue... ")

    if choice == "h"

        clear()
        print("--------- Help section -----------")
        

    clear()

    





