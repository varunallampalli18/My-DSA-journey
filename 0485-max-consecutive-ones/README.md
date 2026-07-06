# LeetCode 485 - Max Consecutive Ones

## Problem

Given a binary array `nums`, return the maximum number of consecutive `1`s in the array.

---

## Pattern Used

- Single Traversal
- Counting
- Running Maximum

---

## Algorithm

1. Create two variables:
   - `current` → stores the current streak of consecutive `1`s.
   - `highest` → stores the longest streak found so far.
2. Traverse the array.
3. If the current element is `1`:
   - Increase `current` by `1`.
   - If `current` is greater than `highest`, update `highest`.
4. If the current element is `0`:
   - Reset `current` to `0`.
5. Return `highest`.

---

## Dry Run

Input:

nums = [1,1,0,1,1,1]

Initially

current = 0

highest = 0

---

Read 1

current = 1

highest = 1

---

Read 1

current = 2

highest = 2

---

Read 0

current = 0

highest = 2

---

Read 1

current = 1

highest = 2

---

Read 1

current = 2

highest = 2

---

Read 1

current = 3

highest = 3

Return

3

---

## Time Complexity

O(n)

The array is traversed only once.

---

## Space Complexity

O(1)

Only two variables are used.
