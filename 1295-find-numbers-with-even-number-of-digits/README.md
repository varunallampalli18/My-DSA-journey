# LeetCode 1295 - Find Numbers with Even Number of Digits

## Problem

Given an integer array `nums`, return how many numbers contain an even number of digits.

---

## Pattern Used

- Single Traversal
- Digit Counting
- Mathematical Operations

---

## Algorithm

1. Create a variable `evenCount` to store the number of integers having an even number of digits.
2. Traverse the array one element at a time.
3. For each number:
   - Create a variable `count` to count its digits.
   - Repeatedly divide the number by `10` until it becomes `0`.
   - Increase `count` after removing each digit.
4. After counting the digits:
   - If `count` is even (`count % 2 == 0`), increment `evenCount`.
5. Return `evenCount`.

---

## Dry Run

Input:

nums = [12,345,2,6,7896]

Initially

evenCount = 0

---

Number = 12

12 → 1 → 0

Digits = 2

2 is even

evenCount = 1

---

Number = 345

345 → 34 → 3 → 0

Digits = 3

Odd

evenCount = 1

---

Number = 2

2 → 0

Digits = 1

Odd

evenCount = 1

---

Number = 6

6 → 0

Digits = 1

Odd

evenCount = 1

---

Number = 7896

7896 → 789 → 78 → 7 → 0

Digits = 4

Even

evenCount = 2

Return

2

---

## Time Complexity

O(n × d)

where

- n = number of elements
- d = number of digits in each number

Since the maximum value is 10⁵, d is at most 6.

Practically, the solution behaves like O(n).

---

## Space Complexity

O(1)

Only two extra variables are used.

---

## Key Learning

- A number can be processed digit by digit using:
  - Modulus (`% 10`) to get the last digit.
  - Integer division (`// 10`) to remove the last digit.
- Nested loops do not always mean O(n²). Here, the inner loop depends only on the number of digits, not on the array size.
