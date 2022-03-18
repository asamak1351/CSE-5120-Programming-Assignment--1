# https://www.tutorialspoint.com/python_data_structure/python_graph_algorithms.htm

#Made DFS deterministic

class graph:
   def __init__(self,gdict=None):
      if gdict is None:
         gdict = {}
      self.gdict = gdict
# Check for the visisted and unvisited nodes
def dfs(graph, start, visited = None):
   if visited is None:
      visited = set()
   visited.add(start)
   print(start)
   #Convert to LIST for alphabetic order
   tmp_epsilon = list(set(graph[start]) - visited)
   tmp_epsilon.sort()
   for next in tmp_epsilon:
      dfs(graph, next, visited)
   return visited

gdict = { 
   "s" : ["b","c","d"],
   "b" : ["e","s"],
   "c" : ["g", "s"],
   "d" : ["s"],
   "e" : ["b","f","g"],
   "f" : ["e","g"],
   "g" : ["c","e","f"]
}

# heuristic table
wdict = {
   "s" : 1,
   "b" : 2,
   "c" : ["g", "s"],
   "d" : ["s"],
   "e" : ["b","f","g"],
   "f" : ["e","g"],
   "g" : ["c","e","f"]
}
dfs(gdict, "s")