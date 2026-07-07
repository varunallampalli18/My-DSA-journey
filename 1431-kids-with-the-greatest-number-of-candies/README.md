# LeetCode 1431 - Kids With the Greatest Number of Candies

## Problem

There are `n` kids, and each kid has a certain number of candies.

You are given:
- An array `candies`, where `candies[i]` is the number of candies the `iᵗʰ` kid has.
- An integer `extraCandies`.

For each kid, determine whether giving **all** the extra candies to that kid would make them have the greatest number of candies among all kids.

Return a boolean array where:
- `True` → The kid can have the greatest number of candies.
- `False` → The kid cannot have the greatest number of candies.

---

## Pattern Used

- Single Traversal
- Maximum Element
- Comparison

---

## Algorithm

### Phase 1: Find the Maximum Number of Candies

1. Create a variable `largest`.
2. Traverse the `candies` array.
3. Update `largest` whenever a greater value is found.

---

### Phase 2: Check Every Kid

1. Create an empty boolean array `result`.
2. Traverse the array again.
3. For every kid:
   - Calculate

     current = candies[i] + extraCandies

   - If

     current >= largest

     append `True`.

   - Otherwise append `False`.

4. Return the `result` array.

---

## Dry Run

Input

candies = [2,3,5,1,3]

extraCandies = 3

Largest = 5

---

Kid 1

2 + 3 = 5

5 >= 5

Append

True

---

Kid 2

3 + 3 = 6

6 >= 5

Append

True

---

Kid 3

5 + 3 = 8

8 >= 5

Append

True

---

Kid 4

1 + 3 = 4

4 >= 5

Append

False

---

Kid 5

3 + 3 = 6

6 >= 5

Append

True

Return

[True, True, True, False, True]

---

## Time Complexity

O(n)

- First traversal finds the largest value.
- Second traversal checks every kid.

Overall:

O(2n) = O(n)

---

## Space Complexity

O(n)

A new boolean array is created to store the answer.

---

## Key Learning

- Sometimes solving a problem is easier by breaking it into two phases:
  1. Collect information (find the maximum).
  2. Use that information to solve the problem.
- A temporary variable (`current`) lets us calculate a value without modifying the original array.
- Return a result only after processing every element.
