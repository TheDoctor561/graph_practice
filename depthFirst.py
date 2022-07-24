

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
    curr = stack.pop(0) 
    print(curr)
    for i in graph[curr]: 
      stack.append(i)

depthFirstPrint(graph, 'a')