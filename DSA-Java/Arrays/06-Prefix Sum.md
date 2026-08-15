6. Prefix Sum
Prefix Sum is a technique used to precompute cumulative sums so that we can answer sum-related queries efficiently.

Instead of repeatedly calculating the sum of elements, we calculate a prefix/suffix array once and reuse it.

1. Prefix Sum
A prefix sum at index i represents the sum of all elements from index 0 to i.

Example
Array:

arr = [2, 4, 6, 8, 10]
Prefix sums:

[2, 6, 12, 20, 30]
Because:

prefix[0] = 2
prefix[1] = 2 + 4 = 6
prefix[2] = 2 + 4 + 6 = 12
prefix[3] = 2 + 4 + 6 + 8 = 20
prefix[4] = 2 + 4 + 6 + 8 + 10 = 30
Formula
prefix[i] = prefix[i - 1] + arr[i]
For the first element:

prefix[0] = arr[0]
Java
int[] arr = {2, 4, 6, 8, 10};

int[] prefix = new int[arr.length];

prefix[0] = arr[0];

for (int i = 1; i < arr.length; i++) {
    prefix[i] = prefix[i - 1] + arr[i];
}
Result:

prefix = [2, 6, 12, 20, 30]
Complexity
Time:  O(n)
Space: O(n)
2. Suffix Sum
A suffix sum at index i represents the sum of all elements from index i to the end of the array.

Example
arr = [2, 4, 6, 8, 10]
Suffix sums:

[30, 28, 24, 18, 10]
Because:

suffix[4] = 10

suffix[3] = 8 + 10 = 18

suffix[2] = 6 + 8 + 10 = 24

suffix[1] = 4 + 6 + 8 + 10 = 28

suffix[0] = 2 + 4 + 6 + 8 + 10 = 30
Formula
suffix[i] = suffix[i + 1] + arr[i]
Java
int[] arr = {2, 4, 6, 8, 10};

int n = arr.length;

int[] suffix = new int[n];

suffix[n - 1] = arr[n - 1];

for (int i = n - 2; i >= 0; i--) {
    suffix[i] = suffix[i + 1] + arr[i];
}
Result:

suffix = [30, 28, 24, 18, 10]
Complexity
Time:  O(n)
Space: O(n)
3. Prefix Sum Array
A prefix sum array is simply an array containing the cumulative sums of the original array.

For:

arr = [3, 1, 4, 2, 5]
Prefix sum array:

[3, 4, 8, 10, 15]
Visualization:

Index:   0   1   2   3   4
         ↓   ↓   ↓   ↓   ↓

Array:   3   1   4   2   5

Prefix:  3   4   8  10  15
The important property is:

prefix[i] = sum(arr[0 ... i])
This allows us to calculate range sums quickly.

4. Range Sum Queries
Suppose we have:

arr = [2, 4, 6, 8, 10]
And we want:

sum from index 1 to 3
That means:

4 + 6 + 8 = 18
Using a prefix array:

prefix = [2, 6, 12, 20, 30]
We can calculate:

rangeSum(L, R) = prefix[R] - prefix[L - 1]
Therefore:

rangeSum(1, 3)

= prefix[3] - prefix[0]

= 20 - 2

= 18
Special Case
If:

L = 0
there is no prefix[L - 1].

So:

rangeSum(0, R) = prefix[R]
Java
static int rangeSum(int[] prefix, int left, int right) {

    if (left == 0) {
        return prefix[right];
    }

    return prefix[right] - prefix[left - 1];
}
Why Prefix Sum?
Without prefix sum:

Each query → O(n)
With prefix sum:

Build prefix → O(n)

Each query → O(1)
This is extremely useful when there are many range-sum queries.

5. Subarray Sum Using Prefix Sum
Prefix sum can also help us calculate the sum of any subarray.

For:

arr = [2, 4, 6, 8, 10]
Suppose we need:

sum(1, 3)
The subarray is:

[4, 6, 8]
Using prefix sum:

prefix = [2, 6, 12, 20, 30]
Formula:

sum(L, R) = prefix[R] - prefix[L - 1]
Therefore:

sum(1, 3)
= prefix[3] - prefix[0]
= 20 - 2
= 18
Alternative: Prefix Sum with Extra Zero
A very useful technique is creating a prefix array of size n + 1.

arr = [2, 4, 6, 8, 10]

prefix = [0, 2, 6, 12, 20, 30]
Now:

prefix[i] = sum of first i elements
The range sum becomes:

sum(L, R) = prefix[R + 1] - prefix[L]
Example:

L = 1
R = 3

sum = prefix[4] - prefix[1]

    = 20 - 2

    = 18
Java
static int[] buildPrefix(int[] arr) {

    int n = arr.length;

    int[] prefix = new int[n + 1];

    for (int i = 0; i < n; i++) {
        prefix[i + 1] = prefix[i] + arr[i];
    }

    return prefix;
}
Range sum:

static int rangeSum(int[] prefix, int left, int right) {

    return prefix[right + 1] - prefix[left];
}
This version is often easier to use because it eliminates special handling for left == 0.

6. Prefix Sum + HashMap
This is one of the most important Prefix Sum patterns in DSA.

It is commonly used to solve:

Find the number of subarrays whose sum is equal to k.

Example
arr = [1, 2, 3]
k = 3
Subarrays with sum 3:

[1, 2]
[3]
Answer:

2
Key Idea
Suppose the current prefix sum is:

currentSum
We need some previous prefix sum:

previousSum
such that:

