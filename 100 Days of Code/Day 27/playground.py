# def add(numbers):
#     return sum(numbers)

# print(add([88, 43, 123]))

def add(*args):
    for n in args:
        n += n
    return n

print(add(1,2,3,90,132))