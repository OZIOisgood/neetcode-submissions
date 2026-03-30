"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

START = 1
END   = -1

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = []

        for interval in intervals:
            heapq.heappush(events, (interval.start, START))
            heapq.heappush(events, (interval.end,   END))
        
        min_rooms = 0
        cur_rooms = 0
        while events:
            _, event = heapq.heappop(events)
            if event == START: cur_rooms += 1
            elif event == END: cur_rooms -= 1
            min_rooms = max(min_rooms, cur_rooms)
        
        return min_rooms