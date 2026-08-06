# Text Search

---

# What Will You Learn?

In this chapter, you'll learn:

- What is Text Search?
- Why Text Search is Needed
- Text Index
- createIndex()
- $text Operator
- $search Operator
- Searching Multiple Words
- Phrase Search
- Text Score
- Real-World Examples
- Common Mistakes
- Interview Questions

---

# What is Text Search?

## Definition

**Text Search** allows MongoDB to search for words and phrases inside string fields.

Instead of matching the **entire text**, MongoDB searches for the required words.

Think of it like the search bar in:

- Google
- YouTube
- Amazon
- Instagram
- Gmail

---

# Why Do We Need Text Search?

Imagine a collection named **articles**.

```json
{
"title":"Learn MongoDB Basics"
}

{
"title":"Node.js Backend Development"
}

{
"title":"MongoDB Aggregation Pipeline"
}

{
"title":"React Complete Guide"
}
```

Suppose the user searches

```
MongoDB
```

Without Text Search,

MongoDB looks for an exact match.

There is no document with exactly

```
MongoDB
```

So no result is returned.

With **Text Search**,

MongoDB finds every document containing the word **MongoDB**.

---

# What is a Text Index?

Before MongoDB can perform a text search,

it must create a **Text Index**.

Think of a Text Index like the index at the back of a book.

Example

```
Aggregation → Page 120

MongoDB → Page 30

Pipeline → Page 150
```

MongoDB creates a similar structure for words.

---

# Creating a Text Index

## Syntax

```javascript
db.collection.createIndex({
field:"text"
})
```

---

# Example

```javascript
db.articles.createIndex({
title:"text"
})
```

MongoDB creates a text index on the `title` field.

Now you can search words inside the title.

---

# Creating Text Index on Multiple Fields

Example

```javascript
db.articles.createIndex({

title:"text",

description:"text"

})
```

Now MongoDB searches both

- title
- description

---

# $text Operator

## Definition

`$text` tells MongoDB to perform a text search.

---

## Syntax

```javascript
db.collection.find({

$text:{

$search:"word"

}

})
```

---

# Example

Collection

```json
{
"title":"Learn MongoDB"
}

{
"title":"MongoDB Aggregation"
}

{
"title":"React Tutorial"
}
```

Query

```javascript
db.articles.find({

$text:{

$search:"MongoDB"

}

})
```

Output

```text
Learn MongoDB

MongoDB Aggregation
```

---

# How $search Works

Suppose the search word is

```
MongoDB
```

MongoDB checks

```
Learn MongoDB ✔

MongoDB Aggregation ✔

React Tutorial ✖
```

Only matching documents are returned.

---

# Searching Multiple Words

Suppose the collection contains

```json
{
"title":"MongoDB Aggregation"
}

{
"title":"Node.js Backend"
}

{
"title":"React MongoDB Project"
}
```

Query

```javascript
db.articles.find({

$text:{

$search:"MongoDB React"

}

})
```

MongoDB searches for

- MongoDB
- React

Documents containing either word are returned.

---

# Phrase Search

Suppose you want to search an exact sentence.

Use **double quotes** inside `$search`.

Example

```javascript
db.articles.find({

$text:{

$search:"\"MongoDB Aggregation\""

}

})
```

Output

```
MongoDB Aggregation
```

MongoDB searches for the exact phrase,

not individual words.

---

# Excluding Words

You can exclude a word using `-`.

Example

```javascript
db.articles.find({

$text:{

$search:"MongoDB -React"

}

})
```

Meaning

Find documents containing

```
MongoDB
```

but **not**

```
React
```

---

# Text Score

When multiple documents match,

MongoDB calculates a **Text Score**.

The more relevant the document,

the higher its score.

---

# Showing Text Score

Example

```javascript
db.articles.find(

{

$text:{

$search:"MongoDB"

}

},

{

score:{

$meta:"textScore"

}

}

)
```

Output

```json
{
"title":"MongoDB Basics",
"score":2.5
}

{
"title":"MongoDB Guide",
"score":1.8
}
```

Higher score means higher relevance.

---

# Sorting by Text Score

Example

```javascript
db.articles.find(

{

$text:{

$search:"MongoDB"

}

},

{

score:{

$meta:"textScore"

}

}

)

.sort({

score:{

$meta:"textScore"

}

})
```

Most relevant documents appear first.

---

# Combining Text Search with Other Queries

Example

Find

- MongoDB articles
- Category = Database

```javascript
db.articles.find({

$text:{

$search:"MongoDB"

},

category:"Database"

})
```

MongoDB returns only database articles related to MongoDB.

