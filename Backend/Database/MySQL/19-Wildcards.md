# Lesson 19 — Wildcards in MySQL

## Learning Objectives

By the end of this lesson, you will understand:

- What Wildcards are
- Why Wildcards are useful
- The `LIKE` operator
- `%` wildcard
- `_` wildcard
- Combining wildcards
- Escaping wildcard characters
- Real-world searching examples
- Common mistakes
- Best practices
- Interview questions
- Practice exercises

---

# What are Wildcards?

Wildcards are **special characters** used with the `LIKE` operator to search for patterns instead of exact values.

Without wildcards:

```sql
SELECT * FROM students
WHERE name = 'John';
```

This only finds **John**.

With wildcards:

```sql
SELECT * FROM students
WHERE name LIKE 'Jo%';
```

This finds:

```
John
Johnny
Jordan
Joseph
Joanna
```

Wildcards make searching flexible.

---

# Why Use Wildcards?

Imagine an e-commerce website with thousands of products.

Instead of remembering the exact product name,

You can search:

```
iphone
```

and find

```
iPhone 13
iPhone 14
iPhone 15 Pro
```

Wildcards make this possible.

---

# The LIKE Operator

Wildcards work only with the `LIKE` operator.

Syntax

```sql
SELECT columns
FROM table_name
WHERE column_name LIKE 'pattern';
```

Example

```sql
SELECT *
FROM students
WHERE name LIKE 'A%';
```

---

# Wildcard Symbols

MySQL mainly provides two wildcard characters.

| Wildcard | Meaning |
|----------|----------|
| `%` | Zero or more characters |
| `_` | Exactly one character |

These are the most commonly used pattern matching symbols.

---

# The % Wildcard

The `%` symbol matches **zero, one, or many characters**.

Think of it as:

```
Anything can come here
```

Example

```sql
LIKE '%'
```

matches everything.

---

# Starts With

Find students whose names start with "A".

```sql
SELECT *
FROM students
WHERE name LIKE 'A%';
```

Example Data

| Name |
|------|
|Alice|
|Andrew|
|Ananya|
|Arjun|
|Bob|

Result

```
Alice
Andrew
Ananya
Arjun
```

---

# Ends With

Find names ending with "n".

```sql
SELECT *
FROM students
WHERE name LIKE '%n';
```

Matches

```
John
Arjun
Kiran
```

---

# Contains

Find names containing "an".

```sql
SELECT *
FROM students
WHERE name LIKE '%an%';
```

Matches

```
Ananya
Karan
Manoj
Jonathan
```

The letters can appear anywhere.

---

# Find Email Domains

Suppose

| Email |
|--------|
|abc@gmail.com|
|john@yahoo.com|
|alice@gmail.com|

Find Gmail users.

```sql
SELECT *
FROM users
WHERE email LIKE '%@gmail.com';
```

Result

```
abc@gmail.com
alice@gmail.com
```

---

# Find Product Names

Products

```
Wireless Mouse
Gaming Mouse
Mouse Pad
Keyboard
```

Search

```sql
SELECT *
FROM products
WHERE product_name LIKE '%Mouse%';
```

Result

```
Wireless Mouse
Gaming Mouse
Mouse Pad
```

---

# Find Phone Numbers

Suppose

```
9876543210
9123456789
8899001122
```

Find numbers beginning with 98.

```sql
SELECT *
FROM customers
WHERE phone LIKE '98%';
```

---

# Find URLs

```sql
SELECT *
FROM websites
WHERE url LIKE 'https%';
```

Matches

```
https://google.com

https://openai.com
```

---

# The _ Wildcard

The underscore `_` represents **exactly one character**.

This is different from `%`.

```
_ = one character only

% = any number of characters
```

---

# Example

```sql
SELECT *
FROM students
WHERE name LIKE 'J_n';
```

Matches

```
Jan

Jen

Jon
```

Does NOT match

```
John
Jason
Jonathan
```

because those have more than one character between J and n.

---

# Two Underscores

```sql
LIKE 'A__'
```

Means

```
A + two characters
```

Matches

```
Amy

Ann

Ava
```

Does not match

```
Andrew

Alexander
```

---

# Four Letter Names

```sql
SELECT *
FROM students
WHERE name LIKE '____';
```

Matches

```
John

Ryan

Emma

Noah
```

Only names with exactly four letters.

---

# Combining % and _

Find names starting with A and having at least three characters.

```sql
SELECT *
FROM students
WHERE name LIKE 'A__%';
```

Matches

```
Alex

Arjun

Ananya

Akhil
```

---

# More Examples

Starts with S

```sql
LIKE 'S%'
```

Ends with y

```sql
LIKE '%y'
```

Contains oo

```sql
LIKE '%oo%'
```

Second letter is a

```sql
LIKE '_a%'
```

Five letters

```sql
LIKE '_____'
```

Starts with A and ends with n

```sql
LIKE 'A%n'
```

---

# Pattern Matching

Imagine these names.

```
Alice

Albert

Andrew

Bob

Charlie
```

Pattern

```sql
LIKE 'Al%'
```

Matches

```
Alice

Albert
```

Pattern

```sql
LIKE '%ie'
```

Matches

```
Charlie
```

Pattern

```sql
LIKE '_o%'
```

