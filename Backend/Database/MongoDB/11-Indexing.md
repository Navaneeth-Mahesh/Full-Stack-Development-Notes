# Indexing

---

# What Will You Learn?

In this chapter, you'll learn:

- What is an Index?
- Why Indexing is Needed
- Searching Without an Index
- Searching With an Index
- B-Tree Index (Easy Explanation)
- createIndex()
- Single Field Index
- Compound Index
- Unique Index
- getIndexes()
- dropIndex()
- Advantages
- Disadvantages
- Real-World Examples
- Interview Questions

---

# What is an Index?

## Definition

An **Index** is a special data structure that helps MongoDB find documents much faster.

Think of an index like the **index page of a textbook**.

Instead of reading every page,

you look at the index,

find the page number,

and directly jump to that page.

MongoDB works the same way.

---

# Real-Life Example

Imagine a library with **50,000 books**.

You want a book named

```
Java Programming
```

### Without an Index

You check

Book 1

↓

Book 2

↓

Book 3

↓

...

↓

Book 50,000

Very slow.

---

### With an Index

You open the library index.

```
Java Programming

↓

Shelf B

↓

Row 12
```

You directly reach the book.

Very fast.

---

# Why Do We Need Indexing?

Suppose your collection contains

```
10 documents
```

Searching is easy.

Now imagine

```
10 Million Documents
```

Searching every document takes time.

Indexes make searching much faster.

---

# Searching Without an Index

Suppose collection

```json
{
"name":"Rahul"
}

{
"name":"Ajay"
}

{
"name":"Kiran"
}

{
"name":"Anjali"
}
```

Query

```javascript
db.students.find({
name:"Kiran"
})
```

MongoDB checks

```
Rahul

↓

Ajay

↓

Kiran ✔

↓

Stop
```

This is called

## Collection Scan

MongoDB scans every document one by one.

For millions of records,

this becomes slow.

---

# Searching With an Index

Now create an index

```
name
```

MongoDB builds a separate structure.

```
Ajay

↓

Anjali

↓

Kiran

↓

Rahul
```

Now searching

```
Kiran
```

MongoDB directly finds it.

Much faster.

---

# Think Like a Dictionary

Suppose you want

```
Apple
```

in a dictionary.

You don't start reading from page 1.

You directly go near

```
A
```

because the dictionary is already sorted.

An Index works exactly the same way.

---

# B-Tree Index (Easy Explanation)

MongoDB stores indexes using a

## B-Tree (Balanced Tree)

Don't worry about the complex name.

Think of it like

```
                M
             /      \
          G          T
        /   \      /   \
      C     J    P      Z
```

Instead of checking every value,

MongoDB quickly moves through the tree.

This makes searching extremely fast.

---

# Without B-Tree

```
1

↓

2

↓

3

↓

4

↓

5

↓

6

↓

7
```

Need to check every value.

---

# With B-Tree

```
      4
    /   \
   2     6
  / \   / \
 1  3 5   7
```

MongoDB reaches the correct value in very few steps.

---

# createIndex()

## Definition

Creates an index on one or more fields.

---

## Syntax

```javascript
db.collection.createIndex({
field:1
})
```

---

# Single Field Index

Create an index on

```
name
```

Example

```javascript
db.students.createIndex({
name:1
})
```

Output

```json
{
"ok":1
}
```

MongoDB creates an index on the `name` field.

---

# Meaning of 1 and -1

```javascript
1
```

Ascending Index

```javascript
-1
```

Descending Index

Both improve search speed.

The direction mainly matters for sorting.

---

# Example

Ascending

```javascript
db.students.createIndex({
marks:1
})
```

Descending

```javascript
db.students.createIndex({
marks:-1
})
```

---

# Compound Index

## Definition

Creates an index using multiple fields.

---

Example

```javascript
db.students.createIndex({

course:1,

marks:-1

})
```

MongoDB first indexes

```
course
```

Then inside each course,

it indexes

```
marks
```

---

# Real-Life Example

Employees

```
Department

Salary
```

Create

```javascript
db.employees.createIndex({

department:1,

salary:-1

})
```

Now searching

```
IT Department

Highest Salary
```

becomes very fast.

---

# Unique Index

## Definition

Prevents duplicate values.

Example

Email

Every user must have a unique email.

---

Syntax

```javascript
db.users.createIndex(

{
email:1
},

{
unique:true
}

)
```

---

Collection

```json
{
email:"abc@gmail.com"
}
```

Trying to insert

```json
{
email:"abc@gmail.com"
}
```

MongoDB throws an error.

