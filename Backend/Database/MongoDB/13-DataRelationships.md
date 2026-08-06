# Data Relationships (Embedded Documents & Referenced Documents)

# What Will You Learn?

In this chapter, you'll learn:

- What are Data Relationships?
- Why Relationships are Needed
- Embedded Documents
- Referenced Documents
- One-to-One Relationship
- One-to-Many Relationship
- Many-to-Many Relationship
- Embedded vs Referenced
- Best Practices
- Real-World Examples
- Interview Questions

---

# What are Data Relationships?

## Definition

A **Data Relationship** is a way to connect one document with another document.

In real-world applications, data is often related.

For example:

- A customer places orders.
- A student enrolls in courses.
- A user writes posts.
- A post has comments.

Instead of storing everything in one document, MongoDB provides ways to manage related data efficiently.

---

# Why Do We Need Relationships?

Imagine you're building an **E-Commerce Website**.

One customer can place many orders.

Customer

```json
{
    "name":"Rahul",
    "email":"rahul@gmail.com"
}
```

Orders

```json
{
    "product":"Laptop",
    "price":60000
}

{
    "product":"Mouse",
    "price":1000
}
```

Since both are related,

MongoDB provides two approaches:

- Embedded Documents
- Referenced Documents

---

# Types of Relationships

MongoDB mainly uses two approaches:

| Relationship Type | Description |
|-------------------|-------------|
| Embedded Documents | Store related data inside the same document |
| Referenced Documents | Store related data in separate collections and connect using IDs |

---

# Embedded Documents

## Definition

An **Embedded Document** stores one document **inside another document**.

Everything is kept together.

Think of it as a **document inside a document**.

---

# Example

Customer

```json
{
    "_id":1,
    "name":"Rahul",
    "email":"rahul@gmail.com",

    "address":{
        "city":"Hyderabad",
        "state":"Telangana",
        "pincode":500001
    }
}
```

Notice

The address is stored **inside** the customer document.

---

# Structure

```
Customer

│

├── Name

├── Email

└── Address

      ├── City

      ├── State

      └── Pincode
```

Everything belongs to one document.

---

# Another Example

User

```json
{
    "name":"Ajay",

    "skills":[
        "Java",
        "MongoDB",
        "Node.js"
    ]
}
```

Here,

the `skills` array is embedded inside the user document.

---

# When Should You Use Embedded Documents?

Use Embedded Documents when:

- Data always belongs to one document.
- Data is small.
- Data is rarely shared with other documents.
- You usually read both pieces of data together.

---

# Real-Life Example

A user's address.

Whenever you view a user,

you also need their address.

Keeping both together makes fetching faster.

---

# Advantages of Embedded Documents

✅ Faster reads

Only one document needs to be fetched.

---

✅ Simple structure

Everything is in one place.

---

✅ No joins required

MongoDB reads one document only.

---

# Disadvantages of Embedded Documents

❌ Large documents

If embedded data grows too much,

the document becomes very large.

---

❌ Duplicate data

If the same information is needed in many places,

it gets copied repeatedly.

---

❌ Difficult to update shared data

Updating one embedded copy does not update others.

---

# Referenced Documents

## Definition

A **Referenced Document** stores related data in different collections.

The documents are connected using an ID.

---

# Example

## Users Collection

```json
{
    "_id":101,
    "name":"Rahul"
}
```

---

## Orders Collection

```json
{
    "_id":1,
    "product":"Laptop",
    "userId":101
}

{
    "_id":2,
    "product":"Keyboard",
    "userId":101
}
```

Notice

The order stores only

```
userId
```

instead of the complete user information.

---

# Structure

```
Users Collection

Rahul (101)

↓

Orders Collection

Laptop → userId 101

Keyboard → userId 101
```

The documents are connected using IDs.

---

# Why Use Referenced Documents?

Suppose Rahul changes his email.

If data is duplicated in 500 orders,

you must update all 500 documents.

With references,

you update only one user document.

Every order still points to the updated user.

---

# Advantages of Referenced Documents

✅ No duplicate data

---

✅ Easier updates

---

✅ Better for large applications

---

✅ Saves storage

---

# Disadvantages of Referenced Documents

❌ Multiple queries may be needed.

---

❌ Slightly slower than embedded documents.

---

# Embedded vs Referenced

