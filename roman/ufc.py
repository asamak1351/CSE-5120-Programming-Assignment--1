# modified https://www.tutorialspoint.com/python_data_structure/python_graph_algorithms.htm

from operator import add
import heapq


class graph:
   def __init__(self,gdict=None):
      if gdict is None:
         gdict = {}
      self.gdict = gdict

pq = []
path = []

def ufc(graph, start, cost, goal, explored = None ):
   if explored is None:
      explored = set()
   explored.add(start)
   print("exploring " + start)
   global path
   if(goal == start):
      return True #stop upper recursive calls
   
   global pq
   
   for ll in graph[start]:
      tmp = [ll[0], (ll[1] + cost)]
      pq.append(tmp)
   #pq = sorted(pq, key=lambda x : x[1]) # sort by cumulative cost
   pq.sort(key=lambda x:x[1])

   pq = prune_visited(pq, explored) #cyclic pruning
   
   printll(pq)

   if (len(pq) == 0):
      print("No more to explore")
      return False
   ll = pq[0] #get least cost
   if(ufc(graph, ll[0], ll[1], goal, explored)):
      return True
   return False

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
ufc(gdict, "s", 0, "g")
for node in path:
   print(node,end="")