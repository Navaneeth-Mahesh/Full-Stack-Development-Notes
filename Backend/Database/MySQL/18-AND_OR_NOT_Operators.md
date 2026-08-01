# Lesson 18 — AND, OR, NOT Operators

## Learning Objectives

By the end of this lesson, you will understand:

- What logical operators are
- How `AND` works
- How `OR` works
- How `NOT` works
- Combining multiple conditions
- Operator precedence
- Using parentheses for clarity
- Real-world examples
- Best practices
- Common mistakes
- Interview questions
- Practice exercises

---

# Introduction

When retrieving data from a database, you often need to filter records based on **multiple conditions**.

Logical operators allow you to combine these conditions.

MySQL provides three primary logical operators:

- AND
- OR
- NOT

These operators are mainly used with the `WHERE` clause.

---

# Sample Table

We'll use this `employees` table throughout this lesson.

| emp_id | name    | department | salary | city      | experience |
|---------|---------|------------|--------|-----------|------------|
| 1 | Navaneeth | IT | 75000 | Hyderabad | 3 |
| 2 | Rahul | HR | 45000 | Chennai | 2 |
| 3 | Sneha | IT | 95000 | Bangalore | 6 |
| 4 | Arjun | Finance | 68000 | Hyderabad | 5 |
| 5 | Priya | IT | 55000 | Chennai | 1 |
| 6 | Kiran | HR | 85000 | Bangalore | 7 |

---

# The WHERE Clause

Logical operators are usually used with `WHERE`.

Example:

```sql
SELECT *
FROM employees
WHERE salary > 50000;
```

This returns employees earning more than ₹50,000.

---

# AND Operator

## Definition

The `AND` operator returns rows **only if all conditions are true**.

Think of it as:

```
Condition A  ✔
Condition B  ✔

Result ✔
```

If even one condition is false:

```
Condition A ✔
Condition B ✖

Result ✖
```

---

## Syntax

```sql
SELECT columns
FROM table_name
WHERE condition1
AND condition2;
```

---

## Example 1

Employees from the IT department earning more than ₹60,000.

```sql
SELECT *
FROM employees
WHERE department = 'IT'
AND salary > 60000;
```

Output:

| name | department | salary |
|------|------------|--------|
| Navaneeth | IT | 75000 |
| Sneha | IT | 95000 |

Priya is excluded because her salary is only ₹55,000.

---

## Example 2

Employees in Hyderabad with more than 4 years of experience.

```sql
SELECT *
FROM employees
WHERE city = 'Hyderabad'
AND experience > 4;
```

Output:

| name |
|------|
| Arjun |

---

## Example 3

Multiple AND conditions

```sql
SELECT *
FROM employees
WHERE department = 'IT'
AND city = 'Bangalore'
AND salary > 90000;
```

Output:

| name |
|------|
| Sneha |

---

# OR Operator

## Definition

The `OR` operator returns rows if **at least one condition is true**.

Truth Table

| Condition A | Condition B | Result |
|-------------|-------------|--------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

---

## Syntax

```sql
SELECT *
FROM table_name
WHERE condition1
OR condition2;
```

---

## Example 1

Employees from Hyderabad or Chennai.

```sql
SELECT *
FROM employees
WHERE city = 'Hyderabad'
OR city = 'Chennai';
```

Output:

- Navaneeth
- Rahul
- Arjun
- Priya

---

## Example 2

Employees earning less than ₹50,000 or working in HR.

```sql
SELECT *
FROM employees
WHERE salary < 50000
OR department = 'HR';
```

Output:

- Rahul
- Kiran

Rahul satisfies both conditions.

Kiran satisfies the HR condition.

---

## Example 3

IT employees OR employees with salary above ₹90,000.

```sql
SELECT *
FROM employees
WHERE department='IT'
OR salary > 90000;
```

Output

- Navaneeth
- Sneha
- Priya

Sneha appears only once even though she satisfies both conditions.

---

# NOT Operator

## Definition

`NOT` reverses a condition.

It means:

```
NOT TRUE

↓

FALSE
```

```
NOT FALSE

↓

TRUE
```

---

## Syntax

```sql
SELECT *
FROM table_name
WHERE NOT condition;
```

---

## Example 1

Employees not from IT.

```sql
SELECT *
FROM employees
WHERE NOT department = 'IT';
```

Output:

- Rahul
- Arjun
- Kiran

Equivalent:

```sql
SELECT *
FROM employees
WHERE department <> 'IT';
```

---

## Example 2

Employees not from Hyderabad.

```sql
SELECT *
FROM employees
WHERE NOT city = 'Hyderabad';
```

Output:

- Rahul
- Sneha
- Priya
- Kiran

---

## Example 3

Salary not greater than ₹70,000.

```sql
SELECT *
FROM employees
WHERE NOT salary > 70000;
```

Equivalent:

```sql
WHERE salary <=70000;
```

---

# Combining AND and OR

Real queries often use both.

Example

```sql
SELECT *
FROM employees
WHERE department='IT'
OR city='Hyderabad';
```

Returns employees who satisfy either condition.

---

# More Complex Example

Employees in IT earning above ₹60,000 OR employees in HR.

```sql
SELECT *
FROM employees
WHERE department='IT'
AND salary>60000
OR department='HR';
```

At first glance, this looks correct.

But operator precedence matters.

