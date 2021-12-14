# https://leetcode.com/problems/design-authentication-manager/

# time O(1), space O(n)
from collections import OrderedDict


class TTL():
    def __init__(self, TTL):
        self.expire = OrderedDict()
        self.life = TTL

    def removeIfExpire(self, currentTime):
        # remove all expire value
        while self.expire and next(iter(self.expire.values())) <= currentTime:
            self.expire.pop(0)

    def generate(self, str, currentTime):
        # remove all expire value
        self.removeIfExpire(currentTime)
        self.expire[str] = self.life + currentTime

    def renew(self, str, currentTime):
        self.removeIfExpire(currentTime)
        if str in self.expire:
            self.expire.move_to_end(str)  # move it to the end
            self.expire[str] = self.life + currentTime

    def countUnexpire(self, currentTime):
        self.removeIfExpire(currentTime)
        return len(self.expire)


class googleExamTTL():
    def __init__(self):
        self.expire = OrderedDict()

    def removeExpire(self, currentTime):
        m = sorted(self.expire.items(), key=lambda item:item[1])
        self.expire.clear()
        self.expire.update(m)
        while self.expire and next(iter(self.expire.values())) < currentTime:
            self.expire.popitem(last=0)

    def putFunction(self, keys, currentTime):
        # if keys in already in expire

        sorted(self.expire.values())
        if keys in self.expire.keys():
            # self.expire.move_to_end(keys)
            self.expire[keys] = self.expire[keys] + currentTime
        else:
            # key is tuple : (key, value)
            self.expire[keys] = currentTime

    def getFunction(self, key, currentTime):
        self.removeExpire(currentTime)
        # nothing to return
        if not self.expire:
            return -1
        return key

    def print(self):
        print(self.expire)


c = googleExamTTL()
c.putFunction((10, 5), 5)
c.putFunction((10, 5), 7)
c.putFunction((10, 4), 3)
c.putFunction((5, 2), 20)
c.print()

print(c.getFunction((10, 5), 14))

c.print()
