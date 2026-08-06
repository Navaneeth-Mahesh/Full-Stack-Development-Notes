# MongoDB CRUD Operations (Part 2)
# Querying Data with find() Conditions
---

# What Will You Learn?

In Part 1, we learned:

- insertOne()
- insertMany()
- find()
- findOne()

Now we'll learn how to search data more intelligently using **query operators**.

Imagine you have 10,000 student records.

You don't want to see all students.

Instead, you may want to find:

- Students older than 20
- Students from Hyderabad
- Students whose marks are above 80
- Students studying MCA

This is where **Query Operators** help.

---

# Sample Collection

Suppose we have a collection called **students**

```json
{
    "name":"Rahul",
    "age":20,
    "course":"MCA",
    "marks":75,
    "city":"Hyderabad"
}

{
    "name":"Ajay",
    "age":22,
    "course":"BCA",
    "marks":82,
    "city":"Guntur"
}

{
    "name":"Kiran",
    "age":21,
    "course":"MCA",
    "marks":91,
    "city":"Hyderabad"
}

{
    "name":"Anjali",
    "age":19,
    "course":"B.Tech",
    "marks":68,
    "city":"Vijayawada"
}
```

---

# What is a Query Operator?

A Query Operator tells MongoDB **how to compare values**.

Instead of checking only exact matches,

we can check:

- Greater than
- Less than
- Equal to
- Not equal
- Inside a list
- Not inside a list

MongoDB operators always begin with **$**

Example

```javascript
$gt
$lt
$eq
$ne
$in
$nin
```

---

# 1. $eq (Equal To)

## Definition

Returns documents where the value is exactly equal.

Syntax

```javascript
db.students.find({
    age:{
        $eq:21
    }
})
```

Example

```javascript
db.students.find({
    course:{
        $eq:"MCA"
    }
})
```

Output

```json
Rahul
Kiran
```

Both students are studying MCA.

---

## Shortcut

Instead of

```javascript
db.students.find({
    course:{
        $eq:"MCA"
    }
})
```

You can simply write

```javascript
db.students.find({
    course:"MCA"
})
```

Both are exactly the same.

---

# 2. $gt (Greater Than)

## Definition

Returns documents whose value is greater than the specified value.

Syntax

```javascript
db.students.find({
    age:{
        $gt:20
    }
})
```

Meaning

```
Age > 20
```

Output

```json
Ajay
Kiran
```

Because

```
22 > 20

21 > 20
```

---

## Real-Life Example

Find employees whose salary is above ₹50,000.

```javascript
db.employees.find({
    salary:{
        $gt:50000
    }
})
```

---

# 3. $lt (Less Than)

## Definition

Returns documents whose value is less than the given value.

Syntax

```javascript
db.students.find({
    age:{
        $lt:21
    }
})
```

Meaning

```
Age < 21
```

Output

```json
Rahul
Anjali
```

---

Example

Find students whose marks are below 80.

```javascript
db.students.find({
    marks:{
        $lt:80
    }
})
```

Output

```
Rahul

Anjali
```

---

# 4. $gte (Greater Than or Equal)

Definition

Returns documents whose value is greater than or equal to the specified value.

Syntax

```javascript
db.students.find({
    marks:{
        $gte:80
    }
})
```

Meaning

```
Marks ≥ 80
```

Output

```json
Ajay

Kiran
```

---

# 5. $lte (Less Than or Equal)

Definition

Returns documents whose value is less than or equal to the given value.

Example

```javascript
db.students.find({
    age:{
        $lte:20
    }
})
```

Output

```json
Rahul

Anjali
```

---

# 6. $ne (Not Equal)

Definition

Returns every document whose value is NOT equal.

Syntax

```javascript
db.students.find({
    city:{
        $ne:"Hyderabad"
    }
})
```

Output

```json
Ajay

Anjali
```

Because these students are not from Hyderabad.

---

## Real-Life Example

Show all products except Apple.

```javascript
db.products.find({
    brand:{
        $ne:"Apple"
    }
})
```

---

# 7. $in

## Definition

Checks whether a value exists inside a given list.

Think of it like

```
OR OR OR
```

Syntax

