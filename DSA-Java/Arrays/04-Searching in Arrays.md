# DSA — Arrays

## 3. Searching in Arrays

Searching is the process of finding a target value or position inside an array.

The two fundamental searching techniques are:

```text
Linear Search
Binary Search
```

Binary Search is especially important because many advanced problems are variations of the same technique.

---

## 1. Linear Search

### What is Linear Search?

Linear Search checks every element one by one until the target is found.

Example:

```text
Array:
[10, 20, 30, 40, 50]

Target = 40

10 → No
20 → No
30 → No
40 → Found
```

### Java Implementation

```java
public static int linearSearch(int[] arr, int target) {

    for (int i = 0; i < arr.length; i++) {

        if (arr[i] == target) {
            return i;
        }
    }

    return -1;
}
```

Usage:

```java
int[] arr = {10, 20, 30, 40, 50};

int result = linearSearch(arr, 40);

System.out.println(result);
```

Output:

```text
3
```

If the target does not exist:

```text
-1
```

### Complexity

| Case    | Time |
| ------- | ---: |
| Best    | O(1) |
| Average | O(n) |
| Worst   | O(n) |

Space:

```text
O(1)
```

### When to use Linear Search?

Use it when:

* The array is unsorted.
* The array is small.
* You only need one search.
* Sorting the array would be unnecessary.

---

# 2. Binary Search

Binary Search is an efficient searching algorithm that repeatedly divides the search space into two halves.

Example:

```text
[10, 20, 30, 40, 50, 60, 70]
```

Target:

```text
60
```

Start with the middle:

```text
        40
        ↑
[10, 20, 30, 40, 50, 60, 70]
```

Since:

```text
60 > 40
```

we can eliminate the entire left half.

Search only:

```text
[50, 60, 70]
```

Then repeat.

### Complexity

```text
Time  → O(log n)
Space → O(1)
```

---

# 3. Binary Search Prerequisites

Before using traditional Binary Search, you need to understand its requirements.

## Requirement 1 — Sorted Array

The standard binary search algorithm requires sorted data.

Valid:

```text
[10, 20, 30, 40, 50]
```

Invalid for standard binary search:

```text
[30, 10, 50, 20, 40]
```

Why?

Because binary search depends on knowing which side can be eliminated.

---

## Requirement 2 — Ordered Search Space

You must be able to determine:

```text
Target < Middle
```

or:

```text
Target > Middle
```

and safely discard one side.

---

## Requirement 3 — Correct Boundaries

The standard exact-search version uses:

```java
int left = 0;
int right = arr.length - 1;
```

and:

```java
while (left <= right)
```

---

# 4. Iterative Binary Search

Iterative Binary Search uses a loop.

### Standard Template

```java
public static int binarySearch(int[] arr, int target) {

    int left = 0;
    int right = arr.length - 1;

    while (left <= right) {

        int mid = left + (right - left) / 2;

        if (arr[mid] == target) {
            return mid;
        }

        if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return -1;
}
```

### Example

```java
int[] arr = {10, 20, 30, 40, 50, 60, 70};

System.out.println(
    binarySearch(arr, 60)
);
```

Output:

```text
5
```

---

## Dry Run

Array:

```text
[10, 20, 30, 40, 50, 60, 70]
```

Target:

```text
60
```

Initially:

```text
left = 0
right = 6
```

Calculate:

```text
mid = 3
arr[mid] = 40
```

Since:

```text
60 > 40
```

move right:

```text
left = mid + 1
```

Now:

```text
left = 4
right = 6
```

Next:

```text
mid = 5
arr[mid] = 60
```

Found.

```text
return 5
```

---

# 5. Why `left + (right - left) / 2`?

You may see:

```java
int mid = (left + right) / 2;
```

This usually works, but can potentially cause integer overflow when `left` and `right` are very large.

Prefer:

```java
int mid = left + (right - left) / 2;
```

This is the standard safe formula.

---

# 6. Recursive Binary Search

Binary Search can also be implemented using recursion.

Instead of repeatedly modifying variables inside a loop, we call the function again with a smaller range.

### Java

```java
public static int binarySearch(
        int[] arr,
        int left,
        int right,
        int target) {

    if (left > right) {
        return -1;
    }

    int mid = left + (right - left) / 2;

    if (arr[mid] == target) {
        return mid;
    }

    if (arr[mid] < target) {

        return binarySearch(
            arr,
            mid + 1,
            right,
            target
        );
    }

    return binarySearch(
        arr,
        left,
        mid - 1,
        target
    );
}
```

