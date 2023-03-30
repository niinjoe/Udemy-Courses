# def add(numbers):
#     return sum(numbers)

# print(add([88, 43, 123]))


def add(*args):
    for n in args:
        n += n
    return n


# print(add(1,2,3,90,132))


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(5, add=3, multiply=5)
