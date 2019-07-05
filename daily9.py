#Given a string representing an abstract file system return the longest (number of characters) absolute path to a file within our system.
def strippern(string):
    names = string.split("\n")
    return names


def starter(string):
    biggest = 0

    names = strippern(string)
    for name in names:
        if "." in name:
            depth = name.count("\t")
            path = [name.strip("\t")]
            where = names.index(name)
            fullpath = names[:where]
            for name in reversed(fullpath):
                if name.count("\t") < depth:
                    toinsert = name.strip("\t")
                    toinsert = toinsert + "\\"
                    path.insert(0,toinsert)
                    depth = depth - 1
                else:
                    pass
            length = "".join(path)
            if len(length) > biggest:
                biggest = len(length)
    return biggest
        

    
        






test = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"

print(starter(test))