---

# Operator Precedence

MySQL evaluates operators in this order:

1. NOT
2. AND
3. OR

This means:

```sql
department='IT'
AND salary>60000
OR department='HR'
```

is interpreted as:

```sql
(
department='IT'
AND salary>60000
)
OR department='HR'
```

Result:

- Navaneeth
- Sneha
- Rahul
- Kiran

---

# Using Parentheses

Always use parentheses to improve readability.

Example

```sql
SELECT *
FROM employees
WHERE
(
department='IT'
OR department='HR'
)
AND salary>70000;
```

Output

- Navaneeth
- Sneha
- Kiran

---

# Another Example

Employees who:

- Live in Hyderabad OR Bangalore
- Have salary above ₹70,000

```sql
SELECT *
FROM employees
WHERE
(
city='Hyderabad'
OR city='Bangalore'
)
AND salary>70000;
```

Output

- Navaneeth
- Sneha
- Kiran

---

# Using NOT with AND

Example

Employees not in IT and earning above ₹60,000.

```sql
SELECT *
FROM employees
WHERE
NOT department='IT'
AND salary>60000;
```

Output

- Arjun
- Kiran

---

# Using NOT with OR

Employees who are neither from Hyderabad nor Chennai.

```sql
SELECT *
FROM employees
WHERE
NOT
(
city='Hyderabad'
OR city='Chennai'
);
```

Equivalent:

```sql
SELECT *
FROM employees
WHERE city<>'Hyderabad'
AND city<>'Chennai';
```

Output

- Sneha
- Kiran

---

# Real-World Examples

## Example 1

Online Shopping

Find products:

- Electronics
- Price below ₹50,000

```sql
SELECT *
FROM products
WHERE category='Electronics'
AND price<50000;
```

---

## Example 2

Netflix

Movies

- English
- Rating above 8

```sql
SELECT *
FROM movies
WHERE language='English'
AND rating>8;
```

---

## Example 3

Hospital

Patients

- Age above 60
- Diabetes

```sql
SELECT *
FROM patients
WHERE age>60
AND disease='Diabetes';
```

---

## Example 4

College

Students from CSE or ECE.

```sql
SELECT *
FROM students
WHERE department='CSE'
OR department='ECE';
```

---

# Common Mistakes

## Forgetting Parentheses

Bad

```sql
WHERE city='Hyderabad'
OR city='Chennai'
AND salary>50000;
```

This is evaluated as:

```sql
city='Hyderabad'
OR
(
city='Chennai'
AND salary>50000
)
```

If your intention is different, use parentheses.

Correct

```sql
WHERE
(
city='Hyderabad'
OR city='Chennai'
)
AND salary>50000;
```

---

## Using NOT Incorrectly

Incorrect

```sql
NOT salary>50000;
```

Correct

```sql
WHERE NOT salary>50000;
```

or

```sql
WHERE salary<=50000;
```

---

# Best Practices

- Always use parentheses when combining `AND` and `OR`.
- Write SQL keywords in uppercase.
- Keep conditions readable.
- Test complex queries with sample data.
- Prefer simpler comparisons over `NOT` when possible (e.g., `<=` instead of `NOT >`).

---

# Interview Questions

### 1. What does the AND operator do?

Returns rows only when **all conditions are true**.

---

### 2. What does the OR operator do?

Returns rows when **at least one condition is true**.

---

### 3. What does the NOT operator do?

Reverses a condition.

---

### 4. Which operator has higher precedence?

1. NOT
2. AND
3. OR

---

### 5. Why should parentheses be used?

To control the order of evaluation and make queries easier to understand.

---

### 6. Can multiple AND conditions be used?

Yes.

Example:

```sql
WHERE department='IT'
AND city='Hyderabad'
AND salary>70000;
```

---

### 7. Can AND and OR be combined?

Yes. Parentheses are recommended for clarity and correctness.

---

# Practice Exercises

### Exercise 1

Find employees:

- From IT
- Salary above ₹70,000

---

### Exercise 2

Find employees:

- From Hyderabad
- Experience greater than 3 years

---

### Exercise 3

Find employees:

- From Hyderabad OR Bangalore

---

### Exercise 4

Find employees:

- Not from HR

---

### Exercise 5

Find employees:

- Salary above ₹60,000
- IT OR Finance department

---

### Exercise 6

Find employees:

- Not from Chennai
- Salary below ₹80,000

---

### Challenge

Write a query to find employees who:

- Work in IT or HR
- Earn more than ₹70,000
- Are not from Chennai

<details>
<summary>Solution</summary>

```sql
SELECT *
FROM employees
WHERE
(
department='IT'
OR department='HR'
)
AND salary>70000
AND city<>'Chennai';
```

</details>

---

# Summary

In this lesson, you learned:

- Logical operators in MySQL
- `AND`
- `OR`
- `NOT`
- Combining multiple conditions
- Operator precedence (`NOT` → `AND` → `OR`)
- Using parentheses
- Real-world filtering examples
- Common mistakes
- Best practices
- Interview questions
- Practice exercises

---

# Next Lesson

**Lesson 19 — Wildcards**

Topics covered:

- `%` Wildcard
- `_` Wildcard
- `LIKE` Operator
- Pattern Matching
- Searching Partial Text
- Escaping Wildcards
- Real-world Examples
- Practice Exercises