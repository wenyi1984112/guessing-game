# -*- coding: utf-8 -*-

from random import randint
print "Guessing game starts."
num=randint(1,10)
while True:
    guess=input("Please guess the number [1,10]: ")
    if guess!=num:
        print "Please guess the number again."
    else:
        print "That's right. Well done!"
        break
