# LeetCode 747 - Largest Number At Least Twice of Others

## Problem

Given an integer array `nums` where the largest element is unique, determine whether the largest element is at least twice as large as every other element.

- If the condition is true, return the index of the largest element.
- Otherwise, return `-1`.

---

## Pattern Used

- Single Traversal
- Maximum Element
- Verification

---

## Algorithm

### Phase 1: Find the Largest Element

1. Create two variables:
   - `largest` → stores the largest value.
   - `largestIndex` → stores the index of the largest value.
2. Traverse the array.
3. If the current element is greater than `largest`:
   - Update `largest`.
   - Update `largestIndex`.

---

### Phase 2: Verify the Condition

1. Traverse the array again.
2. Skip the largest element itself.
3. Check whether:

largest >= 2 × current element

4. If the condition fails for any element:
   - Return `-1`.
5. If the loop finishes successfully:
   - Return `largestIndex`.

---

## Dry Run

Input:

nums = [3,6,1,0]

### First Traversal

largest = 6

largestIndex = 1

---

### Second Traversal

Current = 3

6 >= 2 × 3

6 >= 6

True

---

Current = 6

Skip

---

Current = 1

6 >= 2 × 1

6 >= 2

True

---

Current = 0

6 >= 2 × 0

6 >= 0

True

All comparisons passed.

Return

1

---

## Another Example

Input:

nums = [1,2,3,4]

Largest = 4

Check:

4 >= 2 × 1 ✔

4 >= 2 × 2 ✔

4 >= 2 × 3 ✘

Return

-1

---

## Time Complexity

O(n)

- First traversal finds the largest element.
- Second traversal verifies the condition.

Overall:

O(2n) = O(n)

---

## Space Complexity

O(1)

Only two extra variables are used.

---

## Key Learning

- Use one traversal to collect information.
- Use another traversal to verify a condition.
- Use `continue` to skip unnecessary comparisons.
- Use **early return** when a condition fails.
