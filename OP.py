import pandas as pd
import numpy as np
import networkx as nx
from itertools import permutations

table = np.array([
    ['NaN', '>', '>', '>'],
    ['<', '>', '<', '>'],
    ['<', '>', '>', '>'],
    ['<', '<', '<', 'NaN']
])

df = pd.DataFrame(table, index=['i', '+', '*', '$'], columns=['i', '+', '*', '$'])


def parse_expression(expression):
    stack = []
    stack.append('$')
    i = 0
    while i < len(expression):
        if expression[i] in df.columns and stack[-1] in df.index:
            if df[expression[i]][stack[-1]] == '>':
                stack.pop()
            elif df[expression[i]][stack[-1]] == '<':
                stack.append(expression[i])
            else:
                print('The expression is not accepted')
                return
        else:
            print('The expression is not accepted')
            return
        i += 1
    if stack[-1] == '$':
        print('The expression is accepted')
    else:
        print('The expression is not accepted')


def longestPathLength(graph, node, visited=None):
    visited = set()

    neighbors = graph.neighbors(node)

    if not neighbors:
        return 0

    max_path_length = 0

    for neighbor in neighbors:
        if neighbor not in visited:
            path_length = longestPathLength(graph, neighbor, visited)
            max_path_length = max(path_length, max_path_length)

    return max_path_length + 1


def constructGraph(df):
    G = nx.DiGraph()
    G.add_nodes_from(['f' + i for i in list(df.index)], bipartite=0)
    G.add_nodes_from(['g' + i for i in list(df.index)], bipartite=1)
    posEdges = list(permutations(list(df.index), 2))
    edges = []
    for i in posEdges:
        if df[i[0]][i[1]] == '>':
            i0 = str(i[0])
            i1 = str(i[1])
            edge = ('f' + i1, 'g' + i0)
            edges.append(edge)
        elif df[i[0]][i[1]] == '<':
            i0 = str(i[0])
            i1 = str(i[1])
            edge = ('g' + i0, 'f' + i1)
            edges.append(edge)
        else:
            pass

    G.add_edges_from(edges)
    return G


def precedenceFunction():
    G = constructGraph(df)
    f = {}
    g = {}

    for node in G.nodes():
        terminal = node[1]

        if node[0] == 'f':
            f[terminal] = longestPathLength(G, node)
        else:
            g[terminal] = longestPathLength(G, node)

    return f, g


parse_expression('i+i*i$')
print(precedenceFunction())