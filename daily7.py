#Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings 
#in the set that have s as a prefix.
dictionary = ["dog","deer","deal"]
autocomplete =[]
def query(string):
    for element in dictionary:
        if element[:len(string)] == string:
            autocomplete.append(element)
    return print(autocomplete)
query("do")