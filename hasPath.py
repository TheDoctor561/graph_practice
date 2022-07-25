graph = {
  'f': ['g', 'i'],
  'g': ['h'], 
  'h': [], 
  'i': ['g','k'], 
  'j': ['i'], 
  'k': []
  }

# f -> g -> h 
# |   /
# i  <- j 
# | 
# k 

def hasPath (graph, src, dst): 
  if src == dst: 
    return True 
  
  for i in graph[src]: 
    if hasPath(graph, i, dst): 
      return True
  return False 

# print(hasPath(graph, 'f', 'p'))
  
def hasPathBFS(graph, src, dst): 
  queue = [src]

  while len(queue) > 0: 
    curr = queue.pop(0)
    if curr == dst: 
      return True 
    for i in graph[curr]: 
      queue.append(i)
  return False 

print(hasPathBFS(graph, 'f', 'k'))
# Is there a path between a given source and destination node
 