Usage:

```java
int[] arr = {10, 20, 30, 40, 50};

int result = binarySearch(
    arr,
    0,
    arr.length - 1,
    40
);

System.out.println(result);
```

Output:

```text
3
```

### Complexity

```text
Time  → O(log n)
Space → O(log n)
```

The extra space comes from recursive call-stack frames.

### Iterative vs Recursive

| Version   |     Time |    Space |
| --------- | -------: | -------: |
| Iterative | O(log n) |     O(1) |
| Recursive | O(log n) | O(log n) |

For most DSA problems, the iterative version is more space-efficient.

---

# 7. Lower Bound

Lower Bound is one of the most important binary-search patterns.

### Definition

The Lower Bound is the **first index where:**

```text
arr[index] >= target
```

Example:

```text
arr = [10, 20, 20, 20, 30, 40]
target = 20
```

The first valid position is:

```text
index = 1
```

because:

```text
arr[1] = 20
```

---

## Example Without the Target

```text
arr = [10, 20, 30, 40, 50]
target = 25
```

The first value satisfying:

```text
arr[index] >= 25
```

is:

```text
30
```

Therefore:

```text
Lower Bound = 2
```

---

## Java Implementation

```java
public static int lowerBound(int[] arr, int target) {

    int left = 0;
    int right = arr.length;

    while (left < right) {

        int mid = left + (right - left) / 2;

        if (arr[mid] >= target) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }

    return left;
}
```

Notice:

```java
int right = arr.length;
```

instead of:

```java
arr.length - 1
```

This is because the answer can be:

```text
arr.length
```

when every element is smaller than the target.

### Complexity

```text
Time  → O(log n)
Space → O(1)
```

---

# 8. Upper Bound

Upper Bound finds the **first index where:**

```text
arr[index] > target
```

Notice the difference:

```text
Lower Bound → arr[index] >= target

Upper Bound → arr[index] > target
```

Example:

```text
arr = [10, 20, 20, 20, 30, 40]
target = 20
```

Lower Bound:

```text
1
```

Upper Bound:

```text
4
```

Because:

```text
arr[4] = 30
```

and:

```text
30 > 20
```

---

## Java Implementation

```java
public static int upperBound(int[] arr, int target) {

    int left = 0;
    int right = arr.length;

    while (left < right) {

        int mid = left + (right - left) / 2;

        if (arr[mid] > target) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }

    return left;
}
```

### Complexity

```text
Time  → O(log n)
Space → O(1)
```

---

# 9. Lower Bound vs Upper Bound

This is extremely important.

| Concept     | Condition                |
| ----------- | ------------------------ |
| Lower Bound | First `arr[i] >= target` |
| Upper Bound | First `arr[i] > target`  |

Example:

```text
[10, 20, 20, 20, 30, 40]
```

For:

```text
target = 20
```

we get:

```text
Lower Bound = 1
Upper Bound = 4
```

---

# 10. First Occurrence

Suppose:

```text
[10, 20, 20, 20, 30]
```

Target:

```text
20
```

The target occurs at:

```text
index 1
index 2
index 3
```

The **first occurrence** is:

```text
1
```

A normal binary search is not guaranteed to return the first occurrence.

We need a modified version.

---

## Algorithm

When we find the target:

```text
Store the answer
Move LEFT
```

Therefore:

```java
right = mid - 1;
```

---

## Java

```java
public static int firstOccurrence(
        int[] arr,
        int target) {

    int left = 0;
    int right = arr.length - 1;

    int answer = -1;

    while (left <= right) {

        int mid = left + (right - left) / 2;

        if (arr[mid] == target) {

            answer = mid;

            // Look for an earlier occurrence
            right = mid - 1;

        } else if (arr[mid] < target) {

            left = mid + 1;

        } else {

            right = mid - 1;
        }
    }

    return answer;
}
```

---

# 11. Last Occurrence

Using the same array:

```text
[10, 20, 20, 20, 30]
```

Target:

```text
20
```

The **last occurrence** is:

```text
3
```

When the target is found:

```text
Store answer
Move RIGHT
```

Therefore:

```java
left = mid + 1;
```

---

## Java

