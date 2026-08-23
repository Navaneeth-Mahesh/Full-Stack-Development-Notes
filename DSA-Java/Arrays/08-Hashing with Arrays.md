# 9. Hashing with Arrays

Hashing is one of the most important techniques in DSA for solving array problems efficiently.

The basic idea is:

> **Use extra space to store information about elements so that we can find, count, or check them quickly.**

Without hashing, many array problems require repeatedly scanning the array, which can lead to `O(n²)` time complexity.

With hashing, many of these problems can be reduced to `O(n)` average time.

---

## 9.1 What is Hashing?

Hashing is a technique that stores data in a structure where we can perform operations such as:

* Search
* Insert
* Delete
* Count frequency

efficiently.

In Java, the most commonly used hashing data structures are:

```java
HashMap
HashSet
```

Example:

```java
HashMap<Integer, Integer> map = new HashMap<>();
```

The first `Integer` represents the key.

The second `Integer` represents the value.

For example:

```text
Number → Frequency

5 → 3
2 → 1
7 → 4
```

---

# 9.2 Why Hashing is Useful in Arrays

Consider:

```text
arr = [2, 5, 2, 7, 5, 2]
```

Suppose we want to count how many times each number appears.

A brute-force approach may repeatedly scan the array.

Hashing allows us to build:

```text
2 → 3
5 → 2
7 → 1
```

Now we can retrieve the frequency of `2` quickly.

### Typical Complexity

For `HashMap` and `HashSet`:

```text
Average Search:   O(1)
Average Insert:   O(1)
Average Delete:   O(1)
```

Therefore, processing an array of `n` elements is often:

```text
O(n)
```

---

# 9.3 Frequency Array

A **Frequency Array** is the simplest form of hashing when the possible values are within a small, known range.

For example:

```text
arr = [1, 2, 2, 3, 1, 4, 2]
```

We can create:

```java
int[] freq = new int[5];
```

Then:

```java
for (int num : arr) {
    freq[num]++;
}
```

Result:

```text
Number:    0  1  2  3  4
Frequency: 0  2  3  1  1
```

Therefore:

```text
1 → 2
2 → 3
3 → 1
4 → 1
```

---

## Why Does `freq[num]++` Work?

Suppose:

```text
num = 2
```

Initially:

```text
freq[2] = 0
```

After seeing `2`:

```text
freq[2] = 1
```

Another `2`:

```text
freq[2] = 2
```

Another:

```text
freq[2] = 3
```

Therefore:

```java
freq[num]++;
```

means:

> Increase the frequency of this number by one.

---

# 9.4 Frequency Array Example

```java
public class Main {

    public static void main(String[] args) {

        int[] arr = {1, 2, 2, 3, 1, 4, 2};

        int[] freq = new int[5];

        for (int num : arr) {
            freq[num]++;
        }

        for (int i = 0; i < freq.length; i++) {

            if (freq[i] > 0) {
                System.out.println(
                    i + " -> " + freq[i]
                );
            }
        }
    }
}
```

Output:

```text
1 -> 2
2 -> 3
3 -> 1
4 -> 1
```

### Complexity

```text
Time:  O(n + k)
Space: O(k)
```

where `k` is the value range.

---

# 9.5 When Should You Use a Frequency Array?

Frequency arrays are ideal when:

```text
Values are integers
AND
The value range is relatively small
```

For example:

```text
0 to 100
1 to 1000
ASCII characters
Grades
Dice values
```

Example:

```java
int[] freq = new int[101];
```

works well for values from:

```text
0 → 100
```

---

## Problem with Frequency Arrays

Suppose:

```text
arr = [10, 1000000000]
```

Creating:

```java
int[] freq = new int[1000000001];
```

would waste enormous memory.

In such cases, use:

```java
HashMap
```

instead.

---

# 9.6 HashMap with Arrays

`HashMap` stores data as:

```text
Key → Value
```

