n = int(input())
def fizz_buzz(n):
    for i in range(1, n + 1):  # Проходим по числам от 1 до n
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz")   # Делится на 3 и 5 
        elif i % 5 == 0:
            print("Buzz")      # Делится только на 5
        elif i % 3 == 0:
            print("Fizz")     # Делится только на 3
        else:
            print(i)           # Печатаем само число

print(fizz_buzz(n))