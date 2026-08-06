# Logical Operators ($and, $or, $not, $nor)

---

# What Will You Learn?

In this chapter, you'll learn how to combine multiple conditions while querying data.

Topics covered:

- $and
- $or
- $not
- $nor
- Combining Logical Operators
- Real-world Examples
- Interview Questions

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
    "city":"Hyderabad"
}

{
    "_id":4,
    "name":"Anjali",
    "age":19,
    "course":"B.Tech",
    "marks":68,
    "city":"Vijayawada"
}
```

---

# What are Logical Operators?

Logical operators allow MongoDB to check **multiple conditions** in a query.

Imagine asking:

- Students older than 20 **AND** studying MCA
- Students from Hyderabad **OR** Guntur
- Students **NOT** from Hyderabad
- Students who are **neither** from Hyderabad **nor** studying MCA

These queries are possible using logical operators.

---

# MongoDB Logical Operators

| Operator | Meaning |
|----------|----------|
| $and | All conditions must be true |
| $or | At least one condition must be true |
| $not | Reverse a condition |
| $nor | None of the conditions should be true |

---

# $and Operator

## Definition

Returns documents only if **every condition is true**.

Think of it like

```
Condition 1 ✔

AND

Condition 2 ✔

↓

Return document
```

If even one condition fails,

MongoDB ignores the document.

---

## Syntax

```javascript
db.collection.find({
    $and:[
        {condition1},
        {condition2}
    ]
})
```

---

## Example

Find students

- Age greater than 20
- Course is MCA

```javascript
db.students.find({
    $and:[
        {age:{$gt:20}},
        {course:"MCA"}
    ]
})
```

Output

```json
{
"name":"Kiran",
"age":21,
"course":"MCA"
}
```

Rahul is MCA but age is only 20.

Ajay is older than 20 but not MCA.

Only Kiran satisfies both conditions.

---

# Shortcut

Instead of writing

```javascript
db.students.find({
$and:[
{age:{$gt:20}},
{course:"MCA"}
]
})
```

You can write

```javascript
db.students.find({
age:{$gt:20},
course:"MCA"
})
```

MongoDB automatically treats it as an AND condition.

---

# Real-Life Example

Find products

- Brand = Samsung
- Price below ₹30,000

```javascript
db.products.find({
brand:"Samsung",
price:{
$lt:30000
}
})
```

---

# $or Operator

## Definition

Returns documents if **at least one condition is true**.

Think like

```
Condition A

OR

Condition B
```

If either condition is true,

the document is returned.

---

## Syntax

```javascript
db.collection.find({
$or:[
{condition1},
{condition2}
]
})
```

---

## Example

Find students from

- Hyderabad
OR
- Guntur

```javascript
db.students.find({
$or:[
{city:"Hyderabad"},
{city:"Guntur"}
]
})
```

Output

```json
Rahul

Ajay

Kiran
```

Anjali is from Vijayawada,

so she is not returned.

---

# Another Example

Find students

- MCA
OR
- Marks above 85

```javascript
db.students.find({
$or:[
{course:"MCA"},
{marks:{$gt:85}}
]
})
```

Output

```
Rahul

Ajay

Kiran
```

---

# Difference Between AND and OR

Suppose

```
Age >20

Course=MCA
```

| Student | Age>20 | MCA | AND | OR |
|----------|---------|------|------|------|
| Rahul | ❌ | ✔ | ❌ | ✔ |
| Ajay | ✔ | ❌ | ❌ | ✔ |
| Kiran | ✔ | ✔ | ✔ | ✔ |

Notice

AND is stricter.

OR is more flexible.

---

# $not Operator

## Definition

`$not` reverses a condition.

It means

```
NOT THIS CONDITION
```

---

## Syntax

```javascript
db.collection.find({
field:{
$not:{
condition
}
}
})
```

---

## Example

Find students whose marks are **NOT greater than 80**

```javascript
db.students.find({
marks:{
$not:{
$gt:80
}
}
})
```

Output

```
Rahul

Anjali
```

Because

```
75

68
```

are not greater than 80.

---

# Another Example

Find students whose age is **NOT less than 21**

```javascript
db.students.find({
age:{
$not:{
$lt:21
}
}
})
```

Output

```
Ajay

