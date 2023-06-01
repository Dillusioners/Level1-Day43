'''
Author - Debag101
Purpose - Average of a list of numbers
Date - 01 06 2023
'''

# Getting an arbitrary list of numbers, say multiples of 17
data = [x for x in range(10001) if x % 17 == 0]


# Returns avg by using the sum func to get sum of all the numbers in the list
def get_avg(lst):
    return sum(lst) / len(lst)

# Printing the list to user
print("The list is : ",  data)
# Printing result i.e avg sum of all the numbers in the list
print("Average of all numbers in the list = ", get_avg(data))
