# MongoDB CRUD Operations (Part 3)
# Update & Delete Operations

---

# What Will You Learn?

In Part 1, you learned:

- insertOne()
- insertMany()
- find()
- findOne()

In Part 2, you learned:

- Query Operators
- $eq
- $gt
- $lt
- $gte
- $lte
- $ne
- $in
- $nin

In this Part, you will learn:

- updateOne()
- updateMany()
- replaceOne()
- deleteOne()
- deleteMany()
- $set
- $unset
- $inc

---

# UPDATE Operation

Update means

> **Changing existing data inside a document.**

Example

Before Update

```json
{
    "name":"Rahul",
    "age":20,
    "city":"Hyderabad"
}
```

After Update

```json
{
    "name":"Rahul",
    "age":21,
    "city":"Hyderabad"
}
```

Only age changed.

---

# updateOne()

## Definition

Updates **only one matching document**.

Even if many documents satisfy the condition,

MongoDB updates only the first one.

---

## Syntax

```javascript
db.collection.updateOne(
    { condition },
    { update }
)
```

General Syntax

```javascript
db.students.updateOne(
    { name:"Rahul" },
    {
        $set:{
            age:21
        }
    }
)
```

---

## Example

Collection

```json
{
"name":"Rahul",
"age":20
}

{
"name":"Rahul",
"age":25
}
```

Command

```javascript
db.students.updateOne(
{
    name:"Rahul"
},
{
    $set:{
        age:30
    }
})
```

Result

```json
{
"name":"Rahul",
"age":30
}

{
"name":"Rahul",
"age":25
}
```

Only first Rahul changed.

---

# Output

```javascript
{
 acknowledged:true,
 matchedCount:1,
 modifiedCount:1
}
```

Meaning

| Output | Meaning |
|---------|----------|
| acknowledged | Operation successful |
| matchedCount | Documents found |
| modifiedCount | Documents updated |

---

# $set Operator

## Definition

`$set` is used to

- Add a new field
- Change an existing field

Think of it like

```
Set this value.
```

---

Example

```javascript
db.students.updateOne(
{
name:"Rahul"
},
{
$set:{
city:"Guntur"
}
})
```

Before

```json
{
"name":"Rahul",
"age":20
}
```

After

```json
{
"name":"Rahul",
"age":20,
"city":"Guntur"
}
```

Notice

City didn't exist.

MongoDB automatically added it.

---

Another Example

```javascript
$set:{
age:25
}
```

Age already exists,

so MongoDB updates it.

---

# updateMany()

## Definition

Updates **all matching documents**.

---

## Syntax

```javascript
db.collection.updateMany(
    { condition },
    {
        $set:{}
    }
)
```

---

Example

Collection

```json
{
city:"Hyderabad"
}

{
city:"Hyderabad"
}

{
city:"Guntur"
}
```

Command

```javascript
db.students.updateMany(
{
city:"Hyderabad"
},
{
$set:{
state:"Telangana"
}
})
```

Result

```json
{
city:"Hyderabad",
state:"Telangana"
}

{
city:"Hyderabad",
state:"Telangana"
}

{
city:"Guntur"
}
```

Both Hyderabad documents updated.

---

# Difference

| updateOne() | updateMany() |
|--------------|--------------|
| Updates first matching document | Updates every matching document |

---

# replaceOne()

## Definition

Completely replaces one document.

Everything is removed

except `_id`.

---

Syntax

```javascript
db.collection.replaceOne(
    { condition },
    {
        new document
    }
)
```

---

Example

Before

```json
{
"name":"Rahul",
"age":20,
"city":"Hyderabad"
}
```

Command

```javascript
db.students.replaceOne(
{
name:"Rahul"
},
{
name:"Rahul Kumar",
course:"MCA"
})
```

After

```json
{
"_id":ObjectId(...),
"name":"Rahul Kumar",
"course":"MCA"
}
```

Notice

Age

City

Both disappeared.

Because replaceOne replaces the entire document.

---

# Difference

| $set | replaceOne |
|------|-------------|
| Updates selected fields | Replaces entire document |
| Old fields remain | Old fields disappear |

---

# $unset

## Definition

Deletes a field from a document.

Not the document.

Only one field.

---

Syntax

```javascript
db.students.updateOne(
{
name:"Rahul"
},
{
$unset:{
city:""
}
})
```

Before

```json
{
"name":"Rahul",
"age":20,
"city":"Hyderabad"
}
```

After

```json
{
"name":"Rahul",
"age":20
}
```

City removed.

---

# $inc

## Definition

Increases or decreases a number.

Very useful for

