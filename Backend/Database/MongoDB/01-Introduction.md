# MongoDB Introduction 

> **Level:** Beginner to Intermediate  
> **Goal:** Understand MongoDB from scratch before learning CRUD operations.

---

# Table of Contents

1. What is MongoDB?
2. Why was MongoDB created?
3. What is NoSQL?
4. SQL vs MongoDB
5. Features of MongoDB
6. Advantages
7. Disadvantages
8. Real-world Applications
9. Installation
10. MongoDB Compass
11. MongoDB Shell
12. Database
13. Collection
14. Document
15. BSON
16. Data Types
17. Hierarchy of MongoDB
18. Summary

---

# 1. What is MongoDB?

MongoDB is an **open-source NoSQL database** that stores data in the form of **documents** instead of tables.

Unlike MySQL, where data is stored inside rows and columns, MongoDB stores data as **JSON-like objects**.

MongoDB was developed by **MongoDB Inc.**

It is written in **C++**.

It is designed for applications that require:

- High speed
- Large amounts of data
- Flexible structure
- Easy scalability

---

## Definition

> MongoDB is a document-oriented NoSQL database that stores data as BSON documents instead of rows and columns.

---

## Example

### MySQL

Students Table

| ID | Name | Age |
|----|------|-----|
|1|Rahul|22|

---

### MongoDB

```json
{
   "id":1,
   "name":"Rahul",
   "age":22
}
```

This single object is called a **Document**.

Many documents together form a **Collection**.

---

# 2. Why was MongoDB Created?

Traditional SQL databases have some limitations.

Suppose you have a social media application.

A user can have

- Name
- Phone
- Email
- Bio
- Friends
- Posts
- Images
- Videos
- Likes
- Comments

Every user may have different information.

Some users may have

- Twitter link

Others may have

- Instagram
- YouTube
- Website

Adding new columns every time becomes difficult.

MongoDB solves this problem because every document can have different fields.

Example

Rahul

```json
{
"name":"Rahul",
"age":21
}
```

Priya

```json
{
"name":"Priya",
"age":22,
"instagram":"@priya"
}
```

Notice that both documents have different fields.

MongoDB allows this flexibility.

---

# 3. What is NoSQL?

NoSQL means

> **Not Only SQL**

It does **NOT** mean SQL is bad.

It simply means another way of storing data.

There are four types of NoSQL databases.

### 1. Document Database

Stores data as documents.

Example

- MongoDB

---

### 2. Key-Value Database

Stores data as key-value pairs.

Example

```
username → navaneeth
```

Examples

- Redis

---

### 3. Column Database

Stores data column-wise.

Examples

- Cassandra

---

### 4. Graph Database

Stores relationships.

Example

Facebook Friends

Examples

- Neo4j

---

MongoDB belongs to the

> Document Database category.

---

# 4. SQL vs MongoDB

| SQL | MongoDB |
|------|----------|
|Database|Database|
|Table|Collection|
|Row|Document|
|Column|Field|
|Primary Key|_id|
|Schema Fixed|Schema Flexible|
|Uses SQL|Uses JSON Queries|

---

Example

## MySQL

Student Table

|ID|Name|Age|
|--|----|---|
|1|Rahul|20|

---

## MongoDB

```json
{
"_id":1,
"name":"Rahul",
"age":20
}
```

---

# 5. Features of MongoDB

## 1. Document-Oriented

Stores data as documents.

Example

```json
{
"name":"John",
"age":25
}
```

---

## 2. Flexible Schema

Different documents can contain different fields.

Example

```json
{
"name":"Ram"
}
```

Another document

```json
{
"name":"Sam",
"phone":"9999999999"
}
```

Both are valid.

---

## 3. High Performance

MongoDB reads and writes data very quickly.

Used in applications requiring millions of users.

---

## 4. Scalability

Can distribute data across multiple servers.

Called

> Horizontal Scaling

---

## 5. Replication

Copies data into multiple servers.

If one server crashes

Another server continues working.

This provides

- High Availability
- Backup

---

## 6. Indexing

Indexes make searching much faster.

Without index

Searching

```
1
2
3
4
5
6
...
1000000
```

With index

MongoDB directly jumps to required data.

---

## 7. Aggregation

Aggregation performs calculations on data.

Example

- Total Sales
- Average Salary
- Maximum Price

---

# 6. Advantages of MongoDB

### Easy to Learn

JSON format is easy to understand.

---

### Flexible

No fixed schema.

---

### Fast

Excellent read/write performance.

---

### Scalable

Can handle huge applications.

---

