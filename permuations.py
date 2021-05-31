""" Decorator function for reporting a functions execution time """
from timer import timer as timer


@timer
def cnt(n):
    for i in range(1, 10):
        n += i
        print(n)


# multiple arguments
def take_all(*args):
    for arg in args:
        print(arg)


# can take any number of positional arguments
take_all(1, 2, 3, 4, 5, 6)
take_all(1, 2)

# if arguments are in list, * is needed before the list to unpack it like line 19
some_list = [1, 2, 3, 4, 5, 6]
take_all(*some_list)


# permutation function
def permutations(word):
    if len(word) == 1:
        return [word]

    perms = permutations(word[1:])
    char = word[0]
    result = list()

    for perm in perms:
        for i in range(len(perm) + 1):
            result.append(perm[:i] + char + perm[i])

    return result


def mysum(lst):
    # print(lst)
    if not lst:
        return 0
    else:
        # print(lst[0] + mysum(lst[1:]))
        print(lst[0] + mysum(lst[1:]))
        return lst[0] + mysum(lst[1:])


# showint that recrusion list gets smaller
mysum([1, 2, 3, 4, 5])


def print_hello():
    """Only prints doesn't return object"""
    print('hello\t\thello')


def print_hello2():
    """Returns object, which is different from printing"""
    return 'hello/transferhello'


print_hello()
print_hello2()


nested_list = [1, [2, [3, 4], 5], 6, [7, 8]]
sum(nested_list)
for item in nested_list:
    print(item)


def sumtree(lst):
    tot = 0
    for x in lst:
        if not isinstance(x, list):
            tot += x
        else:
            tot += sumtree(x)
    return tot


# isinstance, build in type checker of object instance
isinstance('test string', str)


# lambda expressions can go into a list, whereas def statements cannot
list1 = [lambda x: x**2,
         lambda x: x**3,
         lambda x: x**4]

for func in list1:
    print(func(2))
