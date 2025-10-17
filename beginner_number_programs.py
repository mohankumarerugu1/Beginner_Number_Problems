# -----------------------------------------------
# Beginner Number Problems Collection
# Author: Mohan Kumar Erugu
# -----------------------------------------------

# 1️⃣ Sum of first N numbers
def sum_of_first_n():
    n = int(input("Enter a number: "))
    total = sum(range(1, n + 1))
    print(f"Sum of first {n} numbers = {total}")

# 2️⃣ Factorial of a number
def factorial():
    n = int(input("Enter a number: "))
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(f"Factorial of {n} = {fact}")

# 3️⃣ Palindrome number check
def palindrome():
    n = int(input("Enter a number: "))
    original = n
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
    if rev == original:
        print(f"{original} is a Palindrome")
    else:
        print(f"{original} is not a Palindrome")

# 4️⃣ Print all divisors
def divisors():
    n = int(input("Enter a number: "))
    print(f"Divisors of {n} are:", end=" ")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")
    print()

# 5️⃣ Fibonacci sequence up to N terms
def fibonacci():
    n = int(input("Enter number of terms: "))
    a, b = 0, 1
    print("Fibonacci sequence:", end=" ")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

# 6️⃣ GCD of two numbers
def gcd():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    g = 1
    for i in range(1, min(x, y) + 1):
        if x % i == 0 and y % i == 0:
            g = i
    print(f"GCD of {x} and {y} = {g}")

# 7️⃣ LCM of two numbers
def lcm():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    g = 1
    for i in range(1, min(x, y) + 1):
        if x % i == 0 and y % i == 0:
            g = i
    l = (x * y) // g
    print(f"LCM of {x} and {y} = {l}")

# 8️⃣ Armstrong number check
def armstrong():
    n = int(input("Enter a number: "))
    original = n
    total = 0
    while n > 0:
        digit = n % 10
        total += digit ** 3
        n //= 10
    if total == original:
        print(f"{original} is an Armstrong number")
    else:
        print(f"{original} is not an Armstrong number")

# 9️⃣ Perfect number check
def perfect():
    n = int(input("Enter a number: "))
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    if total == n:
        print(f"{n} is a Perfect number")
    else:
        print(f"{n} is not a Perfect number")

# --------------------------------------------------
# Run any program by calling its function below 👇
# Example: sum_of_first_n()
# --------------------------------------------------

# Uncomment one line at a time to test:
# sum_of_first_n()
# factorial()
# palindrome()
# divisors()
# fibonacci()
# gcd()
# lcm()
# armstrong()
# perfect()
