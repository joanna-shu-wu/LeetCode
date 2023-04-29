# a    ->    c
# |          |
# v          v
# b          e
# |          
# v  
# d   ->   f
#
#
# return acebdf


def breadthFirstSearchIterative(graph, source_node):
    queue=[source_node]
   # stack=graph[source]
    while len(queue)>0:
        current=queue.pop(0)
        print(current)
        for neigbhor in graph[current]:
            queue.append(neigbhor)

def depthFirstSearchRecursive(graph, source_node):
    print(source_node)
    for neighbor in graph[source_node]:
        depthFirstSearchRecursive(graph,neighbor)

def main():
    graph={
        'a':['c','b'],
        'b':['d'],
        'c':['e'],
        'd':['f'],
        'e':[],
        'f':[]
    }

    print(breadthFirstSearchIterative(graph,'a')) #acebdf
    #print(depthFirstSearchRecursive(graph,'a')) #acebdf



if __name__=='__main__':
    main()