Kiran
```

Equivalent to

```
Age >=21
```

---

# When is $not Used?

Mostly with comparison operators.

Example

```javascript
$not:{
$eq:20
}
```

or

```javascript
$not:{
$gt:80
}
```

---

# $nor Operator

## Definition

`$nor` means

> None of the given conditions should be true.

Think like

```
NOT

Condition A

AND

NOT

Condition B
```

---

## Syntax

```javascript
db.collection.find({
$nor:[
{condition1},
{condition2}
]
})
```

---

## Example

Find students who are

- NOT from Hyderabad
- NOT studying MCA

```javascript
db.students.find({
$nor:[
{city:"Hyderabad"},
{course:"MCA"}
]
})
```

Output

```
Ajay

Anjali
```

Because

Rahul

❌ Hyderabad

❌ MCA

Kiran

❌ Hyderabad

❌ MCA

Ajay

✔ Guntur

✔ BCA

Anjali

✔ Vijayawada

✔ B.Tech

---

# Difference Between $not and $nor

| $not | $nor |
|------|-------|
| Negates one condition | Negates multiple conditions |
| Works on a field | Works on multiple query expressions |

---

# Combining Logical Operators

Example

Students

- MCA
AND
- (Marks above 80 OR City is Hyderabad)

```javascript
db.students.find({
course:"MCA",
$or:[
{marks:{$gt:80}},
{city:"Hyderabad"}
]
})
```

Output

```
Rahul

Kiran
```

Rahul

✔ MCA

✔ Hyderabad

Kiran

✔ MCA

✔ Marks>80

---

# Another Example

Find students

- Age above 20
AND
- Not from Hyderabad

```javascript
db.students.find({
age:{
$gt:20
},
city:{
$ne:"Hyderabad"
}
})
```

Output

```
Ajay
```

---

# Real-World Examples

## E-Commerce

Samsung phones OR Apple phones

```javascript
db.products.find({
$or:[
{brand:"Samsung"},
{brand:"Apple"}
]
})
```

---

## Banking

Accounts

Balance above ₹50,000

AND

Status Active

```javascript
db.accounts.find({
balance:{
$gt:50000
},
status:"Active"
})
```

---

## Hospital

Patients

Age above 60

OR

Critical

```javascript
db.patients.find({
$or:[
{age:{
$gt:60
}},
{critical:true}
]
})
```

---

## School

Students

NOT failed

```javascript
db.students.find({
result:{
$ne:"Fail"
}
})
```

---

# Common Beginner Mistakes

## ❌ Forgetting []

Wrong

```javascript
$or:{
city:"Hyderabad",
city:"Guntur"
}
```

Correct

```javascript
$or:[
{city:"Hyderabad"},
{city:"Guntur"}
]
```

---

## ❌ Using AND unnecessarily

Instead of

```javascript
$and:[
{name:"Rahul"},
{age:20}
]
```

Simply write

```javascript
{
name:"Rahul",
age:20
}
```

MongoDB automatically treats it as AND.

---

## ❌ Confusing $not with $ne

`$ne`

Checks

```
Not Equal
```

`$not`

Reverses another operator.

---

# Interview Questions

### What is `$and`?

Returns documents only when all conditions are true.

---

### What is `$or`?

Returns documents when at least one condition is true.

---

### What is `$not`?

Negates a condition and works with comparison operators.

---

### What is `$nor`?

Returns documents only when none of the specified conditions are true.

---

### Which operator is automatically applied when multiple fields are written inside `find()`?

```
AND
```

Example

```javascript
db.students.find({
course:"MCA",
age:{
$gt:20
}
})
```

---

### Difference between `$ne` and `$not`?

`$ne`

Checks inequality.

`$not`

Negates another operator such as `$gt`, `$lt`, or `$eq`.

---

# Quick Revision

| Operator | Easy Meaning |
|-----------|--------------|
| $and | Every condition must be true |
| $or | Any one condition is enough |
| $not | Reverse one condition |
| $nor | None of the conditions should be true |

---

# Summary

- **`$and`** returns documents only when every condition is satisfied.
- Writing multiple fields inside `find()` automatically behaves like an **AND** query.
- **`$or`** returns documents when at least one condition matches.
- **`$not`** reverses a comparison operator and is used on a single field.
- **`$nor`** returns documents only when none of the listed conditions match.
- Logical operators are commonly combined to create powerful and flexible queries in real-world applications.
