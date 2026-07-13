# Problem Statement

Given an integer `n`, return a string array `answer` (1-indexed) where:

- `answer[i] == "FizzBuzz"` if `i` is divisible by both **3** and **5**.
- `answer[i] == "Fizz"` if `i` is divisible by **3**.
- `answer[i] == "Buzz"` if `i` is divisible by **5**.
- `answer[i] == str(i)` if none of the above conditions are true.

---

# Example 1

## Input

```text
n = 3
```

## Output

```text
["1","2","Fizz"]
```

### Explanation

| Number | Result |
|---------|--------|
|1| "1" |
|2| "2" |
|3| "Fizz" |

---

# Example 2

## Input

```text
n = 5
```

## Output

```text
["1","2","Fizz","4","Buzz"]
```

---

# Example 3

## Input

```text
n = 15
```

## Output

```text
[
"1",
"2",
"Fizz",
"4",
"Buzz",
"Fizz",
"7",
"8",
"Fizz",
"Buzz",
"11",
"Fizz",
"13",
"14",
"FizzBuzz"
]
```

---

# Constraints

```text
1 <= n <= 10^4
```

---

# Understanding the Problem

Imagine you are counting numbers from **1** to **n**.

For every number, decide what should be added to the answer.

Example:

```
1
2
3
4
5
6
...
```

Some numbers stay the same.

Some numbers are replaced by words.

---

# Rules

## Rule 1

If the number is divisible by **3**

Replace it with

```text
Fizz
```

Example

```
3
6
9
12
```

↓

```
Fizz
Fizz
Fizz
Fizz
```

---

## Rule 2

If the number is divisible by **5**

Replace it with

```text
Buzz
```

Example

```
5
10
15
20
```

↓

```
Buzz
Buzz
Buzz
Buzz
```

---

## Rule 3

If the number is divisible by **both 3 and 5**

Replace it with

```text
FizzBuzz
```

Example

```
15
30
45
```

↓

```
FizzBuzz
FizzBuzz
FizzBuzz
```

---

## Rule 4

If none of the conditions are true

Keep the number itself.

Example

```
7
```

↓

```
"7"
```

Notice it is a **string**, not an integer.

---

# Important Concept

## What is Divisibility?

A number is divisible by another number when the remainder is **0**.

Python uses the **modulus operator**.

```python
number % divisor
```

Examples

```python
9 % 3
```

Output

```text
0
```

Means

```
9 is divisible by 3
```

---

```python
20 % 5
```

Output

```text
0
```

Means

```
20 is divisible by 5
```

---

```python
7 % 3
```

Output

```text
1
```

Means

```
7 is NOT divisible by 3
```

---

# Biggest Mistake Beginners Make

Many beginners write

```python
if divisible by 3
    Fizz

elif divisible by 5
    Buzz

elif divisible by 3 and 5
    FizzBuzz
```

This is WRONG.

Suppose

```
15
```

First condition

```
Is 15 divisible by 3?
```

Yes.

So Python immediately executes

```
Fizz
```

It never checks

```
FizzBuzz
```

---

# Correct Order

Always check

```
Both
↓

3

↓

5

↓

Number
```

Because

```
15
```

matches all three conditions.

The most specific condition must come first.

---

# Step-by-Step Algorithm

```
Create an empty list.

Repeat from 1 to n.

Check if the number is divisible by both 3 and 5.
    Add "FizzBuzz"

Otherwise check divisible by 3.
    Add "Fizz"

Otherwise check divisible by 5.
    Add "Buzz"

Otherwise
    Add the number as a string.

Return the list.
```

---

# Dry Run

Suppose

```
n = 15
```

| Number | Divisible by 3 | Divisible by 5 | Output |
|---------|----------------|----------------|--------|
|1|No|No|"1"|
|2|No|No|"2"|
|3|Yes|No|"Fizz"|
|4|No|No|"4"|
|5|No|Yes|"Buzz"|
|6|Yes|No|"Fizz"|
|7|No|No|"7"|
|8|No|No|"8"|
|9|Yes|No|"Fizz"|
|10|No|Yes|"Buzz"|
|11|No|No|"11"|
|12|Yes|No|"Fizz"|
|13|No|No|"13"|
|14|No|No|"14"|
|15|Yes|Yes|"FizzBuzz"|

---

# Python Solution

```python
from typing import List

class Solution(object):
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []

        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))

        return answer
```

---

# Code Explanation

## Create Empty List

```python
answer = []
```

Stores the final result.

---

## Loop

```python
for i in range(1, n + 1):
```

Visits every number from

```
1

↓

n
```

---

## Check Both

```python
if i % 3 == 0 and i % 5 == 0:
```

If divisible by both

Add

```
FizzBuzz
```

---

## Check 3

```python
elif i % 3 == 0:
```

Add

```
Fizz
```

---

## Check 5

```python
elif i % 5 == 0:
```

Add

```
Buzz
```

---

## Otherwise

```python
else:
```

Convert number to string

```python
str(i)
```

Add it.

---

## Return

```python
return answer
```

Returns the complete list.

---

# Time Complexity

```
O(n)
```

We visit every number exactly once.

---

# Space Complexity

```
O(n)
```

Because we store `n` strings inside the answer list.

---

# Concepts Learned

- Variables
- Integers
- Strings
- Lists
- Loops
- for loop
- range()
- if
- elif
- else
- Modulus Operator (%)
- Boolean Operator (and)
- append()
- str()
- Return Statement

---

# Interview Tips

Whenever you see

```
Check every number from 1 to n
```

Think

```
Loop
```

Whenever you see

```
Divisible
```

Think

```
%
```

Whenever you see

```
Different actions based on conditions
```

Think

```
if
elif
else
```

Whenever multiple conditions overlap, always check the **most specific condition first**.

---

## Code

from typing import List

class Solution(object):
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []

        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))

        return answer


# Key Takeaways

- Use `%` to check divisibility.
- Check **3 and 5 together** before checking them individually.
- Use a loop to process every number from `1` to `n`.
- Store results in a list using `append()`.
- Convert numbers to strings using `str()`.
- Return the completed list after processing all numbers.