#Given an array of time intervals (start, end) for classroom lectures, find the minimum number of rooms required.
#[(30,75),(0,50),(60,150)] should return 2

array = [(30,75),(0,50),(60,150)]

def lectureFree(tup1,tup2): #Returns true if tup1 and tup2 times do not collide
    if tup1[0] < tup2[0] < tup1[1] or tup1[0] < tup2[1] < tup1[1]:
        return False
    else: 
        return True

def roomTaken(room, toAdd): #Returns true if a room is taken during a specified time interval (toAdd)
    collide = False
    for lecture in room:
        if lectureFree(lecture, toAdd):
            collide = True
            break
    return collide


def num_rooms(array):
    rooms = []
    for time in array:
        if len(rooms) == 0: #First entry will create a room with the first time
            rooms=[[[None,None]]]
            rooms[0][0]=time
        else:
            roomed = 0     #Subsequent entries will check to see if the rooms are free
            for room in rooms:
                if not roomTaken(room, time):
                    room.append(time) #Append them if they are free and go to the next time
                    roomed=1
                    break
            if not roomed:
                rooms.append([time]) #Create a new room for the class if it conflicts with all others
    return len(rooms)
            

print(num_rooms(array))
            