Example:

```java
HashMap<Integer, Integer> map = new HashMap<>();
```

For frequency counting:

```text
Number → Frequency
```

Example:

```text
2 → 3
5 → 2
7 → 1
```

---

## Basic HashMap Operations

### Create

```java
HashMap<Integer, Integer> map = new HashMap<>();
```

### Insert

```java
map.put(5, 10);
```

### Get

```java
int value = map.get(5);
```

### Check Key

```java
map.containsKey(5);
```

### Remove

```java
map.remove(5);
```

### Size

```java
map.size();
```

---

# 9.7 Frequency Counting with HashMap

Consider:

```text
arr = [2, 5, 2, 7, 5, 2]
```

We want:

```text
2 → 3
5 → 2
7 → 1
```

### Java

```java
import java.util.HashMap;

public class Main {

    public static void main(String[] args) {

        int[] arr = {2, 5, 2, 7, 5, 2};

        HashMap<Integer, Integer> map =
            new HashMap<>();

        for (int num : arr) {

            map.put(
                num,
                map.getOrDefault(num, 0) + 1
            );
        }

        System.out.println(map);
    }
}
```

The important line is:

```java
map.getOrDefault(num, 0) + 1
```

Meaning:

```text
If num exists:
    get its current frequency

Otherwise:
    use 0

Then:
    increase by 1
```

---

# 9.8 HashSet with Arrays

A `HashSet` stores **unique elements**.

Unlike `HashMap`:

```text
HashMap:
Key → Value
```

HashSet:

```text
Only values
```

Example:

```java
HashSet<Integer> set = new HashSet<>();
```

If we insert:

```text
1
2
2
3
3
3
```

The set contains:

```text
[1, 2, 3]
```

Duplicates are automatically ignored.

---

## Basic HashSet Operations

### Create

```java
HashSet<Integer> set = new HashSet<>();
```

### Add

```java
set.add(10);
```

### Check

```java
set.contains(10);
```

### Remove

```java
set.remove(10);
```

### Size

```java
set.size();
```

---

# 9.9 Duplicate Detection

One of the simplest applications of `HashSet` is detecting duplicates.

Example:

```text
arr = [1, 2, 3, 4, 2]
```

We need to determine whether any value occurs more than once.

### Java

```java
import java.util.HashSet;

class Solution {

    public boolean containsDuplicate(int[] nums) {

        HashSet<Integer> set = new HashSet<>();

        for (int num : nums) {

            if (set.contains(num)) {
                return true;
            }

            set.add(num);
        }

        return false;
    }
}
```

### How it works

Process:

```text
1
```

Set:

```text
{1}
```

Process:

```text
2
```

Set:

```text
{1, 2}
```

Process:

```text
3
```

Set:

```text
{1, 2, 3}
```

Process:

```text
4
```

Set:

```text
{1, 2, 3, 4}
```

Process:

```text
2
```

`2` already exists.

Therefore:

```text
Duplicate found
```

### Complexity

```text
Time:  O(n) average
Space: O(n)
```

---

# 9.10 Frequency Counting

Frequency counting means determining how many times each value appears.

Example:

```text
arr = [4, 2, 4, 1, 2, 4]
```

Frequency:

```text
1 → 1
2 → 2
4 → 3
```

---

## Using Frequency Array

```java
int[] freq = new int[5];

for (int num : arr) {
    freq[num]++;
}
```

---

## Using HashMap

```java
HashMap<Integer, Integer> freq = new HashMap<>();

for (int num : arr) {
    freq.put(
        num,
        freq.getOrDefault(num, 0) + 1
    );
}
```

---

# 9.11 Frequency Array vs HashMap

| Feature        | Frequency Array     | HashMap                    |
| -------------- | ------------------- | -------------------------- |
| Data type      | Usually integers    | Any suitable object types  |
| Value range    | Small/known         | Large/unbounded            |
| Memory         | Depends on range    | Depends on unique elements |
| Average lookup | O(1)                | O(1)                       |
| Simplicity     | Very simple         | Slightly more code         |
| Best use       | Small integer range | General-purpose hashing    |

