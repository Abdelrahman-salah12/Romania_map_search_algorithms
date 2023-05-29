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
