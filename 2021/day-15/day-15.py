from collections import defaultdict
from collections import deque
from functools import reduce
import itertools as it
import operator
import math
import os
import re
from queue import PriorityQueue
import sys

INF = int(0x3F3F3F3F)


# Inspired by https://www.geeksforgeeks.org/shortest-paths-from-all-vertices-to-a-destination/

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    lines = [l.strip() for l in file.readlines()]
    grid = {}

    c = 0
    for y, row in enumerate(lines):
        for x, col in enumerate(row):
            grid[(x, y)] = {"id": c, "value": int(col)}
            c += 1

    directions = [
        [0, -1],
        [1, 0],
        [0, 1],
        [-1, 0],
    ]


class Graph:
    def __init__(self, V):

        self.V = V
        self.adj = [[] for _ in range(V)]

    def addEdgeRev(self, u: int, v: int, w: int):
        self.adj[v].append((u, w))

    def shortestPath(self, dest: int):
        pq = PriorityQueue()
        dist = [INF for _ in range(self.V)]
        pq.put((0, dest))
        dist[dest] = 0

        while not pq.empty():
            u = pq.get()[1]
            for i in self.adj[u]:
                v = i[0]
                weight = i[1]
                if dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight
                    pq.put((dist[v], v))

        return dist[self.V - 1]


def part1():
    V = 10000
    g = Graph(V)

    for (coords, val) in grid.items():
        for [dx, dy] in directions:
            new_coords = (coords[0] + dx, coords[1] + dy)
            if new_coords in grid:
                g.addEdgeRev(val["id"], grid[new_coords]["id"], val["value"])

    return g.shortestPath(0)


def part2():
    V, step = 250000, 100
    g = Graph(V)

    extended_x_grid, extended_x_y_grid = {}, {}

    c = 0
    for i in range(5):
        for (coords, value) in grid.items():
            new_val = value["value"] + i
            extended_x_grid[(coords[0] + i * step, coords[1])] = {
                "id": c,
                "value": new_val if new_val < 10 else (new_val % 10) + 1,
            }
            c += 1

    c = 0
    for i in range(5):
        for (coords, value) in extended_x_grid.items():
            new_val = value["value"] + i
            extended_x_y_grid[(coords[0], coords[1] + i * step)] = {
                "id": c,
                "value": new_val if new_val < 10 else (new_val % 10) + 1,
            }
            c += 1

    for (coords, val) in extended_x_y_grid.items():
        for [dx, dy] in directions:
            new_coords = (coords[0] + dx, coords[1] + dy)
            if new_coords in extended_x_y_grid:
                g.addEdgeRev(
                    val["id"], extended_x_y_grid[new_coords]["id"], val["value"]
                )

    return g.shortestPath(0)


print(f"Part 1: {part1()}")  # 498
print(f"Part 2: {part2()}")  # 2901
