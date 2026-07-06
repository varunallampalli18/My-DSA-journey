class Solution:
    def removeDuplicates(self, nums):

        # If the array is empty, there are no unique elements.
        if not nums:
            return 0

        # res points to the position where the next unique element
        # should be placed.
        # The first element is always unique.
        res = 1

        # Start from the second element.
        for i in range(1, len(nums)):

            # Compare the current element with the previous element.
            # If they are different, we found a new unique value.
            if nums[i] != nums[i - 1]:

                # Place the unique element at the next available position.
                nums[res] = nums[i]

                # Move the pointer to the next position.
                res += 1

        # res is the number of unique elements.
        return res
