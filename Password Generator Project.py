
import random
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_chr = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
from logo import logo
print(logo)
letters= int(input("How many letters would you like in your password?\n")) 
symbols = int(input(f"How many symbols would you like in your password?\n"))
numbers = int(input(f"How many numbers would you like in your password?\n"))

passlist=[]
for i in range(1,letters + 1):
    passlist+=random.choice(alphabets)
for i in range(1,symbols + 1):
    passlist+=random.choice(special_chr)
for i in range(1,numbers + 1):
    passlist+=random.choice(digits)
random.shuffle(passlist)
password=""
for i in passlist:
    password += i
print(f'Your Password is :{password}')