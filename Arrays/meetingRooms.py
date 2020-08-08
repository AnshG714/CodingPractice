import math
import heapq


def meetingRooms(meetings: [[int]]):
    """
    Given an array of meeting time intervals consisting of start and end times 
    [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

    For example,
    Given [[0, 30],[5, 10],[15, 20]],
    return false.
    """

    meetings.sort(key=lambda x: x[0])

    for i in range(1, len(meetings)):
        if meetings[i][0] < meetings[i - 1][1]:
            return False

    return True


def overlap(interval1, interval2):
    if interval1[0] > interval2[0]:
        interval1, interval2 = interval2, interval1

    return interval2[0] < interval1[1]


def meetingRoomsII(meetings: [[int]]):
    """
    Given an array of meeting time intervals consisting of start and end times 
    [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms 
    required.

    For example,
    Given [[0, 30],[5, 10],[15, 20]],
    return 2.
    """
    mins = []
    meetingRooms = 1
    meetings.sort(key=lambda x: x[0])

    for interval in meetings:
        while mins and interval[0] >= mins[0]:
            heapq.heappop(mins)

        heapq.heappush(mins, interval[1])
        meetingRooms = max(meetingRooms, len(mins))

    return meetingRooms
