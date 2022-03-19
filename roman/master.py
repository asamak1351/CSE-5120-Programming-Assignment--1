# modified https://www.tutorialspoint.com/python_data_structure/python_graph_algorithms.htm

from operator import add
from typing import List


class graph:
   def __init__(self,gdict=None):
      if gdict is None:
         gdict = {}
      self.gdict = gdict


def a_star(graph,hdict,start, goal, cost = 0, explored = None, pq = None, pqh = None ):
   
   if explored is None:
      explored = set()
      pq = []
      pqh = []
      pqh.append([[start,cost]]) #need for backtracing
   explored.add(start)
   
   #Print exploring in real-time
   print("exploring " + start +":"+str(cost))
   
   #check if goal has been explored
   if( start == goal):
      backtrace_optimal([start,cost],pqh)
      return True #stop upper recursive calls
   
   
   #add to adjacent node to priority queue  #add heuristic to cost
   for list1 in graph[start]:
      pq.append([list1[0], (list1[1] + cost + hdict[list1[0]]) ])
   
   # sort by cumulative cost; manually maintain priortiy queue 
   pq.sort(key=lambda x:x[1])
   
   #cyclic pruning ##a_star uses prune worse paths instead of cyclic pruning
   #pq = prune_explored(pq, explored) 

   #prune worse paths
   prune_worse_paths(pq)
   
   # debug show priority queue
   printll(pq)

   #keep track of history
   pqh.append(pq)

   #return False and annouce failure to find goal
   if (len(pq) == 0):
      print("No more to explore; therefore couldn't find goal")
      return False
   
   #pop least cost
   list1 = pq[0] 
   pq = pq[1:]
 
   #continue algorithm #subtract heuristic to get actual cost
   if(a_star(graph, hdict, list1[0], goal, list1[1] - hdict[list1[0]], explored, pq, pqh)):
      return True
   return False

def ufc(graph,hdict,start, goal, cost = 0, explored = None, pq = None, pqh = None ):
   
   if explored is None:
      explored = set()
      pq = []
      pqh = []
      pqh.append([[start,cost]]) #need for backtracing
   explored.add(start)
   
   #Print exploring in real-time
   print("exploring " + start +":"+str(cost))
   
   #check if goal has been explored
   if( start == goal):
      backtrace_optimal([start,cost],pqh)
      return True #stop upper recursive calls
   
   
   #add to adjacent node to priority queue  #add heuristic to cost
   for list1 in graph[start]:
      pq.append([list1[0], (list1[1] + cost) ])
   
   # sort by cumulative cost; manually maintain priortiy queue 
   pq.sort(key=lambda x:x[1])
   
   #cyclic pruning
   pq = prune_explored(pq, explored) 

   #prune worse paths
   #prune_worse_paths(pq)
   
   # debug show priority queue
   printll(pq)

   #keep track of history
   pqh.append(pq)

   #return False and annouce failure to find goal
   if (len(pq) == 0):
      print("No more to explore; therefore couldn't find goal")
      return False
   
   #pop least cost
   list1 = pq[0] 
   pq = pq[1:]
 
   #continue algorithm #subtract heuristic to get actual cost
   if(ufc(graph, hdict, list1[0], goal, list1[1], explored, pq, pqh)):
      return True
   return False

def dfsw(graph,start, goal, cost = None, explored = None):
    if explored is None:
      explored = set()
      cost = 0
      print("Path: ",end="")
    explored.add(start)
    print(start,end=" ")
    if(goal == start):
        print("\nCost: " + str(cost))
        return False

    frontier = graph[start]
    # sort by weight
    frontier.sort(key=lambda x:x[1])
    # Debug
    # printll(ll)
    frontier = prune_explored(frontier, explored)
    
    # Debug
    # print("explored: ", end="")
    # for letter1 in explored:
    #    print(letter1,end="")
    # print()
    # #-----
    # print("\nafter pruning")
    # printll(frontier)

    for list1 in frontier:
        if(dfsw(graph, list1[0], goal, cost + list1[1], explored ) == False):
            return False
    return True

def dfs(graph,start, goal, cost = None, explored = None):
    if explored is None:
      explored = set()
      cost = 0
      print("Path: ",end="")
    explored.add(start)
    print(start,end=" ")
    if(goal == start):
        print("\nCost: " + str(cost))
        return False

    frontier = graph[start]
    # sort by weight
    frontier.sort(key=lambda x:x[0])
    # Debug
    # printll(ll)
    frontier = prune_explored(frontier, explored)
    
    # Debug
    # print("explored: ", end="")
    # for letter1 in explored:
    #    print(letter1,end="")
    # print()
    # #-----
    # print("\nafter pruning")
    # printll(frontier)

    for list1 in frontier:
        if(dfs(graph, list1[0], goal, cost + list1[1], explored ) == False):
            return False
    return True



def prune_explored(listoflist, explored):
   rtn_ll = []
   for list1 in listoflist:
      if (list1[0] not in explored):
         rtn_ll.append(list1)
   return rtn_ll
   

def backtrace_optimal(final, pqh):
   path = list()
   #print cost of optimal path
   print("\tOptimal Path Cost: " + str(final[1]))

   #add final(aka self) to path
   path=[final[0]]
   
   #backtrack
   pqh.reverse()
   for sub_pqh_ll in pqh:
      #printll(sub_pqh_ll)
      if (final not in sub_pqh_ll):
         final = sub_pqh_ll[0]
         path.append(final[0])
   path.reverse()
   
   #print
   print("\tOptimal Path: ",end='')
   for letter1 in path:
      print(letter1,end=" ")
   return path   


#prune the worse paths from the frontier
def prune_worse_paths(pq, index = 0):
   if(index >= len(pq) - 1):
      return
   #get letter
   gl = lambda x:x[0]
   for i in reversed(range(index + 1,len(pq))):
      if (gl(pq[index]) == gl(pq[i])):
         pq.remove(pq[i])
   prune_worse_paths(pq, index + 1)


def printll(ll):
   for list1 in ll:
      print("[" + str(list1[0]) + "," + str(list1[1]) + "],", end="")
   print("")


#graph
gdict1 = { 
   "s" : [["b",2],["c",1],["d",10]],
   "b" : [["e",7],["s",2]],
   "c" : [["g",15], ["s",1]],
   "d" : [["s",10]],
   "e" : [["b",7],["f",1],["g",2]],
   "f" : [["e",1],["g",3]],
   "g" : [["c",15],["e",2],["f",3]]
}
# heuristic table
hdict1 = {
   "s" : 9,
   "b" : 7,
   "c" : 10,
   "d" : 7,
   "e" : 1,
   "f" : 1,
   "g" : 0
}

gdict2 ={
   "a" : [["b",4],["c",1]],
   "b" : [["c",2],["g",6]],
   "c" : [["b",2],["g",9]],
   "g" : []
}

hdict2 = {
   "a" : 8,
   "b" : 3,
   "c" : 7,
   "g" : 0
}

print("\n\nDFS")
dfs(gdict1, "s", "g")
print("\nDFS")
dfs(gdict2, "a", "g")

print("\n\nDFS by weight")
dfsw(gdict1, "s", "g")
print("\nDFS by weight")
dfsw(gdict2, "a", "g")

print("\n\nUniform Cost")
ufc(gdict1,hdict1, "s", "g")
print("\nUniform Cost")
ufc(gdict2,hdict2, "a", "g")

print("\n\na*")
a_star(gdict1,hdict1, "s", "g")
print("\na*")
a_star(gdict2,hdict2, "a", "g")