Matches

```
Bob
```

because

```
_ = B

o = second character

% = remaining characters
```

---

# NOT LIKE

Exclude matching values.

Example

```sql
SELECT *
FROM students
WHERE name NOT LIKE 'A%';
```

Returns everyone except names beginning with A.

---

# Escaping Wildcards

Sometimes your actual data contains `%` or `_`.

Example

```
50% Discount

100% Organic
```

Searching like this

```sql
LIKE '%%'
```

matches everything.

Instead, escape the `%`.

```sql
SELECT *
FROM products
WHERE product_name LIKE '%\%%';
```

This searches for the actual `%` symbol.

Similarly,

```sql
LIKE '%\_%'
```

searches for an underscore.

You can explicitly specify the escape character.

```sql
SELECT *
FROM products
WHERE product_name LIKE '%!%%'
ESCAPE '!';
```

Here, `!` is treated as the escape character, so `%` is matched literally.

---

# Real-World Examples

## E-Commerce Search

```sql
SELECT *
FROM products
WHERE product_name LIKE '%Laptop%';
```

---

## Student Search

```sql
SELECT *
FROM students
WHERE name LIKE 'S%';
```

---

## Employee Emails

```sql
SELECT *
FROM employees
WHERE email LIKE '%@company.com';
```

---

## Movie Titles

```sql
SELECT *
FROM movies
WHERE title LIKE '%Avengers%';
```

---

## Search Cities

```sql
SELECT *
FROM customers
WHERE city LIKE '%York%';
```

Matches

```
New York

Yorkshire

Little York
```

---

# Common Mistakes

## Mistake 1

Using `=` instead of `LIKE`.

Wrong

```sql
WHERE name = 'A%'
```

Correct

```sql
WHERE name LIKE 'A%'
```

---

## Mistake 2

Forgetting quotes.

Wrong

```sql
LIKE A%
```

Correct

```sql
LIKE 'A%'
```

---

## Mistake 3

Confusing `_` with `%`.

```
_ = exactly one character

% = zero or more characters
```

---

## Mistake 4

Using `%` when an exact match is needed.

```sql
WHERE name = 'Alice'
```

is faster than

```sql
WHERE name LIKE 'Alice'
```

for exact matches.

---

# Performance Note

Patterns like

```sql
LIKE 'A%'
```

can often use indexes efficiently.

Patterns like

```sql
LIKE '%A'
```

or

```sql
LIKE '%A%'
```

usually require scanning more rows because the search starts with a wildcard.

Whenever possible, avoid leading `%` on very large tables.

---

# Best Practices

- Use `LIKE` only for pattern matching.
- Use `%` for unknown-length text.
- Use `_` for fixed-length patterns.
- Prefer exact matches (`=`) when possible.
- Avoid leading `%` on huge tables for better performance.
- Escape `%` and `_` when searching for literal characters.
- Write readable search patterns.

---

# Interview Questions

## 1. What is a wildcard?

A wildcard is a special character used with the `LIKE` operator to search for patterns.

---

## 2. Which operator is used with wildcards?

`LIKE`

---

## 3. What does `%` represent?

Zero or more characters.

---

## 4. What does `_` represent?

Exactly one character.

---

## 5. Difference between `%` and `_`?

| `%` | `_` |
|------|------|
|Zero or more characters|Exactly one character|

---

## 6. How do you exclude matching patterns?

Use `NOT LIKE`.

Example

```sql
WHERE name NOT LIKE 'A%'
```

---

## 7. How do you search for a literal `%`?

Escape it.

```sql
LIKE '%\%%'
```

or use an `ESCAPE` clause.

---

# Practice Exercises

## Exercise 1

Find students whose names start with "R".

---

## Exercise 2

Find students whose names end with "a".

---

## Exercise 3

Find products containing the word "Phone".

---

## Exercise 4

Find emails ending with `@gmail.com`.

---

## Exercise 5

Find names containing "ar".

---

## Exercise 6

Find names with exactly five letters.

---

## Exercise 7

Find employees whose second letter is "a".

---

## Exercise 8

Find all names that do **not** start with "S".

---

## Exercise 9

Search for products containing a literal `%` character.

---

# Mini Project

Create a `customers` table.

```text
Name
Email
City
Phone
```

Insert at least 15 records.

Write queries to:

1. Find names starting with **A**.
2. Find names ending with **n**.
3. Find emails ending with **@gmail.com**.
4. Find cities containing **York**.
5. Find phone numbers beginning with **98**.
6. Find names with exactly four letters.
7. Find names whose second letter is **a**.
8. Exclude customers whose names start with **S**.
9. Search for records containing a literal `%` in a text column.

---

# Summary

In this lesson, you learned:

- What Wildcards are
- The `LIKE` operator
- `%` wildcard (zero or more characters)
- `_` wildcard (exactly one character)
- Pattern matching
- Searching partial text
- `NOT LIKE`
- Escaping wildcard characters
- Real-world examples
- Performance considerations
- Best practices
- Practice exercises

---

# Next Lesson

**Lesson 20 — ORDER BY**

Topics covered:

- Sorting Data
- ASC
- DESC
- Multiple Columns
- NULL Values
- ORDER BY with LIMIT
- Real-world Examples
- Practice Exercises