Example:

```text
Values: 0 → 100
```

Use:

```text
Frequency Array
```

Example:

```text
Values:
-1000000000
500000000
999999999
```

Use:

```text
HashMap
```

---

# 9.12 First Unique Element

The First Unique Element is the first element whose frequency is exactly `1`.

Example:

```text
arr = [4, 5, 1, 2, 0, 4]
```

Frequencies:

```text
4 → 2
5 → 1
1 → 1
2 → 1
0 → 1
```

The first unique element is:

```text
5
```

---

## Two Pass Approach

### Step 1

Count frequencies.

### Step 2

Traverse the array again and find the first element whose frequency is `1`.

### Java

```java
import java.util.HashMap;

class Solution {

    public int firstUnique(int[] arr) {

        HashMap<Integer, Integer> freq =
            new HashMap<>();

        for (int num : arr) {

            freq.put(
                num,
                freq.getOrDefault(num, 0) + 1
            );
        }

        for (int num : arr) {

            if (freq.get(num) == 1) {
                return num;
            }
        }

        return -1;
    }
}
```

### Complexity

```text
Time:  O(n)
Space: O(n)
```

---

# 9.13 Majority Element

A majority element is an element that appears more than:

```text
n / 2
```

times.

Example:

```text
arr = [2, 2, 1, 1, 1, 2, 2]
```

Array size:

```text
n = 7
```

Majority threshold:

```text
7 / 2 = 3
```

`2` appears `4` times.

Therefore:

```text
Answer = 2
```

---

## HashMap Approach

Count every element.

```java
import java.util.HashMap;

class Solution {

    public int majorityElement(int[] nums) {

        HashMap<Integer, Integer> map =
            new HashMap<>();

        int n = nums.length;

        for (int num : nums) {

            int count =
                map.getOrDefault(num, 0) + 1;

            map.put(num, count);

            if (count > n / 2) {
                return num;
            }
        }

        return -1;
    }
}
```

Complexity:

```text
Time:  O(n)
Space: O(n)
```

---

## Important Alternative: Boyer-Moore Voting Algorithm

For the classic majority-element problem, we can do even better in terms of space.

```java
class Solution {

    public int majorityElement(int[] nums) {

        int candidate = 0;
        int count = 0;

        for (int num : nums) {

            if (count == 0) {
                candidate = num;
            }

            if (num == candidate) {
                count++;
            } else {
                count--;
            }
        }

        return candidate;
    }
}
```

Complexity:

```text
Time:  O(n)
Space: O(1)
```

Hashing is still important because the problem belongs to the frequency/counting pattern.

---

# 9.14 Pair Sum Using Hashing

Pair Sum can be solved using a HashSet or HashMap.

Example:

```text
arr = [2, 7, 11, 15]
target = 9
```

We need:

```text
2 + 7 = 9
```

---

## HashSet Approach

For every number:

```text
complement = target - number
```

Check whether the complement already exists.

### Java

```java
import java.util.HashSet;

class Solution {

    public boolean hasPairSum(
        int[] nums,
        int target
    ) {

        HashSet<Integer> set =
            new HashSet<>();

        for (int num : nums) {

            int complement = target - num;

            if (set.contains(complement)) {
                return true;
            }

            set.add(num);
        }

        return false;
    }
}
```

### Example

```text
target = 9

num = 2
complement = 7
```

`7` does not exist.

Store:

```text
{2}
```

Next:

```text
num = 7
complement = 2
```

`2` exists.

Therefore:

```text
Pair found
```

### Complexity

```text
Time:  O(n) average
Space: O(n)
```

---

# 9.15 HashMap Pair Sum

If the problem asks for indices, use a `HashMap`.

Store:

```text
value → index
```

