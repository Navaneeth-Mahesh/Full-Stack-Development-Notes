# DSA — Arrays

## 2. Basic Array Operations in Java

Array operations are the fundamental actions performed on an array.

The core operations are:

* Traversing
* Insertion
* Deletion
* Searching
* Updating
* Reversing
* Copying
* Merging
* Comparing

Understanding these operations is essential before solving advanced array problems.

---

# 1. Traversing an Array

## What is Traversal?

**Traversal** means visiting every element of an array one by one.

Example:

```text
Array:
[10, 20, 30, 40, 50]

Traversal:
10 → 20 → 30 → 40 → 50
```

---

## Using a `for` Loop

```java
public class Main {

    public static void main(String[] args) {

        int[] arr = {10, 20, 30, 40, 50};

        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        }
    }
}
```

Output:

```text
10
20
30
40
50
```

### How it works

```text
i = 0 → arr[0]
i = 1 → arr[1]
i = 2 → arr[2]
i = 3 → arr[3]
i = 4 → arr[4]
```

### Complexity

```text
Time  → O(n)
Space → O(1)
```

---

# 2. Traversal Using Enhanced For Loop

Java provides the enhanced `for` loop.

```java
int[] arr = {10, 20, 30, 40, 50};

for (int value : arr) {
    System.out.println(value);
}
```

Here:

```text
value
  ↓
10
20
30
40
50
```

### When to use it?

Use enhanced `for` when you only need the values.

Use the normal `for` loop when you need the indexes.

---

# 3. Insertion

## What is Insertion?

Insertion means adding a new element to an array.

Java arrays have a **fixed size**, so you cannot directly increase their size.

Therefore, insertion usually means:

1. Create a larger array.
2. Shift/copy existing elements.
3. Insert the new element.

---

# Inserting at the End

Suppose:

```text
[10, 20, 30, 40]
```

We want to insert:

```text
50
```

Result:

```text
[10, 20, 30, 40, 50]
```

Java:

```java
public class Main {

    public static void main(String[] args) {

        int[] arr = {10, 20, 30, 40};

        int[] newArr = new int[arr.length + 1];

        for (int i = 0; i < arr.length; i++) {
            newArr[i] = arr[i];
        }

        newArr[arr.length] = 50;

        arr = newArr;

        for (int value : arr) {
            System.out.print(value + " ");
        }
    }
}
```

Output:

```text
10 20 30 40 50
```

### Complexity

```text
Time  → O(n)
Space → O(n)
```

---

# 4. Inserting at a Specific Position

Suppose:

```text
Original:

[10, 20, 30, 40]
```

Insert `25` at index `2`.

Expected:

```text
[10, 20, 25, 30, 40]
```

The elements after index `2` must move right.

```text
Before:

10  20  30  40
        ↓   ↓
       shift right

After:

10  20  25  30  40
```

Java:

```java
public class Main {

    public static void main(String[] args) {

        int[] arr = {10, 20, 30, 40};

        int index = 2;
        int value = 25;

        int[] newArr = new int[arr.length + 1];

        for (int i = 0; i < index; i++) {
            newArr[i] = arr[i];
        }

        newArr[index] = value;

        for (int i = index; i < arr.length; i++) {
            newArr[i + 1] = arr[i];
        }

        arr = newArr;

        for (int num : arr) {
            System.out.print(num + " ");
        }
    }
}
```

Output:

```text
10 20 25 30 40
```

### Complexity

```text
Time  → O(n)
Space → O(n)
```

---

# 5. Deletion

## What is Deletion?

Deletion means removing an element from an array.

Since Java arrays have fixed size, we generally create a new smaller array.

Suppose:

```text
[10, 20, 30, 40, 50]
```

Delete `30`.

Result:

```text
[10, 20, 40, 50]
```

---

# Delete by Index

```java
public class Main {

    public static void main(String[] args) {

        int[] arr = {10, 20, 30, 40, 50};

        int deleteIndex = 2;

        int[] newArr = new int[arr.length - 1];

        for (int i = 0, j = 0; i < arr.length; i++) {

            if (i == deleteIndex) {
                continue;
            }

            newArr[j] = arr[i];
            j++;
        }

        arr = newArr;

        for (int value : arr) {
            System.out.print(value + " ");
        }
    }
}
```

Output:

```text
10 20 40 50
```

### Complexity

```text
Time  → O(n)
Space → O(n)
```

---

# 6. Searching

## What is Searching?

Searching means finding whether a particular value exists in the array.

There are two important searching techniques:

```text
Linear Search
Binary Search
```

Binary search requires a sorted array.

---

# Linear Search

Linear search checks elements one by one.

Example:

```text
[10, 20, 30, 40, 50]
             ↑
           search 40
```

Java:

```java
public class Main {

    public static void main(String[] args) {

        int[] arr = {10, 20, 30, 40, 50};

        int target = 40;

        int index = -1;

        for (int i = 0; i < arr.length; i++) {

            if (arr[i] == target) {
                index = i;
                break;
            }
        }

        System.out.println("Index: " + index);
    }
}
```

Output:

```text
Index: 3
```

If the element does not exist:

```text
Index: -1
```

### Complexity

```text
Best Case  → O(1)
Worst Case → O(n)
Average    → O(n)
Space      → O(1)
```

---

# 7. Binary Search

Binary search works on a **sorted array**.

Example:

```text
[10, 20, 30, 40, 50, 60, 70]
```

Search for `60`.

Instead of checking every element, binary search repeatedly divides the search range in half.

### Java

```java
public class Main {

    public static void main(String[] args) {

        int[] arr = {10, 20, 30, 40, 50, 60, 70};

        int target = 60;

        int left = 0;
        int right = arr.length - 1;

        int index = -1;

        while (left <= right) {

            int mid = left + (right - left) / 2;

            if (arr[mid] == target) {
                index = mid;
                break;
            }

            if (arr[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        System.out.println("Index: " + index);
    }
}
```

Output:

```text
Index: 5
```

### Complexity

```text
Time  → O(log n)
Space → O(1)
```

Remember:

```text
Linear Search  → O(n)

Binary Search  → O(log n)
                ↓
          Sorted array required
```

---

# 8. Updating an Array

## What is Updating?

Updating means changing the value stored at a particular index.

Suppose:

```text
[10, 20, 30, 40]
```

Change index `2` to `100`.

Result:

```text
[10, 20, 100, 40]
```

Java:

```java
int[] arr = {10, 20, 30, 40};

arr[2] = 100;

System.out.println(arr[2]);
```

Output:

```text
100
```

### Complexity

```text
Time  → O(1)
Space → O(1)
```

Because the index provides direct access.

---

# 9. Reversing an Array

## What is Reversing?

Reversing means changing:

```text
[10, 20, 30, 40, 50]
```

into:

```text
[50, 40, 30, 20, 10]
```

One of the most important DSA techniques is reversing using **two pointers**.

---

# Two-Pointer Reversal

Use:

```text
left
right
```

Initially:

```text
left  = 0
right = n - 1
```

Swap:

```text
arr[left]
arr[right]
```

Then move:

```text
left++
right--
```

Continue until:

```text
left >= right
```

---

## Java Implementation

```java
public class Main {

    public static void main(String[] args) {

        int[] arr = {10, 20, 30, 40, 50};

        int left = 0;
        int right = arr.length - 1;

        while (left < right) {

            int temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;

            left++;
            right--;
        }

        for (int value : arr) {
            System.out.print(value + " ");
        }
    }
}
```

Output:

```text
50 40 30 20 10
```

### Complexity

```text
Time  → O(n)
Space → O(1)
```

This is an **in-place reversal** because we don't create another array.

---

# 10. Copying Arrays

Copying means creating another array containing the same elements.

Original:

```text
[10, 20, 30, 40]
```

Copy:

```text
[10, 20, 30, 40]
```

---

# Method 1 — Manual Copy

```java
int[] arr = {10, 20, 30, 40};

int[] copy = new int[arr.length];

for (int i = 0; i < arr.length; i++) {
    copy[i] = arr[i];
}
```

---

# Method 2 — `Arrays.copyOf()`

Java provides:

```java
Arrays.copyOf()
```

Example:

```java
import java.util.Arrays;

int[] arr = {10, 20, 30, 40};

int[] copy = Arrays.copyOf(arr, arr.length);

System.out.println(Arrays.toString(copy));
```

Output:

```text
[10, 20, 30, 40]
```

---

# Method 3 — `System.arraycopy()`

Java also provides:

```java
System.arraycopy()
```

Example:

```java
int[] arr = {10, 20, 30, 40};

int[] copy = new int[arr.length];

System.arraycopy(
    arr,
    0,
    copy,
    0,
    arr.length
);
```

Meaning:

```text
source array       → arr
source position    → 0
destination array  → copy
destination pos    → 0
number of elements → arr.length
```

### Complexity

Copying `n` elements:

```text
Time  → O(n)
Space → O(n)
```

