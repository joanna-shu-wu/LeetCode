# O(n^2) time | O(1) space
def bubbleSort(array):
    isSorted = False
    counter = 0  # Tracks number of sorted elements

    while not isSorted:
        isSorted = True  # Assume sorted unless a swap happens
        for i in range(len(array) - 1 - counter):  # Reduce comparisons each pass
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]  # Swap elements
                isSorted = False  # A swap happened, keep sorting
        counter += 1  # Reduce range for next pass (last elements are sorted)

    return array
