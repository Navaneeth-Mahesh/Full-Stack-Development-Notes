# Querying Data - Projection, Sorting, Limiting & Skipping

---

# What Will You Learn?

In this chapter, you'll learn how to control **what data** MongoDB returns and **how it returns it**.

Topics covered:

- Projection
- sort()
- limit()
- skip()

---

# Sample Collection

Assume our **students** collection contains:

```json
{
    "_id":1,
    "name":"Rahul",
    "age":20,
    "course":"MCA",
    "marks":75,
    "city":"Hyderabad"
}

{
    "_id":2,
    "name":"Ajay",
    "age":22,
    "course":"BCA",
    "marks":90,
    "city":"Guntur"
}

{
    "_id":3,
    "name":"Kiran",
    "age":21,
    "course":"MCA",
    "marks":82,
    "city":"Vijayawada"
}

{
    "_id":4,
    "name":"Anjali",
    "age":19,
    "course":"B.Tech",
    "marks":68,
    "city":"Hyderabad"
}
```

---

# What is Projection?

## Definition

**Projection** means selecting **which fields** you want MongoDB to return.

Without projection,

MongoDB returns **every field**.

Example

```javascript
db.students.find()
```

Output

```json
{
"name":"Rahul",
"age":20,
"course":"MCA",
"marks":75,
"city":"Hyderabad"
}
```

Everything is displayed.

---

# Why Do We Need Projection?

Imagine a document contains

```json
{
"name":"Rahul",
"age":20,
"phone":"9876543210",
"email":"rahul@gmail.com",
"password":"abc123",
"address":"Hyderabad"
}
```

Suppose your website only needs

- Name
- Age

There is no need to send

- Password
- Email
- Address

Projection helps return only the required data.

---

# Projection Syntax

```javascript
db.collection.find(
    { condition },
    { projection }
)
```

General Form

```javascript
db.students.find(
{},
{
name:1,
age:1
})
```

---

# Include Fields

To include a field,

use

```javascript
1
```

Example

```javascript
db.students.find(
{},
{
name:1,
age:1
})
```

Output

```json
{
"name":"Rahul",
"age":20
}

{
"name":"Ajay",
"age":22
}
```

Only Name and Age are displayed.

---

# Exclude Fields

To remove a field,

use

```javascript
0
```

Example

```javascript
db.students.find(
{},
{
marks:0
})
```

Output

```json
{
"name":"Rahul",
"age":20,
"course":"MCA",
"city":"Hyderabad"
}
```

Marks field is hidden.

---

# Important Rule

You **cannot mix**

```javascript
1
```

and

```javascript
0
```

Example

❌ Wrong

```javascript
db.students.find(
{},
{
name:1,
marks:0
})
```

MongoDB throws an error.

---

# Exception

The `_id` field can be excluded while including other fields.

Example

```javascript
db.students.find(
{},
{
_id:0,
name:1,
age:1
})
```

Output

```json
{
"name":"Rahul",
"age":20
}
```

---

# Why Does _id Appear Automatically?

MongoDB automatically returns `_id`.

Example

```javascript
db.students.find(
{},
{
name:1
})
```

Output

```json
{
"_id":1,
"name":"Rahul"
}
```

To hide it,

```javascript
_id:0
```

---

# Projection Summary

| Value | Meaning |
|--------|----------|
| 1 | Include field |
| 0 | Exclude field |
| _id:0 | Hide ID |

---

# Sorting Data

## Definition

Sorting means arranging data in a particular order.

Examples

- Highest marks first
- Lowest salary first
- Alphabetical names
- Latest orders first

MongoDB uses

```javascript
sort()
```

---

# Syntax

```javascript
db.collection.find().sort(
{
field:1
})
```

---

# Ascending Order

Ascending means

```
Small → Large

A → Z

1 → 100
```

Use

```javascript
1
```

Example

```javascript
db.students.find().sort(
{
age:1
})
```

Output

```
19

20

21

22
```

---

# Descending Order

Descending means

```
Large → Small

Z → A

100 → 1
```

Use

```javascript
-1
```

Example

```javascript
db.students.find().sort(
{
marks:-1
})
```

Output

```
90

82

75

68
```

Highest marks first.

---

# Sort by Name

Example

```javascript
db.students.find().sort(
{
name:1
})
```

Output

```
Ajay

Anjali

Kiran

Rahul
```

Alphabetical order.

---

# Multiple Sorting

MongoDB can sort by multiple fields.

Example

```javascript
db.students.find().sort(
{
course:1,
marks:-1
})
```

Meaning

- Sort course alphabetically.
- Inside each course, show highest marks first.

---

# Real-Life Example

Instagram

Latest posts first

