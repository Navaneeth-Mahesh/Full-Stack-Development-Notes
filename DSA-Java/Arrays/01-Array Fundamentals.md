# DSA — Arrays

## 1. Array Fundamentals

Arrays are one of the most important data structures in DSA.

They provide a way to store **multiple values of the same data type** under a single variable name and access those values efficiently using an **index**.

---

# 1. What is an Array?

An **array** is a linear data structure that stores a fixed number of elements of the same data type in contiguous memory locations.

### Example

```text
Array:
[10, 20, 30, 40, 50]

Index:
  0   1   2   3   4
```

In Java:

```java
int[] numbers = {10, 20, 30, 40, 50};
```

Accessing an element:

```java
System.out.println(numbers[2]);
```

Output:

```text
30
```

The index starts from `0`.

---

# 2. Array Characteristics

Important characteristics of arrays:

### 1. Fixed Size

Once an array is created, its size cannot be changed.

```java
int[] arr = new int[5];
```

This array can store exactly `5` integers.

You cannot directly increase it to `10`.

---

### 2. Same Data Type

An array normally stores elements of the same type.

```java
int[] arr = {10, 20, 30};
```

All elements are `int`.

You cannot normally do:

```java
int[] arr = {10, 20, "Hello"};
```

---

### 3. Indexed Access

Every element has an index.

```text
Value:  10  20  30  40  50
Index:   0   1   2   3   4
```

Access:

```java
arr[0]
arr[1]
arr[2]
```

---

### 4. Fast Random Access

Accessing an element using its index takes:

```text
O(1)
```

Example:

```java
System.out.println(arr[3]);
```

The computer can directly locate index `3`.

---

### 5. Ordered Collection

Elements maintain their position.

```text
[10, 20, 30, 40]
```

`10` comes before `20`, which comes before `30`.

---

### 6. Contiguous Memory Concept

In a traditional array model, elements are stored next to each other in memory.

Conceptually:

```text
Memory:

+------+------+------+------+------+
|  10  |  20  |  30  |  40  |  50  |
+------+------+------+------+------+
   0      1      2      3      4
```

This is one of the reasons indexed access is efficient.

---

# 3. Static vs Dynamic Arrays

## Static Array

A static array has a fixed size.

Example:

```java
int[] arr = new int[5];
```

It can contain:

```text
5 elements
```

The size cannot be changed after creation.

### Advantages

* Simple
* Fast access
* Memory-efficient for known sizes

### Disadvantages

* Fixed size
* May waste unused space
* Cannot automatically grow

---

# Dynamic Array

A dynamic array can grow when more space is required.

Examples in Java include:

```java
ArrayList<Integer>
```

Example:

```java
import java.util.ArrayList;

ArrayList<Integer> arr = new ArrayList<>();

arr.add(10);
arr.add(20);
arr.add(30);
```

The `ArrayList` manages resizing internally.

Conceptually:

```text
Initial capacity

[10][20][30][ ][ ]

        ↓ resize

[10][20][30][40][50][ ][ ][ ]
```

### Important DSA distinction

When studying DSA, understand the difference between:

```text
Array
    ↓
Fixed size

Dynamic Array
    ↓
Resizable
```

---

# 4. 1D Arrays

A **one-dimensional array** stores elements in a single sequence.

Example:

```java
int[] arr = {10, 20, 30, 40, 50};
```

Visualization:

```text
Index:  0   1   2   3   4
       ---------------------
Array: |10 |20 |30 |40 |50 |
       ---------------------
```

Access:

```java
System.out.println(arr[0]);
```

Output:

```text
10
```

---

## Traversing a 1D Array

Using a normal `for` loop:

```java
int[] arr = {10, 20, 30, 40, 50};

for (int i = 0; i < arr.length; i++) {
    System.out.println(arr[i]);
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

---

# 5. 2D Arrays

A 2D array is essentially an array containing arrays.

It is commonly used to represent:

* Matrices
* Tables
* Grids
* Game boards
* Graph representations

Example:

```java
int[][] matrix = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
};
```

Visualization:

```text
        Column
        0   1   2

Row 0   1   2   3
Row 1   4   5   6
Row 2   7   8   9
```

Access:

```java
System.out.println(matrix[1][2]);
```

Output:

```text
6
```

The first index represents the row.

The second index represents the column.

```text
matrix[row][column]
```

---

# 6. Traversing a 2D Array

Use nested loops.

```java
int[][] matrix = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
};

