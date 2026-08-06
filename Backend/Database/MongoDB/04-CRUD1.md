# MongoDB CRUD Operations (Part 1)
# insertOne(), insertMany(), find(), findOne()

---

# What is CRUD?

CRUD is the most basic and important concept in MongoDB.

CRUD stands for:

| Letter | Meaning | Purpose |
|---------|----------|---------|
| C | Create | Insert new data |
| R | Read | Read/View existing data |
| U | Update | Modify existing data |
| D | Delete | Remove data |

Example:

Imagine you have a **Students Collection**

```
students
```

Inside it,

```json
{
    "name":"Navaneeth",
    "age":21,
    "course":"MCA"
}
```

CRUD simply means

- Add new students
- View students
- Edit students
- Delete students

---

# MongoDB Data Structure

Before learning CRUD, remember this structure.

```
MongoDB
   │
Database
   │
Collection
   │
Document
```

Example

```
College
   │
Students
   │
{
   name:"Rahul",
   age:20,
   city:"Hyderabad"
}
```

Think like this:

```
Database = School

Collection = Classroom

Document = Student
```

---

# CREATE Operation

Create means

**Adding new documents into a collection.**

MongoDB provides two methods.

```
insertOne()

insertMany()
```

---

# 1. insertOne()

## Definition

`insertOne()` inserts **only one document** into a collection.

Syntax

```javascript
db.collectionName.insertOne(
{
   field1:value1,
   field2:value2
})
```

General Syntax

```javascript
db.students.insertOne(
{
   name:"Rahul",
   age:20,
   city:"Hyderabad"
})
```

---

## Example

```javascript
db.students.insertOne(
{
   name:"Navaneeth",
   age:21,
   course:"MCA",
   city:"Guntur"
})
```

Document Stored

```json
{
   "_id":ObjectId("..."),
   "name":"Navaneeth",
   "age":21,
   "course":"MCA",
   "city":"Guntur"
}
```

---

## Output

```javascript
{
   acknowledged: true,
   insertedId: ObjectId(...)
}
```

Meaning

| Output | Meaning |
|---------|----------|
| acknowledged:true | MongoDB successfully inserted the document |
| insertedId | Unique ID generated automatically |

---

# What is _id?

Every document must have a unique identity.

MongoDB automatically creates

```json
"_id"
```

Example

```json
{
 "_id":ObjectId("6892d...."),
 "name":"Rahul"
}
```

Think of it like

- Aadhaar Number
- Student Roll Number
- Employee ID

No two documents can have the same `_id`.

---

## Can we give our own _id?

Yes.

Example

```javascript
db.students.insertOne(
{
   _id:101,
   name:"Rahul",
   age:20
})
```

Result

```json
{
   "_id":101,
   "name":"Rahul",
   "age":20
}
```

If another document has `_id:101`

MongoDB throws an error because duplicate IDs are not allowed.

---

# Important Notes

✅ Collection doesn't exist?

MongoDB automatically creates it.

Example

```javascript
db.employees.insertOne(
{
   name:"Ram"
})
```

If "employees" collection does not exist,

MongoDB automatically creates

```
employees Collection
```

and inserts the document.

---

# Real Life Example

Instagram

When a new user signs up

```json
{
    "username":"john",
    "email":"john@gmail.com",
    "followers":0
}
```

Backend executes

```javascript
insertOne()
```

because only one account is created.

---

# 2. insertMany()

## Definition

`insertMany()` inserts **multiple documents at once**.

Instead of inserting one by one,

MongoDB inserts all together.

---

Syntax

```javascript
db.collectionName.insertMany(
[
   {},
   {},
   {}
])
```

Notice

```
Square Brackets []
```

Because multiple documents are stored inside an array.

---

Example

```javascript
db.students.insertMany([
{
   name:"Rahul",
   age:20
},
{
   name:"Kiran",
   age:22
},
{
   name:"Ajay",
   age:21
}
])
```

---

Documents Stored

```json
{
"name":"Rahul",
"age":20
}

{
"name":"Kiran",
"age":22
}

{
"name":"Ajay",
"age":21
}
```

---

Output

```javascript
{
 acknowledged:true,
 insertedIds:{
   '0':ObjectId(...),
   '1':ObjectId(...),
   '2':ObjectId(...)
 }
}
```

---

## Why use insertMany()?

Imagine

You have 500 students.

Instead of

