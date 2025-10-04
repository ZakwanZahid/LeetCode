
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):  # Iterate using indices
            for j in range(i + 1, len(nums)):
                ans = nums[i] + nums[j]
                if ans == target:
                    return [i, j]
        return []  # Return an empty list if no solution is found

# Main function to call the solution
if _name_ == "_main_":
    nums = [11, 15, 2, 7]
    target = 9
    solution = Solution()  # Create an instance of the Solution class
    result = solution.twoSum(nums, target)  # Call the twoSum method
    print("Indices:", result)  # Output the result