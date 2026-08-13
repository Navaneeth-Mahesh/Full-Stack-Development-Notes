# DSA — Arrays

## 5. Array Manipulation

Array manipulation problems focus on **modifying, rearranging, rotating, removing, and combining elements** efficiently.

These problems are extremely important because they introduce patterns such as:

* Two Pointers
* In-place modification
* Swapping
* Reversal technique
* Partitioning
* Stable vs unstable rearrangement
* Array indexing
* Space optimization

---

# 1. Reverse an Array

Reversing an array means changing the order of elements so that the first element becomes the last, the second becomes the second-last, and so on.

### Example

```text
Before:
[10, 20, 30, 40, 50]

After:
[50, 40, 30, 20, 10]
```

## Approach — Two Pointers

Use two pointers:

```text
left  → beginning
right → end
```

Swap them and move toward the center.

```text
[10, 20, 30, 40, 50]
 ↑                 ↑
left              right
```

Swap:

```text
[50, 20, 30, 40, 10]
```

Then:

```text
[50, 40, 30, 20, 10]
```

## Java

```java
public static void reverse(int[] arr) {

    int left = 0;
    int right = arr.length - 1;

    while (left < right) {

        int temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;

        left++;
        right--;
    }
}
```

### Complexity

```text
Time  → O(n)
Space → O(1)
```

This is an **in-place** algorithm because we modify the original array without creating another array.

---

# 2. Rotate Array

Array rotation means shifting elements while maintaining their relative order.

Example:

```text
Original:
[1, 2, 3, 4, 5]
```

Left rotation by 2:

```text
[3, 4, 5, 1, 2]
```

Right rotation by 2:

```text
[4, 5, 1, 2, 3]
```

---

# 3. Left Rotation

A left rotation moves elements from the beginning toward the end.

### Left Rotation by 1

```text
[1, 2, 3, 4, 5]
```

becomes:

```text
[2, 3, 4, 5, 1]
```

### Left Rotation by 2

```text
[1, 2, 3, 4, 5]
```

becomes:

```text
[3, 4, 5, 1, 2]
```

---

## Simple Approach

Store the first element, shift everything left, and put the saved element at the end.

```java
public static void leftRotateByOne(int[] arr) {

    int first = arr[0];

    for (int i = 1; i < arr.length; i++) {
        arr[i - 1] = arr[i];
    }

    arr[arr.length - 1] = first;
}
```

### Complexity

```text
Time  → O(n)
Space → O(1)
```

---

# 4. Right Rotation

Right rotation moves elements from the end toward the beginning.

### Right Rotation by 1

```text
[1, 2, 3, 4, 5]
```

becomes:

```text
[5, 1, 2, 3, 4]
```

### Right Rotation by 2

```text
[1, 2, 3, 4, 5]
```

becomes:

```text
[4, 5, 1, 2, 3]
```

---

## Java

```java
public static void rightRotateByOne(int[] arr) {

    int last = arr[arr.length - 1];

    for (int i = arr.length - 1; i > 0; i--) {
        arr[i] = arr[i - 1];
    }

    arr[0] = last;
}
```

---

# 5. Rotate by K Positions

This is a very common interview problem.

Suppose:

```text
arr = [1, 2, 3, 4, 5, 6, 7]
```

Rotate right by:

```text
k = 3
```

Result:

```text
[5, 6, 7, 1, 2, 3, 4]
```

---

## Important: Reduce K

If:

```text
n = 7
k = 10
```

Rotating by 10 is equivalent to rotating by:

```text
10 % 7 = 3
```

Therefore always do:

```java
k = k % arr.length;
```

---

# 6. Reversal Algorithm for Rotation

The most important technique for rotating an array in-place is the **reversal algorithm**.

For right rotation by `k`:

### Step 1

Reverse the entire array.

```text
[1, 2, 3, 4, 5, 6, 7]

↓

[7, 6, 5, 4, 3, 2, 1]
```

### Step 2

Reverse the first `k` elements.

```text
[7, 6, 5, 4, 3, 2, 1]

↓

[5, 6, 7, 4, 3, 2, 1]
```

### Step 3

Reverse the remaining elements.

```text
[5, 6, 7, 4, 3, 2, 1]

↓

[5, 6, 7, 1, 2, 3, 4]
```

Done.

---

## Java

```java
public static void rotateRight(int[] arr, int k) {

    int n = arr.length;

    if (n == 0) {
        return;
    }

    k = k % n;

    reverse(arr, 0, n - 1);

    reverse(arr, 0, k - 1);

    reverse(arr, k, n - 1);
}
```

