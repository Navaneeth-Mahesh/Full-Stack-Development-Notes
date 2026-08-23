# 10. Subarrays

Subarrays are one of the **most important concepts in Array DSA** because many problems involving sums, maximum/minimum values, frequencies, prefix sums, and sliding windows are based on them.

A strong understanding of subarrays will help you solve problems using:

* Brute Force
* Prefix Sum
* Sliding Window
* HashMap
* Kadane's Algorithm
* Two Pointers
* Dynamic Programming

---

## 1. What is a Subarray?

A **subarray** is a contiguous part of an array.

### Example

Consider:

```text
arr = [1, 2, 3, 4]
```

Some valid subarrays are:

```text
[1]
[2]
[3]
[4]

[1, 2]
[2, 3]
[3, 4]

[1, 2, 3]
[2, 3, 4]

[1, 2, 3, 4]
```

Every element in a subarray must be **next to each other** in the original array.

### Important

```text
[1, 2, 3]
```

is a subarray.

But:

```text
[1, 3]
```

is **not** a subarray because `2` was skipped.

---

## Subarray vs Subsequence vs Subset

These concepts are commonly confused.

### Subarray

Elements must be contiguous.

```text
[1, 2, 3, 4]

[2, 3]     → Subarray
```

### Subsequence

Elements must maintain their original order, but they don't need to be contiguous.

```text
[1, 2, 3, 4]

[1, 3, 4]  → Subsequence
```

### Subset

Order and contiguity do not matter.

```text
[1, 2, 3, 4]

[4, 1]     → Subset
```

### Quick Rule

```text
Subarray    → Contiguous
Subsequence → Same order, not necessarily contiguous
Subset      → Anything
```

---

# 2. Subarray Representation

A subarray can be represented using two indexes:

```text
start
end
```

For:

```text
arr = [10, 20, 30, 40, 50]
```

Suppose:

```text
start = 1
end = 3
```

Then the subarray is:

```text
[20, 30, 40]
```

We can write:

```text
arr[start...end]
```

or:

```text
arr[1...3]
```

---

# 3. Subarray Generation

One of the first things you should learn is how to generate **all possible subarrays**.

There are two common approaches.

---

## Approach 1: Three Loops

We choose:

1. Starting index
2. Ending index
3. Print elements between them

### Example

```text
arr = [1, 2, 3]
```

Possible subarrays:

```text
[1]
[1, 2]
[1, 2, 3]

[2]
[2, 3]

[3]
```

### Java

```java
public class Main {
    public static void main(String[] args) {

        int[] arr = {1, 2, 3};

        for (int start = 0; start < arr.length; start++) {

            for (int end = start; end < arr.length; end++) {

                for (int i = start; i <= end; i++) {
                    System.out.print(arr[i] + " ");
                }

                System.out.println();
            }
        }
    }
}
```

### Output

```text
1
1 2
1 2 3
2
2 3
3
```

### Complexity

There are three loops:

```text
Time: O(n³)
Space: O(1)
```

This approach is useful for learning but is usually too slow for large arrays.

---

# 4. Number of Subarrays

For an array containing `n` elements, the total number of non-empty subarrays is:

```text
n × (n + 1) / 2
```

or:

```text
n(n + 1) / 2
```

---

## Why?

For every starting position, count how many possible ending positions exist.

For:

```text
[1, 2, 3, 4]
```

Starting from index `0`:

```text
[1]
[1,2]
[1,2,3]
[1,2,3,4]

→ 4
```

Starting from index `1`:

```text
[2]
[2,3]
[2,3,4]

→ 3
```

Starting from index `2`:

```text
[3]
[3,4]

→ 2
```

Starting from index `3`:

```text
[4]

→ 1
```

Total:

```text
4 + 3 + 2 + 1 = 10
```

Formula:

```text
4 × 5 / 2 = 10
```

---

## Example

For:

```text
n = 5
```

Number of subarrays:

```text
5 × 6 / 2
= 15
```

For:

```text
n = 100
```

```text
100 × 101 / 2
= 5050
```

### Important

This counts **non-empty** subarrays.

If empty subarray is also considered:

```text
n(n + 1)/2 + 1
```

But most DSA problems consider non-empty subarrays unless stated otherwise.

---

# 5. Maximum Subarray

The **Maximum Subarray Problem** asks:

