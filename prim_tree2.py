from collections import defaultdict
from heapq import *
 
def prim( nodes, edges ):
    connection = defaultdict( list )
    for n1,n2,c in edges:
        connection[ n1 ].append( (c, n1, n2) )
        connection[ n2 ].append( (c, n2, n1) )
 
    mst = []
    used = set( nodes[ 0 ] )
    usable_edges = connection[ nodes[0] ][:]
    heapify( usable_edges )
 
    while usable_edges:
        cost, n1, n2 = heappop( usable_edges )
        if n2 not in used:
            used.add( n2 )
            mst.append( ( n1, n2, cost ) )
 
            for e in connection[ n2 ]:
                if e[ 2 ] not in used:
                    heappush( usable_edges, e )
    return mst
 
#test
nodes = list("123456789")
edges = [ ("1", "2", 2), ("2", "3", 2),
          ("1", "3", 2), ("1", "3", 2), ("1", "9", 7),
      ("9", "4", 2),
      ("3", "4", 1), ("2", "5", 3),
      ("5", "3", 3), ("3", "6", 4),
      ("5", "6", 4),("5","7",5),("6","8", 6),("7","8", 1)]
 
print "prim:", prim( nodes, edges )
#output
#prim: [('A', 'D', 5), ('D', 'F', 6), ('A', 'B', 7), ('B', 'E', 7), ('E', 'C', 5), ('E', 'G', 9)]