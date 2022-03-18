# https://www.tutorialspoint.com/python_data_structure/python_graph_algorithms.htm

from operator import add, itemgetter
from pickle import TRUE


class graph:
   def __init__(self,gdict=None):
      if gdict is None:
         gdict = {}
      self.gdict = gdict
# Check for the visisted and unvisited nodes
def dfs(graph, start, target, visited = None, ):
   if visited is None:
      visited = set()
   visited.add(start)
   print("exploring " + start)
   if(target == start):
      return False

   ll = graph[start]
   ll = sorted(ll, key=lambda x:x[1]) # sort by weight
   # Debug
   # printll(ll)
   ll = prune_visited(ll, visited)
   
   # Debug
   # print("visited: ", end="")
   # for letter1 in visited:
   #    print(letter1,end="")
   # print()
   # #-----
   # print("\nafter")
   # printll(ll)

   for list1 in ll:
      if(dfs(graph, list1[0], target, visited ) == False):
         return False
   return True

def prune_visited(listoflist, visited):
   rtn_ll = []
   
   for list1 in listoflist:
      if (list1[0] not in visited):
         rtn_ll.append(list1)
   return rtn_ll
   

def printll(ll):
   for list1 in ll:
      print("[" + str(list1[0]) + "," + str(list1[1]) + "],", end="")
   print("")

gdict = { 
   "s" : [["b",2],["c",1],["d",10]],
   "b" : [["e",7],["s",2]],
   "c" : [["g",15], ["s",1]],
   "d" : [["s",10]],
   "e" : [["b",7],["f",1],["g",2]],
   "f" : [["e",1],["g",3]],
   "g" : [["c",15],["e",2],["f",3]]
}

# heuristic table
hdict = {
   "s" : 9,
   "b" : 7,
   "c" : 10,
   "d" : 7,
   "e" : 1,
   "f" : 1,
   "g" : 0
}
dfs(gdict, "s", "g")