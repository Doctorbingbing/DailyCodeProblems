#Given an array of integers and a number k, where k is between 1 and the lenght of the array, compute the maximum values of each sub array of length k.

array = [10,2]
k = 1
#Should return [10,7,8,8]


def parser(array,k):
    i = 0
    while i <= len(array)-k:
        temp1 = array[i:(k+i)]
        temp1.sort()
        print(temp1[-1])
        i=i+1
        continue
    return

parser(array,k)