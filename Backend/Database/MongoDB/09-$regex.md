# Regular Expressions ($regex)

---

# What Will You Learn?

In this chapter, you'll learn:

- What is Regular Expression (Regex)?
- Why Regex is used?
- $regex Operator
- Starts With (^)
- Ends With ($)
- Contains Text
- Case-Insensitive Search (i)
- Combining Regex with Other Queries
- Real-World Examples
- Common Mistakes
- Interview Questions

---

# What is a Regular Expression?

A **Regular Expression (Regex)** is a pattern used to search text.

Instead of searching for an exact value,

Regex allows us to search for

- Words
- Letters
- Patterns
- Partial Text

Think of Regex as a **smart search tool**.

---

# Why Do We Need Regex?

Imagine a collection

```json
{
"name":"Rahul"
}

{
"name":"Rakesh"
}

{
"name":"Raj"
}

{
"name":"Ajay"
}
```

Suppose you want

> Show every student whose name starts with "Ra"

Without Regex,

You must write

```javascript
name:"Rahul"

name:"Raj"

name:"Rakesh"
```

Impossible if there are thousands of names.

Regex solves this.

---

# Sample Collection

```json
{
"name":"Rahul",
"city":"Hyderabad"
}

{
"name":"Raj",
"city":"Guntur"
}

{
"name":"Rakesh",
"city":"Hyderabad"
}

{
"name":"Ajay",
"city":"Vijayawada"
}

{
"name":"Anjali",
"city":"Hyderabad"
}
```

---

# $regex Operator

## Definition

`$regex` is used to search text using a pattern.

Syntax

```javascript
db.collection.find({
field:{
$regex:"pattern"
}
})
```

Example

```javascript
db.students.find({
name:{
$regex:"Rah"
}
})
```

Output

```json
Rahul
```

Because Rahul contains "Rah".

---

# How Regex Works

Suppose

```
Pattern = Rah
```

MongoDB checks

```
Rahul ✔

Rakesh ❌

Raj ❌

Ajay ❌
```

Only Rahul matches.

---

# Starts With (^)

## Definition

The symbol

```
^
```

means

> Starts With

Syntax

```javascript
db.students.find({
name:{
$regex:"^Ra"
}
})
```

Meaning

```
Name starts with "Ra"
```

Output

```text
Rahul

Raj

Rakesh
```

Ajay is ignored because it starts with A.

---

# Real-Life Example

Search all products beginning with

```
Sam
```

Example

```javascript
db.products.find({
name:{
$regex:"^Sam"
}
})
```

Output

```
Samsung TV

Samsung Phone

Samsung Watch
```

---

# Ends With ($)

## Definition

The symbol

```
$
```

means

> Ends With

Example

```javascript
db.students.find({
name:{
$regex:"ul$"
}
})
```

Meaning

```
Ends with "ul"
```

Output

```
Rahul
```

---

Another Example

```javascript
$regex:"ya$"
```

Matches

```
Divya

Priya

Surya
```

---

# Contains Text

To search anywhere in the string,

simply use the word.

Example

```javascript
db.students.find({
name:{
$regex:"aj"
}
})
```

Output

```
Ajay

Raj
```

Because

```
Ajay

Raj
```

both contain

```
aj
```

---

# Case-Insensitive Search

By default,

Regex is

```
Case Sensitive
```

Meaning

```
Rahul

≠

rahul
```

---

Suppose collection

```json
Rahul

rahul

RAHUL
```

Searching

```javascript
$regex:"Rahul"
```

returns only

```
Rahul
```

---

# Option "i"

To ignore uppercase and lowercase,

use

```
i
```

Syntax

```javascript
db.students.find({
name:{
$regex:"rahul",
$options:"i"
}
})
```

Output

```
Rahul

rahul

RAHUL
```

---

# Why Use "i"?

Real users may search

```
rahul

RAHUL

RahUl
```

You still want all results.

---

# Starts With + Ignore Case

Example

```javascript
db.students.find({
name:{
$regex:"^ra",
$options:"i"
}
})
```

Output

```
Rahul

Raj

Rakesh

rahul
```

---

# Ends With + Ignore Case

```javascript
db.students.find({
name:{
$regex:"ul$",
$options:"i"
}
})
```

Matches

