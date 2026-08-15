# 8. Two Pointer Technique

The **Two Pointer Technique** is an important array and string problem-solving technique used to reduce the time complexity of many problems.

Instead of repeatedly scanning the same elements using nested loops, we maintain **two indices (pointers)** and move them intelligently based on the problem's conditions.

---

## 8.1 Two Pointer Fundamentals

### What is the Two Pointer Technique?

Two Pointer means using two variables to represent positions in an array or string.

For example:

```java
int left = 0;
int right = arr.length - 1;
Here:

left points to the first element.
right points to the last element.
We move either left, right, or both depending on the condition.
Basic Structure
while (left < right) {

    // Process arr[left] and arr[right]

    if (condition) {
        left++;
    } else {
        right--;
    }
}
Why use Two Pointers?
Consider finding whether a sorted array contains two numbers whose sum is target.

Brute force:

for (int i = 0; i < n; i++) {
    for (int j = i + 1; j < n; j++) {
        if (arr[i] + arr[j] == target) {
            return true;
        }
    }
}
Time Complexity:

O(n²)
Using two pointers:

int left = 0;
int right = arr.length - 1;

while (left < right) {

    int sum = arr[left] + arr[right];

    if (sum == target) {
        return true;
    } 
    else if (sum < target) {
        left++;
    } 
    else {
        right--;
    }
}
Time Complexity:

O(n)
The major advantage is that each pointer moves through the array only once.

8.2 Types of Two Pointer Techniques
There are two major patterns:

1. Opposite Direction Pointers
Pointers start from opposite ends.

left → → →       ← ← ← right
Example:

int left = 0;
int right = arr.length - 1;
Common problems:

Pair Sum
Two Sum in Sorted Array
Container With Most Water
Palindrome
Reverse Array
Trapping Rain Water
2. Same Direction Pointers
Both pointers move from left to right.

slow →
fast → → →
Example:

int slow = 0;

for (int fast = 0; fast < arr.length; fast++) {
    // process
}
Common problems:

Remove Duplicates
Remove Element
Move Zeroes
Partitioning
Fast and Slow Pointer problems
8.3 Opposite Direction Pointers
In this pattern, one pointer starts at the beginning and the other starts at the end.

int left = 0;
int right = arr.length - 1;
The pointers move toward each other.

Example:

Array:

[1, 2, 3, 4, 5, 6]

 ↑                 ↑
left             right
After movement:

[1, 2, 3, 4, 5, 6]

    ↑           ↑
   left       right
Eventually:

[1, 2, 3, 4, 5, 6]

        ↑
      left/right
The loop normally looks like:

while (left < right) {
    // process
}
Important Idea
The key is not simply having two variables.

The important part is:

Move the correct pointer based on the problem’s condition.

8.4 Same Direction Pointers
In this pattern, both pointers move from left to right.

Usually one pointer is responsible for scanning the array and another pointer is responsible for maintaining the position where the next valid element should go.

The common names are:

slow
fast
Example:

int slow = 0;

for (int fast = 0; fast < arr.length; fast++) {

    if (arr[fast] != 0) {
        arr[slow] = arr[fast];
        slow++;
    }
}
Here:

fast scans every element.
slow tracks the position for the next valid element.
This pattern is very useful for:

Removing duplicates
Removing elements
Moving zeroes
Partitioning arrays
In-place modifications
8.5 Pair Sum
The Pair Sum problem asks us to find two elements whose sum equals a given target.

Example:

Array = [1, 2, 3, 4, 6]
Target = 6
Answer:

2 + 4 = 6
Brute Force
for (int i = 0; i < n; i++) {
    for (int j = i + 1; j < n; j++) {

        if (arr[i] + arr[j] == target) {
            return true;
        }
    }
}
Complexity:

Time: O(n²)
Space: O(1)
Two Pointer Approach
Two pointers work directly when the array is sorted.

int left = 0;
int right = arr.length - 1;

while (left < right) {

    int sum = arr[left] + arr[right];

    if (sum == target) {
        return true;
    }

    if (sum < target) {
        left++;
    } else {
        right--;
    }
}

return false;
Why does this work?
Suppose:

[1, 2, 3, 4, 6]
 ↑           ↑
 L           R
Sum:

1 + 6 = 7
Target:

6
The sum is too large.

Because the array is sorted, moving left right would increase the sum.

So we move right:

[1, 2, 3, 4, 6]
 ↑        ↑
 L        R
Now:

1 + 4 = 5
Too small.

Therefore move left:

[1, 2, 3, 4, 6]
    ↑     ↑
    L     R
Now:

2 + 4 = 6
Found.

Complexity
Time: O(n)
Space: O(1)
8.6 Two Sum
Two Sum asks:

Find two numbers whose sum equals the target.

Example:

nums = [2, 7, 11, 15]
target = 9
Answer:

2 + 7 = 9
There are two important approaches.

Approach 1: HashMap
This works for an unsorted array.

import java.util.HashMap;

class Solution {

    public int[] twoSum(int[] nums, int target) {

        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {

            int complement = target - nums[i];

            if (map.containsKey(complement)) {
                return new int[] {
                    map.get(complement),
                    i
                };
            }

            map.put(nums[i], i);
        }

        return new int[] {};
    }
}
Complexity:

Time: O(n)
Space: O(n)
Approach 2: Two Pointers
Two pointers require a sorted array.

int left = 0;
int right = nums.length - 1;

while (left < right) {

    int sum = nums[left] + nums[right];

    if (sum == target) {
        return true;
    }

    if (sum < target) {
        left++;
    } else {
        right--;
    }
}

return false;
Complexity:

Time: O(n)
Space: O(1)
If the original array is unsorted and you sort it first:

Sorting: O(n log n)
Two pointers: O(n)

Total: O(n log n)
8.7 Three Sum
Three Sum asks us to find three numbers whose sum is equal to a target.

A common version uses:

target = 0
Example:

[-1, 0, 1, 2, -1, -4]
Valid combinations:

[-1, -1, 2]
[-1, 0, 1]
Main Idea
Three Sum combines:

One normal loop
+
Two Pointer technique
First sort the array.

[-4, -1, -1, 0, 1, 2]
Then fix one element.

for (int i = 0; i < nums.length - 2; i++) {

    int left = i + 1;
    int right = nums.length - 1;

    while (left < right) {

        int sum = nums[i] + nums[left] + nums[right];

        if (sum == 0) {
            // found triplet
        }
        else if (sum < 0) {
            left++;
        }
        else {
            right--;
        }
    }
}
Complete Java Implementation
import java.util.*;

class Solution {

    public List<List<Integer>> threeSum(int[] nums) {

        List<List<Integer>> result = new ArrayList<>();

        Arrays.sort(nums);

        for (int i = 0; i < nums.length - 2; i++) {

            // Skip duplicate first elements
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            int left = i + 1;
            int right = nums.length - 1;

            while (left < right) {

                int sum = nums[i] + nums[left] + nums[right];

                if (sum == 0) {

                    result.add(
                        Arrays.asList(
                            nums[i],
                            nums[left],
                            nums[right]
                        )
                    );

                    left++;
                    right--;

                    // Skip duplicates
                    while (left < right &&
                           nums[left] == nums[left - 1]) {
                        left++;
                    }

                    while (left < right &&
                           nums[right] == nums[right + 1]) {
                        right--;
                    }

                }
                else if (sum < 0) {
                    left++;
                }
                else {
                    right--;
                }
            }
        }

        return result;
    }
}
Complexity
Sorting:

O(n log n)
Outer loop + two pointers:

O(n²)
Overall:

Time: O(n²)
Space: O(1)
Ignoring the output list.

8.8 Four Sum
Four Sum extends the same idea.

We need four numbers whose sum equals a target.

Example:

[1, 0, -1, 0, -2, 2]
target = 0
Possible answers:

[-2, -1, 1, 2]
[-2, 0, 0, 2]
[-1, 0, 0, 1]
Main Idea
Four Sum:

Fix first number
        ↓
Fix second number
        ↓
Use two pointers for remaining two numbers
Structure:

for (int i = 0; i < n - 3; i++) {

    for (int j = i + 1; j < n - 2; j++) {

        int left = j + 1;
        int right = n - 1;

        while (left < right) {

            long sum =
                (long) nums[i]
                + nums[j]
                + nums[left]
                + nums[right];

            if (sum == target) {
                // found
            }
            else if (sum < target) {
                left++;
            }
            else {
                right--;
            }
        }
    }
}
Why use
long?
Integer overflow can occur when adding four integers.

For example:

2,000,000,000
2,000,000,000
2,000,000,000
2,000,000,000
The sum is larger than the maximum Java int.

Therefore:

long sum = ...
is safer.

Complexity
Time: O(n³)
Space: O(1)
Ignoring output space.

8.9 Remove Duplicates
A classic same-direction two-pointer problem.

Consider:

[1, 1, 2, 2, 3]
We want:

[1, 2, 3]
The array is sorted.

We use:

slow → position of last unique element
fast → scans the array
Example:

[1, 1, 2, 2, 3]
 ↑  ↑
 S  F
If:

nums[fast] != nums[slow]
then we found a new unique element.

Move slow and copy the element.

Java
class Solution {

    public int removeDuplicates(int[] nums) {

        if (nums.length == 0) {
            return 0;
        }

        int slow = 0;

        for (int fast = 1; fast < nums.length; fast++) {

            if (nums[fast] != nums[slow]) {

                slow++;

                nums[slow] = nums[fast];
            }
        }

        return slow + 1;
    }
}
Example:

Input:

[1, 1, 2, 2, 3]

Process:

slow = 0
fast = 1

1 == 1
skip

fast = 2

2 != 1
slow++
nums[1] = 2

Array:

[1, 2, 2, 2, 3]

fast = 3

2 == 2
skip

fast = 4

3 != 2
slow++
nums[2] = 3

Array:

[1, 2, 3, 2, 3]
Only the first 3 elements are valid.

Answer length:

3
Complexity
Time: O(n)
Space: O(1)
8.10 Container With Most Water
Problem:

Given an array where each value represents the height of a vertical line, find the maximum amount of water that can be stored between two lines.

Example:

[1,8,6,2,5,4,8,3,7]
The area between two lines is:

Area = width × minimum_height
For two pointers:

int width = right - left;

int height =
    Math.min(height[left], height[right]);

int area = width * height;
Brute Force
Check every pair.

for (int i = 0; i < n; i++) {

    for (int j = i + 1; j < n; j++) {

        int width = j - i;

        int height = Math.min(height[i], height[j]);

        int area = width * height;

        max = Math.max(max, area);
    }
}
Complexity:

O(n²)
Two Pointer Approach
Start from both ends.

int left = 0;
int right = height.length - 1;

int maxArea = 0;

while (left < right) {

    int width = right - left;

    int currentHeight =
        Math.min(height[left], height[right]);

    int area = width * currentHeight;

    maxArea = Math.max(maxArea, area);

    if (height[left] < height[right]) {
        left++;
    } else {
        right--;
    }
}
Why move the smaller height?
Suppose:

left height  = 3
right height = 8
The container height is limited by:

3
Moving the right pointer inward decreases the width.

The only possibility of increasing the area is to find a taller left boundary.

Therefore:

if (height[left] < height[right]) {
    left++;
}
Otherwise:

right--;
Complexity
Time: O(n)
Space: O(1)
8.11 Trapping Rain Water
This is one of the most important two-pointer problems.

Example:

[0,1,0,2,1,0,1,3,2,1,2,1]
Rainwater can be trapped between taller boundaries.

For every position:

Water =
min(maxLeft, maxRight) - currentHeight
The challenge is calculating maxLeft and maxRight efficiently.

Brute Force
For every index:

Find maximum height on the left.
Find maximum height on the right.
Calculate trapped water.
Complexity:

O(n²)
Prefix/Suffix Approach
We can precompute:

leftMax[]
rightMax[]
Then:

water += Math.min(leftMax[i], rightMax[i])
         - height[i];
Complexity:

Time: O(n)
Space: O(n)
Two Pointer Approach
We can reduce extra space to O(1).

Use:

int left = 0;
int right = height.length - 1;

int leftMax = 0;
int rightMax = 0;

int water = 0;
Java
class Solution {

    public int trap(int[] height) {

        int left = 0;
        int right = height.length - 1;

        int leftMax = 0;
        int rightMax = 0;

        int water = 0;

        while (left < right) {

            if (height[left] <= height[right]) {

                if (height[left] >= leftMax) {
                    leftMax = height[left];
                } else {
                    water += leftMax - height[left];
                }

                left++;

            } else {

                if (height[right] >= rightMax) {
                    rightMax = height[right];
                } else {
                    water += rightMax - height[right];
                }

                right--;
            }
        }

        return water;
    }
}
Key Concept
If:

height[left] <= height[right]
then the left side is the limiting side.

So we can safely calculate water for the left position.

Otherwise, calculate from the right side.

Complexity
Time: O(n)
Space: O(1)
8.12 Merge Sorted Arrays
Two pointers are commonly used to merge sorted arrays.

Example:

A = [1, 3, 5]
B = [2, 4, 6]
Result:

[1, 2, 3, 4, 5, 6]
Use:

int i = 0;
int j = 0;
i scans array A.

j scans array B.

Compare:

if (A[i] <= B[j])
and take the smaller value.

Java
import java.util.*;

class Solution {

    public static int[] merge(int[] a, int[] b) {

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
}
Complexity
Time: O(n + m)
Space: O(n + m)
where:

n = size of A
m = size of B
8.13 Partitioning Arrays
Partitioning means rearranging an array around a certain condition.

Examples:

Move negative numbers to one side
Move zeroes to one side
Separate even and odd numbers
Partition around a pivot
Two pointers are extremely useful here.

Example: Move Zeroes
Input:

[0,1,0,3,12]
Output:

[1,3,12,0,0]
Use:

slow → next position for non-zero
fast → scans array
Java
class Solution {

    public void moveZeroes(int[] nums) {

        int slow = 0;

        for (int fast = 0; fast < nums.length; fast++) {

            if (nums[fast] != 0) {

                int temp = nums[slow];

                nums[slow] = nums[fast];

                nums[fast] = temp;

                slow++;
            }
        }
    }
}
Complexity:

Time: O(n)
Space: O(1)
Partition Around a Pivot
Suppose:

Array = [9, 4, 7, 3, 10, 5]
Pivot = 6
We want:

Elements < 6 | Pivot-related region | Elements > 6
A partition algorithm uses pointers to place elements on the correct side.

One common approach:

int left = 0;
int right = nums.length - 1;

while (left <= right) {

    while (left <= right && nums[left] < pivot) {
        left++;
    }

    while (left <= right && nums[right] >= pivot) {
        right--;
    }

    if (left < right) {

        int temp = nums[left];
        nums[left] = nums[right];
        nums[right] = temp;

        left++;
        right--;
    }
}
This idea is fundamental to:

Quick Sort
Quick Select
Dutch National Flag
Array partitioning problems
8.14 Two Pointer Decision Framework
When you see a problem, ask these questions.

Question 1: Is the array sorted?
If yes, immediately consider:

Two Pointers
Binary Search
Question 2: Are we looking for a pair?
Consider:

left = 0
right = n - 1
Example:

Pair Sum
Two Sum
Question 3: Are we looking for three or four values?
Think:

Fix one/two elements
+
Two Pointers
Examples:

Three Sum
Four Sum
Question 4: Are we removing duplicates?
Think:

slow + fast
Question 5: Are we rearranging elements in-place?
Think:

Two Pointers
Examples:

Move Zeroes
Partition Array
Segregate Even/Odd
Move Negatives
Question 6: Are the pointers coming from opposite ends?
Use:

left = 0;
right = n - 1;
Typical condition:

while (left < right)
Question 7: Are both pointers moving forward?
Use:

slow + fast
Typical structure:

for (int fast = 0; fast < n; fast++) {
    
    if (condition) {
        // use slow
        slow++;
    }
}
8.15 Opposite Direction vs Same Direction
Pattern

Pointer Movement

Common Problems

Opposite Direction

left →, right ←

Pair Sum

Same Direction

slow →, fast →

Remove Duplicates

Fixed + Two Pointers

One fixed, two move

Three Sum

Two Fixed + Two Pointers

Two fixed, two move

Four Sum

Partition

Pointers move based on conditions

Quick Sort

Boundary Pointers

Track left/right maximum

Trapping Rain Water

8.16 Important Two Pointer Templates
Template 1: Opposite Direction
int left = 0;
int right = arr.length - 1;

while (left < right) {

    if (condition) {
        left++;
    } else {
        right--;
    }
}
Template 2: Same Direction
int slow = 0;

for (int fast = 0; fast < arr.length; fast++) {

    if (condition) {

        arr[slow] = arr[fast];

        slow++;
    }
}
Template 3: Pair Sum
int left = 0;
int right = arr.length - 1;

while (left < right) {

    int sum = arr[left] + arr[right];

    if (sum == target) {
        // found
        break;
    }

    if (sum < target) {
        left++;
    } else {
        right--;
    }
}
Template 4: Three Sum
Arrays.sort(nums);

for (int i = 0; i < nums.length - 2; i++) {

    int left = i + 1;
    int right = nums.length - 1;

    while (left < right) {

        int sum =
            nums[i] +
            nums[left] +
            nums[right];

        if (sum == target) {
            // found
        }
        else if (sum < target) {
            left++;
        }
        else {
            right--;
        }
    }
}
8.17 Why Two Pointers Improve Complexity
Suppose:

n = 1,000,000
Brute force pair checking:

O(n²)
would require approximately:

1,000,000 × 1,000,000
= 1,000,000,000,000
comparisons in the worst-case scale.

Two pointers:

O(n)
require approximately:

1,000,000
pointer movements.

This is why recognizing the two-pointer pattern is extremely important in DSA.

8.18 Common Mistakes
Mistake 1: Using Two Pointers on an Unsorted Array
For Pair Sum:

[5, 1, 8, 3]
you cannot directly apply the standard sorted two-pointer logic.

You can either:

Use HashMap
or:

Sort the array first
But sorting changes the original indices.

Mistake 2: Moving the Wrong Pointer
For Pair Sum:

if (sum < target) {
    left++;
}
not:

right--;
Because increasing the left value increases the sum in a sorted array.

Mistake 3: Forgetting Duplicate Handling
Three Sum and Four Sum commonly contain duplicate values.

For example:

[-1, -1, 0, 1]
Without duplicate handling, the same combination may be added multiple times.

Mistake 4: Incorrect Loop Condition
Most opposite-direction problems use:

while (left < right)
not:

while (left <= right)
The correct condition depends on the problem, but using the wrong one can cause duplicate processing or invalid access.

Mistake 5: Losing the Original Indices
Sorting can make two-pointer solutions easier, but it changes element positions.

For example:

Original:
[3, 2, 4]

Sorted:
[2, 3, 4]
If the problem asks for original indices, sorting directly may not be appropriate unless you store the indices with the values.

8.19 Time Complexity Summary
Problem

Typical Approach

Time

Extra Space

Pair Sum

Two Pointers

O(n)

O(1)

Two Sum

HashMap

O(n)

O(n)

Two Sum Sorted

Two Pointers

O(n)

O(1)

Three Sum

Sort + Two Pointers

O(n²)

O(1)*

Four Sum

Sort + Two Pointers

O(n³)

O(1)*

Remove Duplicates

Slow/Fast

O(n)

O(1)

Container With Most Water

Two Pointers

O(n)

O(1)

Trapping Rain Water

Two Pointers

O(n)

O(1)

Merge Sorted Arrays

Two Pointers

O(n + m)

O(n + m)

Move Zeroes

Slow/Fast

O(n)

O(1)

Partition Array

Two Pointers

O(n)

O(1)

* Ignoring the space required for the output and implementation-dependent sorting details.

8.20 How to Identify Two Pointer Problems
Look for these clues in a problem statement:

"sorted array"
"pair"
"two numbers"
"three numbers"
"find a combination"
"remove duplicates"
"in-place"
"rearrange"
"partition"
"from both ends"
"maximum area"
"minimum difference"
"palindrome"
These are strong signals that you should consider Two Pointers.

8.21 Mental Model
The most important thing is not memorizing code.

Understand what each pointer represents.

Opposite Direction
left                    right
 ↓                        ↓
[ 1  2  3  4  5  6  7  8 ]

Move toward each other
Think:

“I am narrowing the search space.”

Same Direction
slow
 ↓
[ valid valid ? ? ? ? ]

       fast
        ↓
[ valid valid current ? ? ? ]
Think:

“Fast explores, slow builds the answer.”

Three Sum
i
↓
[ -4  -1  -1   0   1   2 ]
      ↑               ↑
    left             right
Think:

“Fix one element, then solve Pair Sum.”

Four Sum
i
j
↓
↓
[ a  b  c  d  e  f  g ]
      ↑           ↑
    left         right
Think:

“Fix two elements, then solve Pair Sum.”

8.22 Final Summary
The Two Pointer Technique is mainly about reducing unnecessary work by maintaining two intelligently controlled positions in a data structure.

The most important patterns to master are:

1. Opposite Direction
   left →       ← right

2. Same Direction
   slow → fast →

3. Fixed + Two Pointers
   i + left/right

4. Two Fixed + Two Pointers
   i + j + left/right

5. Partitioning
   left/right based on conditions
The most important problems to practice are:

1. Pair Sum
2. Two Sum
3. Three Sum
4. Four Sum
5. Remove Duplicates
6. Container With Most Water
7. Trapping Rain Water
8. Merge Sorted Arrays
9. Move Zeroes
10. Partition Array
The core rule to remember is:

Two pointers are useful when you can eliminate a portion of the search space after comparing elements at two positions.

Once you understand why a pointer moves, rather than simply memorizing the template, many array and string problems become significantly easier.