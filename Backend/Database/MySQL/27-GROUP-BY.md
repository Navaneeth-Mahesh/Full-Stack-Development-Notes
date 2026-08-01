# Lesson 27 — GROUP BY

## Learning Objectives

By the end of this lesson, you will understand:

- What `GROUP BY` is
- Why `GROUP BY` is used
- How aggregate functions work
- Difference between `WHERE` and `HAVING`
- Grouping by multiple columns
- Using `GROUP BY` with `ORDER BY`
- Real-world examples
- Best practices
- Common mistakes
- Interview questions
- Practice exercises

---

# What is GROUP BY?

The `GROUP BY` clause is used to **group rows that have the same values** in one or more columns.

Instead of returning every row individually, MySQL combines similar rows into groups.

It is commonly used together with **aggregate functions** such as:

- COUNT()
- SUM()
- AVG()
- MAX()
- MIN()

---

## Example

Employee Table

| id | name | department | salary |
|----|------|------------|--------|
|1|Alice|HR|40000|
|2|Bob|IT|70000|
|3|Charlie|IT|65000|
|4|David|HR|45000|
|5|Emma|Sales|50000|

Without GROUP BY:

```sql
SELECT department
FROM employees;
```

Output:

```
HR
IT
IT
HR
Sales
```

With GROUP BY:

```sql
SELECT department
FROM employees
GROUP BY department;
```

Output:

```
HR
IT
Sales
```

Each department appears only once.

---

# Why Use GROUP BY?

Suppose you want to know:

- Number of employees in each department
- Total sales per city
- Average salary by department
- Maximum marks in each class

Without `GROUP BY`, MySQL cannot summarize the data.

---

# Aggregate Functions

Aggregate functions calculate a value from multiple rows.

---

## COUNT()

Counts rows.

```sql
SELECT department,
COUNT(*) AS total_employees
FROM employees
GROUP BY department;
```

Output

| Department | Total Employees |
|------------|----------------:|
|HR|2|
|IT|2|
|Sales|1|

---

## SUM()

Adds values.

Example

```sql
SELECT department,
SUM(salary) AS total_salary
FROM employees
GROUP BY department;
```

Output

| Department | Total Salary |
|------------|-------------:|
|HR|85000|
|IT|135000|
|Sales|50000|

---

## AVG()

Returns average.

```sql
SELECT department,
AVG(salary) AS average_salary
FROM employees
GROUP BY department;
```

Output

| Department | Average Salary |
|------------|---------------:|
|HR|42500|
|IT|67500|
|Sales|50000|

---

## MAX()

Highest value.

```sql
SELECT department,
MAX(salary)
FROM employees
GROUP BY department;
```

---

## MIN()

Lowest value.

```sql
SELECT department,
MIN(salary)
FROM employees
GROUP BY department;
```

---

# Combining Multiple Aggregate Functions

```sql
SELECT
department,
COUNT(*) AS employees,
SUM(salary) AS total_salary,
AVG(salary) AS average_salary,
MAX(salary) AS highest_salary,
MIN(salary) AS lowest_salary
FROM employees
GROUP BY department;
```

Output

| Department | Employees | Total | Average | Max | Min |
|------------|----------:|------:|--------:|----:|----:|
|HR|2|85000|42500|45000|40000|
|IT|2|135000|67500|70000|65000|
|Sales|1|50000|50000|50000|50000|

---

# GROUP BY Multiple Columns

Suppose a company has multiple offices.

Orders Table

| id | city | category | amount |
|----|------|----------|-------:|
|1|Hyderabad|Electronics|1000|
|2|Hyderabad|Furniture|2000|
|3|Delhi|Electronics|1500|
|4|Delhi|Furniture|3000|
|5|Delhi|Electronics|2500|

Group by city and category.

```sql
SELECT city,
category,
SUM(amount) AS total_sales
FROM orders
GROUP BY city, category;
```

Output

| City | Category | Total |
|------|----------|------:|
|Delhi|Electronics|4000|
|Delhi|Furniture|3000|
|Hyderabad|Electronics|1000|
|Hyderabad|Furniture|2000|

MySQL creates one group for every unique combination of `city` and `category`.

---

# WHERE vs HAVING

Many beginners confuse these.

### WHERE

Filters **rows before grouping**.

### HAVING

Filters **groups after grouping**.

---

Example

```sql
SELECT department,
COUNT(*)
FROM employees
GROUP BY department
HAVING COUNT(*) > 1;
```

Output

```
HR
IT
```

Sales is excluded because it has only one employee.

---

# Why WHERE Cannot Use Aggregate Functions

Incorrect

```sql
SELECT department,
COUNT(*)
FROM employees
WHERE COUNT(*) > 1
GROUP BY department;
```

Error!

Because `WHERE` executes before grouping.

Correct

```sql
SELECT department,
COUNT(*)
FROM employees
GROUP BY department
HAVING COUNT(*) > 1;
```

---

# WHERE and HAVING Together

Example

Find departments having more than one employee whose salary is greater than 40000.

