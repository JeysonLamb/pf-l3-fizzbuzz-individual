for valor in range(1, 1001):
    if valor % 3 == 0 and i % 5 == 0:
        print("Fizzbuzz") 
    elif valor % 3 == 0:
        print("Fizz")
    elif valor % 5 == 0:
        print("Buzz")
    else:
        print(valor)