- Likes
- Followers
- Balance
- Views
- Score

---

Example

Before

```json
{
likes:100
}
```

Command

```javascript
db.posts.updateOne(
{
_id:1
},
{
$inc:{
likes:1
}
})
```

After

```json
{
likes:101
}
```

---

Decrease

```javascript
$inc:{
balance:-500
}
```

If balance

```
10000
```

After

```
9500
```

---

# DELETE Operation

Delete means

Removing documents.

MongoDB provides

```
deleteOne()

deleteMany()
```

---

# deleteOne()

## Definition

Deletes only the first matching document.

---

Syntax

```javascript
db.collection.deleteOne(
{
condition
})
```

---

Example

Collection

```json
{
name:"Rahul"
}

{
name:"Rahul"
}

{
name:"Ajay"
}
```

Command

```javascript
db.students.deleteOne(
{
name:"Rahul"
})
```

Result

Only first Rahul deleted.

---

Output

```javascript
{
acknowledged:true,
deletedCount:1
}
```

---

# deleteMany()

## Definition

Deletes all matching documents.

---

Syntax

```javascript
db.collection.deleteMany(
{
condition
})
```

---

Example

```javascript
db.students.deleteMany(
{
city:"Hyderabad"
})
```

Every student from Hyderabad removed.

---

Delete All Documents

```javascript
db.students.deleteMany({})
```

Because

```
{}
```

means

```
Match every document.
```

All documents deleted.

Collection remains.

---

# deleteMany() vs drop()

| deleteMany({}) | drop() |
|----------------|---------|
| Deletes documents only | Deletes entire collection |
| Collection remains | Collection removed |

---

# Real-Life Examples

## Instagram

Increase likes

```javascript
$inc:{
likes:1
}
```

---

## Banking

Update balance

```javascript
$set:{
balance:50000
}
```

---

## College

Update student city

```javascript
$set:{
city:"Hyderabad"
}
```

---

## Shopping

Delete cancelled order

```javascript
deleteOne()
```

---

## Company

Update every employee salary

```javascript
updateMany()
```

---

# Common Beginner Mistakes

## ❌ Forgetting $set

Wrong

```javascript
updateOne(
{name:"Rahul"},
{
age:22
})
```

Correct

```javascript
updateOne(
{name:"Rahul"},
{
$set:{
age:22
}
})
```

---

## ❌ Using replaceOne instead of updateOne

replaceOne removes old fields.

updateOne changes only selected fields.

---

## ❌ deleteMany({})

Many beginners accidentally delete every document.

Always check your condition before executing.

---

# Comparison Table

| Method | Purpose |
|----------|----------|
| updateOne() | Update first matching document |
| updateMany() | Update all matching documents |
| replaceOne() | Replace entire document |
| deleteOne() | Delete first matching document |
| deleteMany() | Delete all matching documents |
| $set | Add or modify fields |
| $unset | Remove a field |
| $inc | Increase or decrease numeric value |

---

# Interview Questions

### What is the difference between updateOne() and updateMany()?

- updateOne() updates only the first matching document.
- updateMany() updates all matching documents.

---

### What does `$set` do?

It adds a new field or changes the value of an existing field.

---

### What does `$unset` do?

It removes a specific field from a document.

---

### What does `$inc` do?

It increments or decrements a numeric field by a specified value.

---

### What is the difference between replaceOne() and updateOne()?

- `replaceOne()` replaces the entire document (except `_id`).
- `updateOne()` modifies only the specified fields.

---

### What is the difference between deleteOne() and deleteMany()?

- `deleteOne()` removes the first matching document.
- `deleteMany()` removes all matching documents.

---

### What happens if you run `deleteMany({})`?

It deletes **all documents** from the collection, but the collection itself still exists.

---

# Quick Revision

| Method | Easy Meaning |
|---------|--------------|
| updateOne() | Update one document |
| updateMany() | Update all matching documents |
| replaceOne() | Replace complete document |
| $set | Add or change field |
| $unset | Remove field |
| $inc | Increase or decrease number |
| deleteOne() | Delete one document |
| deleteMany() | Delete all matching documents |

---

# Summary

- **updateOne()** modifies only the first matching document.
- **updateMany()** modifies every matching document.
- **$set** adds new fields or updates existing fields.
- **$unset** removes a field from a document.
- **$inc** increases or decreases numeric values.
- **replaceOne()** replaces the entire document except for `_id`.
- **deleteOne()** removes the first matching document.
- **deleteMany()** removes all matching documents that match the condition.
- Using **`deleteMany({})`** deletes every document but keeps the collection.
