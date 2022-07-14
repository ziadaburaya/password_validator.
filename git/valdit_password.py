from colorama import Fore

lower, upper, special, digit = 0, 0, 0, 0
pword =open("PASSWORD.txt", "r")
password=""
for password1 in pword:
 password+=""+password1
 if (len(password) >= 10):
  for i in password:
    if(i.isupper()):
         upper += 1
    if(i.islower()):
        lower += 1
    if(i.isdigit()):
        digit += 1
    if(i== '@' or i == '$' or i == '_' or i == '#' or i=="/" or i=="*" or i=="-"or i=="+"or i=="%"or i=="^"or i=="&"or i=="!"):
        special += 1

 else: print("Password should be more than 10 characters")

 if ( upper >= 1 and lower>=1 and digit>=1 and special>=1 ):
    print( Fore.GREEN +"Valid Password: 1")

 else:
    print(Fore.RED +"Not a Valid Password: 0 because","\n")
    if (lower==0): print("password must include lower case")
    if (upper==0):  print("password must include upper case")
    if (digit==0):  print("password must include numbers ")
    if(special==0):  print("password must include special case" )
 password=""
 lower, upper, special, digit = 0, 0, 0, 0
