# DSA — Arrays

# 3. Searching in Arrays

Searching is the process of finding whether a particular element exists in an array and, if it exists, determining its position.

The two fundamental searching techniques are:

```text
Linear Search
Binary Search
```

Understanding binary search is especially important because many advanced DSA problems are actually **binary search on an answer/search space** in disguise.

---

# 1. Linear Search

## What is Linear Search?

Linear Search checks elements one by one from left to right until:

1. The target is found, or
2. The entire array has been checked.

Example:

```text
Array:

[10, 20, 30, 40, 50]
             ↑
           target
```

We want to find `40`.

The algorithm checks:

```text
10 → No
20 → No
30 → No
40 → Yes
```

Therefore:

```text
Index = 3
```

---

## Java Implementation

```java
public class Main {

    static int linearSearch(int[] arr, int target) {

        for (int i = 0; i < arr.length; i++) {

            if (arr[i] == target) {
                return i;
            }
        }

        return -1;
    }

    public static void main(String[] args) {

        int[] arr = {10, 20, 30, 40, 50};

        int target = 40;

        int index = linearSearch(arr, target);

        System.out.println("Index: " + index);
    }
}
```

Output:

```text
Index: 3
```

---

## If Element Does Not Exist

```java
int[] arr = {10, 20, 30, 40, 50};

int target = 100;
```

The algorithm checks every element.

Since `100` does not exist:

```text
return -1
```

---

## Time Complexity

### Best Case

Target is the first element.

```text
[50, 10, 20, 30, 40]
 ↑
target
```

Only one comparison.

```text
O(1)
```

### Worst Case

Target is the last element or does not exist.

```text
O(n)
```

### Space

```text
O(1)
```

---

## Linear Search Complexity

| Case    | Complexity |
| ------- | ---------: |
| Best    |       O(1) |
| Average |       O(n) |
| Worst   |       O(n) |
| Space   |       O(1) |

---

# 2. Binary Search

Binary Search is a much faster searching algorithm for **sorted data**.

Instead of checking every element, it repeatedly divides the search space into two halves.

Example:

```text
[10, 20, 30, 40, 50, 60, 70]
             ↑
            mid
```

Suppose the target is:

```text
60
```

Compare `60` with `40`.

```text
60 > 40
```

Therefore, we know the target cannot be on the left side.

We search only:

```text
[50, 60, 70]
```

Then continue dividing.

---

# 3. Binary Search Prerequisites

Before using traditional binary search, understand these requirements.

## Requirement 1 — Data Must Be Sorted

Example:

```text
[10, 20, 30, 40, 50, 60]
```

This works.

But:

```text
[30, 10, 50, 20, 40]
```

does not work with standard binary search.

---

## Requirement 2 — Search Space Must Have an Order

Binary search works because we can determine which half can be eliminated.

For example:

```text
target > arr[mid]
```

means:

```text
Search right half
```

while:

```text
target < arr[mid]
```

means:

```text
Search left half
```

Without an ordering property, we cannot safely eliminate half the elements.

---

## Requirement 3 — Correct Search Boundaries

The most common binary-search implementation uses:

```java
int left = 0;
int right = arr.length - 1;
```

The search continues while:

```java
left <= right
```

---

# 4. Binary Search Mental Model

Suppose:

```text
arr = [10, 20, 30, 40, 50, 60, 70]
```

Initially:

```text
left = 0
right = 6
```

Calculate:

```java
int mid = left + (right - left) / 2;
```

Therefore:

```text
mid = 3
```

Element:

```text
arr[3] = 40
```

If target is `60`:

```text
60 > 40
```

Therefore:

```text
left = mid + 1
```

Now:

```text
left = 4
right = 6
```

Search:

```text
[50, 60, 70]
```

---

# 5. Why Use This Mid Formula?

You will often see:

```java
int mid = (left + right) / 2;
```

It works in many cases.

However, this version is safer against integer overflow:

```java
int mid = left + (right - left) / 2;
```

Use this version as your standard binary-search formula.

