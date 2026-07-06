# LeetCode 1480 - Running Sum of 1D Array

## Problem

Given an integer array `nums`, return the running sum of the array.

The running sum at index `i` is the sum of all elements from index `0` to index `i`.

Formula:

runningSum[i] = nums[0] + nums[1] + ... + nums[i]

---

## Pattern Used

- Single Traversal
- Running Sum (Prefix Sum)

---

## Algorithm

1. Create an empty array `new` to store the running sums.
2. Create a variable `running` and initialize it to `0`.
3. Traverse the array.
4. Add the current element to `running`.
5. Append the updated `running` value to the new array.
6. After the traversal is complete, return the new array.

---

## Dry Run

Input:

nums = [1,2,3,4]

Initially

running = 0

new = []

---

Read 1

running = 1

new = [1]

---

Read 2

running = 3

new = [1,3]

---

Read 3

running = 6

new = [1,3,6]

---

Read 4

running = 10

new = [1,3,6,10]

Return

[1,3,6,10]

---

## Time Complexity

O(n)

The array is traversed only once.

---

## Space Complexity

O(n)

A new array is created to store the running sums.

---

## Key Learning

- Running sum keeps a cumulative total while traversing the array.
- Instead of calculating the sum from the beginning every time, reuse the previous sum.
- This is one of the simplest applications of the Prefix Sum pattern.