Helper method:

```java
public static void reverse(
        int[] arr,
        int left,
        int right) {

    while (left < right) {

        int temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;

        left++;
        right--;
    }
}
```

### Complexity

```text
Time  → O(n)
Space → O(1)
```

This is much better than repeatedly rotating one position `k` times:

```text
O(n × k)
```

---

# 7. Left Rotation by K

For:

```text
[1, 2, 3, 4, 5]
```

left rotate by:

```text
k = 2
```

result:

```text
[3, 4, 5, 1, 2]
```

You can implement left rotation using reversal.

### Steps

Reverse first `k`:

```text
[1, 2] → [2, 1]
```

Reverse remaining:

```text
[3, 4, 5] → [5, 4, 3]
```

Then reverse the whole array:

```text
[2, 1, 5, 4, 3]
          ↓
[3, 4, 5, 1, 2]
```

## Java

```java
public static void rotateLeft(int[] arr, int k) {

    int n = arr.length;

    if (n == 0) {
        return;
    }

    k = k % n;

    reverse(arr, 0, k - 1);

    reverse(arr, k, n - 1);

    reverse(arr, 0, n - 1);
}
```

---

# 8. Move Zeroes

Problem:

> Move all zeroes to the end while maintaining the relative order of non-zero elements.

Example:

```text
[0, 1, 0, 3, 12]
```

Result:

```text
[1, 3, 12, 0, 0]
```

The important requirement is:

```text
Non-zero elements maintain their relative order.
```

---

# 9. Move Zeroes — Two Pointer Approach

Use a pointer:

```text
insertIndex
```

It represents where the next non-zero element should be placed.

### Example

```text
[0, 1, 0, 3, 12]
    ↑
insertIndex
```

Find `1` and put it at index `0`.

Then find `3` and put it at index `1`.

Then `12` at index `2`.

Finally fill the remaining positions with zeroes.

---

## Java

```java
public static void moveZeroes(int[] arr) {

    int insertIndex = 0;

    // Move non-zero elements forward
    for (int i = 0; i < arr.length; i++) {

        if (arr[i] != 0) {

            arr[insertIndex] = arr[i];

            insertIndex++;
        }
    }

    // Fill remaining positions with zero
    while (insertIndex < arr.length) {

        arr[insertIndex] = 0;

        insertIndex++;
    }
}
```

### Complexity

```text
Time  → O(n)
Space → O(1)
```

---

# 10. Rearrange Elements

Rearrangement means changing the positions of elements according to a particular condition.

Examples:

```text
Move zeroes
Move negatives
Separate even and odd
Rearrange positive and negative
Partition around a value
```

The important idea is:

> Don't immediately create another array. First check whether the problem can be solved **in-place** using pointers.

---

# 11. Rearrange Positive and Negative Numbers

Suppose:

```text
[1, -2, 3, -4, 5, -6]
```

One possible rearrangement is:

```text
[1, 3, 5, -2, -4, -6]
```

or:

```text
[-2, -4, -6, 1, 3, 5]
```

depending on the problem's requirements.

The exact output requirement matters.

---

# 12. Partition-Based Approach

Use two pointers.

```text
left
right
```

Move `left` until you find an element that belongs on the other side.

Move `right` similarly.

Then swap.

For example, if the goal is:

```text
negative → left
positive → right
```

you can partition the array.

---

## Java

```java
public static void rearrangePositiveNegative(int[] arr) {

    int left = 0;
    int right = arr.length - 1;

    while (left <= right) {

        if (arr[left] < 0) {
            left++;
        } else if (arr[right] >= 0) {
            right--;
        } else {

            int temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;

            left++;
            right--;
        }
    }
}
```

Example:

```text
Input:
[1, -2, 3, -4, 5, -6]

Possible output:
[-6, -2, -4, 3, 5, 1]
```

Notice that the relative order is **not guaranteed**.

### Complexity

```text
Time  → O(n)
Space → O(1)
```

---

# 13. Stable Rearrangement of Positive and Negative Numbers

Sometimes the problem requires the original relative order to be preserved.

Example:

```text
Input:
[1, -2, 3, -4, 5]
```

Stable positive-first result:

```text
[1, 3, 5, -2, -4]
```

Here:

```text
Positive order:
1 → 3 → 5
```

is preserved.

And:

```text
Negative order:
-2 → -4
```

is preserved.

A simple solution uses an additional array.

