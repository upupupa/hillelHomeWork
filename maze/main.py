#!/bin/usr/python3
# -*- encoding: utf-8 -*-
from queue import Queue
def getmaze():
    with open("maze.txt", "r") as f:
        maze = []
        for line in f:
            maze.append(line.strip())
        f.close()
    return maze

def findway(maze):
    was = []
    q = Queue()
    start = "x"
    end = "#"
    way = ["0", "#"]
    point = []
    for i in range(0, len(maze)):
        for j in range(0, len(maze[i])):
            if maze[i][j] == start:
                point = [i, j]
            if maze[i][j] == end:
                endpoint = (i, j)
    q.put(point)
    print(point, endpoint)     
    while point[0] != endpoint[0]:
        count = 0
        qnow = point
        fromCross = []
        if maze[qnow[0]+1][qnow[1]] in way:
            if (qnow[0]+1, qnow[1]) not in was:
                count+=1
                q.put((qnow[0]+1, qnow[1]))
                # was.append((point[0]+1, point[1]))
        if maze[qnow[0]][qnow[1]+1] in way:
            if (qnow[0], qnow[1]+1) not in was:
                count+=1
                q.put((qnow[0], qnow[1]+1))
                # was.append((qnow[0], qnow[1]+1))
        if maze[qnow[0]-1][qnow[1]] in way:
            if (qnow[0]-1, qnow[1]) not in was:
                count+=1
                q.put((qnow[0]-1, qnow[1]))
                # was.append((qnow[0]-1, qnow[1]))
        if maze[qnow[0]][qnow[1]-1] in way:
            if (qnow[0], qnow[1]-1) not in was:
                count+=1
                q.put((qnow[0], qnow[1]-1))
                # was.append((qnow[0], qnow[1]-1))
        if count > 1:
            fromCross.append(point)
        was.append(qnow)
        point = q.get()
        print(point)
    print("done")

if __name__ == "__main__":
    maze = getmaze()
    findway(maze)