currentSum - previousSum = k
Therefore:

previousSum = currentSum - k
So while traversing the array:

Calculate current prefix sum.
Check whether currentSum - k exists in the HashMap.
If it exists, those previous positions create subarrays with sum k.
Store the current prefix sum in the HashMap.
Example
arr = [1, 2, 3]
k = 3
Start:

sum = 0
map = {0 : 1}
count = 0
Element 1
sum = 1

needed = sum - k
       = 1 - 3
       = -2
-2 doesn’t exist.

Store:

map = {0:1, 1:1}
Element 2
sum = 3

needed = 3 - 3
       = 0
0 exists.

Therefore we found:

[1, 2]
Count:

count = 1
Element 3
sum = 6

needed = 6 - 3
       = 3
3 exists.

Therefore:

[3]
Count:

count = 2
Answer:

2
Java
import java.util.HashMap;

static int subarraySum(int[] arr, int k) {

    HashMap<Integer, Integer> map = new HashMap<>();

    map.put(0, 1);

    int sum = 0;
    int count = 0;

    for (int num : arr) {

        sum += num;

        int needed = sum - k;

        if (map.containsKey(needed)) {
            count += map.get(needed);
        }

        map.put(sum, map.getOrDefault(sum, 0) + 1);
    }

    return count;
}
Complexity
Time:  O(n)
Space: O(n)
Important Pattern
Remember:

currentPrefixSum - requiredPrefixSum = target
Therefore:

requiredPrefixSum = currentPrefixSum - target
This pattern appears frequently in subarray problems.

7. Equilibrium Index
An equilibrium index is an index where:

sum of elements on the left
=
sum of elements on the right
The element at the equilibrium index is usually not included in either side.

Example
arr = [1, 3, 5, 2, 2]
Check index 2:

Left side:
1 + 3 = 4

Right side:
2 + 2 = 4
Therefore:

Equilibrium Index = 2
Using Total Sum
We don’t actually need two arrays.

First calculate:

totalSum
Then traverse the array while maintaining:

leftSum
At index i:

rightSum = totalSum - leftSum - arr[i]
If:

leftSum == rightSum
then i is an equilibrium index.

Java
static int equilibriumIndex(int[] arr) {

    int totalSum = 0;

    for (int num : arr) {
        totalSum += num;
    }

    int leftSum = 0;

    for (int i = 0; i < arr.length; i++) {

        int rightSum = totalSum - leftSum - arr[i];

        if (leftSum == rightSum) {
            return i;
        }

        leftSum += arr[i];
    }

    return -1;
}
Complexity
Time:  O(n)
Space: O(1)
8. Pivot Index
A pivot index is very similar to an equilibrium index.

At index i:

sum of elements before i
=
sum of elements after i
Example:

arr = [1, 7, 3, 6, 5, 6]
At index 3:

Left:
1 + 7 + 3 = 11

Right:
5 + 6 = 11
Therefore:

Pivot Index = 3
Difference Between Pivot Index and Equilibrium Index
In most DSA problems, they are essentially the same concept.

Equilibrium Index
        ↓
Left Sum == Right Sum

Pivot Index
        ↓
Left Sum == Right Sum
The main difference is terminology depending on the problem/platform.

Java
static int pivotIndex(int[] arr) {

    int totalSum = 0;

    for (int num : arr) {
        totalSum += num;
    }

    int leftSum = 0;

    for (int i = 0; i < arr.length; i++) {

        int rightSum = totalSum - leftSum - arr[i];

        if (leftSum == rightSum) {
            return i;
        }

        leftSum += arr[i];
    }

    return -1;
}
Complexity
Time:  O(n)
Space: O(1)
Prefix Sum Patterns You Should Remember
Pattern 1: Build Prefix Sum
prefix[i] = prefix[i - 1] + arr[i]
Pattern 2: Range Sum
sum(L, R) = prefix[R] - prefix[L - 1]
Or with an extra zero:

sum(L, R) = prefix[R + 1] - prefix[L]
Pattern 3: Subarray Sum = K
Use:

HashMap<PrefixSum, Frequency>
And look for:

currentSum - k
Pattern 4: Equilibrium / Pivot
Calculate:

rightSum = totalSum - leftSum - arr[i]
Then check:

leftSum == rightSum
Quick Comparison
Topic

Main Idea

Typical Complexity

Prefix Sum

Sum from beginning

O(n)

Suffix Sum

Sum from end

O(n)

Prefix Sum Array

Store cumulative sums

O(n)

Range Sum

Calculate subarray sum quickly

O(1) per query

Subarray Sum

Find sum of a subarray

O(1) with prefix lookup

Prefix Sum + HashMap

Find/count subarrays with target sum

O(n)

Equilibrium Index

Left sum = right sum

O(n)

Pivot Index

Left sum = right sum

O(n)

Most Important Mental Model
Think of Prefix Sum as remembering everything that has been accumulated so far.

Original:
[2, 4, 6, 8, 10]

Prefix:
[2, 6, 12, 20, 30]
Instead of repeatedly doing:

2 + 4 + 6 + 8
we can simply do:

prefix[3] = 20
And for a range:

L -------- R
↓           ↓

[2, 4, 6, 8, 10]
    └───────┘

prefix[R] - prefix[L-1]
The three patterns you should master first are:

1. Prefix Sum → Range Sum
2. Prefix Sum + HashMap → Subarray Sum = K
3. Prefix Sum → Equilibrium / Pivot Index
These patterns cover a large number of array problems.