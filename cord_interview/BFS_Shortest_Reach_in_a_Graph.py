"""
Problem : BFS: Shortest Reach in a Graph
Explain : https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem
Input : integer, q, denoting the number of queries.
        integers describing the respective values of n (the number of nodes) and m (the number of edges) in the graph.
        integers, u and v, describing an edge connecting node u to node v.
        single integer, s, denoting the index of the starting node.
Output : For each of the q queries, print a single line of n-1 space-separated integers denoting the shortest distances to each of
         the n-1 other nodes from starting position s.
         These distances should be listed sequentially by node number (i.e., 1, 2,..., n), but should not include node s. If some node
         is unreachable from s, print -1 as the distance to that node.

q : 쿼리 수
n : 노드 수
m : edge 수
u : edge 시작 노드
v : edge 끝 노드
s : 시작 노드

q
n m
u v
u v
s
"""

from queue import Queue
from collections import defaultdict


class Graph:
    def __init__(self, n):
        self.node_num = n
        self.edges = defaultdict(list)  # m

    def connect(self, x, y):
        self.edges[x].append(y)
        self.edges[y].append(x)

    def show(self):
        print(self.node_num)
        print(self.edges)
        print(self.edges.keys())

    def find_all_distances(self, s):
        distances = [-1 for i in range(1, self.node_num + 1)]
        nodes = [i for i in range(1, self.node_num + 1)]

        q = Queue()
        q.put(s)
        nodes.remove(s)

        distances[s - 1] = 0
        while not q.qsize() == 0:
            node = q.get_nowait()
            part_node = self.edges[node]
            height = distances[node - 1]

            for i in part_node:
                if i in nodes:
                    distances[i - 1] = height + 6
                    nodes.remove(i)
                    q.put(i)

        del distances[s - 1]

        print(' '.join(list((map(str, distances)))))


t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x,y)
    s = int(input())
    graph.find_all_distances(s)