```
Rahul

RAHUL
```

---

# Combining Regex with Other Conditions

Example

Find

Students

Starting with R

AND

City Hyderabad

```javascript
db.students.find({
name:{
$regex:"^R"
},
city:"Hyderabad"
})
```

Output

```
Rahul

Rakesh
```

---

# Regex with sort()

Example

```javascript
db.students.find({
name:{
$regex:"^R"
}
})
.sort({
name:1
})
```

Output

```
Rahul

Raj

Rakesh
```

Alphabetically sorted.

---

# Regex with limit()

Example

```javascript
db.students.find({
name:{
$regex:"^R"
}
})
.limit(2)
```

Returns only

```
Rahul

Raj
```

---

# Regex with Projection

Example

```javascript
db.students.find(
{
name:{
$regex:"^R"
}
},
{
_id:0,
name:1
}
)
```

Output

```json
{
"name":"Rahul"
}

{
"name":"Raj"
}
```

---

# Real-World Examples

## Instagram

Search usernames

```
nav
```

Find

```
navaneeth

navin

navya
```

---

## Amazon

Search

```
iphone
```

Returns

```
iPhone 14

iPhone 15

iPhone Charger
```

---

## YouTube

Search

```
mongodb
```

Returns every video containing

```
mongodb
```

---

## Gmail

Search

```
meeting
```

Returns every email containing

```
meeting
```

---

# Common Regex Symbols

| Symbol | Meaning |
|----------|----------|
| ^ | Starts With |
| $ | Ends With |
| . | Any single character |
| .* | Any number of characters |
| i | Ignore uppercase/lowercase |

---

# Examples

Starts with A

```javascript
$regex:"^A"
```

---

Ends with n

```javascript
$regex:"n$"
```

---

Contains "nav"

```javascript
$regex:"nav"
```

---

Starts with S

Ignore Case

```javascript
$regex:"^S",
$options:"i"
```

---

# Common Beginner Mistakes

## ❌ Forgetting $regex

Wrong

```javascript
name:"^Ra"
```

Correct

```javascript
name:{
$regex:"^Ra"
}
```

---

## ❌ Forgetting Quotes

Wrong

```javascript
$regex:^Ra
```

Correct

```javascript
$regex:"^Ra"
```

---

## ❌ Forgetting "i"

Searching

```
rahul
```

won't find

```
Rahul
```

unless

```javascript
$options:"i"
```

is used.

---

# Difference Between Normal Search and Regex

Normal Search

```javascript
db.students.find({
name:"Rahul"
})
```

Returns only

```
Rahul
```

---

Regex Search

```javascript
db.students.find({
name:{
$regex:"Rah"
}
})
```

Returns every name containing

```
Rah
```

---

# Interview Questions

### What is Regex?

Regex is a pattern used to search text inside documents.

---

### Which MongoDB operator is used for Regex?

```
$regex
```

---

### Which symbol means "Starts With"?

```
^
```

---

### Which symbol means "Ends With"?

```
$
```

---

### What does `$options:"i"` mean?

It makes the search **case-insensitive**, so uppercase and lowercase letters are treated as the same.

---

### Difference between Normal Search and Regex?

- Normal search requires an exact match.
- Regex can search partial text and patterns.

---

# Quick Revision

| Pattern | Meaning |
|----------|----------|
| ^A | Starts with A |
| n$ | Ends with n |
| nav | Contains "nav" |
| $options:"i" | Ignore case |
| $regex | Pattern search |

---

# Summary

- **Regular Expressions (Regex)** allow pattern-based text searching.
- **`$regex`** is the MongoDB operator used for Regex searches.
- **`^`** matches the beginning of a string.
- **`$`** matches the end of a string.
- Writing plain text inside `$regex` searches for that text anywhere in the field.
- **`$options:"i"`** performs a case-insensitive search.
- Regex can be combined with **Projection**, **sort()**, **limit()**, **skip()**, and logical operators.
- Regex is commonly used in search bars, e-commerce websites, social media platforms, and email applications.

---

# MongoDB Querying Module Completed ✅

You have now completed:

- ✅ Projection
- ✅ sort()
- ✅ limit()
- ✅ skip()
- ✅ $and
- ✅ $or
- ✅ $not
- ✅ $nor
- ✅ $regex

