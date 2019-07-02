# Given an array of integers, find the missing positive integer in constant space. In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.
#Should return 3. Question asks to do this in linear time, but that is beyond me

array = [0,1,43,-4,2]
def finder(array):
    setOfArray = set(array)
    i=1
    while i in setOfArray:
        i += 1
    return i

print(finder(array))
