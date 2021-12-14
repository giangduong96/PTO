# V0

# V1 
# http://bookshadow.com/weblog/2015/12/27/leetcode-coin-change/
# IDEA : DP
# DP state equation :  dp[x + c] = min(dp[x] + 1, dp[x + c])
import collections
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0] + [-1] * amount
        print("dp", dp)
        for x in range(amount):
            if dp[x] < 0:
                continue
            for c in coins:
                if x + c > amount:
                    continue
                if dp[x + c] < 0 or dp[x + c] > dp[x] + 1:
                    dp[x + c] = dp[x] + 1
        return dp[amount]

### Test case : dev 

# V1'
# http://bookshadow.com/weblog/2015/12/27/leetcode-coin-change/
# IDEA : BFS 
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        steps = collections.defaultdict(int)
        queue = collections.deque([0])
        steps[0] = 0
        while queue:
            front = queue.popleft()
            level = steps[front]
            if front == amount:
                return level
            for c in coins:
                if front + c > amount:
                    continue
                if front + c not in steps:
                    queue += front + c,
                    steps[front + c] = level + 1
        return -1

# V1''
# https://leetcode.com/problems/coin-change/solution/
# IDEA : DP
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1 

# V1'''
# https://leetcode.com/problems/coin-change/discuss/114993/Four-kinds-of-solutions%3A-DP-BFS-DFS-improved-DFS
# IDEA : DP
class Solution:
    def coinChange(self, coins, amount):
        M = float('inf')        
        # dynamic programming
        dp = [0] + [M] * amount
        for i in range(1, amount+1):
            dp[i] = 1 + min([dp[i-c] for c in coins if i >= c] or [M])
        return dp[-1] if dp[-1] < M else -1


# V1''''
# https://leetcode.com/problems/coin-change/discuss/114993/Four-kinds-of-solutions%3A-DP-BFS-DFS-improved-DFS
# IDEA : BFS
class Solution:
    def coinChange(self, coins, amount):    
        # BFS, graph search. Keep records of visited nodes
        visited = [True] + [False] * amount
        
        par = [0]  # parents
        child = []  # children
        step = 0
        while par:
            step += 1
            for p in par:
                for c in coins:
                    tmp = p + c
                    if tmp == amount:
                        return step
                    elif tmp < amount and not visited[tmp]:
                        visited[tmp] = True
                        child.append(tmp)
            par, child = child, []
        
        return -1 if amount else 0

# V1'''''
# https://leetcode.com/problems/coin-change/discuss/114993/Four-kinds-of-solutions%3A-DP-BFS-DFS-improved-DFS
# IDDA : DFS
class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        
        coins.sort(reverse=True)
        if amount < coins[-1]:
            return -1
        
        l = len(coins)
        self.cur = float('inf')
        # current answer(the worst case)
        def dfs(ptr, rem, count):
            '''ptr is the pointer to current index in coins,
               rem denotes remainder. The money left to be made up.
               count denotes current number of coins used.'''
            if not rem:  # remainder is 0, so one branch of dfs is done.
                self.cur = min(self.cur, count)
            else:
                for i in range(ptr, l):
                    # this following if condition is marvelous!
                    if coins[i] <= rem < coins[i] * (self.cur - count):
                    # coins[i] <= rem gaurantees that 'rem' passed to following dfs will be positive
                    # if coins[i] * (self.cur - count) <= rem, 
                    # then we know we cannot get better results
                    # just suppose coins[i] = 1, self.cur = 3, rem = 5. 
                    # We can see there is no need to do dfs(i, 4, count+1).
                        dfs(i, rem-coins[i], count+1)
            
        for i in range(l):
            dfs(i, amount, 0)
        
        return self.cur if self.cur < float('inf') else -1

# V1''''''
# https://leetcode.com/problems/coin-change/discuss/114993/Four-kinds-of-solutions%3A-DP-BFS-DFS-improved-DFS
# IDEA : DFS
class Solution:
    def coinChange(self, coins, amount):
                """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # improved dfs, use division first
        l = len(coins) - 1
        coins.sort(reverse=True)
        self.ans = float('inf')
        
        def dfs(start, rem, step):
            if start > l:
                return 
            
            div, mod = rem // coins[start], rem % coins[start]
            
            if not mod:
                self.ans = min(self.ans, step + div)
            else:                
                rem, step = mod, step + div                
                dfs(start+1, rem, step)
                
                if start < l:
                    for i in range(div):
                        rem += coins[start]    
                        step -= 1
                        if (self.ans - step) * coins[start+1] > rem:  # hope still exists
                            dfs(start+1, rem, step)
        
        dfs(0, amount, 0)
        return self.ans if self.ans < float('inf') else -1

# V1'''''''
# https://leetcode.com/problems/coin-change/discuss/77416/Python-11-line-280ms-DFS-with-early-termination-99-up
# IDEA : DFS
class Solution(object):
    def coinChange(self, coins, amount):
        coins.sort(reverse = True)
        lenc, self.res = len(coins), 2**31-1
    
        def dfs(pt, rem, count):
            if not rem:
                self.res = min(self.res, count)
            for i in range(pt, lenc):
                if coins[i] <= rem < coins[i] * (self.res-count): # if hope still exists
                    dfs(i, rem-coins[i], count+1)

        for i in range(lenc):
            dfs(i, amount, 0)
    return self.res if self.res < 2**31-1 else -1

# V2 
# Time:  O(n * k), n is the number of coins, k is the amount of money
# Space: O(k)
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        INF = 0x7fffffff  # Using float("inf") would be slower.
        amounts = [INF] * (amount + 1)
        amounts[0] = 0
        for i in range(amount + 1):
            if amounts[i] != INF:
                for coin in coins:
                    if i + coin <= amount:
                        amounts[i + coin] = min(amounts[i + coin], amounts[i] + 1)
        return amounts[amount] if amounts[amount] != INF else -1