> Find the contiguous subarray having the maximum possible value according to the problem's objective.

The most common version is:

> Find the contiguous subarray with the maximum sum.

Example:

```text
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
```

The maximum-sum subarray is:

```text
[4, -1, 2, 1]
```

Sum:

```text
4 + (-1) + 2 + 1 = 6
```

Therefore:

```text
Maximum Subarray Sum = 6
```

---

# 6. Minimum Subarray

The opposite problem is finding a contiguous subarray having the **minimum sum**.

Example:

```text
arr = [3, -4, 2, -3, -1, 7]
```

Consider:

```text
[-4, 2, -3, -1]
```

Sum:

```text
-4 + 2 - 3 - 1 = -6
```

So the minimum subarray sum is:

```text
-6
```

This can also be solved using a variation of Kadane's Algorithm.

---

# 7. Maximum Subarray Sum

The problem is:

> Find the largest possible sum among all contiguous subarrays.

Example:

```text
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
```

Possible useful subarrays include:

```text
[4]
[4, -1]
[4, -1, 2]
[4, -1, 2, 1]
```

Their sums:

```text
4
3
5
6
```

Therefore:

```text
Maximum Sum = 6
```

---

## Brute Force Approach

We can calculate the sum of every subarray.

Instead of using three loops, we can maintain a running sum.

```java
public static int maxSubarraySum(int[] arr) {

    int maxSum = Integer.MIN_VALUE;

    for (int start = 0; start < arr.length; start++) {

        int sum = 0;

        for (int end = start; end < arr.length; end++) {

            sum += arr[end];

            maxSum = Math.max(maxSum, sum);
        }
    }

    return maxSum;
}
```

### Complexity

```text
Time: O(n²)
Space: O(1)
```

This is much better than generating every subarray explicitly with three loops.

---

# 8. Kadane's Algorithm

Kadane's Algorithm is one of the **most important array algorithms**.

It solves:

> Maximum Subarray Sum in O(n) time.

Instead of checking every subarray, Kadane's Algorithm makes a decision at every element:

> Should I continue the current subarray or start a new subarray here?

---

## Core Idea

Maintain:

```text
currentSum
maximumSum
```

At every element:

```text
currentSum = max(arr[i], currentSum + arr[i])
```

Then:

```text
maximumSum = max(maximumSum, currentSum)
```

---

## Example

Consider:

```text
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
```

Start:

```text
currentSum = -2
maximumSum = -2
```

Next:

```text
1
```

Choose between:

```text
1
-2 + 1 = -1
```

Take:

```text
1
```

Now:

```text
currentSum = 1
maximumSum = 1
```

Next:

```text
-3
```

Choices:

```text
-3
1 + (-3) = -2
```

Take:

```text
-2
```

Next:

```text
4
```

Choices:

```text
4
-2 + 4 = 2
```

Take:

```text
2
```

Continue:

```text
-1
```

```text
2 + (-1) = 1
```

Then:

```text
2
```

```text
1 + 2 = 3
```

Then:

```text
1
```

```text
3 + 1 = 4
```

Maximum encountered:

```text
6
```

Therefore:

```text
Maximum Subarray Sum = 6
```

---

## Java Implementation

```java
public static int kadane(int[] arr) {

    int currentSum = arr[0];
    int maxSum = arr[0];

    for (int i = 1; i < arr.length; i++) {

        currentSum = Math.max(arr[i], currentSum + arr[i]);

        maxSum = Math.max(maxSum, currentSum);
    }

    return maxSum;
}
```

### Complexity

```text
Time: O(n)
Space: O(1)
```

This is optimal for the standard maximum subarray sum problem because every element must be examined at least once.

---

# 9. Why Kadane's Algorithm Works

Suppose:

```text
currentSum < 0
```

and the next element is:

```text
x
```

We have two choices:

```text
currentSum + x
```

or:

```text
x
```

Since `currentSum` is negative:

```text
x > currentSum + x
```

Therefore, carrying a negative sum forward only makes the result worse.

So we discard the previous subarray and start a new one.

This is the central idea behind Kadane's Algorithm.

---

# 10. Kadane's Algorithm with All Negative Numbers

Consider:

```text
arr = [-5, -2, -8, -1]
```

The answer should be:

```text
-1
```

because:

```text
[-1]
```

has the largest sum.