```java
public static int lastOccurrence(
        int[] arr,
        int target) {

    int left = 0;
    int right = arr.length - 1;

    int answer = -1;

    while (left <= right) {

        int mid = left + (right - left) / 2;

        if (arr[mid] == target) {

            answer = mid;

            // Look for a later occurrence
            left = mid + 1;

        } else if (arr[mid] < target) {

            left = mid + 1;

        } else {

            right = mid - 1;
        }
    }

    return answer;
}
```

---

# 12. First vs Last Occurrence

Memorize this:

```text
FIRST OCCURRENCE

Found target
     ↓
Store answer
     ↓
Move LEFT

right = mid - 1
```

```text
LAST OCCURRENCE

Found target
     ↓
Store answer
     ↓
Move RIGHT

left = mid + 1
```

---

# 13. Search Insert Position

This problem asks:

> If the target exists, return its index. Otherwise, return the index where it should be inserted while maintaining sorted order.

Example:

```text
arr = [10, 20, 30, 40]
target = 30
```

Answer:

```text
2
```

Because `30` already exists.

---

### Target Does Not Exist

```text
arr = [10, 20, 30, 40]
target = 25
```

It should become:

```text
[10, 20, 25, 30, 40]
```

Therefore:

```text
index = 2
```

---

## Java

Search Insert Position is essentially a **Lower Bound** problem.

```java
public static int searchInsert(
        int[] arr,
        int target) {

    int left = 0;
    int right = arr.length;

    while (left < right) {

        int mid = left + (right - left) / 2;

        if (arr[mid] >= target) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }

    return left;
}
```

---

# 14. Search in a Sorted Array

If an array is sorted, binary search is generally preferred over linear search when you need efficient lookup.

Example:

```text
[5, 10, 15, 20, 25, 30, 35]
```

Target:

```text
25
```

Use:

```text
Binary Search
```

Complexity:

```text
O(log n)
```

instead of:

```text
O(n)
```

for linear search.

---

## Java's Built-in Method

Java provides:

```java
Arrays.binarySearch()
```

Example:

```java
import java.util.Arrays;

int[] arr = {10, 20, 30, 40, 50};

int index = Arrays.binarySearch(arr, 40);

System.out.println(index);
```

Output:

```text
3
```

However, while learning DSA, you should implement binary search yourself rather than relying entirely on the library.

---

# 15. Search in Rotated Sorted Array

This is one of the most important binary-search variations.

Start with a sorted array:

```text
[10, 20, 30, 40, 50, 60, 70]
```

Rotate it:

```text
[40, 50, 60, 70, 10, 20, 30]
```

The array is no longer globally sorted.

However, there is still a useful property:

> At least one half of the current search range is sorted.

---

# 16. Understanding the Rotated Array

Consider:

```text
[40, 50, 60, 70, 10, 20, 30]
```

We can see two sorted portions:

```text
[40, 50, 60, 70]
```

and:

```text
[10, 20, 30]
```

At each binary-search step, determine which half is sorted.

---

# 17. Rotated Search Algorithm

Suppose:

```text
left
mid
right
```

First check:

```java
if (arr[mid] == target)
```

If not found, determine the sorted half.

### Left Half Sorted

If:

```java
arr[left] <= arr[mid]
```

then:

```text
left → mid
```

is sorted.

Now check whether the target belongs inside that range.

```java
if (arr[left] <= target && target < arr[mid])
```

If yes:

```java
right = mid - 1;
```

Otherwise:

```java
left = mid + 1;
```

---

### Right Half Sorted

Otherwise:

```text
mid → right
```

is sorted.

Check:

```java
if (arr[mid] < target && target <= arr[right])
```

If yes:

```java
left = mid + 1;
```

Otherwise:

```java
right = mid - 1;
```

---

# 18. Java Implementation

```java
public static int searchRotated(
        int[] arr,
        int target) {

    int left = 0;
    int right = arr.length - 1;

    while (left <= right) {

        int mid = left + (right - left) / 2;

        // Target found
        if (arr[mid] == target) {
            return mid;
        }

        // Left half is sorted
        if (arr[left] <= arr[mid]) {

            if (arr[left] <= target &&
                target < arr[mid]) {

                right = mid - 1;

            } else {

                left = mid + 1;
            }

        }

        // Right half is sorted
        else {

            if (arr[mid] < target &&
                target <= arr[right]) {

                left = mid + 1;

            } else {

                right = mid - 1;
            }
        }
    }

    return -1;
}
```

---

# 19. Rotated Search Example

```java
int[] arr = {
    40, 50, 60, 70,
    10, 20, 30
};

int target = 20;

System.out.println(
    searchRotated(arr, target)
);
```

