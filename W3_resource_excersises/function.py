"""1.Write a Python program to reverse a string. 
Sample String : "1234abcd"
Expected Output : "dcba4321"""""

# str_input = "Gayathri Adimulam"
# str_input = str_input[::-1]
# print(str_input)
#
# Input_str = "1234abcd"
# reversed_str = "".join(reversed(Input_str))
# print(reversed_str)
#
#
# str_input = "1234abcd"
#
# a = str()
# for i in reversed(str_input):
#    a += i
# print(f"Reverse of {str_input} is {a}")

"""def reverse_str(str_input):
    str_value = str()
    index = len(str_input)-1
    while index>=0:
        a = str_input[index]
        str_value += a
        index -= 1
    return str_value

reverse = reverse_str("dcba4321")
print(reverse)"""

"""Using __reversed__ magic method to reverse iterator values"""
# class Gfg:
#     vowels = ['a', 'e', 'i', 'o', 'u']
#
#     def __reversed__(self):
#         return reversed(self.vowels)
#
#
# obj = Gfg()
# print((tuple(reversed(obj))))

"""1. Write a Python function to find the Max of three numbers."""

# def max_of_3numbs(a, b, c):
#     max_num = max(a, b, c)
#     return max_num
#
#
# x = int(input("Enter Number1 : "))
# y = int(input("Enter Number2 : "))
# z = int(input("Enter Number3 : "))
#
# result = max_of_3numbs(x, y, z)
# print(f"Maximum of three numbers : {result}")

"""Alternate method to get max of three numbers"""

# def max_of_two_num(a,b):
#     if a>b:
#         return a
#     else:
#         return b
#
# x = int(input("Enter Number1 : "))
# y = int(input("Enter Number2 : "))
# z = int(input("Enter Number3 : "))
#
# result = max_of_two_num(max_of_two_num(x,y),z)
# print(f"The maximum of {x},{y} and {z} is {result}")

"""2. Write a Python function to sum all the numbers in a list. Go to the editor
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20"""

# def sum(value):
#     sum_of_list = 0
#     for i in value:
#         sum_of_list += i
#     return sum_of_list
#
#
# result = sum((8, 2, 3, 0, 7))
# print(f"Sum of list_values is {result}")

"""Alternate method to get sum of numbers"""
# def summation(value):
#     sum_of_num = sum(value)
#     return sum_of_num
#
#
# result = summation((8, 2, 3, 0, 7))
# print(f"Sum of list_values is {result}")

"""3. Write a Python function to multiply all the numbers in a list. Go to the editor
Sample List : (8, 2, 3, -1, 7)
Expected Output : -336"""

# def multiples(list_value):
#     multi = 1
#     for value in list_value:
#         multi *= value
#     return multi
#
# multiples_of_list = multiples([8, 2, 3, -1, 7])
# print(f"Multiples of list : {multiples_of_list}")

"""5. Write a Python function to calculate the factorial of a number (a non-negative integer). 
The function accepts the number as an argument."""

# def factorial_of_num(value):
#     factorial = 1
#     while value > 0:
#         factorial *= value
#         value -= 1
#     return factorial
#
#
# num = int(input("Enter Number to find factorial :"))
# print(f"Factorial of {num} is {factorial_of_num(num)}")

"""Using for-loop"""
# def factor(val):
#     fact = 1
#     if val > 0:
#         for i in range(1,val+1):
#             fact *= i
#     return fact


# number = int(input('Enter a number to get factorial :'))
# print(f"factorial of {number} : {factor(number)}")

"""6.Write a Python function to check whether a number falls in a given range."""

# def num_in_range(value):
#     if value in range(1,100001):
#         return f"{value} is in range"
#     else:
#         return f"{value} is not in range"
#
#
# numb= int(input("Enter number to check if it is range or not :"))
# res = num_in_range(numb)
# print(res)

"""7. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. 
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12"""

# def str_count(val):
#     if type(val) == type(str()):  # accepts a string
#         uppercase_letters = 0
#         lowercase_letters = 0
#
#         for i in val:
#             if i.isupper():
#                 uppercase_letters += 1
#             elif i.islower():
#                 lowercase_letters += 1
#             else:
#                 pass
#
#         print(f"Uppercase letters : {uppercase_letters} & Lowercase letters : {lowercase_letters} ")
#
#
# user_input = input("Enter something :")
# str_count(user_input)

"""8. Write a Python function that takes a list and returns a new list with unique elements of the first list.
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]"""

# def unique_list(value):
#     unique = []
#
#     for i in value:
#         if i not in unique:
#             unique.append(i)
#
#     return unique


# list_val = [1, 2, 3, 3, 3, 3, 4, 5]
# print(unique_list(list_val))

"""Alternate method"""
# def sample_list(list):
#     return set(list)
#
#
# print(list(sample_list([1, 2, 3, 3, 3, 3, 4, 5])))

"""9. Write a Python function that takes a number as a parameter and check the number is prime or not.
Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself."""

# def prime(num):
#     count = 0
#     if num == 2:
#         print(f"{num} is even prime number")
#     else:
#         for i in range(1, num + 1):
#             if num % i == 0:
#                 count += 1
#         if count == 2:
#             print(f"The Number {num} is prime Number")
#         else:
#             print(f"{num} is not Prime number")
#
#
# user_input = int(input("Enter a number to check if its prime or not : "))
# prime(user_input)

"""10. Write a Python program to print the even numbers from a given list. Go to the editor
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]"""

# def even_list(list_values):
#     even_num = list()
#     for num in list_values:
#         if num % 2 == 0:
#             even_num.append(num)
#     return even_num
#
#
# list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(f"Even list : {even_list(list_num)}")

"""11. Write a Python function to check whether a number is perfect or not.
According to Wikipedia : In number theory, a perfect number is a positive integer that is equal to the
sum of its proper positive divisors, that is, the sum of its positive divisors excluding the number itself (also known as its aliquot sum). 
Equivalently, a perfect number is a number that is half the sum of all of its positive divisors (including itself).
Example : The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6. 
Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. 
The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128."""

# def perfect_num(n):
#     empty_list = []
#     for i in range(1, n):
#         if n % i == 0:
#             empty_list.append(i)
#     if sum(empty_list) == n:
#         print(f"Number:{n} is a perfect number")
#     else:
#         print(f"Number:{n} is not a perfect number")
#
#
# num = int(input("Enter a number to check if its perfect or not :  "))
# perfect_num(num)

"""12. Write a Python function that checks whether a passed string is palindrome or not.
Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run."""

# def palindrome_check(str_value):
#     string = str()
#     index = len(str_value) - 1
#     while index >= 0:
#         string += str_value[index]
#         index -= 1
#     if string == str_value:
#         print(f"The word {str_value} is palindrome")
#     else:
#         print(f"The word {str_value} is not palindrome")
#
#
# input_str = input("Enter a word or phrase to check if its palindrome or not: ")
# palindrome_check(input_str)

"""13.Write a Python function to check whether a string is a pangram or not.

Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : 'The quick brown fox jumps over the lazy dog'"""


def is_pangram(string):
    print(string.isascii())


input = "The quick brown fox jumps over the lazy dog"
is_pangram(input)

