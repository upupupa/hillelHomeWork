#!/bin/usr/python3
# -*- encoding: utf-8 -*-
from queue import Queue
def getmaze():
    with open("maze.txt", "r") as f:
        maze = []
        for line in f:
            maze.append(list(line.strip()))
        f.close()
    return maze

def findway(maze):
    removal = []
    was = {}
    q = Queue()
    start = "x"
    end = "#"
    way = ["0", "#"]
    for i in range(0, len(maze)):
        for j in range(0, len(maze[i])):
            if maze[i][j] == start:
                point = (i, j)
            if maze[i][j] == end:
                endpoint = (i, j)
    print("Start: {}, end: {}".format(point, endpoint))
    # Поиск пути по "0", добавление в was:dict и q:queue
    while point != endpoint:
        qnow = point
        if maze[qnow[0]+1][qnow[1]] in way:
            if (qnow[0]+1, qnow[1]) not in removal:
                q.put((qnow[0]+1, qnow[1]))
        if maze[qnow[0]][qnow[1]+1] in way:
            if (qnow[0], qnow[1]+1) not in removal:
                q.put((qnow[0], qnow[1]+1))
        if maze[qnow[0]-1][qnow[1]] in way:
            if (qnow[0]-1, qnow[1]) not in removal:
                q.put((qnow[0]-1, qnow[1]))
        if maze[qnow[0]][qnow[1]-1] in way:
            if (qnow[0], qnow[1]-1) not in removal:
                q.put((qnow[0], qnow[1]-1))
        removal.append(qnow)
        point = q.get()
        was[qnow] = point

    # Поиск короткого пути
    finalway = []
    reverseKeys = []
    for i in was.keys():
        reverseKeys.append(i)
    reverseKeys = reverseKeys[::-1]
    temp = endpoint
    finalway.append(temp)
    for i in range(0, len(reverseKeys)):
        if (reverseKeys[i][0]+1, reverseKeys[i][1]) == temp:
            temp = reverseKeys[i]
            finalway.append(temp)
        elif (reverseKeys[i][0]-1, reverseKeys[i][1]) == temp:
            temp = reverseKeys[i]
            finalway.append(temp)
        elif (reverseKeys[i][0], reverseKeys[i][1]+1) == temp:
            temp = reverseKeys[i]
            finalway.append(temp)
        elif (reverseKeys[i][0], reverseKeys[i][1]-1) == temp:
            temp = reverseKeys[i]
            finalway.append(temp)
        else:
            continue
    print("Way: {}".format(finalway[::-1]))
    print("Way length: {}".format(len(finalway)))
    
    # Отрисовка маршрута
    for i in range(1, len(finalway)-1): 
        maze[finalway[i][0]][finalway[i][1]] = "@"
    for i in range(0, len(maze)):
        print(maze[i])

if __name__ == "__main__":
    maze = getmaze()
    findway(maze)