Duplicate values are not allowed.

---

# Why Use Unique Index?

Examples

- Email
- Aadhaar Number
- Employee ID
- Username
- Passport Number

All should be unique.

---

# getIndexes()

## Definition

Shows every index created in a collection.

---

Syntax

```javascript
db.students.getIndexes()
```

Output

```json
[
{
"name":"_id_"
},

{
"name":"name_1"
}
]
```

---

# Why is _id Indexed Automatically?

Every MongoDB collection automatically creates an index on

```
_id
```

Because `_id` is unique for every document.

You don't need to create it manually.

---

# dropIndex()

## Definition

Deletes an index.

---

Syntax

```javascript
db.students.dropIndex("name_1")
```

MongoDB removes the index.

---

# dropIndexes()

Deletes every custom index.

```javascript
db.students.dropIndexes()
```

Only `_id` index remains.

---

# Index Example

Collection

```json
{
name:"Rahul",
city:"Hyderabad"
}

{
name:"Ajay",
city:"Guntur"
}

{
name:"Kiran",
city:"Hyderabad"
}
```

Create Index

```javascript
db.students.createIndex({

city:1

})
```

Now query

```javascript
db.students.find({

city:"Hyderabad"

})
```

MongoDB uses the index.

Search becomes much faster.

---

# Advantages of Indexing

✅ Faster Searching

Instead of scanning every document,

MongoDB directly finds data.

---

✅ Faster Sorting

Sorting large collections becomes much faster.

---

✅ Better Performance

Applications respond faster.

---

✅ Useful for Large Databases

Millions of records can be searched quickly.

---

# Disadvantages of Indexing

❌ Extra Storage

Indexes occupy additional disk space.

---

❌ Slower Insert

When inserting a document,

MongoDB updates

- Collection
- Index

Both need updating.

---

❌ Slower Update

If indexed fields change,

MongoDB updates the index too.

---

❌ Slower Delete

Deleting documents also updates indexes.

---

# Real-World Examples

## Instagram

Search username

```
navaneeth
```

Uses index.

---

## Amazon

Search product

```
iPhone 16
```

Uses index.

---

## Banking

Find account

```
Account Number
```

Uses index.

---

## Hospital

Find patient

```
Patient ID
```

Uses index.

---

## College

Search student

```
Roll Number
```

Uses index.

---

# Common Beginner Mistakes

## ❌ Creating Too Many Indexes

Every index consumes memory.

Create indexes only when needed.

---

## ❌ Indexing Every Field

Not every field should have an index.

Choose frequently searched fields.

---

## ❌ Forgetting Unique Index

Email should usually be unique.

Without a unique index,

duplicate emails can be inserted.

---

# Interview Questions

### What is an Index?

An Index is a data structure that improves the speed of searching documents.

---

### Why is Indexing Needed?

To reduce search time and improve query performance.

---

### Which command creates an index?

```javascript
createIndex()
```

---

### Which command displays indexes?

```javascript
getIndexes()
```

---

### Which command removes one index?

```javascript
dropIndex()
```

---

### Which command removes all custom indexes?

```javascript
dropIndexes()
```

---

### Which field is automatically indexed?

```
_id
```

---

### What is a Compound Index?

An index created using multiple fields.

---

### What is a Unique Index?

An index that prevents duplicate values in a field.

---

### What are the disadvantages of Indexing?

- Uses extra storage
- Slows inserts
- Slows updates
- Slows deletes

---

# Quick Revision

| Command | Purpose |
|----------|----------|
| createIndex() | Create an index |
| getIndexes() | View indexes |
| dropIndex() | Remove one index |
| dropIndexes() | Remove all custom indexes |

---

# Summary

- An **Index** helps MongoDB locate documents much faster.
- Without an index, MongoDB performs a **Collection Scan**, checking documents one by one.
- MongoDB stores indexes using a **B-Tree** data structure for efficient searching.
- Use **`createIndex()`** to create indexes.
- A **Single Field Index** indexes one field, while a **Compound Index** indexes multiple fields.
- A **Unique Index** prevents duplicate values in a field.
- **`getIndexes()`** displays all indexes, and **`dropIndex()`** removes a specific index.
- Every collection automatically has an index on the **`_id`** field.
- Indexes improve query performance but require additional storage and slightly slow insert, update, and delete operations.

---

# ✅ Part 5B Completed

You now understand **Indexing**, one of the most frequently asked MongoDB interview topics.

**Next:** **Part 5C – Text Search**, where you'll learn how MongoDB performs Google-like searches using **Text Indexes**, **`$text`**, and **`$search`**.
