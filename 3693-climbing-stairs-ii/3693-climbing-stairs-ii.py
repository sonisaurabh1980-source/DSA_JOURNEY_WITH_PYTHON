class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        # dp[i] represents the minimum cost to reach step i
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # Starting at step 0 with cost 0
        
        for i in range(n):
            if dp[i] == float('inf'):
                continue
            # You can jump to i + 1, i + 2, or i + 3
            for j in range(i + 1, min(i + 4, n + 1)):
                # Cost from i to j: destination cost + (j - i)^2
                cost = dp[i] + costs[j - 1] + (j - i) ** 2
                if cost < dp[j]:
                    dp[j] = cost
                    
        return dp[n]