### Cloud Friendly

Works well with cloud services.

---

### Supports Big Data

Used by companies handling millions of records.

---

# 7. Disadvantages

Not suitable for

- Very complex joins

Consumes more storage because field names are stored repeatedly.

Transactions were limited in older versions (modern MongoDB supports multi-document transactions).

---

# 8. Real-World Applications

MongoDB is used in

### Social Media

Users

Posts

Comments

Likes

---

### E-Commerce

Products

Orders

Customers

---

### Banking

Customer Profiles

Transactions

Notifications

---

### Chat Applications

Messages

Groups

Media

---

### IoT

Sensor Data

Temperature

Location

---

### Gaming

Player Profiles

Scores

Achievements

---

# 9. Installation

Download MongoDB Community Server.

Install normally.

After installation

You get

- MongoDB Server
- MongoDB Compass
- MongoDB Shell

---

# 10. MongoDB Compass

Compass is MongoDB's Graphical User Interface (GUI).

Instead of writing commands,

You can

- Create database
- Insert documents
- Delete data
- Update data
- Search data

using buttons.

Think of Compass as

> phpMyAdmin for MySQL.

---

# 11. MongoDB Shell

MongoDB Shell (mongosh) is the command-line interface.

Example

```javascript
show dbs
```

Displays all databases.

Example

```javascript
use college
```

Switches to the `college` database (creates it on first write if it doesn't already exist).

---

# 12. Database

A Database is a container that stores collections.

Example

```
College
```

contains

Students

Teachers

Courses

Departments

---

Example

```
College Database

Students Collection

Teachers Collection

Subjects Collection
```

---

# 13. Collection

A Collection is a group of related documents.

Similar to a table in SQL.

Example

Students Collection

Contains

```json
{
"name":"Rahul"
}
```

```json
{
"name":"Anjali"
}
```

```json
{
"name":"Navaneeth"
}
```

---

# 14. Document

A Document is a single record.

Equivalent to one row in MySQL.

Example

```json
{
"name":"Navaneeth",
"age":22,
"city":"Hyderabad"
}
```

Every document contains fields.

```
name

age

city
```

---

# 15. BSON

MongoDB actually stores data in

> BSON

BSON means

**Binary JSON**

Although we write JSON,

MongoDB converts it into BSON internally.

Why?

Because BSON

- Faster
- More efficient
- Supports extra data types
- Easier for computers to process

---

Example JSON

```json
{
"name":"John",
"age":25
}
```

Internally MongoDB stores it as BSON.

---

# 16. Common Data Types

|Data Type|Example|
|----------|--------|
|String|"Navaneeth"|
|Number|25|
|Boolean|true|
|Array|["Java","MongoDB"]|
|Object|{"city":"Hyderabad"}|
|Date|ISODate()|
|Null|null|
|ObjectId|ObjectId("...")|

---

Example

```json
{
"name":"Navaneeth",
"age":22,
"isStudent":true,
"skills":["Java","MongoDB"],
"address":{
"city":"Hyderabad"
}
}
```

---

# 17. MongoDB Hierarchy

```
MongoDB Server

│

├── Database

│

├── Collection

│

├── Document

│

└── Fields
```

Example

```
MongoDB

│

College Database

│

Students Collection

│

Student Document

│

name

age

city
```

Remember this hierarchy because it is one of the most important concepts in MongoDB.

---

# Quick Revision

- MongoDB is a NoSQL document database.
- It stores data in BSON documents.
- A Database contains Collections.
- A Collection contains Documents.
- A Document contains Fields.
- MongoDB uses JSON-like syntax.
- It has a flexible schema.
- MongoDB is fast, scalable, and cloud-friendly.
- Compass is the GUI.
- mongosh is the command-line shell.
- `_id` uniquely identifies each document.

---

# Interview Questions

### 1. What is MongoDB?

A NoSQL document database that stores data as BSON documents instead of tables.

---

### 2. What is NoSQL?

A database model that stores data in non-relational formats such as documents, key-value pairs, columns, or graphs.

---

### 3. Difference between Table and Collection?

- Table → SQL
- Collection → MongoDB

---

### 4. Difference between Row and Document?

- Row → SQL
- Document → MongoDB

---

### 5. What is BSON?

Binary JSON used internally by MongoDB for storing documents efficiently.

---

### 6. What is Compass?

MongoDB's graphical interface used to manage databases without writing commands.

---

### 7. What is a Collection?

A group of related documents, similar to a table in SQL.

---

### 8. What is a Document?

A single record stored in JSON-like format inside a collection.