Output:

```text
5
```

---

# 20. Rotated Search Dry Run

Array:

```text
[40, 50, 60, 70, 10, 20, 30]
```

Target:

```text
20
```

Initial:

```text
left = 0
right = 6
```

Calculate:

```text
mid = 3
arr[mid] = 70
```

Check:

```text
arr[left] <= arr[mid]

40 <= 70
```

So the left half is sorted:

```text
[40, 50, 60, 70]
```

Does `20` belong there?

```text
40 <= 20 <= 70
```

No.

Therefore eliminate the left half:

```text
left = mid + 1
```

Now search:

```text
[10, 20, 30]
```

Continue binary search until:

```text
arr[5] == 20
```

Answer:

```text
5
```

---

# 21. Rotated Array Complexity

For a rotated sorted array with **distinct elements**:

```text
Time  → O(log n)
Space → O(1)
```

---

# 22. Rotated Array With Duplicates

Duplicates make the problem harder.

Example:

```text
[2, 5, 6, 0, 0, 1, 2]
```

Sometimes:

```text
arr[left] == arr[mid] == arr[right]
```

In this situation, we cannot always determine which side is sorted.

A common solution is:

```java
left++;
right--;
```

This removes the ambiguous boundary elements.

However, in the worst case this can reduce the complexity to:

```text
O(n)
```

So:

```text
Distinct values
→ O(log n)

Duplicates
→ Worst case O(n)
```

---

# 23. Important Binary Search Patterns

At this point, organize everything into a few patterns.

```text
Binary Search
│
├── Exact Search
│   └── Find target
│
├── Boundary Search
│   ├── Lower Bound
│   └── Upper Bound
│
├── Duplicate Search
│   ├── First Occurrence
│   └── Last Occurrence
│
├── Position Search
│   └── Search Insert Position
│
└── Modified Binary Search
    └── Rotated Sorted Array
```

---

# 24. Important Relationships

These problems are closely related.

### Lower Bound

```text
First index where:

arr[i] >= target
```

### Upper Bound

```text
First index where:

arr[i] > target
```

### First Occurrence

For a target that exists:

```text
Lower Bound(target)
```

### Last Occurrence

For a target that exists:

```text
Upper Bound(target) - 1
```

### Search Insert Position

```text
Lower Bound(target)
```

This means you do not need to memorize nine completely different algorithms.

Many are simply variations of binary search.

---

# 25. Count Occurrences

Lower and upper bounds can also count duplicates.

Example:

```text
arr = [10, 20, 20, 20, 20, 30]
target = 20
```

Lower Bound:

```text
1
```

Upper Bound:

```text
5
```

Therefore:

```text
Number of occurrences
=
upperBound - lowerBound
```

```text
5 - 1 = 4
```

Java:

```java
public static int countOccurrences(
        int[] arr,
        int target) {

    int first = lowerBound(arr, target);
    int last = upperBound(arr, target);

    return last - first;
}
```

---

# 26. Binary Search Complexity

| Algorithm               |     Time |    Space |
| ----------------------- | -------: | -------: |
| Linear Search           |     O(n) |     O(1) |
| Iterative Binary Search | O(log n) |     O(1) |
| Recursive Binary Search | O(log n) | O(log n) |
| Lower Bound             | O(log n) |     O(1) |
| Upper Bound             | O(log n) |     O(1) |
| First Occurrence        | O(log n) |     O(1) |
| Last Occurrence         | O(log n) |     O(1) |
| Search Insert Position  | O(log n) |     O(1) |
| Rotated Search          | O(log n) |     O(1) |

For rotated arrays with duplicates:

```text
Worst Case = O(n)
```

---

# 27. Common Binary Search Mistakes

## Mistake 1 — Using Binary Search on Unsorted Data

Wrong:

```text
[30, 10, 50, 20, 40]
```

Standard binary search cannot safely eliminate half the search space.

---

## Mistake 2 — Wrong Loop Condition

For the standard inclusive exact-search template:

```java
while (left <= right)
```

For lower/upper-bound style:

```java
while (left < right)
```

The correct condition depends on the chosen search-space representation.

---

## Mistake 3 — Wrong Boundary Updates

Standard exact search:

```java
left = mid + 1;
```

or:

```java
right = mid - 1;
```

Do not blindly use:

```java
left = mid;
```

or:

```java
right = mid;
```