Example:

```text
2 → 0
7 → 1
```

### Java

```java
import java.util.HashMap;

class Solution {

    public int[] twoSum(
        int[] nums,
        int target
    ) {

        HashMap<Integer, Integer> map =
            new HashMap<>();

        for (int i = 0; i < nums.length; i++) {

            int complement =
                target - nums[i];

            if (map.containsKey(complement)) {

                return new int[] {
                    map.get(complement),
                    i
                };
            }

            map.put(nums[i], i);
        }

        return new int[] {-1, -1};
    }
}
```

---

# 9.16 Subarray Sum

Subarray problems are extremely important.

A **subarray** is a contiguous portion of an array.

Example:

```text
arr = [1, 2, 3, 4]
```

Valid subarrays include:

```text
[1]
[2]
[3]
[4]
[1,2]
[2,3]
[3,4]
[1,2,3]
[2,3,4]
[1,2,3,4]
```

But:

```text
[1,3]
```

is not a subarray because the elements are not contiguous.

---

# 9.17 Subarray Sum Equals K

Problem:

> Count the number of subarrays whose sum equals `k`.

Example:

```text
arr = [1, 1, 1]
k = 2
```

Valid subarrays:

```text
[1,1]
[1,1]
```

Answer:

```text
2
```

---

## Prefix Sum Idea

Suppose the current prefix sum is:

```text
currentSum
```

We want:

```text
currentSum - previousSum = k
```

Therefore:

```text
previousSum = currentSum - k
```

So while traversing the array, we can check whether:

```text
currentSum - k
```

has appeared before.

This is where `HashMap` becomes extremely powerful.

---

# 9.18 Subarray Sum Using HashMap

### Java

```java
import java.util.HashMap;

class Solution {

    public int subarraySum(
        int[] nums,
        int k
    ) {

        HashMap<Integer, Integer> map =
            new HashMap<>();

        map.put(0, 1);

        int prefixSum = 0;
        int count = 0;

        for (int num : nums) {

            prefixSum += num;

            int required =
                prefixSum - k;

            if (map.containsKey(required)) {

                count += map.get(required);
            }

            map.put(
                prefixSum,
                map.getOrDefault(prefixSum, 0) + 1
            );
        }

        return count;
    }
}
```

---

# 9.19 Why `map.put(0, 1)`?

This is extremely important.

Consider:

```text
arr = [3]
k = 3
```

After processing `3`:

```text
prefixSum = 3
```

Required:

```text
3 - 3 = 0
```

We need to know that prefix sum `0` existed before the array started.

Therefore:

```java
map.put(0, 1);
```

means:

> There is one occurrence of prefix sum zero before processing any elements.

---

# 9.20 Subarray Sum Example

Consider:

```text
arr = [1, 2, 3]
k = 3
```

Initially:

```text
map = {0=1}
prefixSum = 0
count = 0
```

Process `1`:

```text
prefixSum = 1
required = -2
```

Not found.

Store:

```text
{0=1, 1=1}
```

Process `2`:

```text
prefixSum = 3
required = 0
```

`0` exists.

Therefore:

```text
count = 1
```

The subarray is:

```text
[1,2]
```

Process `3`:

```text
prefixSum = 6
required = 3
```

`3` exists.

Therefore:

```text
count = 2
```

The second subarray is:

```text
[3]
```

Answer:

```text
2
```

---

# 9.21 Longest Consecutive Sequence

Problem:

Given an unsorted array, find the length of the longest sequence of consecutive integers.

Example:

```text
arr = [100, 4, 200, 1, 3, 2]
```

The longest consecutive sequence is:

```text
1, 2, 3, 4
```

Therefore:

```text
Answer = 4
```

---

# 9.22 Why Sorting is Not Ideal

Sorting gives:

```text
O(n log n)
```

We can do better using hashing.

Use:

```java
HashSet<Integer>
```

to get average `O(1)` lookups.

