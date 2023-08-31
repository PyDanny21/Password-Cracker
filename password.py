import os
from random import *

u_pwd=input('Enter Password:')
pwd=['a','b','c','d','e','f','i','j','k','l','m']

pw=''
while(pw!=u_pwd):
    pw=''
    for letter in range(len(u_pwd)):
        guess_pwd=pwd[randint(0,10)]
        pw=str(guess_pwd)+str(pw)
        print(pw)
        print('Cracking Password...Please wait')
        os.system('cls')
        
print('Your password is :', pw)