for (int i = 0; i < matrix.length; i++) {

    for (int j = 0; j < matrix[i].length; j++) {

        System.out.print(matrix[i][j] + " ");
    }

    System.out.println();
}
```

Output:

```text
1 2 3
4 5 6
7 8 9
```

### Complexity

If the matrix has `R` rows and `C` columns:

```text
Time Complexity = O(R × C)
```

---

# 7. Multidimensional Arrays

Arrays can have more than two dimensions.

Example:

```java
int[][][] arr = new int[2][3][4];
```

This represents:

```text
2 blocks
×
3 rows
×
4 columns
```

Access:

```java
arr[0][1][2]
```

Multidimensional arrays are less common in basic DSA problems but can appear in:

* Dynamic Programming
* 3D grids
* Scientific computing
* Game development
* State-space problems

---

# 8. Array Declaration and Initialization

There are several ways to create arrays in Java.

## Method 1 — Declaration

```java
int[] arr;
```

At this point, the array has not been created.

---

## Method 2 — Create Array

```java
arr = new int[5];
```

Now an array capable of storing `5` integers exists.

---

## Method 3 — Declaration + Creation

```java
int[] arr = new int[5];
```

---

## Method 4 — Direct Initialization

```java
int[] arr = {10, 20, 30, 40, 50};
```

This is commonly used when the values are already known.

---

## Default Values

When you create an array using `new`, Java initializes elements with default values.

For `int`:

```java
int[] arr = new int[5];
```

The array contains:

```text
[0, 0, 0, 0, 0]
```

Some common defaults:

| Data Type       | Default    |
| --------------- | ---------- |
| `int`           | `0`        |
| `long`          | `0`        |
| `float`         | `0.0`      |
| `double`        | `0.0`      |
| `char`          | `'\u0000'` |
| `boolean`       | `false`    |
| Reference types | `null`     |

---

# 9. Array Indexing

Indexing means accessing an element using its position.

Consider:

```java
int[] arr = {10, 20, 30, 40, 50};
```

Visualization:

```text
Value:    10   20   30   40   50
Index:     0    1    2    3    4
```

Therefore:

```java
arr[0] → 10
arr[1] → 20
arr[2] → 30
arr[3] → 40
arr[4] → 50
```

---

## First Index

Always:

```text
0
```

---

## Last Index

For an array of size `n`:

```text
Last Index = n - 1
```

Example:

```java
int[] arr = new int[10];
```

Size:

```text
10
```

Last index:

```text
9
```

---

## Accessing Invalid Index

```java
int[] arr = {10, 20, 30};

System.out.println(arr[5]);
```

This causes:

```text
ArrayIndexOutOfBoundsException
```

Valid indexes are:

```text
0, 1, 2
```

---

# 10. Array Traversal

Traversal means visiting every element of an array.

Example:

```java
int[] arr = {10, 20, 30, 40, 50};

for (int i = 0; i < arr.length; i++) {
    System.out.println(arr[i]);
}
```

---

## Enhanced For Loop

Java also provides the enhanced `for` loop.

```java
for (int value : arr) {
    System.out.println(value);
}
```

This is useful when you only need the values.

---

## Normal Loop vs Enhanced Loop

### Normal Loop

```java
for (int i = 0; i < arr.length; i++) {
    System.out.println(arr[i]);
}
```

Use when you need:

* Index
* Element modification
* Custom traversal

### Enhanced Loop

```java
for (int value : arr) {
    System.out.println(value);
}
```

Use when you only need:

* Element values

---

# 11. Array Length

Java arrays provide the:

```java
.length
```

property.

Example:

```java
int[] arr = {10, 20, 30, 40, 50};

System.out.println(arr.length);
```

Output:

```text
5
```

Important:

```java
arr.length
```

is a property.

It is NOT:

```java
arr.length()
```

---

## Size vs Last Index

If:

```text
array.length = 5
```

Then:

```text
First index = 0
Last index  = 4
```

Formula:

```text
Last Index = length - 1
```

---

# 12. Memory Representation

Understanding memory representation helps explain why array access is `O(1)`.

Suppose:

```java
int[] arr = {10, 20, 30, 40};
```

Conceptually:

```text
Memory

Address
1000 → 10
1004 → 20
1008 → 30
1012 → 40
```

Assuming an `int` occupies 4 bytes in this simplified model.

The elements are located at predictable offsets.

For index `i`:

```text
Address of arr[i]

= Base Address + (i × element size)
```

For example:

```text
arr[2]

= 1000 + (2 × 4)
= 1008
```

Therefore, the computer can directly locate the element.

This is the fundamental idea behind:

```text
Array Access = O(1)
```

---

# 13. Why Array Access is O(1)

Consider:

```java
arr[500];
```

The computer does not need to inspect:

```text
arr[0]
arr[1]
arr[2]
...
arr[499]
```

It can calculate the location directly.

Therefore:

```text
Access by index → O(1)
```

This is called **random access**.

---

# 14. Time Complexity of Array Operations

Assume an array contains `n` elements.

| Operation             | Time Complexity |
| --------------------- | --------------: |
| Access by index       |            O(1) |
| Update by index       |            O(1) |
| Search                |            O(n) |
| Insert at beginning   |            O(n) |
| Insert at middle      |            O(n) |
| Insert at end         |           O(1)* |
| Delete from beginning |            O(n) |
| Delete from middle    |            O(n) |
| Delete from end       |           O(1)* |
| Traversal             |            O(n) |

`*` These are simplified costs for a suitable fixed-size/dynamic-array context; actual insertion/deletion behavior depends on how the array is managed and whether shifting/resizing is required.

---

# 15. Access Operation

```java
int value = arr[3];
```

Complexity:

```text
Time: O(1)
Space: O(1)
```

---

# 16. Update Operation

```java
arr[2] = 100;
```

Example:

```text
Before:

