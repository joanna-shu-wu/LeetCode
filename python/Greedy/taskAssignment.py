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

    sortedTasks=sorted(tasks) #pair the shortest task with the longest task

    for idx in range(k): #2 tasks per worker. So loop through all the worker. 
        task1Duration=sortedTasks[idx] #the shorter task's duration
        idxWithTask1Duration=taskDurationIdx[task1Duration] #use the task duration to grab the list of idx in the dict
        task1Idx=idxWithTask1Duration.pop()#remove the idx at the end of the list

        tasks2SortedIdx=len(tasks)-1-idx #the longer task's duration
        task2Duration=sortedTasks[tasks2SortedIdx]
        idxWithTask2Duration=taskDurationIdx[task2Duration]
        task2Idx=idxWithTask2Duration.pop()

        pairedTasks.append([task1Idx,task2Idx])
        
    return pairedTasks

def getTaskDurationIdx(tasks):
    taskDurationIdx={} #use dict because some tasks takes the same duration. So the key is the task duration, the value is the list of idx

    for idx,taskDuration in enumerate(tasks):
        if taskDuration in taskDurationIdx:
            taskDurationIdx[taskDuration].append(idx)
        else:
            taskDurationIdx[taskDuration]=[idx]
    return taskDurationIdx