```java
public static int[] stableRearrange(int[] arr) {

    int[] result = new int[arr.length];

    int index = 0;

    for (int value : arr) {
        if (value >= 0) {
            result[index++] = value;
        }
    }

    for (int value : arr) {
        if (value < 0) {
            result[index++] = value;
        }
    }

    return result;
}
```

Complexity:

```text
Time  → O(n)
Space → O(n)
```

This illustrates an important trade-off:

```text
In-place
→ O(1) extra space
→ ordering may change

Stable
→ often requires O(n) extra space
→ ordering preserved
```

---

# 14. Segregate Even and Odd Numbers

Segregation means placing elements into groups based on a condition.

For example:

```text
Input:
[1, 2, 3, 4, 5, 6]
```

Possible result:

```text
[2, 4, 6, 1, 5, 3]
```

The requirement may simply be:

```text
Even numbers first
Odd numbers second
```

without requiring order preservation.

---

# 15. Two-Pointer Approach

Use:

```text
left
right
```

Move `left` while the value is already even.

Move `right` while the value is already odd.

Otherwise swap.

---

## Java

```java
public static void segregateEvenOdd(int[] arr) {

    int left = 0;
    int right = arr.length - 1;

    while (left < right) {

        while (left < right && arr[left] % 2 == 0) {
            left++;
        }

        while (left < right && arr[right] % 2 != 0) {
            right--;
        }

        if (left < right) {

            int temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;

            left++;
            right--;
        }
    }
}
```

### Complexity

```text
Time  → O(n)
Space → O(1)
```

---

# 16. Remove Duplicates

There are different versions of this problem.

The most common array version assumes the array is **sorted**.

Example:

```text
[1, 1, 2, 2, 3, 4, 4]
```

After removing duplicates:

```text
[1, 2, 3, 4]
```

---

# 17. Remove Duplicates from Sorted Array

Use two pointers.

```text
read pointer
write pointer
```

The `write` pointer represents the position where the next unique element should go.

---

## Example

```text
[1, 1, 2, 2, 3]
```

Start:

```text
unique:
1
```

Find:

```text
2
```

Place it next:

```text
[1, 2, ...]
```

Then:

```text
3
```

Result:

```text
[1, 2, 3, ...]
```

---

## Java

```java
public static int removeDuplicates(int[] arr) {

    if (arr.length == 0) {
        return 0;
    }

    int write = 1;

    for (int read = 1; read < arr.length; read++) {

        if (arr[read] != arr[read - 1]) {

            arr[write] = arr[read];

            write++;
        }
    }

    return write;
}
```

The returned value represents the number of unique elements.

Example:

```java
int[] arr = {1, 1, 2, 2, 3};

int length = removeDuplicates(arr);

System.out.println(length);
```

Output:

```text
3
```

The meaningful portion of the array is:

```text
[1, 2, 3]
```

### Complexity

```text
Time  → O(n)
Space → O(1)
```

---

# 18. Remove Element

Problem:

> Remove all occurrences of a given value in-place.

Example:

```text
arr = [3, 2, 2, 3]
target = 3
```

After removal:

```text
[2, 2]
```

The new length is:

```text
2
```

---

## Two-Pointer Approach

Use:

```text
write
```

Whenever the current value is not equal to the target, copy it to the `write` position.

---

## Java

```java
public static int removeElement(
        int[] arr,
        int target) {

    int write = 0;

    for (int read = 0; read < arr.length; read++) {

        if (arr[read] != target) {

            arr[write] = arr[read];

            write++;
        }
    }

    return write;
}
```

Example:

```java
int[] arr = {3, 2, 2, 3};

int length = removeElement(arr, 3);

System.out.println(length);
```

Output:

```text
2
```

Valid portion:

```text
[2, 2]
```

### Complexity

```text
Time  → O(n)
Space → O(1)
```

---

# 19. Merge Sorted Arrays

Suppose we have:

```text
A = [1, 3, 5, 7]

B = [2, 4, 6, 8]
```

Merge them into:

```text
[1, 2, 3, 4, 5, 6, 7, 8]
```

Because both arrays are already sorted, we don't need to sort again.

---

# 20. Two-Pointer Merge

Use:

```text
i → Array A
j → Array B
```

Compare:

```text
A[i]
B[j]
```

Take the smaller element and move that pointer.

---

## Example

```text
A = [1, 3, 5]
B = [2, 4, 6]
```

Compare:

```text
1 vs 2 → take 1
```

Then:

```text
3 vs 2 → take 2
```

Then:

```text
3 vs 4 → take 3
```

Continue until both arrays are processed.

---

## Java