```javascript
db.posts.find().sort(
{
createdAt:-1
})
```

Newest post appears first.

---

# sort() Summary

| Value | Meaning |
|--------|----------|
| 1 | Ascending |
| -1 | Descending |

---

# Limiting Data

## Definition

Sometimes we don't need every document.

We only want

- Top 5 students
- Top 10 products
- Latest 3 posts

MongoDB provides

```javascript
limit()
```

---

# Syntax

```javascript
db.collection.find().limit(number)
```

---

# Example

```javascript
db.students.find().limit(2)
```

Output

Only first two documents.

---

Another Example

```javascript
db.students.find()
.sort(
{
marks:-1
})
.limit(3)
```

Output

Top three students by marks.

---

# Why Use limit()?

Imagine

A collection has

```
10,00,000 documents
```

Showing all is slow.

Instead

```javascript
limit(20)
```

shows only 20.

Faster and saves memory.

---

# Pagination

Every website uses

```
limit()
```

Example

Amazon

20 products per page.

Instagram

10 posts at a time.

YouTube

20 videos per page.

---

# Skipping Documents

## Definition

Skip ignores the first few documents.

MongoDB provides

```javascript
skip()
```

---

# Syntax

```javascript
db.collection.find().skip(number)
```

---

# Example

```javascript
db.students.find().skip(2)
```

MongoDB ignores

Document 1

Document 2

Starts from Document 3.

---

Example

Collection

```
Rahul

Ajay

Kiran

Anjali
```

Command

```javascript
db.students.find().skip(2)
```

Output

```
Kiran

Anjali
```

---

# Combining skip() and limit()

This is one of the most common interview questions.

Example

```javascript
db.students.find()
.skip(5)
.limit(5)
```

Meaning

Ignore first five students.

Return next five students.

---

# Pagination Example

Suppose each page shows

```
10 students
```

Page 1

```javascript
db.students.find()
.skip(0)
.limit(10)
```

Page 2

```javascript
db.students.find()
.skip(10)
.limit(10)
```

Page 3

```javascript
db.students.find()
.skip(20)
.limit(10)
```

Formula

```
skip = (pageNumber - 1) × limit
```

Example

Page 4

```
skip=(4-1)×10

skip=30
```

Command

```javascript
db.students.find()
.skip(30)
.limit(10)
```

---

# Combining Everything

Example

```javascript
db.students.find(
{},
{
_id:0,
name:1,
marks:1
})
.sort(
{
marks:-1
})
.skip(1)
.limit(2)
```

What happens?

Step 1

Projection

```
Only Name and Marks
```

↓

Step 2

Sort

```
Highest Marks First
```

↓

Step 3

Skip

```
Ignore First Student
```

↓

Step 4

Limit

```
Return Next Two Students
```

---

# Common Beginner Mistakes

### ❌ Forgetting Projection Position

Wrong

```javascript
find({
name:1
})
```

Correct

```javascript
find(
{},
{
name:1
})
```

---

### ❌ Using limit before sort

Bad

```javascript
find().limit(5).sort({marks:-1})
```

Better

```javascript
find().sort({marks:-1}).limit(5)
```

Sort first, then limit.

---

### ❌ Mixing 1 and 0

Wrong

```javascript
{
name:1,
age:0
}
```

Not allowed (except `_id`).

---

# Interview Questions

### What is Projection?

Projection is the process of selecting which fields should be returned in the query result.

---

### What does `1` mean in Projection?

It includes the field.

---

### What does `0` mean in Projection?

It excludes the field.

---

### Which field is returned automatically?

```
_id
```

---

### How do you hide `_id`?

```javascript
{
_id:0
}
```

---

### What does `sort({marks:1})` do?

Sorts documents by marks in ascending order.

---

### What does `sort({marks:-1})` do?

Sorts documents by marks in descending order.

---

### Why is `limit()` used?

To return only a fixed number of documents, improving performance and supporting pagination.

---

### Why is `skip()` used?

To ignore a certain number of documents, commonly used with `limit()` for pagination.

---

# Quick Revision

| Method | Purpose |
|----------|----------|
| Projection | Select required fields |
| sort() | Arrange documents |
| limit() | Return limited documents |
| skip() | Ignore first documents |

---

# Summary

- **Projection** controls which fields are returned.
- Use **`1`** to include fields and **`0`** to exclude fields.
- `_id` is returned automatically unless you specify `_id:0`.
- **sort()** arranges documents in ascending (`1`) or descending (`-1`) order.
- **limit()** restricts the number of documents returned.
- **skip()** ignores a specified number of documents.
- `sort()`, `skip()`, and `limit()` are commonly combined to implement **pagination** in web applications.
