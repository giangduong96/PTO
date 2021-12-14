"""
https://leetcode.com/problems/design-hit-counter/
1 <= timestamp <= 2 * 109
All the calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing).
At most 300 calls will be made to hit and getHits.
"""


class HitCounter:
    def __init__(self):
        self.current_timestamp = 0
        self.hit_cnt = {}

    def update_timestamp(self, timestamp):
        if timestamp > self.current_timestamp:
            self.current_timestamp = timestamp
            for key in list(self.hit_cnt.keys()):
                if key <= (self.current_timestamp - 300):
                    del (self.hit_cnt[key])
            self.hit_cnt[timestamp] = 0

    def hit(self, timestamp: int) -> None:
        self.update_timestamp(timestamp)
        self.hit_cnt[timestamp] += 1

    def getHits(self, timestamp: int) -> int:
        self.update_timestamp(timestamp)
        return sum(self.hit_cnt.values())