---

# 11. Important: Reference vs Copy

This is extremely important in Java.

Consider:

```java
int[] arr = {10, 20, 30};

int[] copy = arr;
```

This does **not** create a new array.

Both variables point to the same array.

Conceptually:

```text
arr ───────┐
           ↓
       [10, 20, 30]
           ↑
copy ──────┘
```

Now:

```java
copy[0] = 100;
```

The original also changes:

```text
arr = [100, 20, 30]
```

---

## Actual Copy

Use:

```java
int[] copy = Arrays.copyOf(arr, arr.length);
```

Now:

```text
arr  → [10, 20, 30]

copy → [10, 20, 30]
```

They are separate arrays.

---

# 12. Merging Arrays

## What is Merging?

Merging means combining two arrays into one.

Example:

```text
Array 1:
[10, 20, 30]

Array 2:
[40, 50, 60]

Merged:
[10, 20, 30, 40, 50, 60]
```

---

# Manual Merge

```java
public class Main {

    public static void main(String[] args) {

        int[] arr1 = {10, 20, 30};
        int[] arr2 = {40, 50, 60};

        int[] merged = new int[arr1.length + arr2.length];

        for (int i = 0; i < arr1.length; i++) {
            merged[i] = arr1[i];
        }

        for (int i = 0; i < arr2.length; i++) {
            merged[arr1.length + i] = arr2[i];
        }

        for (int value : merged) {
            System.out.print(value + " ");
        }
    }
}
```

Output:

```text
10 20 30 40 50 60
```

### Complexity

If:

```text
arr1 size = n
arr2 size = m
```

Then:

```text
Time  → O(n + m)
Space → O(n + m)
```

---

# 13. Merging Using `System.arraycopy()`

A cleaner Java implementation:

```java
int[] arr1 = {10, 20, 30};
int[] arr2 = {40, 50, 60};

int[] merged = new int[arr1.length + arr2.length];

System.arraycopy(
    arr1,
    0,
    merged,
    0,
    arr1.length
);

System.arraycopy(
    arr2,
    0,
    merged,
    arr1.length,
    arr2.length
);
```

Result:

```text
[10, 20, 30, 40, 50, 60]
```

---

# 14. Comparing Arrays

There are several ways to compare arrays in Java.

Suppose:

```java
int[] arr1 = {10, 20, 30};
int[] arr2 = {10, 20, 30};
```

---

# Wrong Approach: `==`

Do not use:

```java
arr1 == arr2
```

to compare array contents.

`==` checks whether both references point to the same array object.

Example:

```java
int[] arr1 = {10, 20, 30};
int[] arr2 = {10, 20, 30};

System.out.println(arr1 == arr2);
```

Output:

```text
false
```

Even though the contents are identical.

---

# Correct Approach: `Arrays.equals()`

Use:

```java
import java.util.Arrays;

int[] arr1 = {10, 20, 30};
int[] arr2 = {10, 20, 30};

System.out.println(Arrays.equals(arr1, arr2));
```

Output:

```text
true
```

`Arrays.equals()` compares the elements.

---

# 15. Manual Array Comparison

You should also know how to compare arrays without using library methods.

```java
public class Main {

    public static void main(String[] args) {

        int[] arr1 = {10, 20, 30};
        int[] arr2 = {10, 20, 30};

        boolean equal = true;

        if (arr1.length != arr2.length) {
            equal = false;
        } else {

            for (int i = 0; i < arr1.length; i++) {

                if (arr1[i] != arr2[i]) {
                    equal = false;
                    break;
                }
            }
        }

        System.out.println(equal);
    }
}
```

Output:

```text
true
```

### Complexity

```text
Time  → O(n)
Space → O(1)
```

---

# 16. Complete Basic Operations Example

Here is a single Java program demonstrating several basic operations.

```java
import java.util.Arrays;

public class Main {

    public static void main(String[] args) {

        int[] arr = {10, 20, 30, 40, 50};

        // 1. Traversal
        System.out.println("Traversal:");

        for (int value : arr) {
            System.out.print(value + " ");
        }

        System.out.println();


        // 2. Access
        System.out.println("Element at index 2: " + arr[2]);


        // 3. Update
        arr[2] = 100;

        System.out.println(
            "After update: " + Arrays.toString(arr)
        );


        // 4. Search
        int target = 40;
        int index = -1;

        for (int i = 0; i < arr.length; i++) {

            if (arr[i] == target) {
                index = i;
                break;
            }
        }

        System.out.println(
            "Index of " + target + ": " + index
        );


        // 5. Copy
        int[] copy = Arrays.copyOf(arr, arr.length);

        System.out.println(
            "Copy: " + Arrays.toString(copy)
        );


        // 6. Reverse
        int left = 0;
        int right = arr.length - 1;

        while (left < right) {

            int temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;

            left++;
            right--;
        }

        System.out.println(
            "Reversed: " + Arrays.toString(arr)
        );


        // 7. Compare
        System.out.println(
            "Arrays equal: " + Arrays.equals(arr, copy)
        );
    }
}
```

