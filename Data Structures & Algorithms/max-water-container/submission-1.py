class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        hmax = max(heights)
        left,right = 0,n-1
        maxwater = 0

        while left < right:
            water = min(heights[left],heights[right]) * (right - left)
            maxwater = max(water,maxwater)
            if maxwater > hmax *(right - left):
                break
            if heights[left] > heights[right]:
                prev = heights[right]
                right -= 1
                while left<right and prev >= heights[right]:
                    right-=1
            else:
                prev = heights[left]
                left += 1
                while left<right and prev >= heights[left]:
                    left += 1

        return maxwater