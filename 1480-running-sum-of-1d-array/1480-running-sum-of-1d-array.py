class Solution(object):
    def runningSum(self, nums):

        # Stores the running sums.
        new = []

        # Stores the cumulative sum.
        running = 0

        # Traverse every element in the array.
        for i in nums:

            # Add the current element to the running total.
            running += i

            # Store the current running sum.
            new.append(running)

        # Return the running sum array.
        return new
