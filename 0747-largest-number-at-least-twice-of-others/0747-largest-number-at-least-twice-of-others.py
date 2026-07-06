class Solution(object):
    def dominantIndex(self, nums):

        # Stores the largest value found so far.
        largest = float('-inf')

        # Stores the index of the largest value.
        largestIndex = 0

        # ----------------------------
        # First Traversal
        # Find the largest element and its index.
        # ----------------------------
        for i in range(len(nums)):
            if nums[i] > largest:
                largest = nums[i]
                largestIndex = i

        # ----------------------------
        # Second Traversal
        # Verify whether the largest element
        # is at least twice every other element.
        # ----------------------------
        for i in range(len(nums)):

            # Skip the largest element itself.
            if i == largestIndex:
                continue

            # If any element violates the condition,
            # immediately return -1.
            if largest < 2 * nums[i]:
                return -1

        # All elements satisfied the condition.
        return largestIndex
