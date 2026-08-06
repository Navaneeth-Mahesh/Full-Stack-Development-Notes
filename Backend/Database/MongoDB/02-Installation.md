# MongoDB Installation & MongoDB Compass
> Complete Beginner Guide (Easy to Understand)

---

# What is MongoDB?

MongoDB is a **NoSQL Database Management System** that stores data in **JSON-like documents (BSON)** instead of rows and columns like MySQL.

Example:

Instead of storing data like this (MySQL):

| ID | Name | Age |
|----|------|-----|
|1|Navaneeth|22|

MongoDB stores it like this:

```json
{
    "_id": "64ab12cd",
    "name": "Navaneeth",
    "age": 22
}
```

Each object is called a **Document**.

A group of documents is called a **Collection**.

A group of collections is called a **Database**.

---

# Why do we install MongoDB?

Imagine you're creating an application.

Example:
- Instagram
- WhatsApp
- Netflix
- Amazon

These applications need somewhere to save data.

Example:

- User details
- Passwords
- Posts
- Comments
- Messages
- Orders

MongoDB acts as the storage place for all this data.

Without MongoDB, your application cannot permanently save information.

---

# Two Things You Need

To work with MongoDB locally, you need **two software programs**.

## 1. MongoDB Community Server

This is the actual database.

Think of it as:

> A warehouse where all your data is stored.

Without this, there is no database.

---

## 2. MongoDB Compass

This is a GUI (Graphical User Interface).

Think of it as:

> A control panel to view and manage your database.

Instead of writing commands every time, you can click buttons.

---

# Difference Between Them

| MongoDB Community Server | MongoDB Compass |
|--------------------------|----------------|
|Stores the data|Displays the data|
|Actual database|GUI Tool|
|Runs in background|Application you open|
|Required|Optional but recommended|

Think like this:

Database = Engine

Compass = Dashboard

---

# Step 1 — Download MongoDB Community Server

Visit:

https://www.mongodb.com/try/download/community

Choose:

- Version → Latest Stable
- Platform → Windows
- Package → MSI

Click

**Download**

---

# Step 2 — Install MongoDB Community Server

Open the downloaded MSI file.

Click

Next

Accept License

Next

Choose

**Complete Installation**

Click Next.

---

# Install MongoDB as a Service

You'll see an option:

✅ Install MongoDB as a Service

Keep this checked.

Why?

Because Windows automatically starts MongoDB whenever your PC starts.

Otherwise you'll have to manually start it every time.

---

# Install MongoDB Compass

During installation you'll see

✅ Install MongoDB Compass

Keep it checked.

Click

Next

Install

Finish

Now both software are installed.

---

# What Happens After Installation?

Your computer now has:

```
MongoDB Database
        ↓
Stores Data
```

and

```
MongoDB Compass
        ↓
Shows Data
```

---

# Step 3 — Open MongoDB Compass

Search

MongoDB Compass

Open it.

You'll see something like

```
Connection String

mongodb://localhost:27017
```

Don't change anything.

Click

Connect

---

# Why localhost?

```
localhost
```

means

**Your own computer**

MongoDB is running inside your computer.

Not on the internet.

---

# What is 27017?

MongoDB listens on

```
Port 27017
```

Think of a port as a door.

```
Computer
   ↓
Door Number 27017
   ↓
MongoDB
```

Whenever an application wants to talk to MongoDB, it uses this port.

---

# First Screen After Connecting

You'll see:

```
Databases
```

Initially you'll see only:

```
admin
config
local
```

These are system databases.

You don't usually touch them.

---

# Create Your First Database

Click

Create Database

You'll see two fields.

Example:

Database Name

```
college
```

Collection Name

```
students
```

Click

Create Database

Done!

---

# What Happened?

MongoDB created

```
Database
      ↓
college
```

Inside it

```
Collection
      ↓
students
```

Currently

```
students
```

contains

```
0 Documents
```

---

# Insert Your First Document

Open

students

Click

Add Data

↓

Insert Document

You'll see

```json
{
  "_id": ObjectId("...")
}
```

Replace it with

```json
{
    "name":"Navaneeth",
    "age":22,
    "city":"Hyderabad"
}
```

Click

Insert

Congratulations!

Your first MongoDB document is saved.

---

# What You See Now

```
college
      ↓
students
      ↓

{
   name:"Navaneeth",
   age:22,
   city:"Hyderabad"
}
```

---

# Understanding the Structure

```
MongoDB Server
       │
       ▼
Database
       │
       ▼
Collection
       │
       ▼
Documents
       │
       ▼
Fields
```

Example

```
MongoDB
   │
college
   │
students
   │
Document
   │
------------------------
name : Navaneeth
age :22
city : Hyderabad
------------------------
```

---

# What is _id?

Every document gets

```
_id
```

automatically.

Example

```json
{
    "_id":"64ab12345...",
    "name":"Navaneeth",
    "age":22
}
```

It is the unique identity of that document.

Like

Student Roll Number

or

Aadhar Number.

No two documents have the same `_id`.

---

# What Can You Do in MongoDB Compass?

You can

✅ Create Database

✅ Delete Database

✅ Create Collection

✅ Delete Collection

✅ Insert Documents

✅ Edit Documents

✅ Delete Documents

✅ Filter Data

✅ Sort Data

✅ Import JSON/CSV

✅ Export Data

✅ Create Indexes

All without writing commands.

---

# Advantages of MongoDB Compass

✔ Beginner Friendly

✔ Easy to visualize data

✔ No need to remember commands

✔ Faster debugging

✔ Easy editing

✔ Import and Export support

✔ Great for learning MongoDB

---

# MongoDB Compass vs Mongo Shell

|MongoDB Compass|Mongo Shell|
|---------------|------------|
|GUI|Command Line|
|Mouse clicks|Commands|
|Easy for beginners|Better for professionals|
|Visual|Text-based|

Most developers learn using Compass first and later move to Mongo Shell.

---

# Common Problems

## Problem 1

Compass says

```
Connection Failed
```

Reason

MongoDB Server isn't running.

Solution

Restart MongoDB Service.

---

## Problem 2

Port already in use

Another application is using port 27017.

Restart the computer or change the MongoDB port.

---

## Problem 3

Cannot connect to localhost

Check whether MongoDB Community Server is installed correctly.

---

# Real-Life Analogy

Imagine a Library.

```
Library
```

↓

Database

```
Bookshelf
```

↓

Collection

```
Book
```

↓

Document

```
Pages
```

↓

Fields

So,

Library → Database

Bookshelf → Collection

Book → Document

Page Details → Fields

---

# Summary

- MongoDB is a NoSQL database that stores data as documents.
- Install **MongoDB Community Server** to store data.
- Install **MongoDB Compass** to manage data visually.
- Connect using `mongodb://localhost:27017`.
- Create databases, collections, and documents through Compass.
- `_id` is automatically generated for every document.
- Compass is ideal for beginners because it provides a graphical interface without needing commands.

---

# Quick Revision

- **MongoDB Community Server** → Actual database engine.
- **MongoDB Compass** → Graphical tool to manage MongoDB.
- **localhost** → Your own computer.
- **27017** → Default MongoDB port.
- **Database** → Contains collections.
- **Collection** → Contains documents.
- **Document** → Stores actual data in JSON-like format.
- **Field** → Individual key-value pair inside a document.