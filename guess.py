# -*- coding: utf-8 -*-

from random import randint
print "Guessing game starts."
print "You have five chances."
num=randint(1,10)
i=1
while True:
    guess=input("Please guess the number [1,10]: ")
    if i<5:
        if guess!=num:
            print "Please guess the number again."
            i+=1
        else:
            print "That's right. Well done!"
            break
    else:
        if guess!=num:
            print "Sorry, you have reached the maximal chance."
            print "The number is {}.".format(num)
        else:
            print "That's right. Well done!"
        break
    
