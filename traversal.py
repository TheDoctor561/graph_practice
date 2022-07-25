

import unittest

graph = {
  'a': ['b', 'c'], 
  'b': ['d'], 
  'c': ['e'], 
  'd': ['f'], 
  'e': [], 
  'f': []
  } 

# a --> c
# |     |
# \/   \/ 
# b     e 
# | 
# \/
# d --> f 

def DFSRec(graph, source): 
  print(source)
  for node in graph[source]: 
    DFSRec(graph, node)



# print("DFS itter")
# depthFirstPrint(graph, 'a')
# print("DFS rec")
# DFSRec(graph, 'a')
# print("BFS")
# breadthFirstPrint(graph, 'a')



 
# Our code to be tested
class Traversal:
  def depthFirstPrint(graph, source): 
    stack = [source]
    ret = []
    while len(stack) > 0: 

      # Utilization of a queue
      curr = stack.pop() 
      ret.append(curr) 
      for i in graph[curr]: 
        stack.append(i)
    return ret

  def breadthFirstPrint(graph, source): 
    stack = [source]
    ret = []
    while len(stack) > 0: 
      # Utilization of a stack
      curr = stack.pop(0) 
      ret.append(curr)
      for i in graph[curr]: 
        stack.append(i)
    return ret

# The test based on unittest module
class TestTraversal(unittest.TestCase):
    def runTest(self):
        graph = {
          'a': ['b', 'c'], 
          'b': ['d'], 
          'c': ['e'], 
          'd': ['f'], 
          'e': [], 
          'f': []
          } 
        self.assertEqual(Traversal.depthFirstPrint(graph, 'a'), ['a', 'c', 'e', 'b', 'd', 'f'], "incorrect traversal")
        self.assertEqual(Traversal.breadthFirstPrint(graph, 'a'), ['a', 'b', 'c', 'd', 'e', 'f'], "incorrect traversal")
 
# run the test
unittest.main()