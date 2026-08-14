# 6. Prefix Sum

## 1. Prefix Sum

Prefix Sum is a technique used to quickly calculate the sum of elements in an array.

Instead of calculating the sum repeatedly, we preprocess the array and store the cumulative sum.

### Example

```text
Array:
[2, 4, 6, 8, 10]

Prefix Sum:
[2, 6, 12, 20, 30]
```

Formula:

```text
prefix[i] = prefix[i - 1] + arr[i]
```

For the first element:

```text
prefix[0] = arr[0]
```

### JavaScript

```js
function prefixSum(arr) {
    const prefix = new Array(arr.length);

    prefix[0] = arr[0];

    for (let i = 1; i < arr.length; i++) {
        prefix[i] = prefix[i - 1] + arr[i];
    }

    return prefix;
}

console.log(prefixSum([2, 4, 6, 8, 10]));
// [2, 6, 12, 20, 30]
```

### Time Complexity

```text
Time:  O(n)
Space: O(n)
```

---

## 2. Suffix Sum

Suffix Sum is similar to Prefix Sum, but we calculate the sum from **right to left**.

### Example

```text
Array:
[2, 4, 6, 8, 10]

Suffix Sum:
[30, 28, 24, 18, 10]
```

Formula:

```text
suffix[i] = suffix[i + 1] + arr[i]
```

### JavaScript

```js
function suffixSum(arr) {
    const suffix = new Array(arr.length);

    suffix[arr.length - 1] = arr[arr.length - 1];

    for (let i = arr.length - 2; i >= 0; i--) {
        suffix[i] = suffix[i + 1] + arr[i];
    }

    return suffix;
}

console.log(suffixSum([2, 4, 6, 8, 10]));
// [30, 28, 24, 18, 10]
```

### Time Complexity

```text
Time:  O(n)
Space: O(n)
```

---

## 3. Prefix Sum Array

A Prefix Sum Array stores the cumulative sum up to every index.

For:

```text
arr = [3, 5, 2, 7, 4]
```

The prefix sum array is:

```text
prefix = [3, 8, 10, 17, 21]
```

Meaning:

```text
prefix[0] = 3
prefix[1] = 3 + 5 = 8
prefix[2] = 3 + 5 + 2 = 10
prefix[3] = 3 + 5 + 2 + 7 = 17
prefix[4] = 3 + 5 + 2 + 7 + 4 = 21
```

### Why use Prefix Sum?

It allows us to answer range-sum queries in **O(1)** after **O(n)** preprocessing.

---

# 4. Range Sum Queries

A range sum query asks for the sum of elements between two indices.

For:

```text
arr = [2, 4, 6, 8, 10]
```

Suppose we want:

```text
sum(1, 3)
```

That means:

```text
4 + 6 + 8 = 18
```

Using Prefix Sum:

```text
prefix = [2, 6, 12, 20, 30]
```

Formula:

```text
sum(L, R) = prefix[R] - prefix[L - 1]
```

Therefore:

```text
sum(1, 3)
= prefix[3] - prefix[0]
= 20 - 2
= 18
```

### Special Case: L = 0

If the range starts from index `0`:

```text
sum(0, R) = prefix[R]
```

### JavaScript

```js
function rangeSum(arr, L, R) {
    const prefix = new Array(arr.length);

    prefix[0] = arr[0];

    for (let i = 1; i < arr.length; i++) {
        prefix[i] = prefix[i - 1] + arr[i];
    }

    if (L === 0) {
        return prefix[R];
    }

    return prefix[R] - prefix[L - 1];
}

console.log(rangeSum([2, 4, 6, 8, 10], 1, 3));
// 18
```

### Complexity

```text
Preprocessing: O(n)
Each query:    O(1)
```

This is useful when there are **many range-sum queries**.

---

# 5. Subarray Sum Using Prefix Sum

A subarray is a **contiguous part** of an array.

Example:

```text
[2, 4, 6, 8, 10]
```

Some subarrays:

```text
[2, 4]
[4, 6, 8]
[6, 8]
[8, 10]
```

Prefix Sum can calculate the sum of any subarray efficiently.

For:

```text
arr = [2, 4, 6, 8, 10]
```

Prefix:

```text
[2, 6, 12, 20, 30]
```

To find:

```text
sum(2, 4)
```

Use:

```text
prefix[4] - prefix[1]
= 30 - 6
= 24
```

Therefore:

```text
6 + 8 + 10 = 24
```

### Formula

```text
subarraySum(L, R) =
    prefix[R] - prefix[L - 1]
```

---

# 6. Prefix Sum + HashMap

Prefix Sum + HashMap is a very important DSA pattern.

It is commonly used to solve problems such as:

* Subarray Sum Equals K
* Count subarrays with a given sum
* Longest subarray with a given sum
* Subarray with sum 0