---

# Text Search with Projection

Example

```javascript
db.articles.find(

{

$text:{

$search:"MongoDB"

}

},

{

_id:0,

title:1

}

)
```

Output

```json
{
"title":"Learn MongoDB"
}

{
"title":"MongoDB Aggregation"
}
```

---

# Text Search with limit()

Example

```javascript
db.articles.find({

$text:{

$search:"MongoDB"

}

})

.limit(5)
```

Returns only five matching documents.

---

# Real-World Examples

## Google

Search

```
MongoDB Tutorial
```

Google returns pages containing those words.

---

## YouTube

Search

```
Node.js
```

Returns videos containing Node.js.

---

## Amazon

Search

```
Wireless Mouse
```

Returns products matching those words.

---

## Instagram

Search

```
travel
```

Returns users, captions, and hashtags containing "travel".

---

## Gmail

Search

```
meeting
```

Returns emails containing the word "meeting".

---

# Common Beginner Mistakes

## ❌ Forgetting Text Index

Wrong

```javascript
db.articles.find({

$text:{

$search:"MongoDB"

}

})
```

without creating

```javascript
createIndex({

title:"text"

})
```

MongoDB returns an error because a text index is required.

---

## ❌ Confusing $regex with Text Search

`$regex`

- Searches patterns
- Matches characters

`$text`

- Searches words
- Uses a text index
- Better for search functionality

---

## ❌ Forgetting Double Quotes for Phrase Search

Wrong

```javascript
$search:"MongoDB Aggregation"
```

This searches for two separate words.

Correct

```javascript
$search:"\"MongoDB Aggregation\""
```

This searches for the exact phrase.

---

# Difference Between Regex and Text Search

| Regex | Text Search |
|--------|-------------|
| Pattern matching | Word searching |
| Uses `$regex` | Uses `$text` |
| No text index required | Requires text index |
| Good for partial matches | Good for search engines |

---

# Interview Questions

### What is Text Search?

Text Search is a MongoDB feature that searches for words and phrases inside string fields.

---

### Which index is required for Text Search?

A **Text Index**.

---

### Which command creates a Text Index?

```javascript
db.collection.createIndex({
field:"text"
})
```

---

### Which operator performs a Text Search?

```javascript
$text
```

---

### Which operator specifies the search words?

```javascript
$search
```

---

### How do you search an exact phrase?

Use double quotes inside `$search`.

Example

```javascript
$search:"\"MongoDB Aggregation\""
```

---

### What is Text Score?

Text Score is a relevance score assigned to matching documents.

---

### Difference between `$regex` and `$text`?

- `$regex` searches character patterns.
- `$text` searches indexed words and phrases.

---

# Quick Revision

| Feature | Purpose |
|----------|----------|
| Text Index | Enables text searching |
| `$text` | Starts a text search |
| `$search` | Specifies search words |
| `"..."` | Exact phrase search |
| `-word` | Exclude a word |
| `$meta:"textScore"` | Display relevance score |

---

# Summary

- **Text Search** helps search words and phrases inside string fields.
- A **Text Index** must be created before using Text Search.
- **`$text`** performs the text search, and **`$search`** specifies the search terms.
- Multiple words can be searched in a single query.
- Use **double quotes** for exact phrase searches.
- Prefix a word with **`-`** to exclude it from the results.
- **Text Score** ranks documents based on relevance.
- Text Search is commonly used in search bars for websites like Google, YouTube, Amazon, and Gmail.

---

# 🎉 MongoDB Advanced Operations Completed

You have now completed:

## ✅ CRUD Operations
- insertOne()
- insertMany()
- find()
- findOne()
- updateOne()
- updateMany()
- replaceOne()
- deleteOne()
- deleteMany()

## ✅ Querying
- Projection
- sort()
- limit()
- skip()
- $and
- $or
- $not
- $nor
- $regex

## ✅ Advanced Operations
- Aggregation Pipeline
- Indexing
- Text Search

## 🚀 What's Next?

To become **job-ready as a MongoDB fresher**, the next topics you should learn are:

1. **Schema Design**
   - Embedded Documents
   - Referenced Documents
   - One-to-One Relationships
   - One-to-Many Relationships
   - Many-to-Many Relationships

2. **MongoDB with Node.js (Mongoose)**
   - Connecting to MongoDB
   - Defining Schemas
   - Creating Models
   - CRUD using Mongoose
   - Validation
   - Middleware (Hooks)
   - Populate
   - Error Handling

These topics are heavily used in real-world backend development with **Node.js, Express.js, and MongoDB (MERN Stack)**.
