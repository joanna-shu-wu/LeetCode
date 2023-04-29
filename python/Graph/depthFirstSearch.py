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


def depthFirstSearchIterative(graph, source_node):
    stack=[source_node]
   # stack=graph[source]
    while len(stack)>0:
        current=stack.pop()
        print(current) #processing the node after it leaves the stack

        for neighbor in graph[current]: 
            stack.append(neighbor) #push the neighbor on top of the stack

def depthFirstSearchRecursive(graph, source_node):
    print(source_node)
    for neighbor in graph[source_node]:
        depthFirstSearchRecursive(graph,neighbor)

def main():
    graph={
        'a':['b','c'],
        'b':['d'],
        'c':['e'],
        'd':['f'],
        'e':[],
        'f':[]
    }

   # print(depthFirstSearchIterative(graph,'a')) #acebdf
    print(depthFirstSearchRecursive(graph,'a')) #acebdf



if __name__=='__main__':
    main()