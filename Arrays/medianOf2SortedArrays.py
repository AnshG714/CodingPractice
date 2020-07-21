# Very important to review!!
import math


def median(arr1, arr2):
    m = len(arr1)
    n = len(arr2)

    # Make sure arr1 is shorter
    if m > n:
        arr1, arr2 = arr2, arr1
        m, n = min(m, n), max(m, n)

    # Get the halfway splitting point
    if (m + n) % 2 == 0:
        split = (m + n) // 2
    else:
        split = (m + n + 1) // 2

    start = 0
    end = m  # Initialized to m because if this is the breakpoint then we find median
    # purely from second array

    while start <= end:
        # Get splitting point in array 1. THe index at this point signifies the start of the second half
        arr1_mid = (start + end) // 2

        # Get the required split point in the second array
        arr2_mid = split - arr1_mid

        # Get the last elements from the first half from each array
        arr1_firsthalf_last = arr1[arr1_mid -
                                   1] if arr1_mid > 0 else -math.inf
        arr2_firsthalf_last = arr2[arr2_mid -
                                   1] if arr2_mid > 0 else -math.inf

        # Get the first elements from the second half from each array
        arr1_secondhalf_first = arr1[arr1_mid] if arr1_mid < m else math.inf
        arr2_secondhalf_first = arr2[arr2_mid] if arr2_mid < m else math.inf

        # Check for ending condition
        if (arr1_firsthalf_last < arr2_secondhalf_first) and (arr2_firsthalf_last < arr1_secondhalf_first):
            if (m + n) % 2 == 0:
                return 0.5 * (max(arr1_firsthalf_last, arr2_firsthalf_last) +
                              min(arr1_secondhalf_first, arr2_secondhalf_first))
            else:
                return max(arr1_firsthalf_last, arr2_firsthalf_last)

        # Binary search
        if arr1_firsthalf_last > arr2_secondhalf_first:
            end = arr1_mid - 1
        else:
            start = arr1_mid + 1