That's why we should initialize using:

```java
arr[0]
```

rather than:

```java
0
```

Correct:

```java
int currentSum = arr[0];
int maxSum = arr[0];
```

Avoid:

```java
int maxSum = 0;
```

because that would incorrectly return `0` for an array containing only negative values.

---

# 11. Maximum Subarray — Returning the Actual Subarray

Sometimes the problem doesn't ask only for the maximum sum.

It asks:

> Find the maximum-sum subarray.

Then we need to track:

```text
start
end
```

### Java

```java
public static void maxSubarray(int[] arr) {

    int currentSum = arr[0];
    int maxSum = arr[0];

    int start = 0;
    int bestStart = 0;
    int bestEnd = 0;

    for (int i = 1; i < arr.length; i++) {

        if (arr[i] > currentSum + arr[i]) {
            currentSum = arr[i];
            start = i;
        } else {
            currentSum += arr[i];
        }

        if (currentSum > maxSum) {
            maxSum = currentSum;
            bestStart = start;
            bestEnd = i;
        }
    }

    System.out.println("Maximum Sum = " + maxSum);

    System.out.print("Subarray = ");

    for (int i = bestStart; i <= bestEnd; i++) {
        System.out.print(arr[i] + " ");
    }
}
```

For:

```text
[-2, 1, -3, 4, -1, 2, 1, -5, 4]
```

Output:

```text
Maximum Sum = 6
Subarray = 4 -1 2 1
```

---

# 12. Minimum Subarray Sum

We can modify Kadane's Algorithm to find the minimum sum.

Instead of:

```java
Math.max()
```

use:

```java
Math.min()
```

### Java

```java
public static int minSubarraySum(int[] arr) {

    int currentSum = arr[0];
    int minSum = arr[0];

    for (int i = 1; i < arr.length; i++) {

        currentSum = Math.min(arr[i], currentSum + arr[i]);

        minSum = Math.min(minSum, currentSum);
    }

    return minSum;
}
```

### Complexity

```text
Time: O(n)
Space: O(1)
```

---

# 13. Maximum Product Subarray

This problem is similar to Maximum Subarray Sum, but instead of sum we use **product**.

Problem:

> Find the contiguous subarray having the maximum product.

Example:

```text
arr = [2, 3, -2, 4]
```

Possible answer:

```text
[2, 3]
```

Product:

```text
2 × 3 = 6
```

Therefore:

```text
Maximum Product = 6
```

---

## Why Product Is Harder Than Sum

For sums, a negative number generally makes the sum smaller.

But with multiplication:

```text
negative × negative = positive
```

Example:

```text
[-2, 3, -4]
```

Product:

```text
(-2) × 3 × (-4)
= 24
```

So a negative product can become the maximum product later.

Therefore, we need to track **both maximum and minimum products**.

---

## Important Idea

Maintain:

```text
maxProduct
minProduct
```

Why?

Because:

```text
minimum × negative = maximum
```

and:

```text
maximum × negative = minimum
```

---

## Example

Consider:

```text
[2, 3, -2, 4]
```

Initially:

```text
max = 2
min = 2
```

At `3`:

```text
max = max(3, 2 × 3)
    = 6

min = min(3, 2 × 3)
    = 3
```

At `-2`:

The previous maximum and minimum can switch roles because of the negative number.

Therefore we calculate using both.

---

## Java

```java
public static int maxProduct(int[] arr) {

    int maxProduct = arr[0];
    int minProduct = arr[0];
    int answer = arr[0];

    for (int i = 1; i < arr.length; i++) {

        int value = arr[i];

        int oldMax = maxProduct;
        int oldMin = minProduct;

        maxProduct = Math.max(
            value,
            Math.max(value * oldMax, value * oldMin)
        );

        minProduct = Math.min(
            value,
            Math.min(value * oldMax, value * oldMin)
        );

        answer = Math.max(answer, maxProduct);
    }

    return answer;
}
```

### Complexity

```text
Time: O(n)
Space: O(1)
```

---

# 14. Longest Subarray

"Longest Subarray" is a **general category**, not one single algorithm.

Usually the problem provides a condition.

For example:

> Find the longest subarray containing only positive numbers.

Or:

> Find the longest subarray with sum `K`.

Or:

> Find the longest subarray containing equal numbers of 0 and 1.

