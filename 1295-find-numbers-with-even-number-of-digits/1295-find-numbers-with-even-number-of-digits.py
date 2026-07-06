class Solution(object):
    def findNumbers(self, nums):

        # Stores the number of integers
        # having an even number of digits.
        evenCount = 0

        # Traverse every number in the array.
        for i in nums:

            # Counts the digits of the current number.
            count = 0

            # Count digits by repeatedly removing
            # the last digit.
            while i > 0:

                # Extract the last digit.
                digit = i % 10

                # Increase the digit count.
                count += 1

                # Remove the last digit.
                i = i // 10

            # If the digit count is even,
            # increase the answer.
            if count % 2 == 0:
                evenCount += 1

        # Return the number of integers
        # having an even number of digits.
        return evenCount
