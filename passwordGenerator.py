
#This is password generator program

import random

def Password(passs,length):
    Password = ''.join(random.sample(passs,length))
    print(Password)

customeWordList = input("do want customarized symbols in you password:(write YES or NO :")
if customeWordList == 'yes':
    c_sampleWordList = input("Enter the characters that you need in your password:")
    passwordLength = int(input("What is the lenght of the passsword that you need :"))
    Password(c_sampleWordList,passwordLength)
else:
    sampleWordList = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    passwordLength = int(input("What is the lenght of the passsword that you need :"))
    Password(sampleWordList, passwordLength)


