
adjacency_list = {
    'Arad': [('Sibiu', 140), ('Zerind', 75), ('Timisoara', 118)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Vaslui', 142), ('Hirsova', 98)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Iasi', 92), ('Urziceni', 142)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)]
}

# heuristic function with equal values for all nodes


def get_heuristics(stop_node):
    heuristics = {
        'Arad': 366,
        'Bucharest': 0,
        'Craiova': 160,
        'Drobeta': 242,
        'Eforie': 161,
        'Fagaras': 178,
        'Giurgiu': 77,
        'Hirsova': 151,
        'Iasi': 226,
        'Lugoj': 244,
        'Mehadia': 241,
        'Neamt': 234,
        'Oradea': 380,
        'Pitesti': 98,
        'Rimnicu Vilcea': 193,
        'Sibiu': 253,
        'Timisoara': 329,
        'Urziceni': 80,
        'Vaslui': 199,
        'Zerind': 374
    }
    fake_heuristics = {
        'Arad': 1,
        'Bucharest': 1,
        'Craiova': 1,
        'Drobeta': 1,
        'Eforie': 1,
        'Fagaras': 1,
        'Giurgiu': 1,
        'Hirsova': 1,
        'Iasi': 1,
        'Lugoj': 1,
        'Mehadia': 1,
        'Neamt': 1,
        'Oradea': 1,
        'Pitesti': 1,
        'Rimnicu Vilcea': 1,
        'Sibiu': 1,
        'Timisoara': 1,
        'Urziceni': 1,
        'Vaslui': 1,
        'Zerind': 1
    }

    if stop_node == 'Bucharest':
        return heuristics
    else:
        return fake_heuristics


def a_star_algorithm(start_node, stop_node):
    heuristics = get_heuristics(stop_node)
    # open_list is a list of nodes which have been visited, but who's neighbors
    # haven't all been inspected, starts off with the start node
    # closed_list is a list of nodes which have been visited
    # and who's neighbors have been inspected
    open_list = set([start_node])
    closed_list = set([])

    # OVA cost stores distances traveled from start_node to reach every other nodes
    # the default value (if it's not found in the map) is +infinity
    cost = {start_node: 0}

    # parents stores parent of each node in a map
    parents = {start_node: start_node}

    while len(open_list) > 0:
        node = None

        # find a node with the lowest value of f() - evaluation function
        for v in open_list:
            if node is None or cost[v] + heuristics[v] < cost[node] + heuristics[node]:
                node = v

        if node is None:
            print('Path does not exist!')
            return None

        # if the current node is the stop_node
        # then we begin reconstructin the path from it to the start_node
        if node == stop_node:
            reconst_path = []

            while parents[node] != node:
                reconst_path.append(node)
                node = parents[node]

            reconst_path.append(start_node)

            reconst_path.reverse()

            return reconst_path

        # for all neighbors of the current node do
        for (m, weight) in adjacency_list[node]:
            # if the current node isn't in both open_list and closed_list
            # add it to open_list and note n as it's parent
            if m not in open_list and m not in closed_list:
                open_list.add(m)
                # remember neighbour parent
                parents[m] = node
                # neighbour cost = parent cost + neighbour cost
                cost[m] = cost[node] + weight

            # otherwise, check if it's quicker to first visit n, then m
            # and if it is, update parent data and cost data
            # and if the node was in the closed_list, move it to open_list
            else:
                # check if old route cost > new route cost if so change it to new route cost and change parent
                if cost[m] > cost[node] + weight:
                    cost[m] = cost[node] + weight
                    parents[m] = node

                    if m in closed_list:
                        closed_list.remove(m)
                        open_list.add(m)

        # remove n from the open_list, and add it to closed_list
        # because all of his neighbors were inspected
        open_list.remove(node)
        closed_list.add(node)

    print("Path does not exist!")
    return None



from tkinter import *
import tkinter as tk
from typing import List, Tuple, Any

from a_star import a_star_algorithm
from PIL import ImageTk, Image
from pprint import pprint

graph = {
    'Arad': [('Sibiu', 140), ('Zerind', 75), ('Timisoara', 118)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Vaslui', 142), ('Hirsova', 98)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Iasi', 92), ('Urziceni', 142)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)]
}

un_weighted_graph = {
    'Arad': ['Sibiu', 'Zerind', 'Timisoara'],
    'Zerind': ['Arad', 'Oradea'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu Vilcea'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Drobeta'],
    'Drobeta': ['Mehadia', 'Craiova', ],
    'Craiova': ['Drobeta', 'Rimnicu Vilcea', 'Pitesti'],
    'Rimnicu Vilcea': ['Sibiu', 'Craiova', 'Pitesti'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Vaslui', 'Hirsova'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Iasi', 'Urziceni'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi']
}


def bfs(graph, start, goal):
    visited = set()
    visited.add(start)
    queue = []
    # to store parent of every node
    path = []
    parents = {}
    queue.append(start)
    while queue:  # Creating loop to visit each node
        # remove first element

        node = queue.pop(0)
        neighbours = graph.get(node)
        for neighbour in neighbours:

            if neighbour == goal:
                parents[neighbour] = node
                path.append(neighbour)
                while parents.get(neighbour):
                    # append parent
                    path.append(parents[neighbour])
                    # get to the next child in the shortest path
                    neighbour = parents[neighbour]
                path.reverse()
                pprint(path)
                return path

            if neighbour not in visited:
                visited.add(neighbour)
                # add neighbour to end
                queue.append(neighbour)
                parents[neighbour] = node


bfs(un_weighted_graph, 'Oradea', 'Mehadia')


def dfs(graph, start, goal):
    visited = []
    # LIFO
    stack: list[list[tuple[Any, int]] | Any] = [[(start, 0)]]
    while stack:
        path = stack.pop()
        node = path[-1][0]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            print(path)
            keys_path = []
            for v in path:
                keys_path.append(v[0])
            return keys_path
        else:
            # children
            adjacent_nodes = graph.get(node, [])
            for node2, cost in adjacent_nodes:
                new_path = path.copy()
                new_path.append((node2, cost))
                stack.append(new_path)


window = Tk()

window.title("Romania map")
window.geometry("1500x900")

img = ImageTk.PhotoImage(Image.open("romania.png"))
panel = tk.Label(window, image=img)
panel.pack(side="bottom", fill="both")

lable1 = Label(text="Enter starting city")
lable1.pack(padx=30)
entry1 = Entry()
entry1.pack()

label2 = Label(text="Enter goal city")
label2.pack(padx=30)
entry2 = Entry()
entry2.pack()


def a_star_algorithm_on_click():
    start = entry1.get()
    end = entry2.get()
    path = str(a_star_algorithm(start, end))
    result.config(text=path)


def dfs_button_on_click():
    start = entry1.get()
    end = entry2.get()
    path = str(dfs(graph, start, end))
    result.config(text=path)


def bfs_button_on_click():
    start = entry1.get()
    end = entry2.get()
    path = str(bfs(un_weighted_graph, start, end))
    result.config(text=path)


a_star_algorithm_button = Button(window, text="A* algorithm", command=a_star_algorithm_on_click)
a_star_algorithm_button.pack()
dfs_button = Button(window, text="Depth first Search", command=dfs_button_on_click)
dfs_button.pack()

bfs_button = Button(window, text="Breadth first search", command=bfs_button_on_click)
bfs_button.pack()

result = Label(text="Hello there")
result.pack()

window.mainloop()

# window.itemconfig(line, fill='red')
# bbox = window.bbox(line)


# solution = dfs(graph, 'Arad', 'Rimnicu Vilcea')
