from graphviz import Digraph, nohtml
from typing import Any, Deque, Dict, Iterator, List, Optional, Tuple, Union

class Node:

    def __init__(self, value, left=None, right=None,firstpos=set(),lastpos=set(),nullable=False):
        self.value = value  # The node value (float/int/str)
        self.left = left    # Left child
        self.right = right
        self.firstPos=firstpos
        self.lastPos=lastpos
        self.nullable=nullable

    def traversal(self) -> List["Node"]:

        current_nodes = [self]
        result = []

        while len(current_nodes) > 0:
            next_nodes = []
            for node in current_nodes:
                result.append(node)
                if node.left is not None:
                    next_nodes.append(node.left)
                if node.right is not None:
                    next_nodes.append(node.right)
            current_nodes = next_nodes

        return result

    def __iter__(self) -> Iterator["Node"]:

        current_nodes = [self]

        while len(current_nodes) > 0:
            next_nodes = []

            for node in current_nodes:
                yield node

                if node.left is not None:
                    next_nodes.append(node.left)
                if node.right is not None:
                    next_nodes.append(node.right)

            current_nodes = next_nodes


    def graphviz(self, *args: Any, **kwargs: Any) -> Digraph:  # pragma: no cover

        if "node_attr" not in kwargs:
            kwargs["node_attr"] = {
                "shape": "record",
                "style": "filled, rounded",
                "color": "lightgray",
                "fillcolor": "lightgray",
                "fontcolor": "black",
            }
        digraph = Digraph(*args, **kwargs)

        for node in self:
            node_id = str(id(node))

            digraph.node(node_id, nohtml(f"<l>|<v> {node.value,list(node.lastPos),list(node.firstPos),node.nullable}|<r>"))

            if node.left is not None:
                digraph.edge(f"{node_id}:l", f"{id(node.left)}:v")

            if node.right is not None:
                digraph.edge(f"{node_id}:r", f"{id(node.right)}:v")

        return digraph

symbols={}
regex=str(input("Enter regex : "))
firstpos,lastpos=[],[]

for i in regex:
  if i not in '*()|.':
    firstpos.append([i,len(firstpos)+1])
    lastpos.append([i,len(lastpos)+1])

regex+=" . #"

a=regex.split()

def postfix(infix):
    prec = {}
    prec["*"] = 3
    prec["+"] = 2
    prec["."] = 2
    prec["("] = 1
    stack=[]
    postfix=[]

    for token in infix:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ#" or token in "0123456789":
            postfix.append(token)
            symbols[token]=[]
        elif token == '(':
            stack.append(token)
        elif token == ')':
          topToken = stack.pop()
          while topToken != '(':
              postfix.append(topToken)
              topToken = stack.pop()
        else:

          while (stack!=[]) and (prec[stack[-1]] >= prec[token]):
                postfix.append(stack.pop())
          stack.append(token)

    while stack!=[]:
        postfix.append(stack.pop())
    return postfix

def constructTree(postfix):
    stack = []
    followpos = []
    firstpos = []
    lastpos = []
    count=1
    for ch in postfix:
        if ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ#" or ch in "0123456789" :
            new_node = Node(ch)
            new_node.nullable =  False
            fp=set()
            fp.add(count)
            lp=set()
            lp.add(count)
            new_node.firstPos=fp
            new_node.lastPos=lp
            count+=1
            stack.append(new_node)
            symbols[ch].append(count-1)


        else:
          if ch=="*":
            new_node = Node(ch)
            bottom=stack[0]
            new_node.left= stack.pop()
            new_node.nullable =  True
            new_node.firstPos = bottom.firstPos
            new_node.lastPos = bottom.lastPos
            stack.append(new_node)


          else:
            new_node = Node(ch)
            right,left=stack[0],stack[1]
            new_node.right = stack.pop()
            new_node.left = stack.pop()
            if ch=='.':

              if right.nullable and left.nullable:
                new_node.nullable=True
              else:
                new_node.nullable=False

              if left.nullable:
                firstpos=set(left.firstPos).union(set(right.firstPos))
                new_node.firstPos=firstpos
              else:
                new_node.firstPos=left.firstPos

              if right.nullable:
                lastpos=set(left.lastPos).union(set(right.lastPos))
                new_node.lastPos=lastpos
              else:
                new_node.lastPos=lastpos


            if ch=='+':
              if right.nullable or left.nullable:
                new_node.nullable=True
              else:
                new_node.nullable=False
              firstpos=set(left.firstPos).union(set(right.firstPos))
              lastpos=set(left.lastPos).union(set(right.lastPos))
              new_node.firstPos=firstpos
              new_node.lastPos=lastpos

            stack.append(new_node)
    return stack.pop()


def followPos(traversal):
  follow={}
  count=0
  for i in traversal:
    if i.value in "ABCDEFGHIJKLMNOPQRSTUVWXYZ#" or i.value in "0123456789":
      count+=1
      follow[count]=set()

  for i in traversal:
    if i.value=='.':
      lastpos=i.left.firstPos
      firstpos=i.right.lastPos
      for j in lastpos:
        for k in firstpos:
          follow[j].add(k)
    if i.value=='*':
      lastpos=i.firstPos
      firstpos=i.lastPos
      for j in lastpos:
        for k in firstpos:
          follow[j].add(k)

  return follow

def allVisited(states,visitedset):
  for i in states:
    if i not in visitedset:
      return i
  return True

def extractSymbolsFromT(T,symbols,symbol):
  tSymbol=[]
  for i in T:
    if i in symbols[symbol]:
      tSymbol.append(i)
  return tSymbol



def dfa(syntaxTree):
  follow=followPos(syntaxTree.traversal())
  symbols.popitem()
  s0=syntaxTree.lastPos
  states=[]
  states.append(s0)
  visited=set()
  transition={}
  while allVisited(states,visited)!=True:
    t=allVisited(states,visited)
    t=frozenset(t)
    visited.add(t)
    for i in list(symbols.keys()):
      u=set()
      tSymbol=extractSymbolsFromT(t,symbols,i)
      for j in tSymbol:
        u.update(follow[j])
      states.append(u)
      transition[(t,i)]=u
  return transition

syntaxTree=constructTree(postfix(a))
print(dfa(syntaxTree))
syntaxTree.graphviz()
# ( A + B ) * . A . B . B