The technique depends on the condition.

---

## Example

```text
arr = [1, 2, 3, 4, 5]
```

If the condition is:

> Find the longest subarray with sum ≤ K

then we need an appropriate technique such as:

* Sliding Window
* Two Pointers
* Prefix Sum
* HashMap

depending on whether the array contains negative numbers.

---

# 15. Longest Subarray with Given Sum

Problem:

> Find the length of the longest subarray whose sum is equal to `K`.

Example:

```text
arr = [10, 5, 2, 7, 1, 9]
K = 15
```

Consider:

```text
[5, 2, 7, 1]
```

Sum:

```text
5 + 2 + 7 + 1 = 15
```

Length:

```text
4
```

So:

```text
Answer = 4
```

---

# 16. Longest Subarray with Given Sum Using Prefix Sum + HashMap

This approach is especially important when the array can contain **negative numbers**.

Maintain:

```text
prefixSum
```

At index `i`:

```text
prefixSum = sum from 0 to i
```

Suppose:

```text
prefixSum - K
```

has already appeared at an earlier index.

Then the elements between that earlier index and the current index have sum:

```text
K
```

Because:

```text
currentPrefixSum - previousPrefixSum = K
```

Therefore:

```text
previousPrefixSum = currentPrefixSum - K
```

---

## Example

```text
arr = [10, 5, 2, 7, 1, 9]
K = 15
```

At index `3`:

```text
prefixSum = 10 + 5 + 2 + 7
           = 24
```

We need:

```text
24 - 15 = 9
```

If prefix sum `9` existed earlier, then the subarray between those positions has sum `15`.

---

## Java

```java
import java.util.HashMap;

public static int longestSubarraySumK(int[] arr, int k) {

    HashMap<Integer, Integer> map = new HashMap<>();

    int prefixSum = 0;
    int maxLength = 0;

    for (int i = 0; i < arr.length; i++) {

        prefixSum += arr[i];

        if (prefixSum == k) {
            maxLength = i + 1;
        }

        if (map.containsKey(prefixSum - k)) {

            int previousIndex = map.get(prefixSum - k);

            maxLength = Math.max(
                maxLength,
                i - previousIndex
            );
        }

        // Store only the first occurrence
        if (!map.containsKey(prefixSum)) {
            map.put(prefixSum, i);
        }
    }

    return maxLength;
}
```

### Complexity

```text
Time: O(n)
Space: O(n)
```

---

# 17. Why Store the First Prefix Sum?

Suppose a prefix sum occurs multiple times.

For finding the **longest** subarray, we want the earliest occurrence.

Example:

```text
prefixSum = 10
```

appears at:

```text
index 2
index 5
```

If we are currently at index `10`, then:

Using index `2`:

```text
length = 10 - 2 = 8
```

Using index `5`:

```text
length = 10 - 5 = 5
```

Therefore, the earliest index gives the longest subarray.

That's why:

```java
if (!map.containsKey(prefixSum)) {
    map.put(prefixSum, i);
}
```

is important.

---

# 18. Subarray with Given Sum

This problem is slightly different from the previous one.

The question might be:

> Find any subarray whose sum equals K.

Example:

```text
arr = [1, 2, 3, 7, 5]
K = 12
```

We can find:

```text
[2, 3, 7]
```

because:

```text
2 + 3 + 7 = 12
```

If all array values are **positive**, Sliding Window is a very useful approach.

---

# 19. Sliding Window for Given Sum

Example:

```text
arr = [1, 2, 3, 7, 5]
K = 12
```

Start:

```text
left = 0
right = 0
sum = 0
```

Expand the window:

```text
1
1 + 2 = 3
1 + 2 + 3 = 6
1 + 2 + 3 + 7 = 13
```

Now:

```text
13 > 12
```

Remove from the left:

```text
13 - 1 = 12
```

Now:

```text
[2, 3, 7]
```

Sum:

```text
12
```

Found.

---

## Java

```java
public static boolean subarrayWithSumK(int[] arr, int k) {

    int left = 0;
    int sum = 0;

    for (int right = 0; right < arr.length; right++) {

        sum += arr[right];

        while (sum > k && left <= right) {
            sum -= arr[left];
            left++;
        }

        if (sum == k) {
            return true;
        }
    }

    return false;
}
```

### Important Limitation