[10, 20, 30, 40]

After:

[10, 20, 100, 40]
```

Complexity:

```text
Time: O(1)
```

---

# 17. Searching

Suppose:

```java
int[] arr = {10, 20, 30, 40, 50};
```

Searching for `40` using linear search:

```java
for (int i = 0; i < arr.length; i++) {

    if (arr[i] == 40) {
        System.out.println("Found");
        break;
    }
}
```

Worst case:

```text
O(n)
```

Because we may have to inspect every element.

---

# 18. Insertion

Suppose:

```text
[10, 20, 30, 40]
```

We want to insert `25` at index `2`.

Elements must shift:

```text
Before:

[10, 20, 30, 40]

       ↓ shift

[10, 20, 25, 30, 40]
```

This shifting can require:

```text
O(n)
```

time.

---

# 19. Deletion

Suppose:

```text
[10, 20, 30, 40, 50]
```

Delete `30`.

Elements after it need to shift left:

```text
[10, 20, 40, 50]
```

This can require:

```text
O(n)
```

time.

---

# 20. Space Complexity

If an array contains `n` elements:

```text
Space Complexity = O(n)
```

Example:

```java
int[] arr = new int[100];
```

The array requires space proportional to its size.

---

# 21. Auxiliary Space

Be careful to distinguish:

```text
Input Space
```

from:

```text
Auxiliary Space
```

Example:

```java
int sum = 0;

for (int value : arr) {
    sum += value;
}
```

We are using only a few extra variables.

Therefore:

```text
Auxiliary Space = O(1)
```

Even though the input array itself contains `n` elements.

---

# 22. Array Complexity Cheat Sheet

For an array of `n` elements:

```text
Access          → O(1)
Update          → O(1)
Search          → O(n)
Traversal       → O(n)
Insertion       → O(n)
Deletion        → O(n)
Space           → O(n)
```

If the array is sorted, searching can sometimes be improved using binary search:

```text
Binary Search → O(log n)
```

---

# 23. Important Array Formulas

### Last Index

```text
n - 1
```

### Number of Elements

```text
n
```

### Number of Subarrays

For an array containing `n` elements:

```text
n × (n + 1) / 2
```

Example:

```text
n = 5

5 × 6 / 2 = 15
```

So there are:

```text
15 subarrays
```

This formula becomes very important later when solving subarray problems.

---

# 24. Array vs ArrayList in Java

| Feature         | Array               | ArrayList                   |
| --------------- | ------------------- | --------------------------- |
| Size            | Fixed               | Dynamic                     |
| Primitive types | Yes                 | No direct primitive storage |
| Random access   | O(1)                | O(1)                        |
| Insert at end   | Depends on capacity | Amortized O(1)              |
| Insert middle   | O(n)                | O(n)                        |
| Delete middle   | O(n)                | O(n)                        |
| Syntax          | `int[]`             | `ArrayList<Integer>`        |

For DSA fundamentals, learn arrays first.

---

# 25. Complete Java Example

```java
public class Main {

    public static void main(String[] args) {

        // Create array
        int[] arr = {10, 20, 30, 40, 50};

        // Length
        System.out.println("Length: " + arr.length);

        // Access
        System.out.println("Element at index 2: " + arr[2]);

        // Update
        arr[2] = 100;

        // Traversal
        System.out.println("Array:");

        for (int i = 0; i < arr.length; i++) {
            System.out.println(
                "Index " + i + " = " + arr[i]
            );
        }
    }
}
```

Output:

```text
Length: 5
Element at index 2: 30

Array:
Index 0 = 10
Index 1 = 20
Index 2 = 100
Index 3 = 40
Index 4 = 50
```

---

# 26. DSA Mental Model

When you see an array problem, first ask:

```text
1. Is the array sorted?

2. Do I need an index?

3. Do I need to traverse everything?

4. Am I searching for something?

5. Am I inserting/deleting?

6. Do I need a prefix sum?

7. Can two pointers work?

8. Can sliding window work?

9. Can hashing help?

10. Can binary search work?
```

These questions will help you identify the correct DSA pattern later.

---

# 27. Key Takeaways

You should be comfortable with:

* What an array is
* Array indexing
* Zero-based indexing
* Array declaration
* Array initialization
* Array traversal
* 1D arrays
* 2D arrays
* Multidimensional arrays
* Array length
* Static vs dynamic arrays
* Basic memory representation
* Random access
* Time complexity
* Space complexity
* Array insertion
* Array deletion
* Linear search
* Binary search basics
* Java `int[]`
* Java `ArrayList`

The most important complexity concepts are:

```text
arr[i]       → O(1)

arr[i] = x   → O(1)

Search       → O(n)

Traversal    → O(n)

Insertion    → O(n)

Deletion     → O(n)

Space        → O(n)
```

Once these fundamentals are clear, the next major step is learning **array manipulation and searching techniques**, followed by patterns such as **prefix sum, two pointers, sliding window, hashing, and Kadane's algorithm**.
