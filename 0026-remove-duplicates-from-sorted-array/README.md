# LeetCode 26 - Remove Duplicates from Sorted Array

## Problem

Given a sorted array `nums`, remove the duplicates **in-place** such that each unique element appears only once.

Return the number of unique elements (`k`).

The first `k` elements of the array should contain all unique elements in sorted order.

---

## Pattern Used

- Two Pointers
- Single Traversal

---

## Algorithm

1. If the array is empty, return `0`.
2. Assume the first element is unique.
3. Create a pointer `res = 1`.
4. Traverse the array from the second element.
5. Compare the current element with the previous element.
6. If they are different:
   - Place the current element at index `res`.
   - Increment `res`.
7. After the traversal, return `res`.

---

## Dry Run

Input:

nums = [1,1,2]

Initially

res = 1

i = 1

nums[1] == nums[0]

Duplicate

Do nothing.

Array:

[1,1,2]

---

i = 2

nums[2] != nums[1]

Unique element found.

Place it at index res.

nums[1] = 2

Array becomes

[1,2,2]

Increase

res = 2

Traversal complete.

Return

2

First two elements are

[1,2]

---

## Time Complexity

O(n)

The array is traversed only once.

---

## Space Complexity

O(1)

No extra array is created.

<ul>
	<li><code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>-100 &lt;= nums[i] &lt;= 100</code></li>
	<li><code>nums</code> is sorted in <strong>non-decreasing</strong> order.</li>
</ul>