This approach works correctly when the array contains **non-negative values**.

If negative numbers are present, the window sum is no longer monotonic, so Sliding Window may fail.

For arrays containing arbitrary positive and negative numbers, Prefix Sum + HashMap is generally the appropriate technique.

---

# 20. Subarray Sum Equals K

Problem:

> Count how many subarrays have a sum equal to K.

Example:

```text
arr = [1, 1, 1]
K = 2
```

Subarrays with sum `2`:

```text
[1, 1]   → indices 0-1
[1, 1]   → indices 1-2
```

Therefore:

```text
Answer = 2
```

---

# 21. Prefix Sum + HashMap

This is one of the most important patterns in subarray problems.

Maintain:

```text
prefixSum
```

Suppose current prefix sum is:

```text
S
```

We need a previous prefix sum:

```text
S - K
```

because:

```text
S - (S - K) = K
```

If `S-K` has appeared multiple times, then there are multiple subarrays ending at the current position whose sum is `K`.

Therefore, unlike the **longest subarray** problem, we store the **frequency** of each prefix sum.

---

# 22. Example: Subarray Sum Equals K

```text
arr = [1, 1, 1]
K = 2
```

Start with:

```text
map = {0 : 1}
```

Why?

Because before processing any element, the prefix sum is `0`, and it has occurred once.

---

### First element

```text
prefixSum = 1
```

Need:

```text
1 - 2 = -1
```

Not found.

Store:

```text
map = {
    0: 1,
    1: 1
}
```

---

### Second element

```text
prefixSum = 2
```

Need:

```text
2 - 2 = 0
```

`0` exists once.

Therefore:

```text
count = 1
```

---

### Third element

```text
prefixSum = 3
```

Need:

```text
3 - 2 = 1
```

Prefix sum `1` exists once.

Therefore:

```text
count = 2
```

Final:

```text
Answer = 2
```

---

# 23. Java — Subarray Sum Equals K

```java
import java.util.HashMap;

public static int subarraySum(int[] arr, int k) {

    HashMap<Integer, Integer> map = new HashMap<>();

    map.put(0, 1);

    int prefixSum = 0;
    int count = 0;

    for (int num : arr) {

        prefixSum += num;

        if (map.containsKey(prefixSum - k)) {
            count += map.get(prefixSum - k);
        }

        map.put(
            prefixSum,
            map.getOrDefault(prefixSum, 0) + 1
        );
    }

    return count;
}
```

### Complexity

```text
Time: O(n)
Space: O(n)
```

---

# 24. Count Subarrays with Given Sum

This is essentially the same fundamental problem as:

```text
Subarray Sum Equals K
```

The goal is:

> Count the number of contiguous subarrays whose sum equals K.

Example:

```text
arr = [1, 2, 1, 2, 1]
K = 3
```

Valid subarrays include:

```text
[1, 2]
[2, 1]
[1, 2]
[2, 1]
```

So:

```text
Answer = 4
```

The standard solution is:

```text
Prefix Sum + HashMap
```

---

# 25. Difference Between Longest and Count

This distinction is extremely important.

### Longest Subarray with Sum K

We need:

```text
maximum length
```

Therefore:

```text
prefixSum → earliest index
```

Example:

```java
HashMap<Integer, Integer>
```

---

### Count Subarrays with Sum K

We need:

```text
number of subarrays
```

Therefore:

```text
prefixSum → frequency
```

Example:

```java
HashMap<Integer, Integer>
```

but the value represents frequency instead of an index.

### Remember

```text
Longest → Store earliest index
Count   → Store frequency
```

This is a very important interview pattern.

---

# 26. Prefix Sum Concept

Prefix Sum is the foundation behind many subarray problems.

Given:

```text
arr = [2, 4, 1, 3]
```

Prefix sums:

```text
index       0   1   2   3

array       2   4   1   3

prefix      2   6   7   10
```

Prefix sum at index `i` means:

```text
arr[0] + arr[1] + ... + arr[i]
```

---

## Finding Subarray Sum Using Prefix Sum

Suppose:

```text
arr = [2, 4, 1, 3]
```

Find sum from index `1` to `3`:

```text
[4, 1, 3]
```

Sum:

```text
4 + 1 + 3 = 8
```

Using prefix sums:

```text
prefix[3] = 10
prefix[0] = 2
```

Therefore:

```text
10 - 2 = 8
```

General formula:

```text
sum(i...j) = prefix[j] - prefix[i-1]
```

When:

```text
i = 0
```

the sum is simply:

```text
prefix[j]
```

---

# 27. Major Subarray Patterns

Most subarray problems can be categorized into patterns.

## Pattern 1 — Generate Every Subarray

Use:

```text
Nested loops
```

Typical complexity:

```text
O(n²)
```

or `O(n³)` if explicitly printing every element.

---

## Pattern 2 — Maximum Sum

Use:

```text
Kadane's Algorithm
```

Complexity:

```text
O(n)
```

---

## Pattern 3 — Minimum Sum

Use:

```text
Modified Kadane's Algorithm
```

Complexity:

```text
O(n)
```

---

## Pattern 4 — Maximum Product

Use:

```text
Maximum Product + Minimum Product
```

Complexity:

```text
O(n)
```

---

## Pattern 5 — Longest Subarray with Sum K

For arbitrary positive/negative integers:

```text
Prefix Sum + HashMap
```

Store:

```text
prefixSum → earliest index
```

Complexity:

```text
O(n)
```

---

## Pattern 6 — Count Subarrays with Sum K

Use:

```text
Prefix Sum + HashMap
```

Store:

```text
prefixSum → frequency
```

Complexity:

```text
O(n)
```

---

## Pattern 7 — Given Sum with Positive Numbers

Use:

```text
Sliding Window
```

Complexity:

```text
O(n)
```

---

# 28. Important Edge Cases

When solving subarray problems, always consider these cases.

### Single Element

```text
[5]
```

### All Positive

```text
[1, 2, 3, 4]
```

### All Negative

```text
[-1, -2, -3]
```

### Mixed Values

```text
[-2, 3, -1, 4, -5]
```

### Zeroes

```text
[0, 0, 0]
```

### Repeated Values

```text
[1, 1, 1, 1]
```

### Negative Numbers

Especially important for:

```text
Prefix Sum
Kadane
Maximum Product
```

### Integer Overflow

For large values, prefer:

```java
long
```

instead of:

```java
int
```

for sums/products when constraints require it.

---

# 29. Common Mistakes

## Mistake 1 — Confusing Subarray with Subsequence

Wrong:

```text
[1, 3]
```

as a subarray of:

```text
[1, 2, 3]
```

Correct:

```text
[1, 2]
[2, 3]
[1, 2, 3]
```

---

## Mistake 2 — Using Sliding Window with Negative Numbers

For:

```text
[-2, 5, -1, 2]
```

you cannot blindly use the positive-number sliding-window logic.

Use:

```text
Prefix Sum + HashMap
```

when the problem allows arbitrary integers.

---

## Mistake 3 — Initializing Kadane with 0

Wrong:

```java
int maxSum = 0;
```

for the general problem.

For:

```text
[-5, -2, -8]
```

the answer should be:

```text
-2
```

Correct:

```java
int maxSum = arr[0];
```

---

## Mistake 4 — Forgetting `map.put(0, 1)`

For counting subarrays:

```java
map.put(0, 1);
```

is essential.

It handles subarrays that start from index `0`.

---

## Mistake 5 — Storing the Latest Index for Longest Subarray

For longest subarray problems, don't replace an existing prefix sum index.

Use:

```java
if (!map.containsKey(prefixSum)) {
    map.put(prefixSum, i);
}
```

because the earliest index gives the longest length.

---

# 30. Complexity Comparison

| Problem                   | Typical Technique    |          Time | Space |
| ------------------------- | -------------------- | ------------: | ----: |
| Generate subarrays        | Nested loops         | O(n²) / O(n³) |  O(1) |
| Number of subarrays       | Formula              |          O(1) |  O(1) |
| Maximum subarray sum      | Kadane               |          O(n) |  O(1) |
| Minimum subarray sum      | Modified Kadane      |          O(n) |  O(1) |
| Maximum product subarray  | Max + Min tracking   |          O(n) |  O(1) |
| Given sum, positive array | Sliding Window       |          O(n) |  O(1) |
| Longest subarray sum K    | Prefix Sum + HashMap |          O(n) |  O(n) |
| Count subarrays sum K     | Prefix Sum + HashMap |          O(n) |  O(n) |

---

# 31. The Most Important Formulas

