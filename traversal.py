

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

def depthFirstPrint(graph, source): 
  stack = [source]
  while len(stack) > 0: 

    # Utilization of a queue
    curr = stack.pop() 
    print(curr)
    for i in graph[curr]: 
      stack.append(i)

def breadthFirstPrint(graph, source): 
  stack = [source]
  while len(stack) > 0: 
    # Utilization of a stack
    curr = stack.pop(0) 
    print(curr)
    for i in graph[curr]: 
      stack.append(i)

depthFirstPrint(graph, 'a')

breadthFirstPrint(graph, 'a')