# Traditional way of defining code

# numbers = [1, 2 ,3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)
# print(new_list)

# With list comprehensions, it reduces clutter
# Example code:
    # new_list = [new_item for item in list]

# numbers = [1,2,3]
# new_list = [n + 1 for n in numbers]
# print(new_list)

### Challenge

numbers = list(range(1, 10))
print(numbers)

squared_numbers = [n*n for n in numbers]
print(squared_numbers)