### Number of Subarrays

```text
n(n + 1) / 2
```

### Subarray Sum Using Prefix Sum

```text
sum(i...j) = prefix[j] - prefix[i - 1]
```

### Prefix Sum Condition for Sum K

If:

```text
currentPrefix = P
```

then we need:

```text
previousPrefix = P - K
```

because:

```text
P - (P - K) = K
```

---

# 32. Important Java Templates

## Kadane

```java
int current = arr[0];
int best = arr[0];

for (int i = 1; i < arr.length; i++) {
    current = Math.max(arr[i], current + arr[i]);
    best = Math.max(best, current);
}
```

---

## Minimum Kadane

```java
int current = arr[0];
int best = arr[0];

for (int i = 1; i < arr.length; i++) {
    current = Math.min(arr[i], current + arr[i]);
    best = Math.min(best, current);
}
```

---

## Longest Subarray Sum K

```java
HashMap<Integer, Integer> map = new HashMap<>();

int prefixSum = 0;
int maxLength = 0;

for (int i = 0; i < arr.length; i++) {

    prefixSum += arr[i];

    if (prefixSum == k) {
        maxLength = i + 1;
    }

    if (map.containsKey(prefixSum - k)) {
        maxLength = Math.max(
            maxLength,
            i - map.get(prefixSum - k)
        );
    }

    map.putIfAbsent(prefixSum, i);
}
```

---

## Count Subarrays Sum K

```java
HashMap<Integer, Integer> map = new HashMap<>();

map.put(0, 1);

int prefixSum = 0;
int count = 0;

for (int num : arr) {

    prefixSum += num;

    count += map.getOrDefault(prefixSum - k, 0);

    map.put(
        prefixSum,
        map.getOrDefault(prefixSum, 0) + 1
    );
}
```

---

# 33. DSA Thinking Pattern

When you see the word **subarray**, don't immediately start coding.

First identify what the problem is asking.

```text
                    SUBARRAY
                       |
          +------------+------------+
          |            |            |
       Maximum       Minimum       Count
          |            |            |
       Kadane       Kadane        Prefix Sum
          |                         +
          |                       HashMap
          |
    Maximum Product
          |
      Max + Min
```

For sum-based problems:

```text
                SUM
                 |
        +--------+--------+
        |                 |
   Positive only     Negative allowed
        |                 |
 Sliding Window      Prefix Sum
                         +
                      HashMap
```

---

# 34. Interview Recognition Cheat Sheet

When you see:

### "Maximum sum contiguous subarray"

Think:

```text
Kadane's Algorithm
```

### "Minimum sum contiguous subarray"

Think:

```text
Modified Kadane
```

### "Maximum product contiguous subarray"

Think:

```text
Track maximum + minimum
```

### "Longest subarray with sum K"

Think:

```text
Prefix Sum + HashMap
```

Store:

```text
prefixSum → first index
```

### "Count subarrays with sum K"

Think:

```text
Prefix Sum + HashMap
```

Store:

```text
prefixSum → frequency
```

### "Find subarray with sum K"

If all values are non-negative:

```text
Sliding Window
```

If negative values are allowed:

```text
Prefix Sum + HashMap
```

### "How many subarrays are possible?"

Think:

```text
n(n + 1) / 2
```

---

# 35. Final Summary

The most important things to remember from **Subarrays** are:

```text
Subarray
    ↓
Contiguous portion of an array
```

```text
Number of Subarrays
    ↓
n(n + 1) / 2
```

```text
Maximum Subarray Sum
    ↓
Kadane's Algorithm
    ↓
O(n)
```

```text
Minimum Subarray Sum
    ↓
Modified Kadane
    ↓
O(n)
```

```text
Maximum Product Subarray
    ↓
Track max + min product
    ↓
O(n)
```

```text
Longest Subarray with Sum K
    ↓
Prefix Sum + HashMap
    ↓
Store earliest index
```

```text
Count Subarrays with Sum K
    ↓
Prefix Sum + HashMap
    ↓
Store frequency
```

```text
Positive numbers + target sum
    ↓
Sliding Window
```

The **three patterns you should master first** are:

```text
1. Kadane's Algorithm
2. Sliding Window
3. Prefix Sum + HashMap
```

Once these three become comfortable, a large number of subarray problems become pattern-recognition problems rather than completely new problems.
