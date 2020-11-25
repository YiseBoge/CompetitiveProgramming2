#!/bin/python3

import heapq
import os


#
# Complete the cookies function below.
#
def cookies(k, A):
    if len(A) == 1:
        return -1 if A[0] < k else 0

    heap = []
    for sweet in A:
        heapq.heappush(heap, sweet)

    result = 0
    while heap[0] < k:
        if len(heap) < 2:
            return -1
        item_1 = heapq.heappop(heap)
        item_2 = heapq.heappop(heap)
        heapq.heappush(heap, item_1 + 2 * item_2)
        result += 1

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
