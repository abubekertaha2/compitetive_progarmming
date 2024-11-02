class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_coordinates = sorted(set(x for x, y in points))
        max_width = 0
        for i in range(1, len(x_coordinates)):
            width = x_coordinates[i] - x_coordinates[i - 1]
            max_width = max(max_width, width)
        return max_width