```javascript
db.students.find({
    city:{
        $in:[
            "Hyderabad",
            "Guntur"
        ]
    }
})
```

Meaning

Return students whose city is

- Hyderabad
OR
- Guntur

Output

```json
Rahul

Ajay

Kiran
```

---

## Real-Life Example

Find employees working in

- HR
- Sales
- IT

```javascript
db.employees.find({
    department:{
        $in:[
            "HR",
            "Sales",
            "IT"
        ]
    }
})
```

---

# 8. $nin

Definition

Opposite of `$in`.

Returns documents whose values are **NOT** inside the list.

Example

```javascript
db.students.find({
    city:{
        $nin:[
            "Hyderabad",
            "Guntur"
        ]
    }
})
```

Output

```json
Anjali
```

---

# Combining Conditions

MongoDB can check multiple conditions together.

Example

Students studying MCA whose marks are greater than 80.

```javascript
db.students.find({
    course:"MCA",
    marks:{
        $gt:80
    }
})
```

Output

```json
Kiran
```

Because only Kiran satisfies both conditions.

---

# Multiple Operators on Same Field

Example

Students whose marks are between 70 and 90.

```javascript
db.students.find({
    marks:{
        $gt:70,
        $lt:90
    }
})
```

Meaning

```
70 < Marks < 90
```

Output

```json
Rahul

Ajay
```

---

# Difference Between Operators

| Operator | Meaning | Example |
|-----------|---------|---------|
| $eq | Equal | Age = 20 |
| $gt | Greater Than | Age > 20 |
| $lt | Less Than | Age < 20 |
| $gte | Greater Than or Equal | Age ≥ 20 |
| $lte | Less Than or Equal | Age ≤ 20 |
| $ne | Not Equal | City ≠ Hyderabad |
| $in | Value exists in list | Hyderabad or Guntur |
| $nin | Value not in list | Not Hyderabad |

---

# Real-World Examples

## E-Commerce

Find products costing more than ₹10,000

```javascript
db.products.find({
    price:{
        $gt:10000
    }
})
```

---

## School

Find students scoring above 90

```javascript
db.students.find({
    marks:{
        $gt:90
    }
})
```

---

## Hospital

Find patients older than 60

```javascript
db.patients.find({
    age:{
        $gt:60
    }
})
```

---

## Banking

Find accounts with balance less than ₹5,000

```javascript
db.accounts.find({
    balance:{
        $lt:5000
    }
})
```

---

# Common Beginner Mistakes

### ❌ Forgetting the `$`

Wrong

```javascript
gt:20
```

Correct

```javascript
$gt:20
```

---

### ❌ Using parentheses instead of braces

Wrong

```javascript
age($gt:20)
```

Correct

```javascript
age:{
    $gt:20
}
```

---

### ❌ Forgetting square brackets with `$in`

Wrong

```javascript
$in:"Hyderabad","Guntur"
```

Correct

```javascript
$in:[
    "Hyderabad",
    "Guntur"
]
```

---

# Interview Questions

### What are Query Operators?

Query operators are special keywords (starting with `$`) used to compare field values and filter documents.

---

### Which operator means "Greater Than"?

```
$gt
```

---

### Which operator means "Less Than"?

```
$lt
```

---

### Which operator checks equality?

```
$eq
```

---

### Which operator means "Not Equal"?

```
$ne
```

---

### Which operator checks whether a value exists in a list?

```
$in
```

---

### Which operator checks that a value is NOT in a list?

```
$nin
```

---

# Quick Revision

| Operator | Easy Meaning |
|-----------|--------------|
| $eq | Equal |
| $gt | Bigger |
| $lt | Smaller |
| $gte | Bigger or Equal |
| $lte | Smaller or Equal |
| $ne | Not Equal |
| $in | Present in List |
| $nin | Not Present in List |

---

# Summary

- Query operators help filter data based on conditions.
- `$eq` checks for exact matches.
- `$gt` and `$lt` compare greater than and less than values.
- `$gte` and `$lte` include equality in comparisons.
- `$ne` excludes matching values.
- `$in` checks whether a value belongs to a list.
- `$nin` excludes values present in a list.
- Multiple conditions can be combined in a single `find()` query to retrieve more specific results.
