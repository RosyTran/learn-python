x = int(input("Input your number:"))
def fact(x):
    if x ==0:
        return 1
    elif x >=1:
        return x * fact(x-1)
print (fact(x))