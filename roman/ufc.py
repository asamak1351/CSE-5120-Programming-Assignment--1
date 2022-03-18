# modified https://www.tutorialspoint.com/python_data_structure/python_graph_algorithms.htm

from operator import add


class graph:
   def __init__(self,gdict=None):
      if gdict is None:
         gdict = {}
      self.gdict = gdict


pq = []
path = []
pqh = []


def ufc(graph, start, cost, goal, explored = None ):
   global pq, path, pqh

   if explored is None:
      explored = set()
      pqh.append([[start,cost]]) #need for backtracing
   explored.add(start)
   
   #Print exploring in real-time
   #print("exploring " + start)
   
   #check if goal has been explored
   if( start == goal):
      backtrace_optimal([start,cost])
      return True #stop upper recursive calls
   
   
   #add to adjacent node to priority queue 
   for list1 in graph[start]:
      pq.append([list1[0], (list1[1] + cost)])
   
   # sort by cumulative cost; manually maintain priortiy queue 
   pq.sort(key=lambda x:x[1])
   
   #cyclic pruning
   pq = prune_visited(pq, explored) 
   
   # debug show priority queue
   # printll(pq)

   #keep track of history
   pqh.append(pq)

   #return False and annouce failure to find goal
   if (len(pq) == 0):
      print("No more to explore; therefore couldn't find goal")
      return False
   
   #pop least cost
   ll = pq[0] 
   pq = pq[1:]

   #continue algorithm
   if(ufc(graph, ll[0], ll[1], goal, explored)):
      return True
   return False


def prune_visited(listoflist, visited):
   rtn_ll = []
   for list1 in listoflist:
      if (list1[0] not in visited):
         rtn_ll.append(list1)
   return rtn_ll
   

def backtrace_optimal(final):
   global pqh

   #print cost of optimal path
   print("\tOptimal Path Cost: " + str(final[1]))

   #add final(aka self) to path
   path=[final[0]]
   
   #backtrack
   pqh.reverse()
   for sub_pqh_ll in pqh:
      if (final not in sub_pqh_ll):
         final = sub_pqh_ll[0]
         path.append(final[0])
   path.reverse()
   
   #print
   print("\tOptimal Path: ",end='')
   for letter1 in path:
      print(letter1,end=" ")

   
def printll(ll):
   for list1 in ll:
      print("[" + str(list1[0]) + "," + str(list1[1]) + "],", end="")
   print("")


#graph
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


print("Uniform Cost")
ufc(gdict, "s", 0, "g")
