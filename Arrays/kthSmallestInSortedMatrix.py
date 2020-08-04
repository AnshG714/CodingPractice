import heapq


def kthSmallestElementInMatrix(matrix: [[int]], k: int):
    """
    Given a n x n matrix where each of the rows and columns are sorted in 
    ascending order, find the kth smallest element in the matrix.

    Note that it is the kth smallest element in the sorted order, not the kth 
    distinct element.

    The obvious solution is to add all elements to a heap, and pick pop until 
    we get the kth smallest element. This will take O(nlog n) time, with n = #elements.

    O(klog k) algorithm: 

    First, add the top left (smallest) element to a minheap. Also note that we
    have visited (0, 0). Next, the next 2 smallest elements will be to the left
    and to the bottom. Add those two to the minheap, and add their matrix position
    to a HashSet. We get the next two elements by popping an element from the 
    minheap and using that to find which two elements to add. We whenever we pop 
    the i-th element from the min heap, we access the i-th smallest element
    """

    heap = []
    seen = set()
    count = 0
    n = len(matrix)

    heap.append((matrix[0][0], (0, 0)))
    seen.add((0, 0))

    while True:

        value, indices = heapq.heappop(heap)
        count += 1

        if count == k:
            return value

        row, col = indices

        if row < n - 1 and (row + 1, col) not in seen:
            heapq.heappush((matrix[row + 1][col], (row + 1, col)))
            seen.add((row + 1, col))

        if col < n - 1 and (row, col + 1) not in seen:
            heapq.heappush((matrix[row][col + 1], (row, col + 1)))
            seen.add((row, col + 1))
