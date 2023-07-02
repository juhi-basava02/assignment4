#write a python program to square the elements of a list using map() function.

def square(n):
    n = n**2
    return n

integers = list(map(int,input("integer:",).split()))
val = map(square,integers)
print(list(val))
