# lambda - a single expression that returns a value
squared = lambda num : num * num

print(squared(2))


# addtwo = lambda num : num + 2
def addtwo(num): return num + 2

print(addtwo(12))


sum_total = lambda a, b : a + b

print(sum_total(10, 2))

##########################

def func_builder(x):
    return lambda num : num + x

add_ten = func_builder(10)
add_twenty = func_builder(20)

print(add_ten(7))
print(add_twenty(7))

##########################

# lambda num : num * num

numbers = [3, 7, 12, 18, 20, 21]

squared_nums = map(lambda num : num * num, numbers)

print(list(squared_nums))

##########################

# lambda num : num % 2 != 0

odd_nums = filter(lambda num : num % 2 != 0, numbers)

print(list(odd_nums))

##########################

from functools import reduce

# lambda acc, curr: acc + curr

numbers = [1,2,3,4,5,1]

total = reduce(lambda acc, curr: acc + curr, numbers, 10)

print(total)

print(sum(numbers, 10))



names = ['Dave Gray','Sara Ito','John Jacob Jingleheimerschmidt']

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)

print(char_count)