# MongoDB Basics (MongoDB, MongoDB Compass & MongoDB Shell)
> Easy to Understand | Interview Ready |
---

# What is MongoDB?

## Definition

MongoDB is a **NoSQL (Not Only SQL)** database used to store data in the form of **documents** instead of tables.

Unlike MySQL, MongoDB does not use rows and columns.

Instead, it stores data in **JSON-like documents** called **BSON (Binary JSON)**.

Think of MongoDB as a **digital cupboard** where each cupboard contains collections, and each collection stores documents.

---

# Why MongoDB?

Traditional databases like MySQL work well with fixed data.

Example:

Student Table

| ID | Name | Age |
|----|------|-----|
|1|Navaneeth|22|

Every row must have the same columns.

But real-world applications often store different kinds of information.

Example:

User 1

```json
{
   "name":"Navaneeth",
   "age":22
}
```

User 2

```json
{
   "name":"Rahul",
   "age":25,
   "hobbies":["Cricket","Music"]
}
```

Notice that User 2 has an extra field (**hobbies**).

MongoDB allows this.

This is called **Flexible Schema**.

---

# Why is MongoDB called NoSQL?

NoSQL means **Not Only SQL**.

It doesn't mean SQL is bad.

It simply means MongoDB stores data differently.

Instead of

- Tables
- Rows
- Columns

MongoDB uses

- Databases
- Collections
- Documents

---

# SQL vs MongoDB

| SQL Database | MongoDB |
|--------------|----------|
|Database|Database|
|Table|Collection|
|Row|Document|
|Column|Field|
|Primary Key|_id|
|Schema Fixed|Schema Flexible|

Example

MySQL

```
Students
-------------------
ID Name Age
1  Tom  20
```

MongoDB

```json
{
   "_id":"1",
   "name":"Tom",
   "age":20
}
```

---

# Real-Life Example

Imagine a school.

In MySQL

```
School
   |
Students Table
   |
Rows
```

In MongoDB

```
School Database
      |
Students Collection
      |
Student Documents
```

Each student document can contain different information.

---

# What is BSON?

MongoDB stores data as **BSON**.

BSON stands for

> Binary JavaScript Object Notation

Although we write JSON,

MongoDB internally converts it into BSON because BSON is

- Faster
- Smaller
- Easier for computers to process

Example JSON

```json
{
   "name":"Navaneeth",
   "age":22
}
```

MongoDB stores it internally as BSON.

---

# MongoDB Architecture

```
MongoDB Server

│

├── Database
│      │
│      ├── Collection
│      │       │
│      │       ├── Document
│      │       ├── Document
│      │       ├── Document
```

---

# Database

A Database is a container that stores collections.

Example

```
College
Company
Instagram
Netflix
```

Each one is a separate database.

---

# Collection

A Collection is a group of similar documents.

Example

```
Students Collection

Employee Collection

Users Collection
```

Think of Collection as a folder.

---

# Document

A Document is a single record.

Example

```json
{
   "name":"Navaneeth",
   "age":22,
   "city":"Hyderabad"
}
```

A document is similar to one row in MySQL.

---

# Field

Each key-value pair inside a document is called a Field.

Example

```json
{
   "name":"Navaneeth",
   "age":22
}
```

Fields are

```
name
age
```

Values are

```
Navaneeth
22
```

---

# _id Field

Every document automatically gets a unique field called

```
_id
```

Example

```json
{
   "_id":"65ab4c...",
   "name":"Navaneeth"
}
```

It acts like the Primary Key in MySQL.

Every document has a different `_id`.

---

# MongoDB Server

MongoDB Server is the software that actually stores your database.

Without the server,

there is no database.

Think of it as the engine.

---

# What is MongoDB Compass?

MongoDB Compass is the **official graphical user interface (GUI)** for MongoDB.

Instead of writing commands,

you can perform operations using buttons.

---

## Why Compass?

Because beginners find commands difficult.

Compass lets you

- Create databases
- Create collections
- Insert documents
- Edit documents
- Delete documents
- Search documents
- Filter data

without writing code.

---

# Real-Life Example

Think of Microsoft Word.

You don't type formatting commands.

You simply click

- Bold
- Italic
- Font Size

Compass works similarly.

Instead of typing MongoDB commands,

you click buttons.

---

# MongoDB Compass Interface

When Compass opens, you usually see:

```
Connection Screen

↓

Databases

↓

Collections

↓

Documents
```

---

# Features of MongoDB Compass

### Create Database

You can create a database with one click.

---

### Create Collection

Create folders (collections) inside a database.

---

### Insert Document

Add JSON data directly.

Example

```json
{
   "name":"Navaneeth",
   "age":22
}
```

---

### Edit Document

Click Edit.

Modify values.

Save.

---

### Delete Document

Select a document.

Click Delete.

---

### Search Data

Search documents easily.

Example

```
name = "Navaneeth"
```

---

### Visualize Data

Compass provides charts and statistics for your data.

---

# Advantages of Compass

✅ Beginner Friendly

✅ Easy to use

✅ No need to remember commands

✅ Official MongoDB tool

✅ Visual interface

---

# What is MongoDB Shell?

MongoDB Shell is a **Command-Line Interface (CLI)** used to interact with MongoDB by typing commands.

Its executable is commonly called:

```
mongosh
```

---

# Why use MongoDB Shell?

Developers use the shell because it is:

- Fast
- Powerful
- Lightweight
- Preferred in interviews and by professionals

---

# Example

Instead of clicking buttons,

you type commands.

Example

```javascript
show dbs
```

or

```javascript
use college
```

The shell executes the command immediately.

---

# MongoDB Shell vs Compass

| MongoDB Shell | MongoDB Compass |
|---------------|-----------------|
|Command Line|Graphical Interface|
|Fast|Easy|
|Used by Developers|Used by Beginners|
|Requires Commands|Mouse Clicks|
|Powerful|Simple|

---

# Basic Shell Workflow

```
Open Shell

↓

Connect to MongoDB

↓

Create Database

↓

Create Collection

↓

Insert Documents

↓

Read Data

↓

Update Data

↓

Delete Data
```

---

# Example Session

Create a database

```javascript
use college
```

Create a collection automatically by inserting data

```javascript
db.students.insertOne({
    name:"Navaneeth",
    age:22
})
```

View data

```javascript
db.students.find()
```

---

# MongoDB Ecosystem

```
Developer

↓

MongoDB Shell (Commands)

OR

MongoDB Compass (GUI)

↓

MongoDB Server

↓

Database

↓

Collections

↓

Documents
```

---

# Difference Between MongoDB, Compass and Shell

| MongoDB | Compass | Shell |
|----------|----------|--------|
|Database Software|GUI Tool|Command-Line Tool|
|Stores Data|Visual Management|Command-Based Management|
|Backend Engine|Frontend Interface|CLI Interface|
|Runs Database|Uses MongoDB|Uses MongoDB|

---

# Simple Analogy

Imagine a Car.

Car Engine

↓

MongoDB

Steering Wheel

↓

MongoDB Compass

Gear Lever

↓

MongoDB Shell

The engine performs the work.

The steering wheel helps control the car visually.

The gear lever gives direct control.

---

# Advantages of MongoDB

- Flexible Schema
- Fast Performance
- High Scalability
- Stores Large Data
- Easy to Learn
- JSON-like Documents
- Cloud Support
- Open Source
- Widely Used in MERN Stack

---

# Summary

- **MongoDB** is a NoSQL database that stores data as **documents (BSON)**.
- **Database → Collection → Document** is the basic structure.
- **MongoDB Compass** is the official GUI for managing MongoDB visually.
- **MongoDB Shell (mongosh)** is the command-line tool for interacting with MongoDB using commands.
- **Compass and Shell are tools to work with MongoDB; they are not databases themselves.**

---

# Interview Questions

### 1. What is MongoDB?
MongoDB is a NoSQL database that stores data as BSON documents instead of rows and columns.

### 2. What is BSON?
BSON stands for Binary JSON. It is the internal format MongoDB uses to store JSON-like documents efficiently.

### 3. What is MongoDB Compass?
MongoDB Compass is the official graphical interface (GUI) for MongoDB that lets users manage databases visually.

### 4. What is MongoDB Shell?
MongoDB Shell (`mongosh`) is the command-line interface used to interact with MongoDB by writing commands.

### 5. What is the difference between MongoDB, Compass, and Shell?

- **MongoDB:** The database server that stores data.
- **MongoDB Compass:** A GUI application for managing MongoDB visually.
- **MongoDB Shell:** A command-line tool for managing MongoDB using commands.
