
# number = float(input("pick a number"))
# age = int(input("how old are you?"))
# name = input("whats your name?")
# age_in_5_years = age + 5
# doubled_number = number * 2
# print("the number you picked is " + str(number))
# print("hey " + name + " you are " + str(age) + " years old")
# print("In 5 years, you will be " + str(age_in_5_years) + " years old")

# try:
#     number = float(input("pick a number"))
#     if number > 0:
#         print("positive")
#     elif number < 0:
#         print("negative")
#     else:
#         print("zero")
# except ValueError:
#     print("not a number")

# import random

# number = random.randint(1, 10)
# print("random number is " + str(number))

# try :
#     guess = int(input("guess the number"))
#     if guess == number:
#         print("you guessed right")  
#     elif guess > number:
#         print("you guessed too high")
#     else:
#         print("your guess is too low")
# except ValueError:
#     print("not a number")


word = input("pick a word")
length = len(word)
print("the length of the word is " + str(length))



for char in word:
    print(char)

vowels = ["a", "e", "i", "o", "u"]
vowel_count = 0

for char in word:
    if char in vowels:
        print(char)
        vowel_count += 1
