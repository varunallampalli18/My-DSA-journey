class Solution(object):
    def findMaxConsecutiveOnes(self, nums):

        # Stores the current streak of consecutive 1's.
        current = 0

        # Stores the maximum streak found so far.
        highest = 0

        # Traverse every element in the array.
        for i in nums:

            # If the current element is 1,
            # increase the current streak.
            if i == 1:
                current += 1

                # Update the maximum streak if needed.
                if current > highest:
                    highest = current

            # If the current element is 0,
            # the streak is broken.
            else:
                current = 0

        # Return the longest consecutive streak.
        return highest
        
