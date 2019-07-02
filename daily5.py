#Given mapping a=1, b=2, ... z=26, and an encoded message, count the number of ways if can be decoded. 111 gives three 'aaa', 'ak', 'ka'.
#You can assume that the mesasges are decodable, "001" is not allowed.

def counter(string):
    if string.startswith("0"): 
        return 0 #No valid encodings for 0

    elif len(string) <= 1:
        return 1 #One valid encoding for length 1
    
    ways = 0

    if string[:2] <= 26: #Slice string to 2 elements
        ways += counter(string[:2]) #increment ways by number from the slice. 

    ways += counter(string[1:])

    return ways
    