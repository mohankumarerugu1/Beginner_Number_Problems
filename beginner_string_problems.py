# -----------------------------------------------
# Beginner String Problems Collection
# Author: Mohan Kumar Erugu
# -----------------------------------------------

# 1️⃣ Count the number of characters in a string
def count_characters():
    s = input("Enter a string: ")
    print(f"Length = {len(s)}")

# 2️⃣ Convert string to uppercase
def to_uppercase():
    s = input("Enter a string: ")
    print(s.upper())

# 3️⃣ Convert string to lowercase
def to_lowercase():
    s = input("Enter a string: ")
    print(s.lower())

# 4️⃣ Reverse a string
def reverse_string():
    s = input("Enter a string: ")
    print(s[::-1])

# 5️⃣ Check if string is empty
def check_empty():
    s = input("Enter a string: ")
    if len(s) == 0:
        print("Empty")
    else:
        print("Not Empty")

# 6️⃣ Print each character on a new line
def print_each_char():
    s = input("Enter a string: ")
    for ch in s:
        print(ch)

# 7️⃣ Count vowels and consonants
def count_vowels_consonants():
    s = input("Enter a string: ").lower()
    vowels = "aeiou"
    v = c = 0
    for ch in s:
        if ch.isalpha():
            if ch in vowels:
                v += 1
            else:
                c += 1
    print(f"Vowels: {v}, Consonants: {c}")

# 8️⃣ Check palindrome string
def check_palindrome():
    s = input("Enter a string: ")
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

# 9️⃣ Remove spaces from a string
def remove_spaces():
    s = input("Enter a string: ")
    print(s.replace(" ", ""))

# 🔟 Replace vowels with '*'
def replace_vowels():
    s = input("Enter a string: ")
    res = ""
    for ch in s:
        if ch.lower() in "aeiou":
            res += "*"
        else:
            res += ch
    print(res)

# 11️⃣ Count words in a sentence
def count_words():
    s = input("Enter a sentence: ")
    words = s.split()
    print(f"Total words = {len(words)}")

# 12️⃣ Find the longest word
def longest_word():
    s = input("Enter a sentence: ")
    words = s.split()
    longest = max(words, key=len)
    print(f"Longest word: {longest}")

# 13️⃣ Count frequency of each character
def char_frequency():
    s = input("Enter a string: ")
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for k, v in freq.items():
        print(f"{k}: {v}")

# 14️⃣ First non-repeated character
def first_non_repeated():
    s = input("Enter a string: ")
    for ch in s:
        if s.count(ch) == 1:
            print(f"First non-repeated character: {ch}")
            return
    print("No unique character found")

# 15️⃣ Check anagrams
def check_anagram():
    s1 = input("Enter first string: ")
    s2 = input("Enter second string: ")
    if sorted(s1) == sorted(s2):
        print("Anagram")
    else:
        print("Not Anagram")

# 16️⃣ Remove duplicates
def remove_duplicates():
    s = input("Enter a string: ")
    result = ""
    for ch in s:
        if ch not in result:
            result += ch
    print(result)

# 17️⃣ Check if string contains only digits
def only_digits():
    s = input("Enter a string: ")
    print(s.isdigit())

# 18️⃣ Swap case of each character
def swap_case():
    s = input("Enter a string: ")
    print(s.swapcase())

# 19️⃣ Count uppercase, lowercase, digits, special chars
def count_types():
    s = input("Enter a string: ")
    upper = lower = digits = special = 0
    for ch in s:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
        elif ch.isdigit():
            digits += 1
        else:
            special += 1
    print(f"Uppercase: {upper}\nLowercase: {lower}\nDigits: {digits}\nSpecial: {special}")

# --------------------------------------------------
# Run any program by calling its function below 👇
# Example: count_characters()
# --------------------------------------------------

# Uncomment one line at a time to test:
# count_characters()
# to_uppercase()
# to_lowercase()
# reverse_string()
# check_empty()
# print_each_char()
# count_vowels_consonants()
# check_palindrome()
# remove_spaces()
# replace_vowels()
# count_words()
# longest_word()
# char_frequency()
# first_non_repeated()
# check_anagram()
# remove_duplicates()
# only_digits()
# swap_case()
# count_types()
