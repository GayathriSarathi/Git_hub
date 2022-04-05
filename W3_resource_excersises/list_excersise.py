# #1 Write a Python program to sum all the items in a list.
# list_values = [2,5,7,56,34,24,89,28,90,67]
# result = 0
# for i in list_values:
#     result += i
# print(result)
#
# # print(2*5*7*56*34*24*89*28*90*67)
#
# def sum_list(list_items):
#     result = 0
#     for value in list_items:
#         result += value
#     return  result
# print(sum_list([2,5,7,56,34,24,89,28,90,67])) #402
#
# #2.  Write a Python program to multiply all the items in a list.
#
# def list_multiple(list_items):
#     multiple = 1
#     for i in list_items:
#         multiple *= i
#     return multiple
# print(list_multiple([2,5,7,56,34,24,89,28,90,67]))
#
# #3. Write a Python program to get the largest number from a list.
#
# def max_no_list(values):
#     result = max(values)
#     return result
# print(max_no_list([2,5,7,56,34,24,89,28,90,67]))
#
#
# #4.Write a Python program to get the smallest number from a list
#
# def max_no_list(values):
#     result = min(values)
#     return result
# print(max_no_list([2,5,7,56,34,24,89,28,90,67]))

"""5. Write a Python program to count the number of strings where the string length is 2 or more and the first and
last character are same from a given list of strings.
Sample List : ['abc', 'xyz', 'aba', '1221']"""
# sample_list = ['abc', 'xyz', 'aba', '1221']
# def count_strings(value):
#     count = 0
#     for i in value:
#         if len(i) >= 2 and (i[0] == i[-1]):
#             count += 1
#     return count
# print(count_strings(sample_list))


"""6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]"""
# def arrange(m):
#     return m[-1]
# def sorted_list(list):
#     print(sorted(list,key=arrange))
#
# sorted_list([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])

"""7. Write a Python program to remove duplicates from a list."""
def remove_duplicate_val(list):
    return set(list)
value = [10,20,30,20,10,50,60,40,80,50,40]
print(list(remove_duplicate_val(value)))

# alternate sol:
list_values = [10,20,30,20,10,50,60,40,80,50,40]
set_values = set()
list_unique = []
for value in list_values:
    if value not in set_values:
        list_unique.append(value)
        set_values.add(value)
print(f"Unique list : {list_unique}")


# print(set.__dict__)

"""8. Write a Python program to check a list is empty or not."""
def check_list(value):
    if value == []:
        print(f"list is empty")
    else:
        print(f"list is not empty")

list = [10,45]
check_list(list)

"""9. Write a Python program to clone or copy a list"""
list = [1,34,45,78,79]
a = [12]
a= list.copy()
print(a)