## Core Idea

Suppose:

```text
prefix[i] = current prefix sum
```

We want a subarray whose sum is `K`.

If:

```text
currentPrefix - previousPrefix = K
```

Then:

```text
previousPrefix = currentPrefix - K
```

So we store previous prefix sums inside a HashMap.

### Example

```text
arr = [1, 2, 3]
K = 3
```

Prefix sums:

```text
1
3
6
```

At prefix `3`:

```text
3 - 3 = 0
```

We have previously seen prefix sum `0`.

Therefore:

```text
[1, 2]
```

has sum `3`.

### JavaScript

```js
function subarraySum(arr, k) {
    const map = new Map();

    // Prefix sum 0 exists once
    map.set(0, 1);

    let prefix = 0;
    let count = 0;

    for (const num of arr) {
        prefix += num;

        const required = prefix - k;

        if (map.has(required)) {
            count += map.get(required);
        }

        map.set(prefix, (map.get(prefix) || 0) + 1);
    }

    return count;
}

console.log(subarraySum([1, 2, 3], 3));
// 2
```

The two subarrays are:

```text
[1, 2]
[3]
```

### Complexity

```text
Time:  O(n)
Space: O(n)
```

---

# 7. Equilibrium Index

An **Equilibrium Index** is an index where:

```text
sum of elements on the left
=
sum of elements on the right
```

Example:

```text
arr = [1, 3, 5, 2, 2]
```

At index `2`:

```text
Left:
1 + 3 = 4

Right:
2 + 2 = 4
```

Therefore:

```text
Equilibrium Index = 2
```

## Using Prefix Sum

We can calculate the total sum first.

Then maintain a `leftSum`.

At every index:

```text
rightSum = totalSum - leftSum - arr[i]
```

If:

```text
leftSum === rightSum
```

then we found the equilibrium index.

### JavaScript

```js
function equilibriumIndex(arr) {
    const totalSum = arr.reduce((sum, num) => sum + num, 0);

    let leftSum = 0;

    for (let i = 0; i < arr.length; i++) {
        const rightSum = totalSum - leftSum - arr[i];

        if (leftSum === rightSum) {
            return i;
        }

        leftSum += arr[i];
    }

    return -1;
}

console.log(equilibriumIndex([1, 3, 5, 2, 2]));
// 2
```

### Complexity

```text
Time:  O(n)
Space: O(1)
```

---

# 8. Pivot Index

Pivot Index is very similar to Equilibrium Index.

A pivot index is an index where:

```text
sum of elements to the left
=
sum of elements to the right
```

For:

```text
arr = [1, 7, 3, 6, 5, 6]
```

At index `3`:

```text
Left:
1 + 7 + 3 = 11

Right:
5 + 6 = 11
```

Therefore:

```text
Pivot Index = 3
```

### JavaScript

```js
function pivotIndex(arr) {
    const totalSum = arr.reduce((sum, num) => sum + num, 0);

    let leftSum = 0;

    for (let i = 0; i < arr.length; i++) {
        const rightSum = totalSum - leftSum - arr[i];

        if (leftSum === rightSum) {
            return i;
        }

        leftSum += arr[i];
    }

    return -1;
}

console.log(pivotIndex([1, 7, 3, 6, 5, 6]));
// 3
```

### Complexity

```text
Time:  O(n)
Space: O(1)
```

---

# Prefix Sum Cheat Sheet

| Concept           | Main Idea                        | Complexity             |
| ----------------- | -------------------------------- | ---------------------- |
| Prefix Sum        | Cumulative sum from left         | O(n)                   |
| Suffix Sum        | Cumulative sum from right        | O(n)                   |
| Prefix Sum Array  | Store cumulative sums            | O(n)                   |
| Range Sum         | `prefix[R] - prefix[L-1]`        | O(1) per query         |
| Subarray Sum      | Difference of prefix sums        | O(1) with prefix array |
| Prefix + HashMap  | Find/count subarrays efficiently | O(n)                   |
| Equilibrium Index | Left sum = right sum             | O(n)                   |
| Pivot Index       | Left sum = right sum             | O(n)                   |

## Important Patterns to Remember

```text
1. Prefix:
   prefix[i] = prefix[i - 1] + arr[i]

2. Range Sum:
   prefix[R] - prefix[L - 1]

3. Subarray Sum:
   currentPrefix - previousPrefix = target

4. HashMap:
   Store previous prefix sums

5. Equilibrium / Pivot:
   rightSum = totalSum - leftSum - arr[i]
```

### Most Important Formula

```text
Subarray Sum = PrefixSum[R] - PrefixSum[L - 1]
```

And for Prefix Sum + HashMap:

```text
requiredPrefix = currentPrefix - target
```

These two formulas are the **core patterns** you should remember for most Prefix Sum problems.