because this can cause an infinite loop.

---

## Mistake 4 — Forgetting Duplicates

Normal binary search does not guarantee:

```text
First occurrence
```

or:

```text
Last occurrence
```

Use the appropriate variation.

---

## Mistake 5 — Forgetting the Not-Found Case

Always decide what your function should return when the target does not exist.

Common convention:

```text
-1
```

For lower bound / search insert position, however, returning:

```text
arr.length
```

can be valid when no element satisfies the condition.

---

# 28. How to Identify Binary Search Problems

When you see an array searching problem, ask:

```text
1. Is the array sorted?
        ↓
     YES?
        ↓
   Think Binary Search
```

Then:

```text
2. Am I looking for an exact value?
        ↓
   Standard Binary Search
```

Or:

```text
3. Am I looking for the first valid position?
        ↓
   Lower Bound
```

Or:

```text
4. Am I looking for the position after all target values?
        ↓
   Upper Bound
```

Or:

```text
5. Are there duplicates?
        ↓
   First / Last Occurrence
```

Or:

```text
6. Is the sorted array rotated?
        ↓
   Rotated Binary Search
```

---

# 29. Core Templates to Memorize

## Exact Binary Search

```java
public static int binarySearch(int[] arr, int target) {

    int left = 0;
    int right = arr.length - 1;

    while (left <= right) {

        int mid = left + (right - left) / 2;

        if (arr[mid] == target) {
            return mid;
        }

        if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return -1;
}
```

---

## Lower Bound

```java
public static int lowerBound(int[] arr, int target) {

    int left = 0;
    int right = arr.length;

    while (left < right) {

        int mid = left + (right - left) / 2;

        if (arr[mid] >= target) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }

    return left;
}
```

---

## Upper Bound

```java
public static int upperBound(int[] arr, int target) {

    int left = 0;
    int right = arr.length;

    while (left < right) {

        int mid = left + (right - left) / 2;

        if (arr[mid] > target) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }

    return left;
}
```

---

# 30. Final Cheat Sheet

```text
LINEAR SEARCH
─────────────
Works on unsorted arrays.

Time:
O(n)
```

```text
BINARY SEARCH
─────────────
Requires sorted/ordered search space.

Time:
O(log n)
```

```text
LOWER BOUND
───────────
First index:

arr[i] >= target
```

```text
UPPER BOUND
───────────
First index:

arr[i] > target
```

```text
FIRST OCCURRENCE
────────────────
Found target
    ↓
Save answer
    ↓
Search LEFT

right = mid - 1
```

```text
LAST OCCURRENCE
───────────────
Found target
    ↓
Save answer
    ↓
Search RIGHT

left = mid + 1
```

```text
SEARCH INSERT POSITION
──────────────────────
Lower Bound
```

```text
ROTATED SORTED ARRAY
────────────────────
1. Find mid.
2. Determine which half is sorted.
3. Check whether target belongs to that half.
4. Eliminate the other half.
5. Repeat.
```

---

# 31. What You Should Be Able to Do After This Topic

Before moving to the next Array topic, you should be able to implement these from scratch in Java:

```text
✓ Linear Search

✓ Iterative Binary Search

✓ Recursive Binary Search

✓ Lower Bound

✓ Upper Bound

✓ First Occurrence

✓ Last Occurrence

✓ Search Insert Position

✓ Search in Sorted Array

✓ Search in Rotated Sorted Array
```

And you should understand the core idea:

```text
                    SEARCHING
                       │
          ┌────────────┴────────────┐
          │                         │
    Unsorted Array            Sorted Array
          │                         │
          ↓                         ↓
    Linear Search             Binary Search
                                    │
                    ┌───────────────┼───────────────┐
                    │               │               │
                Exact Search    Boundary Search   Rotated
                                    │               │
                              ┌─────┴─────┐         │
                              │           │         │
                         Lower Bound  Upper Bound   │
                              │           │         │
                              └─────┬─────┘         │
                                    │               │
                              First/Last       Rotated Search
                              Occurrence
                                    │
                              Search Insert
                                Position
```

The most important transition is:

```text
Normal Binary Search
        ↓
Understand boundaries
        ↓
Lower / Upper Bound
        ↓
First / Last Occurrence
        ↓
Modified Binary Search
        ↓
Rotated Sorted Array
```

Once this pattern is solid, you are ready for the next major array techniques: **sorting, prefix sums, two pointers, sliding window, and hashing**.