```java
public static int[] mergeSortedArrays(
        int[] a,
        int[] b) {

    int[] result = new int[a.length + b.length];

    int i = 0;
    int j = 0;
    int k = 0;

    while (i < a.length && j < b.length) {

        if (a[i] <= b[j]) {
            result[k++] = a[i++];
        } else {
            result[k++] = b[j++];
        }
    }

    while (i < a.length) {
        result[k++] = a[i++];
    }

    while (j < b.length) {
        result[k++] = b[j++];
    }

    return result;
}
```

### Complexity

```text
Time  → O(n + m)
Space → O(n + m)
```

where:

```text
n = length of first array
m = length of second array
```

---

# 21. Why Not Sort After Combining?

You could do:

```text
A + B
↓
Create combined array
↓
Sort
```

Complexity:

```text
O((n + m) log(n + m))
```

But because both arrays are already sorted, the two-pointer technique does:

```text
O(n + m)
```

This is significantly better.

---

# 22. Core Techniques in Array Manipulation

Most problems in this section can be categorized into a few patterns.

### Pattern 1 — Two Pointers

Used for:

```text
Reverse Array
Segregate Even/Odd
Partition Positive/Negative
Move Zeroes
```

---

### Pattern 2 — Read/Write Pointers

Used for:

```text
Remove Duplicates
Remove Element
Move Zeroes
```

Think:

```text
read  → scans the array
write → constructs the valid portion
```

---

### Pattern 3 — Reversal

Used for:

```text
Rotate Array
Left Rotation
Right Rotation
Rotate by K
```

The key technique:

```text
Reverse → Reverse → Reverse
```

---

### Pattern 4 — Merging

Used for:

```text
Merge Sorted Arrays
```

The core idea:

```text
Two sorted arrays
       ↓
Two pointers
       ↓
Always take the smaller element
```

---

# 23. Complexity Summary

| Problem                     |     Time | Extra Space |
| --------------------------- | -------: | ----------: |
| Reverse Array               |     O(n) |        O(1) |
| Left Rotation by 1          |     O(n) |        O(1) |
| Right Rotation by 1         |     O(n) |        O(1) |
| Rotate by K                 |     O(n) |        O(1) |
| Move Zeroes                 |     O(n) |        O(1) |
| Rearrange Positive/Negative |     O(n) |       O(1)* |
| Stable Positive/Negative    |     O(n) |        O(n) |
| Segregate Even/Odd          |     O(n) |        O(1) |
| Remove Duplicates           |     O(n) |        O(1) |
| Remove Element              |     O(n) |        O(1) |
| Merge Sorted Arrays         | O(n + m) |    O(n + m) |

`*` In-place partitioning does not guarantee preservation of relative order.

---

# 24. Important DSA Concepts to Remember

## In-Place

An operation is **in-place** when it modifies the original array using little or no additional memory.

Example:

```java
reverse(arr);
```

uses:

```text
O(1)
```

extra space.

---

## Stable

A rearrangement is **stable** when equal/category elements maintain their original relative order.

Example:

```text
[1, -2, 3, -4, 5]
```

Positive elements:

```text
1 → 3 → 5
```

If this order remains the same after rearrangement, the operation is stable with respect to the positives.

---

# 25. Pattern Recognition Cheat Sheet

```text
ARRAY MANIPULATION
│
├── Reverse
│   └── Two Pointers
│
├── Rotate
│   ├── Left Rotation
│   ├── Right Rotation
│   └── Reversal Algorithm
│
├── Move Zeroes
│   └── Read / Write Pointer
│
├── Rearrange
│   ├── Positive / Negative
│   └── Even / Odd
│
├── Remove
│   ├── Duplicates
│   └── Element
│
└── Merge
    └── Two Pointers
```

---

# 26. What You Should Be Able to Implement

Before moving forward, you should be comfortable implementing these **without looking at the solution**:

```text
✓ Reverse an Array

✓ Left Rotate by 1

✓ Right Rotate by 1

✓ Left Rotate by K

✓ Right Rotate by K

✓ Move Zeroes

✓ Rearrange Positive and Negative Numbers

✓ Segregate Even and Odd Numbers

✓ Remove Duplicates from Sorted Array

✓ Remove Element

✓ Merge Two Sorted Arrays
```

The most important patterns from this section are:

```text
Two Pointers
      ↓
Read / Write Pointers
      ↓
Reversal Technique
      ↓
Partitioning
      ↓
Merging
```

These patterns will repeatedly appear in **strings, linked lists, sorting, sliding window, and many interview problems**.
