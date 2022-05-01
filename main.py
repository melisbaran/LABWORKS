def func1(n):
 sum = 0
 sumFunc = lambda f: ((n - 3) / (n ** 2))
 for i in range(1, number1+1):
     sum += sumFunc(i)

 return sum

number1 = int(input("Please enter a number : "))
print(func1(number1))



mul=1

def func2(n):
 global mul
 mul*= (n/(n+2))-10
 if n==1:
    return 1
 else:
    return func2(n - 1)

number2 = int(input("Please enter a number : "))
print(func1(number2))