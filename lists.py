# Lists (look a lot like JavaScript arrays)
users = ['Dave', 'John', 'Sara']

data = ['Dave', 42, True]

emptyList = []

print("Dave" in emptyList)

print(users[0])
print(users[-1]) #last value in list

print(users.index('Sara'))

print(users[0:2]) #range (2nd number is exclusive)
print(users[0:]) #all values
print(users[-3:-1])

print(len(data))

users.append('Elsa')
print(users)

users += ['Jason']
print(users)

users.extend(['Robert', 'Jimmy'])
print(users)

# users.extend(data)
# print(users)

users.insert(0, 'Bob')
print(users)

# start at position 2 & end at position 2 (not replacing, just inserting)
users[2:2] = ['Eddie', 'Alex']
print(users)

# refered to as a 'slice' - start at position 1 & end at position 3 (replacing)
users[1:3] = ['Robert', 'JPJ']
print(users)

users.remove('Bob')
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

# del data
data.clear()
print(data)

users[1:2] = ['dave'] #lowercase sorted AFTER uppercase
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)

# nums.sort(reverse=True) #DIFFERENT than the method above
# print(nums)

# global sorted function - does NOT modify original
print(sorted(nums, reverse=True))
print(nums)

# OR MAKE A COPY TO NOT MODIFY
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

my_list = list([1,"Neil",True])
print(my_list)

# Tuples

# Python tuples are a type of data structure that is very similar to lists. The main difference between the two is that tuples are immutable, meaning they cannot be changed once they are created. This makes them ideal for storing data that should not be modified, such as database records.

my_tuple = tuple(('Dave',42,True))
another_tuple = (1,4,2,8)

print(my_tuple)
print(type(my_tuple))

# packing tuples
new_list = list(my_tuple)
new_list.append('Neil')
new_tuple = tuple(new_list)
print(new_tuple)

# unpacking tuples
(one, two, *hey) = another_tuple # *calls remainging values
print(one)
print(two)
print(hey)

print(another_tuple.count(2))