| Embedded Documents | Referenced Documents |
|--------------------|----------------------|
| Data stored together | Data stored separately |
| Faster reads | Better scalability |
| Easy to read | Easy to maintain |
| Can create large documents | Keeps documents smaller |
| Good for small related data | Good for reusable data |

---

# One-to-One Relationship

## Definition

One document is related to exactly one other document.

Example

One User

↓

One Passport

---

## Example

```json
{
    "name":"Rahul",

    "passport":{
        "passportNo":"P1234567",
        "country":"India"
    }
}
```

Since every passport belongs to only one user,

embedding is a good choice.

---

# One-to-Many Relationship

## Definition

One document is related to many documents.

Example

One User

↓

Many Orders

---

Example

Users

```json
{
    "_id":101,
    "name":"Rahul"
}
```

Orders

```json
{
    "product":"Laptop",
    "userId":101
}

{
    "product":"Phone",
    "userId":101
}

{
    "product":"Keyboard",
    "userId":101
}
```

This is the most common relationship in web applications.

---

# Many-to-Many Relationship

## Definition

Many documents are related to many other documents.

Example

Students and Courses.

One student can join many courses.

One course can have many students.

---

Example

Students

```json
{
    "_id":1,
    "name":"Rahul"
}
```

Courses

```json
{
    "_id":10,
    "course":"MongoDB"
}
```

Enrollment

```json
{
    "studentId":1,
    "courseId":10
}
```

This separate collection connects students and courses.

---

# Which Relationship Should You Choose?

## Use Embedded Documents when

- Data is small.
- Data belongs only to one document.
- You always fetch it together.

Examples

- Address
- Phone Numbers
- Skills
- Preferences

---

## Use Referenced Documents when

- Data is shared.
- Data grows frequently.
- Many documents use the same data.

Examples

- Users and Orders
- Users and Posts
- Products and Categories
- Students and Courses

---

# Real-World Examples

## Instagram

User

↓

Many Posts

Use References.

---

## Amazon

Customer

↓

Many Orders

Use References.

---

## College

Student

↓

Address

Use Embedded.

---

## Hospital

Patient

↓

Medical Records

Usually References because records keep growing.

---

# Best Practices

✅ Embed small and closely related data.

---

✅ Reference large or reusable data.

---

✅ Avoid storing duplicate information.

---

✅ Keep documents reasonably small for better performance.

---

# Common Beginner Mistakes

## ❌ Embedding Everything

Not all related data should be embedded.

Large documents reduce performance.

---

## ❌ Referencing Small Data

Using separate collections for tiny data (like an address) can make queries unnecessarily complex.

---

## ❌ Duplicating User Information

Instead of storing the user's name and email inside every order,

store the `userId` and fetch the user details when needed.

---

# Interview Questions

### What is a Data Relationship?

A Data Relationship connects related documents in MongoDB.

---

### What are the two main relationship approaches?

- Embedded Documents
- Referenced Documents

---

### What is an Embedded Document?

A document stored inside another document.

---

### What is a Referenced Document?

A document stored in another collection and connected using an ID.

---

### When should Embedded Documents be used?

When related data is small, belongs together, and is always accessed together.

---

### When should Referenced Documents be used?

When data is large, reusable, or shared among many documents.

---

### Which relationship is faster for reading?

Embedded Documents.

---

### Which relationship is better for large applications?

Referenced Documents.

---

### Give an example of a One-to-Many relationship.

One Customer → Many Orders.

---

### Give an example of a Many-to-Many relationship.

Many Students ↔ Many Courses.

---

# Quick Revision

| Relationship | Example |
|--------------|---------|
| Embedded | User → Address |
| Referenced | User → Orders |
| One-to-One | User → Passport |
| One-to-Many | Customer → Orders |
| Many-to-Many | Students ↔ Courses |

---

# Summary

- **Data Relationships** connect related information in MongoDB.
- MongoDB supports two main approaches: **Embedded Documents** and **Referenced Documents**.
- **Embedded Documents** store related data inside the same document and provide faster reads.
- **Referenced Documents** store related data in separate collections and connect them using IDs.
- **One-to-One** relationships connect one document to one other document.
- **One-to-Many** relationships connect one document to multiple documents.
- **Many-to-Many** relationships are usually implemented using a separate collection that stores references.
- Choosing between embedding and referencing depends on data size, reuse, update frequency, and application requirements.

---

You now understand how MongoDB models relationships between documents.