```sql
SELECT department,
COUNT(*) AS total
FROM employees
WHERE salary > 40000
GROUP BY department
HAVING COUNT(*) > 1;
```

Execution order:

1. WHERE filters rows
2. GROUP BY creates groups
3. Aggregate functions are calculated
4. HAVING filters groups
5. SELECT displays results
6. ORDER BY sorts the final result

---

# GROUP BY with ORDER BY

Sort grouped results.

```sql
SELECT department,
AVG(salary) AS average_salary
FROM employees
GROUP BY department
ORDER BY average_salary DESC;
```

Output

| Department | Average Salary |
|------------|---------------:|
|IT|67500|
|Sales|50000|
|HR|42500|

---

# GROUP BY with Aliases

```sql
SELECT department,
AVG(salary) AS avg_salary
FROM employees
GROUP BY department
ORDER BY avg_salary DESC;
```

Using aliases improves readability.

---

# Real-World Example 1

Online Store

Orders Table

| customer | amount |
|----------|-------:|
|Alice|100|
|Bob|250|
|Alice|300|
|Bob|150|
|Charlie|500|

Find total spending.

```sql
SELECT customer,
SUM(amount) AS total_spent
FROM orders
GROUP BY customer;
```

Output

| Customer | Total Spent |
|----------|------------:|
|Alice|400|
|Bob|400|
|Charlie|500|

---

# Real-World Example 2

School

Marks Table

| student | subject | marks |
|---------|---------|------:|
|John|Math|90|
|John|Science|80|
|Mary|Math|95|
|Mary|Science|85|

Average marks.

```sql
SELECT student,
AVG(marks)
FROM marks
GROUP BY student;
```

---

# Real-World Example 3

Hospital

Appointments

| doctor | patient |
|--------|---------|
|Dr A|John|
|Dr A|Rahul|
|Dr B|Alice|
|Dr A|Emma|

Count patients per doctor.

```sql
SELECT doctor,
COUNT(*) AS patients
FROM appointments
GROUP BY doctor;
```

---

# Common Mistakes

### Forgetting GROUP BY

Incorrect

```sql
SELECT department,
AVG(salary)
FROM employees;
```

If `department` is not aggregated, MySQL (depending on SQL mode) may return an error or undefined behavior.

Correct

```sql
SELECT department,
AVG(salary)
FROM employees
GROUP BY department;
```

---

### Using WHERE Instead of HAVING

Incorrect

```sql
WHERE COUNT(*) > 2
```

Correct

```sql
HAVING COUNT(*) > 2
```

---

### Grouping the Wrong Column

Always group by the column you want summarized.

---

# Best Practices

- Use meaningful aliases.
- Prefer `HAVING` only for aggregate filters.
- Use `WHERE` for row filtering.
- Keep grouped queries readable.
- Use `ORDER BY` when presenting grouped reports.
- Index frequently grouped columns for better performance.

---

# Interview Questions

### 1. What is GROUP BY?

Groups rows having the same values into summary groups.

---

### 2. Which clause filters grouped results?

`HAVING`

---

### 3. Difference between WHERE and HAVING?

| WHERE | HAVING |
|--------|---------|
|Filters rows|Filters groups|
|Runs before grouping|Runs after grouping|
|Cannot use aggregate functions|Can use aggregate functions|

---

### 4. Can GROUP BY use multiple columns?

Yes.

Example

```sql
GROUP BY city, category;
```

---

### 5. Which functions are commonly used with GROUP BY?

- COUNT()
- SUM()
- AVG()
- MAX()
- MIN()

---

# Practice Exercises

## Exercise 1

Count employees in each department.

---

## Exercise 2

Find average salary per department.

---

## Exercise 3

Find the highest salary in every department.

---

## Exercise 4

Find cities where total sales exceed ₹10,000.

(Hint: Use `HAVING SUM(amount) > 10000`.)

---

## Exercise 5

Group orders by customer and calculate:

- Total orders
- Total amount
- Average order value

---

## Exercise 6

Group students by class and find the highest marks.

---

## Mini Project

Create a `sales` table.

```text
id
salesperson
region
amount
```

Insert at least 10 records.

Write queries to:

1. Count sales by region.
2. Calculate total sales by region.
3. Find average sales by salesperson.
4. Show only regions with total sales greater than ₹20,000.
5. Sort regions by highest sales first.

---

# Summary

In this lesson, you learned:

- What `GROUP BY` is
- Why it is used
- Aggregate functions (`COUNT`, `SUM`, `AVG`, `MAX`, `MIN`)
- `HAVING` clause
- Difference between `WHERE` and `HAVING`
- Grouping by multiple columns
- `GROUP BY` with `ORDER BY`
- Real-world examples
- Common mistakes
- Best practices
- Practice exercises

---

# Next Lesson

**Lesson 28 — ROLLUP**

Topics covered:

- What is `WITH ROLLUP`?
- Grand totals
- Subtotals
- Hierarchical grouping
- Practical reporting examples