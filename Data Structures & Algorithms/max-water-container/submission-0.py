class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        n = len(heights)

        left,right = 0,n-1
        maxwater = 0

        while left < right:
            water = min(heights[left],heights[right]) * (right - left)
            maxwater = max(water,maxwater)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return maxwater