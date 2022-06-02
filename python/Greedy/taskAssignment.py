'''
k: # of workers
tasks: durations of tasks that must be completed by the workers 
Each worker must complete 2 tasks and can only work on one at a time 
The number of tasks is always 2k so that each worker always has exactly 2 tasks to complete 

Write a function that returns the optimal assignment of tasks to each worker such that the tasks are completed as fast as possible
'''

def taskAssignment(k, tasks):
    pairedTasks=[]
    taskDurationIdx=getTaskDurationIdx(tasks)

    sortedTasks=sorted(tasks)

    for idx in range(k):
        task1Duration=sortedTasks[idx]
        idxWithTask1Duration=taskDurationIdx[task1Duration]
        task1Idx=idxWithTask1Duration.pop()

        tasks2SortedIdx=len(tasks)-1-idx
        task2Duration=sortedTasks[tasks2SortedIdx]
        idxWithTask2Duration=taskDurationIdx[task2Duration]
        task2Idx=idxWithTask2Duration.pop()

        pairedTasks.append([task1Idx,task2Idx])
        
    return pairedTasks

def getTaskDurationIdx(tasks):
    taskDurationIdx={}

    for idx,taskDuration in enumerate(tasks):
        if taskDuration in taskDurationIdx:
            taskDurationIdx[taskDuration].append(idx)
        else:
            taskDurationIdx[taskDuration]=[idx]
    return taskDurationIdx