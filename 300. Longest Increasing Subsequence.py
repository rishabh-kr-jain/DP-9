#approach using dp array of 1s and comparing i and j pointer based looping to compare elements
#space: O(n)
#time: O(n*n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n= len(nums)
        dp=[1]* n
        mx=1
        for i in range(n):
            for j in range(i):
                if nums[i]> nums[j]:
                    dp[i]=max(dp[i], dp[j]+1)
            mx= max(mx,dp[i])
        
        return mx
