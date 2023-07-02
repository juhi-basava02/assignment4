#write a python program to triple all numbers of a given list of integers.use python map.

def triple(n):
    n = n+n+n
    return n

integers = list(map(int,input("integer:",).split()))
val = map(triple,integers)
print(list(val))
