#Function

def highest_even(list):
    even = []
    for item in list:
        if item % 2 == 0:
            even.append(item)
    max_value = max(even)
    return max_value

#main

my_list = [10, 21 , 3, 4, 8, 11]
high = highest_even(my_list)
print (f"The highest even in the list is {high}")
