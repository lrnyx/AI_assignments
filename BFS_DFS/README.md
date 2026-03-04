BFS and DFS – Water Jug Problem

This program shows how search algorithms work using the water jug problem.

Problem
There are two jugs:
Jug A capacity = 4 litres
Jug B capacity = 3 litres
The goal is to measure exactly 2 litres of water using these jugs.

State Representation

A state is written as (A, B) where:
A = water in jug A
B = water in jug B
Example: (0,0) means both jugs are empty.

Operations

The following actions are possible:
Fill a jug
Empty a jug
Pour water from one jug to the other

Algorithms Used

Two search algorithms are implemented:

Breadth First Search (BFS) – explores states level by level and finds the shortest path.

Depth First Search (DFS) – explores one path deeply before trying other paths.