#write a python program to create a lambda 
#function that adds 25 to a given number passed in as an argument.

argument = lambda n:n+25
num = list(map(int,input("enter number:",).split()))
print(list(map(argument,num)))