---

# 9.23 Longest Consecutive Sequence Using HashSet

### Java

```java
import java.util.HashSet;

class Solution {

    public int longestConsecutive(int[] nums) {

        HashSet<Integer> set =
            new HashSet<>();

        for (int num : nums) {
            set.add(num);
        }

        int longest = 0;

        for (int num : set) {

            // Start only if num is
            // the beginning of a sequence
            if (!set.contains(num - 1)) {

                int current = num;
                int length = 1;

                while (set.contains(current + 1)) {

                    current++;
                    length++;
                }

                longest =
                    Math.max(longest, length);
            }
        }

        return longest;
    }
}
```

---

# 9.24 Why Check `num - 1`?

This is the key optimization.

Suppose:

```text
set = {1, 2, 3, 4}
```

For `2`:

```text
2 - 1 = 1
```

`1` exists.

Therefore `2` is not the beginning.

For `1`:

```text
1 - 1 = 0
```

`0` does not exist.

Therefore `1` is the beginning of the sequence.

We start counting from `1`:

```text
1 → 2 → 3 → 4
```

This prevents repeatedly scanning the same sequence.

---

# 9.25 Longest Consecutive Sequence Complexity

Building the set:

```text
O(n)
```

Checking sequences:

```text
O(n) average
```

Therefore:

```text
Time:  O(n) average
Space: O(n)
```

This is better than:

```text
Sorting:
O(n log n)
```

---

# 9.26 HashMap vs HashSet

Understanding the difference is extremely important.

## HashMap

Stores:

```text
Key → Value
```

Use when you need:

* Frequency
* Index
* Mapping
* Associated information

Example:

```text
Number → Frequency
Number → Index
```

---

## HashSet

Stores only:

```text
Unique Values
```

Use when you need:

* Duplicate detection
* Fast existence checking
* Unique elements
* Consecutive sequence detection

---

# 9.27 Choosing the Correct Hashing Structure

Ask:

### Do I need frequency?

Use:

```text
HashMap
```

Example:

```text
number → count
```

---

### Do I need index?

Use:

```text
HashMap
```

Example:

```text
number → index
```

---

### Do I only need to know whether something exists?

Use:

```text
HashSet
```

Example:

```text
Does 10 exist?
```

---

### Are values small integers?

Consider:

```text
Frequency Array
```

Example:

```text
0 → 100
```

---

# 9.28 Common Hashing Patterns

Most array hashing problems can be categorized into a few patterns.

## Pattern 1: Frequency Counting

```text
Array
 ↓
HashMap
 ↓
Element → Frequency
```

Problems:

```text
Frequency Counting
Majority Element
First Unique Element
```

---

## Pattern 2: Existence Checking

```text
Array
 ↓
HashSet
 ↓
Does element exist?
```

Problems:

```text
Duplicate Detection
Longest Consecutive Sequence
```

---

## Pattern 3: Value → Index

```text
Array
 ↓
HashMap
 ↓
Value → Index
```

Problem:

```text
Two Sum
```

---

## Pattern 4: Prefix Sum + HashMap

```text
Array
 ↓
Prefix Sum
 ↓
HashMap
 ↓
Find previous required sum
```

Problems:

```text
Subarray Sum
Subarray Sum Equals K
```

---

# 9.29 Common Mistakes

## Mistake 1: Forgetting `getOrDefault`

Instead of:

```java
map.put(num, map.get(num) + 1);
```

use:

```java
map.put(
    num,
    map.getOrDefault(num, 0) + 1
);
```

Otherwise `map.get(num)` may return `null`.

---

## Mistake 2: Using HashSet When Frequency is Required

A `HashSet` only tells you:

```text
Does it exist?
```

It does not tell you:

```text
How many times?
```

If frequency is required, use:

```text
HashMap
```

---

## Mistake 3: Using HashMap When Only Existence is Required

If you only need:

```text
Does this number exist?
```

