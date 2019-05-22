#!/usr/bin/env python
  
import random

class Node:
  def __init__(self, label):
    self.label = label
    self.nodes = []
    
  def putNode(self, node):
    self.nodes.append(node)
    
  def nextNode(self):
    n = random.choice(self.nodes)
    self.nodes.remove(n)
    return n
    
  def putLabel(self):
    print(self.label, end=""); return len(self.nodes)

def main():
  cur = n1 = Node("ガ")
  n2 = Node("ン")
  n3 = Node("ズ")
  n4 = Node("ダ")

  n1.putNode(n2); n1.putNode(n2)
  n2.putNode(n1); n2.putNode(n3); n2.putNode(n4)
  n3.putNode(n4)
  n4.putNode(n2); n4.putNode(n2)

  while (cur.putLabel() > 0):
    cur = cur.nextNode()
  print()

if __name__ == "__main__":
  main()