```javascript
insertOne()
insertOne()
insertOne()
```

500 times,

Simply use

```javascript
insertMany()
```

It is

- Faster
- Saves time
- Better performance

---

# Difference

| insertOne() | insertMany() |
|--------------|--------------|
| Inserts one document | Inserts multiple documents |
| Uses {} | Uses [] |
| Faster for one record | Faster for bulk records |

---

# READ Operation

Read means

Viewing documents stored inside a collection.

MongoDB provides

```
find()

findOne()
```

---

# 3. find()

## Definition

Returns **all matching documents**.

If no condition is given,

returns every document.

---

Syntax

```javascript
db.collection.find()
```

Example

```javascript
db.students.find()
```

Suppose collection contains

```json
{
"name":"Rahul",
"age":20
}

{
"name":"Kiran",
"age":22
}

{
"name":"Ajay",
"age":21
}
```

Output

```json
{
"name":"Rahul",
"age":20
}

{
"name":"Kiran",
"age":22
}

{
"name":"Ajay",
"age":21
}
```

Everything is displayed.

---

# find() with Condition

Syntax

```javascript
db.collection.find(
{
 field:value
})
```

Example

```javascript
db.students.find(
{
 age:21
})
```

Output

```json
{
"name":"Ajay",
"age":21
}
```

---

Another Example

```javascript
db.students.find(
{
 city:"Hyderabad"
})
```

Returns every student whose city is Hyderabad.

---

# Why find() Returns Multiple Documents?

Imagine

Classroom

```
Rahul
Ajay
Kiran
Rahul
Rahul
```

Searching

```javascript
name:"Rahul"
```

There are 3 Rahuls.

MongoDB returns

All three.

---

# find({})

Empty braces mean

```
No condition.
```

Example

```javascript
db.students.find({})
```

Returns

Every document inside the collection.

---

# 4. findOne()

## Definition

Returns **only the first matching document**.

Even if there are many matches,

only one is returned.

---

Syntax

```javascript
db.collection.findOne()
```

Example

```javascript
db.students.findOne()
```

Output

```json
{
"name":"Rahul",
"age":20
}
```

Only one document is shown.

---

Example

```javascript
db.students.findOne(
{
age:21
})
```

Output

```json
{
"name":"Ajay",
"age":21
}
```

Only the first matching document is returned.

---

# Difference Between find() and findOne()

Suppose collection

```json
{
"name":"Rahul"
}

{
"name":"Rahul"
}

{
"name":"Rahul"
}
```

Using

```javascript
db.students.find(
{
name:"Rahul"
})
```

Output

```json
Rahul
Rahul
Rahul
```

All documents returned.

---

Using

```javascript
db.students.findOne(
{
name:"Rahul"
})
```

Output

```json
Rahul
```

Only first matching document returned.

---

# Comparison Table

| Method | Purpose | Returns |
|----------|----------|----------|
| insertOne() | Insert one document | One document inserted |
| insertMany() | Insert many documents | Multiple documents inserted |
| find() | Read documents | All matching documents |
| findOne() | Read one document | First matching document |

---

# Interview Questions

### 1. What is CRUD?

CRUD stands for Create, Read, Update and Delete.

---

### 2. Which method inserts one document?

```
insertOne()
```

---

### 3. Which method inserts multiple documents?

```
insertMany()
```

---

### 4. Which method returns all documents?

```
find()
```

---

### 5. Which method returns only one document?

```
findOne()
```

---

### 6. What is `_id`?

A unique identifier automatically generated for every document in MongoDB. It ensures each document can be uniquely identified.

---

### 7. Does MongoDB automatically create a collection?

**Yes.** If you insert a document into a collection that doesn't exist, MongoDB creates the collection automatically.

---

# Quick Revision

| Method | Remember As |
|----------|-------------|
| insertOne() | Add one document |
| insertMany() | Add multiple documents |
| find() | Show all matching documents |
| findOne() | Show only the first matching document |
| _id | Unique identity of every document |

---

# Summary

- **Create** operations are used to insert data into a collection.
- **insertOne()** adds a single document.
- **insertMany()** adds multiple documents in one operation.
- **Read** operations are used to retrieve data.
- **find()** returns all documents that match a condition.
- **findOne()** returns only the first matching document.
- Every document has a unique **`_id`** field, generated automatically unless you provide one.
- MongoDB automatically creates a collection when you insert data into a collection that doesn't already exist.
