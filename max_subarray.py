#kadane's algorithm: O(n) time algorithm(Dynammic programming)

from sys import maxint

def max_subarray_sequence(a, max, index):
    val = max
    seq_list = list()
    while(val != 0):
        seq_list.append(a[index])
        temp = a[index]
        val = val - temp
        index = index -1
    return seq_list

def max_subarray(a):
    Max = 0
    currentMax =0
    for i in a:
        currentMax = max(0, currentMax+i)
        Max = max(Max, currentMax)
        if Max == currentMax:
            index = a.index(i)
    listseq = max_subarray_sequence(a, Max, index)
    return (Max, listseq)


a = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

print max_subarray(a)