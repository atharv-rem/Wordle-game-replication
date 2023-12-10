# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 09:44:23 2022

@author: Atharv Remeshan😎
Cs Project
"""
#linking dictionary with python code
import requests
word_site = "https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt"
response = requests.get(word_site)
word = response.content.splitlines()

#importing modules
import random
import time

#asking the question
f='wanna play wordle?'
for i in f:
    print(i,end='',flush=True)
    time.sleep(0.05)
r=input('\n')

#output printed if the condition is true
if r=='yes' or r=='Yes' or r=='YES':
    print('\033[1;35m'+'Rules:'+'\033[0m')
    print('\033[1;37m'+'* Only 5 letter words have to be entered\n* If the letter is'+'\033[0m',end=' ')
    print('\033[1;32m'+'GREEN'+'\033[0m',end='')
    print('\033[1;37m'+', then the word has the letter in that position\n* If the letter is'+'\033[0m',end=' ')
    print('\033[1;33m'+'YELLOW'+'\033[0m',end='')
    print('\033[1;37m'+', then the word has the letter but not in the same position\n* If the letter is'+'\033[0m',end=' ')
    print('\033[1;30m'+'BLACK'+'\033[0m',end='')
    print('\033[1;37m'+', then the word does not have that letter'+'\033[0m')
    
    #declaring variables
    a=str(random.choice(word))[2:7] #choosing a random word from the dictionary
    d='' #letters to be displayed in green
    x='' #letters to be displayed in yellow
    f='' #letters to be displayed in black
    e=0 #used to show the attempt number while playing
    w=0 #total words
    y=0 #accurate letters
    g=0 #inaccurate letters

    #LOOP - 1
    #accepting the word
    for i in range(5):
        e=e+1
        print('\033[1;37m',end='')
        print('\n#',e,sep='',end='')
        time.sleep(1)
        t=input(' Enter word - ')
        
        #IF CONDITIONS
        #condition to check the length of string
        if len(t)==5:
            pass
            w=w+1
            
        #output shown when the user enters quit    
        elif t=='quit' or t=='Quit' or t=='QUIT':
            print('\033[1;31m'+'Sorry to see you go!😐'+'\033[0m')
            time.sleep(1)
            print('\033[1;34m',end='')
            h='Hey! dont leave yet'
            for i in h:
                print(i,end='',flush=True)
                time.sleep(0.05)
            print('\033[1;37m'+'\nThe correct word was',end=' ')
            print('\033[1;32m'+a.upper()+'\033[0m')
            time.sleep(1)
            print('\033[1;37m',end='')
            n='Hope to see you again!'
            for i in n:
                print(i,end='',flush=True)
                time.sleep(0.05)
            break
        
        #condition to check the length of string
        elif len(t)>5 or len(t)<5:
            print('\033[1;31m'+'Sorry, the word u have entered is either above or below the 5 letter limit.Please try again!'+'\033[0m')
            continue
        
        #output displayed when the user enters the correct word
        if a==t:
            print('\033[1;32m'+a+'\033[0m')
            q='YAAY, YOU HAVE WON!'
            for i in q:
                print(i,end='',flush=True)
                time.sleep(0.05)
            time.sleep(0.2)
            v='\nThanks for playing!'
            for i in v:
                print(i,end='',flush=True)
                time.sleep(0.05)
            time.sleep(0.2)
            y=y+5
            input('\033[1;31m' +"\nPress the ENTER key to get STATS"+'\033[0m')
            k='\nSTATS!'
            for i in k:
                print('\033[1;35m'+i+'\033[0m',end='',flush=True)
                time.sleep(0.05)
            time.sleep(0.2)
            print('\033[1;35m'+'\nNumber of words entered =',w)
            time.sleep(0.2)
            print('\033[1;35m'+'Letter accuracy% =',(y/(w*5))*100)
            time.sleep(0.2)
            print('\033[1;35m'+'Letter inaccuracy% =',(g/(w*5))*100)
            time.sleep(0.2)
            print('Thanks for playing!')
            time.sleep(0.2)
            input('\033[1;31m'+"\nPress the ENTER key to EXIT"+'\033[0m')
            break
        
        #LOOP - 2
        #code for the colours diplayed for each letter
        for j in range(len(a)):
            
            #IF CONDITIONS
            if a[j]==t[j]:
                d=t[j]
                print('\033[1;32m'+d+'\033[0m',end='')
                time.sleep(0.2)
                y=y+1
            elif t[j] in a :
                x=t[j]            
                time.sleep(0.2)
                print('\033[1;33m'+x+'\033[0m',end='')
                y=y+1
            elif a[j]!=t[j]:
                f=t[j]
                print('\033[1;30m'+f+'\033[0m',end='')
                time.sleep(0.2)
                g=g+1
        
        #motivational lines diplayed in attempt 3 and 4        
        if e==3:
            print('\033[1;34m'+'\nAlmost there, DONT STOP TRYING!'+'\033[0m',end='')
        if e==4:
            print('\033[1;34m'+'\nONLY ONE CHANCE LEFT, BEWARE!'+'\033[0m',end='')
        print()
        
    #if quit is entered it will not go into the elif condition followed after this code    
    if t=='quit' or t=='Quit' or t=='QUIT':
        pass
    
    #output shown when the letter entered is not correct
    elif a!=t:
        print('\nThe correct word is',end=' ')
        print('\033[1;32m'+a.upper()+'\033[0m')
        z='\nBETTER LUCK NEXT TIME!'
        for i in z:
           print('\033[1;34m'+i+'\033[0m',end='',flush=True)
           time.sleep(0.05)
        time.sleep(0.2)
        input('\033[1;31m'+"\nPress the ENTER key to get STATS"+'\033[0m')
        l='\nSTATS!'
        for i in l:
            print('\033[1;35m'+i+'\033[0m',end='',flush=True)
            time.sleep(0.05)
        time.sleep(0.2)
        print('\033[1;35m'+'\nNumber of words entered =',w)
        print('\033[1;35m'+'Letter accuracy% =',(y/(w*5))*100,end='')
        print('\033[1;35m'+'%')
        time.sleep(0.2)
        print('\033[1;35m'+'Letter inaccuracy% =',(g/(w*5))*100,end='')
        print('\033[1;35m'+'%')
        time.sleep(0.2)
        print('Thanks for playing!')
        time.sleep(0.2)
        input('\033[1;31m'+"\nPress the ENTER key to EXIT"+'\033[0m')

#output displayed when the user does not want to play the game
else:
    print('😑😑')
