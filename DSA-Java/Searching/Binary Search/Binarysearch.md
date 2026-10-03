Absolutely. Since you understand Linear Search, Binary Search is the perfect next step.

# Binary Search

**Binary Search** is a searching technique used to find an element in a **sorted array**.

The main idea is:

> Instead of checking every element, we check the middle element and eliminate half of the array each time.

---

## 1. Why do we need Binary Search?

Suppose we have:

```text
[10, 20, 30, 40, 50, 60, 70]
```

and we want to find:

```text
60
```

### Linear Search

Linear Search checks:

```text
10 ❌
20 ❌
30 ❌
40 ❌
50 ❌
60 ✅
```

Potentially, we have to check every element.

### Binary Search

Binary Search starts from the middle:

```text
[10, 20, 30, 40, 50, 60, 70]
             ↑
            40
```

We want `60`.

Since:

```text
60 > 40
```

we know `60` **cannot be on the left side**.

So we throw away:

```text
10 20 30 40
```

and only search:

```text
50 60 70
```

Then check the middle again:

```text
50 60 70
   ↑
  60
```

Found!

That's the basic idea.

---

# 2. The most important condition

The array **must be sorted**.

This works:

```text
[10, 20, 30, 40, 50, 60]
```

This doesn't work with normal binary search:

```text
[30, 10, 50, 20, 60, 40]
```

Why?

Because Binary Search makes decisions like:

> "The target is greater than the middle, so I'll search the right side."

That decision is only valid when the array is sorted.

---

# 3. Three important variables

Binary Search uses:

```java
int low;
int mid;
int high;
```

Think of them as boundaries.

For:

```text
[10, 20, 30, 40, 50, 60, 70]
```

initially:

```text
low = 0
high = 6
```

Because indexes are:

```text
Index:  0   1   2   3   4   5   6
Value: 10  20  30  40  50  60  70
```

Then we calculate:

```java
mid = low + (high - low) / 2;
```

So:

```text
mid = 0 + (6 - 0) / 2
    = 3
```

Therefore:

```text
arr[mid] = arr[3] = 40
```

---

# 4. Compare the target with middle

Suppose:

```java
target = 60;
```

We compare:

```text
target = 60
middle = 40
```

Since:

```text
60 > 40
```

we search the **right half**.

So:

```java
low = mid + 1;
```

Which becomes:

```text
low = 4
```

Now our search area is:

```text
[50, 60, 70]
 ↑       ↑
low     high
```

Then calculate `mid` again:

```text
low = 4
high = 6

mid = 4 + (6 - 4) / 2
    = 5
```

```text
arr[5] = 60
```

Target found.

---

# 5. What if target is smaller?

Suppose:

```text
target = 20
```

Initial middle is:

```text
40
```

We compare:

```text
20 < 40
```

Therefore, target must be on the **left side**.

So:

```java
high = mid - 1;
```

Now:

```text
high = 2
```

and we search:

```text
[10, 20, 30]
```

---

# 6. The three possibilities

Every time we calculate `mid`, there are only three possibilities.

### Case 1 — Found

```java
if (arr[mid] == target)
```

Return the index.

### Case 2 — Target is greater

```java
else if (arr[mid] < target)
```

Search right:

```java
low = mid + 1;
```

### Case 3 — Target is smaller

```java
else
```

Search left:

```java
high = mid - 1;
```

---

# 7. Java Code

Now the complete code will make sense:

```java
public class BinarySearch {

    public static void main(String[] args) {

        int[] arr = {10, 20, 30, 40, 50, 60, 70};

        int target = 60;

        int low = 0;
        int high = arr.length - 1;

        while (low <= high) {

            int mid = low + (high - low) / 2;

            if (arr[mid] == target) {
                System.out.println("Element Found at index: " + mid);
                return;
            }

            else if (arr[mid] < target) {
                low = mid + 1;
            }

            else {
                high = mid - 1;
            }
        }

        System.out.println("Element Not Found");
    }
}
```

Output:

```text
Element Found at index: 5
```

---

# 8. Understand the logic, not the code

The entire Binary Search algorithm can be remembered as:

```text
        Find middle
             ↓
       Is middle target?
        /          \
      YES           NO
       ↓             ↓
     Found      Compare target
                 /        \
        target smaller   target greater
             ↓                ↓
        high = mid - 1   low = mid + 1
```

The most important lines are:

```java
int mid = low + (high - low) / 2;
```

```java
low = mid + 1;
```

```java
high = mid - 1;
```

---

# 9. Complexity

This is why Binary Search is important.

### Linear Search

```text
O(n)
```

### Binary Search

```text
O(log n)
```

For a million elements, Binary Search needs only around **20 halving steps** in the worst case.

---

## Your first Binary Search practice

Don't write the code immediately. **Dry-run this first:**

```java
int[] arr = {10, 20, 30, 40, 50, 60, 70, 80, 90};

int target = 80;
```