---

# 6. Iterative Binary Search

Iterative means using a loop.

The standard structure is:

```java
while (left <= right)
```

---

## Java Implementation

```java
public class Main {

    static int binarySearch(int[] arr, int target) {

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

    public static void main(String[] args) {

        int[] arr = {10, 20, 30, 40, 50, 60, 70};

        int target = 60;

        int result = binarySearch(arr, target);

        System.out.println("Index: " + result);
    }
}
```

Output:

```text
Index: 5
```

---

# 7. Iterative Binary Search Dry Run

Array:

```text
[10, 20, 30, 40, 50, 60, 70]
```

Target:

```text
60
```

### Step 1

```text
left = 0
right = 6

mid = 3

arr[mid] = 40
```

Compare:

```text
60 > 40
```

Move right:

```text
left = 4
```

---

### Step 2

```text
left = 4
right = 6

mid = 5

arr[mid] = 60
```

Found.

```text
return 5
```

---

# 8. Binary Search Complexity

Every iteration eliminates approximately half the search space.

```text
n
n/2
n/4
n/8
n/16
...
```

The number of divisions required is:

```text
log₂(n)
```

Therefore:

```text
Time = O(log n)
```

Space:

```text
O(1)
```

for iterative binary search.

---

# 9. Recursive Binary Search

Binary Search can also be implemented using recursion.

Instead of a loop:

```java
while (left <= right)
```

we repeatedly call the function with a smaller search range.

---

## Java Implementation

```java
public class Main {

    static int binarySearch(
        int[] arr,
        int left,
        int right,
        int target
    ) {

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

    public static void main(String[] args) {

        int[] arr = {10, 20, 30, 40, 50, 60, 70};

        int target = 60;

        int result = binarySearch(
            arr,
            0,
            arr.length - 1,
            target
        );

        System.out.println("Index: " + result);
    }
}
```

Output:

```text
Index: 5
```

---

# 10. Recursive Binary Search Complexity

Time:

```text
O(log n)
```

But recursive calls require stack space.

Therefore:

```text
Space = O(log n)
```

Comparison:

| Implementation |     Time | Extra Space |
| -------------- | -------: | ----------: |
| Iterative      | O(log n) |        O(1) |
| Recursive      | O(log n) |    O(log n) |

For interviews, iterative binary search is often preferred when recursion provides no benefit.

---

# 11. Lower Bound

Lower Bound is one of the most important binary-search concepts.

## Definition

For a sorted array, the **lower bound** is the first index where:

```text
arr[index] >= target
```

In other words:

> Find the first position where the value is greater than or equal to the target.

---

## Example

```text
Array:

[10, 20, 20, 20, 30, 40]
          ↑
```

Target:

```text
20
```

The lower bound is:

```text
index = 1
```

because:

```text
arr[1] = 20
```

and it is the first value:

```text
>= 20
```

---

## Another Example

```text
Array:

[10, 20, 30, 40, 50]
```

Target:

```text
25
```

There is no `25`.

The first element greater than or equal to `25` is:

```text
30
```

Therefore:

```text
lowerBound = 2
```

---

# 12. Lower Bound Java Implementation

```java
static int lowerBound(int[] arr, int target) {

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

rather than:

```java
arr.length - 1
```

Why?

Because the answer can be:

```text
arr.length
```

when the target is greater than every element.

---

## Example

```java
int[] arr = {10, 20, 20, 20, 30, 40};

System.out.println(lowerBound(arr, 20));
```

Output:

```text
1
```

---

# 13. Lower Bound Dry Run

Array:

```text
[10, 20, 20, 20, 30, 40]
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

The search looks for the **first possible position**.

Whenever:

```text
arr[mid] >= target
```

we do:

```text
right = mid
```

because `mid` might be the answer, but there could be an earlier valid position.

Eventually:

```text
left = 1
right = 1
```

Answer:

```text
1
```

---

# 14. Upper Bound

The **upper bound** is the first index where:

```text
arr[index] > target
```

Notice the difference:

```text
Lower Bound:
arr[index] >= target

Upper Bound:
arr[index] > target
```

---

## Example

```text
Array:

[10, 20, 20, 20, 30, 40]
```

Target:

```text
20
```

Lower bound:

```text
index 1
```

Upper bound:

```text
index 4
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

# 15. Upper Bound Java Implementation

```java
static int upperBound(int[] arr, int target) {

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

# 16. Lower Bound vs Upper Bound

Remember this table:

| Concept     | Condition          |
| ----------- | ------------------ |
| Lower Bound | `arr[i] >= target` |
| Upper Bound | `arr[i] > target`  |

Example:

```text
Array:
[10, 20, 20, 20, 30]
```

For target `20`:

```text
Lower Bound = 1
Upper Bound = 4
```

This becomes extremely useful for counting occurrences.

---

# 17. Counting Occurrences Using Bounds

Suppose:

```text
[10, 20, 20, 20, 20, 30]
```

Target:

```text
20
```

Then:

```text
lowerBound = 1
upperBound = 5
```

Number of occurrences:

```text
upperBound - lowerBound
```

Therefore:

```text
5 - 1 = 4
```

---

## Java

```java
static int countOccurrences(int[] arr, int target) {

    int first = lowerBound(arr, target);
    int last = upperBound(arr, target);

    return last - first;
}
```

---

# 18. First Occurrence

When duplicates exist, normal binary search may return **any occurrence**.

Example:

```text
[10, 20, 20, 20, 30]
```

Search:

```text
20
```

A normal binary search could return:

```text
1
2
3
```

But sometimes the problem asks:

> Find the first occurrence of the target.

Answer:

```text
1
```

---

# 19. First Occurrence Using Binary Search

The idea is:

1. Find the target.
2. Store the answer.
3. Continue searching left.

---

## Java

```java
static int firstOccurrence(int[] arr, int target) {

    int left = 0;
    int right = arr.length - 1;

    int answer = -1;

    while (left <= right) {

        int mid = left + (right - left) / 2;

        if (arr[mid] == target) {

            answer = mid;

            // Search for an earlier occurrence
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

# 20. First Occurrence Example

```java
int[] arr = {10, 20, 20, 20, 30};

System.out.println(firstOccurrence(arr, 20));
```

Output:

```text
1
```

---

# 21. Last Occurrence

Now suppose:

```text
[10, 20, 20, 20, 30]
```

Target:

```text
20
```

The last occurrence is:

```text
index = 3
```

The logic is similar to first occurrence.

When we find the target:

```text
Store answer
Move right
```

because we want to find a later occurrence.

---

# 22. Last Occurrence Java Implementation

```java
static int lastOccurrence(int[] arr, int target) {

    int left = 0;
    int right = arr.length - 1;

    int answer = -1;

    while (left <= right) {

        int mid = left + (right - left) / 2;

        if (arr[mid] == target) {

            answer = mid;

            // Search for a later occurrence
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

Example:

```java
int[] arr = {10, 20, 20, 20, 30};

System.out.println(lastOccurrence(arr, 20));
```

Output:

```text
3
```

---

# 23. First vs Last Occurrence

Remember:

```text
First occurrence
        ↓
Found target
        ↓
Move LEFT
```

Code:

```java
right = mid - 1;
```

---

```text
Last occurrence
        ↓
Found target
        ↓
Move RIGHT
```

Code:

```java
left = mid + 1;
```

---

# 24. Search Insert Position

This is a very common binary-search problem.

## Problem

Given a sorted array and a target:

* If target exists, return its index.
* Otherwise, return the index where it should be inserted to maintain sorted order.

---

## Example 1

```text
Array:
[10, 20, 30, 40]

Target:
30
```

Output:

```text
2
```

Because `30` already exists.

---

## Example 2

```text
Array:
[10, 20, 30, 40]

Target:
25
```

Expected:

```text
2
```

Because:

```text
[10, 20, 25, 30, 40]
        ↑
       index 2
```

---

# 25. Search Insert Position Java

This is essentially **Lower Bound**.

```java
static int searchInsert(int[] arr, int target) {

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

Example:

```java
int[] arr = {10, 20, 30, 40};

System.out.println(searchInsert(arr, 25));
```

Output:

```text
2
```

---

# 26. Search in a Sorted Array

For a sorted array, binary search should usually be your first thought.

Example:

```text
[5, 10, 15, 20, 25, 30, 35]
```

Search:

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

---

# 27. Java's Built-in Binary Search

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

However, for DSA preparation, you should know how to implement binary search manually.

---

# 28. Important Problem: Duplicates

Suppose:

```text
[10, 20, 20, 20, 30]
```

Using:

```java
Arrays.binarySearch(arr, 20);
```

does not guarantee that you receive:

```text
first occurrence
```

or:

```text
last occurrence
```

If a problem specifically asks for first or last occurrence, implement the appropriate binary-search variation.

---

# 29. Search in Rotated Sorted Array

This is one of the most important binary-search problems.

Consider a sorted array:

```text
[10, 20, 30, 40, 50, 60, 70]
```

Rotate it.

For example:

```text
[40, 50, 60, 70, 10, 20, 30]
```

It is no longer globally sorted.

However, it still contains useful structure.

At least one side of the current search range is always sorted.

This allows binary search to continue.

---

# 30. Understanding the Rotated Array

Original:

```text
[10, 20, 30, 40, 50, 60, 70]
```

After rotation:

```text
[40, 50, 60, 70, 10, 20, 30]
```

There are two sorted portions:

```text
[40, 50, 60, 70]
```

and:

```text
[10, 20, 30]
```

---

# 31. Key Observation

For:

```text
left
mid
right
```

one of these two halves must be sorted:

```text
left → mid
```

or:

```text
mid → right
```

We identify which half is sorted.

Then determine whether the target belongs to that sorted range.

---

# 32. Search in Rotated Sorted Array — Algorithm

Suppose:

```text
arr = [40, 50, 60, 70, 10, 20, 30]
```

Target:

```text
20
```

Calculate:

```text
mid
```

If:

```text
arr[left] <= arr[mid]
```

then:

```text
left half is sorted
```

Otherwise:

```text
right half is sorted
```

Then check whether the target lies inside the sorted half.

---

# 33. Java Implementation

```java
static int searchRotated(int[] arr, int target) {

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

            // Target is inside the sorted left half
            if (arr[left] <= target && target < arr[mid]) {

                right = mid - 1;

            } else {

                left = mid + 1;
            }

        } else {

            // Right half is sorted

            if (arr[mid] < target && target <= arr[right]) {

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

# 34. Rotated Search Example

```java
int[] arr = {40, 50, 60, 70, 10, 20, 30};

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

# 35. Rotated Search Dry Run

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

Therefore:

```text
Left half is sorted.
```

Left sorted range:

```text
[40, 50, 60, 70]
```

Does `20` belong there?

```text
40 <= 20 <= 70
```

No.

Therefore:

```text
Search right half
```

```text
left = mid + 1
```

Now:

```text
[10, 20, 30]
```

Continue binary search.

Eventually:

```text
arr[5] = 20
```

Found.

---

# 36. Rotated Array Complexity

For the standard rotated sorted array problem with **distinct elements**:

```text
Time  → O(log n)
Space → O(1)
```

---

# 37. What If Duplicates Exist?

Consider:

```text
[2, 5, 6, 0, 0, 1, 2]
```

Duplicates can make it impossible to determine which half is sorted using only:

```java
arr[left] <= arr[mid]
```

For example:

```text
arr[left] == arr[mid] == arr[right]
```

In such cases, we may need to shrink the boundaries:

```java
left++;
right--;
```

This can degrade the worst-case complexity to:

```text
O(n)
```

This is an important distinction between rotated-array search with and without duplicates.

---

# 38. Complete Searching Toolkit

At this point, you should recognize these patterns:

```text
Searching
│
├── Linear Search
│
└── Binary Search
      │
      ├── Iterative
      ├── Recursive
      │
      ├── Lower Bound
      ├── Upper Bound
      │
      ├── First Occurrence
      ├── Last Occurrence
      │
      ├── Search Insert Position
      │
      ├── Sorted Array Search
      │
      └── Rotated Sorted Array
```

---

# 39. Binary Search Templates

## Template 1 — Find Exact Element

```java
static int binarySearch(int[] arr, int target) {

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

# 40. Template 2 — Lower Bound

```java
static int lowerBound(int[] arr, int target) {

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

# 41. Template 3 — Upper Bound

```java
static int upperBound(int[] arr, int target) {

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

# 42. Template 4 — First Occurrence

```java
static int firstOccurrence(int[] arr, int target) {

    int left = 0;
    int right = arr.length - 1;

    int answer = -1;

    while (left <= right) {

        int mid = left + (right - left) / 2;

        if (arr[mid] == target) {

            answer = mid;
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

# 43. Template 5 — Last Occurrence

```java
static int lastOccurrence(int[] arr, int target) {

    int left = 0;
    int right = arr.length - 1;

    int answer = -1;

    while (left <= right) {

        int mid = left + (right - left) / 2;

        if (arr[mid] == target) {

            answer = mid;
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

# 44. Binary Search Mistakes to Avoid

## Mistake 1 — Using Binary Search on an Unsorted Array

Wrong:

```text
[30, 10, 50, 20, 40]
```

Standard binary search cannot safely eliminate halves.

---

## Mistake 2 — Wrong Boundary

Incorrect:

```java
while (left < right)
```

for every binary-search problem.

For exact element search using inclusive boundaries, usually:

```java
while (left <= right)
```

For lower/upper bound style search using a half-open range:

```java
while (left < right)
```

The correct condition depends on the template.

---

## Mistake 3 — Incorrect Mid

Prefer:

```java
int mid = left + (right - left) / 2;
```

---

## Mistake 4 — Infinite Loop

Incorrect:

```java
left = mid;
```

or:

```java
right = mid;
```

in a standard inclusive binary search can cause an infinite loop.

Usually use:

```java
left = mid + 1;
```

or:

```java
right = mid - 1;
```

---

## Mistake 5 — Forgetting Duplicates

Normal binary search does not necessarily give:

```text
first occurrence
```

or:

```text
last occurrence
```

Use specialized logic.

---

# 45. Searching Complexity Comparison

| Algorithm               | Sorted Required? |     Best |    Worst |    Space |
| ----------------------- | ---------------- | -------: | -------: | -------: |
| Linear Search           | No               |     O(1) |     O(n) |     O(1) |
| Binary Search           | Yes              |     O(1) | O(log n) |     O(1) |
| Recursive Binary Search | Yes              |     O(1) | O(log n) | O(log n) |
| Lower Bound             | Yes              | O(log n) | O(log n) |     O(1) |
| Upper Bound             | Yes              | O(log n) | O(log n) |     O(1) |
| Rotated Binary Search   | Rotated sorted   |     O(1) | O(log n) |     O(1) |

For rotated arrays containing duplicates, worst-case search can become:

```text
O(n)
```

---

# 46. Most Important Relationships

Memorize these relationships:

```text
Lower Bound
    ↓
First index where
arr[i] >= target
```

```text
Upper Bound
    ↓
First index where
arr[i] > target
```

```text
First Occurrence
    ↓
Lower Bound of target
```

For a target that exists, the first occurrence can be obtained using the lower-bound result.

```text
Last Occurrence
    ↓
Upper Bound(target) - 1
```

provided the target exists at that position.

```text
Search Insert Position
    ↓
Lower Bound
```

These connections significantly reduce the number of separate algorithms you need to memorize.

---

# 47. Example: All Concepts Together

Consider:

```text
arr = [10, 20, 20, 20, 30, 40, 50]
target = 20
```

### Lower Bound

```text
1
```

### Upper Bound

```text
4
```

### First Occurrence

```text
1
```

### Last Occurrence

```text
3
```

### Number of Occurrences

```text
4 - 1 = 3
```

### Search Insert Position

```text
1
```

This demonstrates how several binary-search problems are actually variations of the same fundamental idea.

---

# 48. DSA Decision Making

When you see a searching problem, ask:

```text
Is the array sorted?
        │
        ├── NO
        │    ↓
        │  Think Linear Search
        │
        └── YES
             ↓
        Think Binary Search
```

Then ask:

```text
Do duplicates matter?
        │
        ├── NO
        │    ↓
        │  Standard Binary Search
        │
        └── YES
             ↓
        First / Last / Bounds
```

Then:

```text
Is the sorted array rotated?
        │
        ├── NO
        │    ↓
        │  Normal Binary Search
        │
        └── YES
             ↓
        Rotated Binary Search
```

---

# 49. Practice Problems

After learning this section, practice these problems in order.

## Level 1 — Fundamentals

1. Implement Linear Search.
2. Implement Binary Search.
3. Search for an element in a sorted array.
4. Find the maximum element.
5. Find the minimum element.

## Level 2 — Binary Search Variations

6. Find First Occurrence.
7. Find Last Occurrence.
8. Count Occurrences.
9. Find Lower Bound.
10. Find Upper Bound.
11. Search Insert Position.

## Level 3 — Rotated Arrays

12. Search in Rotated Sorted Array.
13. Find Minimum in Rotated Sorted Array.
14. Find Rotation Count.
15. Search in Rotated Sorted Array with Duplicates.

## Level 4 — Advanced Binary Search

16. Find Peak Element.
17. Find Single Element in Sorted Array.
18. Find Square Root using Binary Search.
19. Find Minimum in Rotated Sorted Array.
20. Median of Two Sorted Arrays.
21. Kth Element of Two Sorted Arrays.

---

# 50. Final Cheat Sheet

```text
LINEAR SEARCH
─────────────
Works on any array

Time:
O(n)

Space:
O(1)
```

```text
BINARY SEARCH
─────────────
Requires ordered/sorted search space

Time:
O(log n)

Space:
O(1)
```

```text
LOWER BOUND
───────────
First index where:

arr[i] >= target
```

```text
UPPER BOUND
───────────
First index where:

arr[i] > target
```

```text
FIRST OCCURRENCE
────────────────
Found target?
Move LEFT

right = mid - 1
```

```text
LAST OCCURRENCE
───────────────
Found target?
Move RIGHT

left = mid + 1
```

```text
SEARCH INSERT POSITION
──────────────────────
Equivalent to:

LOWER BOUND
```

```text
ROTATED SORTED ARRAY
────────────────────
At least one half is sorted.

1. Find mid.
2. Determine sorted half.
3. Check whether target belongs there.
4. Eliminate the other half.
5. Repeat.
```

---

# Final Mental Model

Do not memorize binary-search problems as completely separate algorithms.

Think of them as variations of one idea:

```text
                    BINARY SEARCH
                         │
          ┌──────────────┼──────────────┐
          │              │              │
       Exact          Boundary       Rotated
       Search         Search          Search
          │              │              │
          │       ┌──────┴──────┐       │
          │       │             │       │
          │   Lower Bound   Upper Bound │
          │       │             │       │
          │       └──────┬──────┘       │
          │              │              │
          │       First / Last         │
          │       Occurrence            │
          │                             │
          └─────────────┬───────────────┘
                        │
                Search Insert Position
```

The key skill is not simply knowing the code.

You should be able to look at a problem and identify:

```text
1. Is the search space ordered?
2. Can I eliminate half?
3. What exactly am I looking for?
4. Exact value?
5. First valid position?
6. Last valid position?
7. Insertion position?
8. Rotated sorted structure?
9. Are duplicates present?
10. What should happen when the target doesn't exist?
```

Once you can answer those questions, binary search becomes a reusable **problem-solving pattern**, rather than a piece of code you have to memorize.