a `HashSet` is cleaner.

---

## Mistake 4: Forgetting the Prefix Sum Initialization

For subarray sum:

```java
map.put(0, 1);
```

is essential.

---

## Mistake 5: Assuming Hashing is Always O(1)

HashMap and HashSet provide:

```text
Average: O(1)
```

not an absolute guarantee for every theoretical situation.

For DSA interview analysis, we normally use average-case `O(1)`.

---

# 9.30 Important Java Syntax

## HashMap

```java
HashMap<Integer, Integer> map =
    new HashMap<>();
```

### Insert

```java
map.put(key, value);
```

### Get

```java
map.get(key);
```

### Get or Default

```java
map.getOrDefault(key, 0);
```

### Check

```java
map.containsKey(key);
```

### Remove

```java
map.remove(key);
```

---

## HashSet

```java
HashSet<Integer> set =
    new HashSet<>();
```

### Insert

```java
set.add(value);
```

### Check

```java
set.contains(value);
```

### Remove

```java
set.remove(value);
```

---

# 9.31 Problem-Solving Framework

When you see an array problem, think in this order:

```text
                    Array Problem
                         |
              -----------------------
              |          |          |
          Frequency   Existence    Mapping
              |          |          |
          HashMap     HashSet     HashMap
```

Then ask:

```text
1. Do I need to count?
        ↓
     HashMap

2. Do I need to check existence?
        ↓
     HashSet

3. Do I need value → index?
        ↓
     HashMap

4. Are values small integers?
        ↓
     Frequency Array

5. Is it a subarray sum problem?
        ↓
     Prefix Sum + HashMap

6. Is it a consecutive sequence problem?
        ↓
     HashSet
```

---

# 9.32 Complexity Cheat Sheet

| Operation | Frequency Array |        HashMap |          HashSet |
| --------- | --------------: | -------------: | ---------------: |
| Search    |            O(1) |       O(1) avg |         O(1) avg |
| Insert    |            O(1) |       O(1) avg |         O(1) avg |
| Delete    |            O(1) |       O(1) avg |         O(1) avg |
| Frequency |            O(1) |       O(1) avg |     Not directly |
| Memory    |        O(range) | O(unique keys) | O(unique values) |

---

# 9.33 Topics You Should Master

For this section, make sure you understand these patterns deeply:

```text
1. Frequency Array
       ↓
   Small integer range

2. HashMap
       ↓
   Key → Value

3. HashSet
       ↓
   Unique values / existence

4. Frequency Counting
       ↓
   Element → Frequency

5. Duplicate Detection
       ↓
   HashSet

6. First Unique Element
       ↓
   HashMap + second traversal

7. Majority Element
       ↓
   HashMap / Boyer-Moore

8. Pair Sum
       ↓
   HashSet / HashMap

9. Subarray Sum
       ↓
   Prefix Sum + HashMap

10. Longest Consecutive Sequence
       ↓
   HashSet
```

---

# 9.34 Final Mental Model

Remember these three rules:

```text
RULE 1:
Need COUNT?
→ HashMap / Frequency Array

RULE 2:
Need EXISTENCE?
→ HashSet

RULE 3:
Need PREFIX SUM relationships?
→ HashMap + Prefix Sum
```

And the most important idea behind hashing is:

> **Instead of repeatedly searching the array, store useful information while traversing it so that future searches become fast.**

This is why hashing can transform many problems from:

```text
O(n²)
```

into:

```text
O(n)
```

at the cost of additional memory.

The core patterns to recognize are:

```text
Frequency
    ↓
HashMap

Existence
    ↓
HashSet

Value → Index
    ↓
HashMap

Small integer range
    ↓
Frequency Array

Subarray Sum
    ↓
Prefix Sum + HashMap

Consecutive Sequence
    ↓
HashSet
```

Once these patterns become familiar, a large number of array problems become much easier to identify and solve.

```
```