---

# 17. Complexity Summary

| Operation     |     Time | Extra Space |
| ------------- | -------: | ----------: |
| Traversal     |     O(n) |        O(1) |
| Access        |     O(1) |        O(1) |
| Update        |     O(1) |        O(1) |
| Linear Search |     O(n) |        O(1) |
| Binary Search | O(log n) |        O(1) |
| Insertion     |     O(n) |        O(n) |
| Deletion      |     O(n) |        O(n) |
| Reverse       |     O(n) |        O(1) |
| Copy          |     O(n) |        O(n) |
| Merge         | O(n + m) |    O(n + m) |
| Compare       |     O(n) |        O(1) |

---

# 18. Important Java Methods

You should know these Java utilities:

```java
import java.util.Arrays;
```

### Print Array

```java
Arrays.toString(arr);
```

### Copy Array

```java
Arrays.copyOf(arr, arr.length);
```

### Compare Arrays

```java
Arrays.equals(arr1, arr2);
```

### Sort Array

```java
Arrays.sort(arr);
```

For DSA interviews, however, you should also know how to implement the underlying logic manually.

---

# 19. DSA Patterns You Learn From These Operations

These basic operations introduce several important DSA techniques.

### Traversal

```text
for loop
```

Foundation for almost every array problem.

### Insertion / Deletion

```text
Shifting elements
```

Important for understanding how arrays work internally.

### Searching

```text
Linear Search
Binary Search
```

Foundation for searching algorithms.

### Reversal

```text
Two Pointer
```

One of the most important DSA patterns.

### Copying

```text
Array creation
Memory management
```

### Merging

```text
Multiple arrays
Two-pointer techniques
Merge Sort
```

### Comparing

```text
Element-by-element comparison
```

---

# 20. Interview-Level Questions

After completing this lesson, you should be able to solve:

### Easy

1. Print all elements of an array.
2. Find the length of an array.
3. Find an element using linear search.
4. Update an element.
5. Find the maximum element.
6. Find the minimum element.
7. Reverse an array.
8. Copy an array.
9. Compare two arrays.
10. Merge two arrays.

### Medium

11. Insert an element at a given index.
12. Delete an element from a given index.
13. Remove duplicates from an array.
14. Find the second largest element.
15. Rotate an array.
16. Move all zeroes to the end.
17. Merge two sorted arrays.
18. Find common elements between two arrays.

---

# 21. Key Concepts to Remember

```text
ARRAY BASICS

Traversal
    ↓
Visit every element

Access
    ↓
arr[index]
    ↓
O(1)

Update
    ↓
arr[index] = value
    ↓
O(1)

Search
    ↓
Linear Search → O(n)
Binary Search → O(log n)

Insertion
    ↓
Shift elements
    ↓
O(n)

Deletion
    ↓
Shift elements
    ↓
O(n)

Reverse
    ↓
Two Pointers
    ↓
O(n) time
O(1) space

Copy
    ↓
Arrays.copyOf()
    ↓
O(n)

Merge
    ↓
Combine arrays
    ↓
O(n + m)

Compare
    ↓
Arrays.equals()
    ↓
O(n)
```

---

# Final Takeaway

Before moving to advanced array problems, you should be able to implement these operations **without depending entirely on Java's built-in methods**:

```text
✓ Traverse
✓ Insert
✓ Delete
✓ Search
✓ Update
✓ Reverse
✓ Copy
✓ Merge
✓ Compare
```

The most important DSA patterns introduced here are:

```text
1. Array Traversal
2. Element Shifting
3. Linear Search
4. Binary Search
5. Two Pointers
6. In-place Modification
7. Array Copying
8. Array Merging
```

These concepts become the foundation for the next topics:

```text
Array Operations
      ↓
Searching & Sorting
      ↓
Prefix Sum
      ↓
Two Pointers
      ↓
Sliding Window
      ↓
Hashing
      ↓
Subarrays
      ↓
Advanced Array Problems
```
