# https://www.tutorialspoint.com/python_data_structure/python_graph_algorithms.htm

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
   for next in graph[start] - visited:
      dfs(graph, next, visited)
   return visited

gdict = { 
   "s" : set(["b","c","d"]),
   "b" : set(["s","e"]),
   "c" : set(["g", "s"]),
   "d" : set(["s"]),
   "e" : set(["b","f","g"]),
   "f" : set(["g","e"]),
   "g" : set(["c","e","f"])
}
dfs(gdict, 's')