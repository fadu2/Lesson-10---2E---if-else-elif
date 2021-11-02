# Today's Lesson on if, elif, else
# Warm-up: Some other good string methods to know
# count - counts the number of characters or substrings in a string
s1 = "hello"
print(s1.count('l'))  # 2
print(s1.count("ll"))  # 1
s2 = "Mississipi"
print(s2.count("i")) # 4
print(s2.count("s"))  # 4
print(s2.count("iss")) # 2

# rfind - finds the index position of the character or substring from
# the right of a string
print(s2.rfind("i"))  # 9
print(s2.find("i")) # 1

# len() - Gives the number of characters in a string i.e length
print(len(s2))  # 10
print(len(s1))  # 5

# Today's lesson - if, elif, else
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# if a > b:
#     print("a is greater than b.")
# else:
#     print("a is not greater than b.")

# c = int(input("Enter first number: "))
# d = int(input("Enter second number: "))
# if c > d:
#     print("c is greater than d.")
# elif c == d:
#     print("c is equal to d.")
# else:
#     print("c is not greater than d.")

#Score and Grading system
# score = int(input("Enter the score: "))
# if score > 95:
#     print("Grade: A+")
# elif score > 90:
#     print("Grade: A")
# elif score > 80:
#     print("Grade: B")
# elif score > 70:
#     print("Grade: C")
# elif score > 65:
#     print("Grade: D")
# else:
#     print("Grade: F")

# Check temperature
# temp = int(input("Enter the temperature: "))
# if temp >= 90:
#     print("It is hot!!")
# elif temp >= 50:
#     print("It is fine")
# else:
#     print("It is cold!!!!")

# Find if a person is a teenager
# age = int(input("Enter person's age: "))
# if age >= 13 and age <= 19:
#     print("The person is a teenager")
# else:
#     print("The person is NOT a teenager")

# Check if a number is odd or even
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("even")
else:
    print("odd")