# Aggregation Pipeline

# What Will You Learn?

In this chapter, you'll learn:

- What is Aggregation?
- Why Aggregation is needed
- Aggregation vs find()
- What is a Pipeline?
- Aggregation Syntax
- Pipeline Stages
- `$match`
- `$project`
- `$sort`
- `$limit`
- `$skip`
- `$group`
- `$sum`
- `$avg`
- `$min`
- `$max`
- `$count`
- Real-world Examples
- Interview Questions

---

# What is Aggregation?

## Definition

Aggregation is a process of **collecting, processing, and summarizing data**.

Instead of simply displaying documents, aggregation can:

- Filter data
- Group data
- Calculate totals
- Calculate averages
- Find minimum values
- Find maximum values
- Count records
- Transform data

Think of Aggregation as **MongoDB's data analysis tool**.

---

# Real-Life Example

Imagine a school has 10,000 students.

The principal asks:

- Total number of students?
- Average marks?
- Highest marks?
- Lowest marks?
- Total students in each course?

Using `find()` is difficult because it only retrieves documents.

Aggregation can answer all these questions easily.

---

# Aggregation vs find()

## find()

`find()` is used to retrieve documents.

Example

```javascript
db.students.find({
course:"MCA"
})
```

Output

```
Rahul

Kiran

Suresh
```

It only displays documents.

---

## Aggregation

Aggregation can calculate information.

Example

```
Average Marks

Highest Marks

Total Students

Total Salary
```

---

# Difference

| find() | aggregate() |
|---------|-------------|
| Returns documents | Processes documents |
| No calculations | Performs calculations |
| Simple queries | Advanced data analysis |
| Faster for retrieval | Powerful for reports |

---

# What is a Pipeline?

Imagine a water pipeline.

```
Water

↓

Filter

↓

Clean

↓

Store
```

Aggregation works exactly like this.

Documents move through multiple stages.

Each stage performs one task.

```
Documents

↓

Match

↓

Sort

↓

Group

↓

Output
```

This is called an **Aggregation Pipeline**.

---

# Syntax

```javascript
db.collection.aggregate([
    { Stage1 },
    { Stage2 },
    { Stage3 }
])
```

Notice

Aggregation uses

```
[]
```

because multiple stages are executed one after another.

---

# Sample Collection

```json
{
"name":"Rahul",
"course":"MCA",
"marks":80
}

{
"name":"Ajay",
"course":"BCA",
"marks":90
}

{
"name":"Kiran",
"course":"MCA",
"marks":70
}

{
"name":"Anjali",
"course":"B.Tech",
"marks":95
}
```

---

# Pipeline Stage 1 — $match

## Definition

`$match` filters documents.

It works like `find()`.

---

## Syntax

```javascript
db.students.aggregate([
{
$match:{
course:"MCA"
}
}
])
```

Output

```
Rahul

Kiran
```

Only MCA students are returned.

---

## Real-Life Example

Show only active users.

```javascript
$match:{
status:"Active"
}
```

---

# Pipeline Stage 2 — $project

## Definition

`$project` selects which fields should appear.

Similar to Projection in `find()`.

---

Example

```javascript
db.students.aggregate([
{
$project:{
_id:0,
name:1,
marks:1
}
}
])
```

Output

```json
{
"name":"Rahul",
"marks":80
}

{
"name":"Ajay",
"marks":90
}
```

---

# Pipeline Stage 3 — $sort

Sorts documents.

Ascending

```javascript
{
$sort:{
marks:1
}
}
```

Descending

```javascript
{
$sort:{
marks:-1
}
}
```

Example

```javascript
db.students.aggregate([
{
$sort:{
marks:-1
}
}
])
```

Output

```
95

90

80

70
```

---

# Pipeline Stage 4 — $limit

Returns only the required number of documents.

Example

```javascript
db.students.aggregate([
{
$limit:2
}
])
```

Output

Only first two documents.

---

# Pipeline Stage 5 — $skip

Skips documents.

Example

```javascript
db.students.aggregate([
{
$skip:2
}
])
```

Output

Starts from third document.

---

# Combining Stages

Example

Show

- MCA students
- Highest marks first
- Only top two

```javascript
db.students.aggregate([
{
$match:{
course:"MCA"
}
},
{
$sort:{
marks:-1
}
},
{
$limit:2
}
])
```

Pipeline Flow

```
Students

↓

MCA only

↓

Sort

↓

Top 2

↓

Result
```

---

# $group

## Definition

`$group` groups multiple documents together.

Think like

```
Group students

by

Course
```

---

## Syntax

```javascript
{
$group:{
_id:"$field"
}
}
```

Notice

```
$course
```

means

Use the value inside the **course field**.

---

# Example

```javascript
db.students.aggregate([
{
$group:{
_id:"$course"
}
}
])
```

Output

```
MCA

BCA

B.Tech
```

---

# $sum

## Definition

Adds values together.

---

## Example 1

Count students in each course.

```javascript
db.students.aggregate([
{
$group:{
_id:"$course",
totalStudents:{
$sum:1
}
}
}
])
```

Output

```
MCA

2

BCA

1

B.Tech

1
```

---

## Example 2

Calculate total marks.

```javascript
db.students.aggregate([
{
$group:{
_id:null,
totalMarks:{
$sum:"$marks"
}
}
}
])
```

Output

```
335
```

---

# $avg

Calculates average.

Example

```javascript
db.students.aggregate([
{
$group:{
_id:null,
averageMarks:{
$avg:"$marks"
}
}
}
])
```

Output

```
83.75
```

---

# $min

Returns smallest value.

Example

```javascript
db.students.aggregate([
{
$group:{
_id:null,
minimumMarks:{
$min:"$marks"
}
}
}
])
```

Output

```
70
```

---

# $max

Returns largest value.

```javascript
db.students.aggregate([
{
$group:{
_id:null,
highestMarks:{
$max:"$marks"
}
}
}
])
```

Output

```
95
```

---

# $count

Counts documents.

Example

```javascript
db.students.aggregate([
{
$count:"totalStudents"
}
])
```

Output

```json
{
"totalStudents":4
}
```

---

# Complete Example

Find

- MCA Students
- Marks greater than 70
- Show only Name and Marks
- Highest Marks First

```javascript
db.students.aggregate([

{
$match:{
course:"MCA",
marks:{
$gt:70
}
}
},

{
$project:{
_id:0,
name:1,
marks:1
}
},

{
$sort:{
marks:-1
}
}

])
```

Pipeline

```
Students

↓

MCA

↓

Marks >70

↓

Projection

↓

Sort

↓

Result
```

---

# Real-World Examples

## Amazon

Top-selling products

```
$sort

↓

$limit
```

---

## Instagram

Newest posts

```
$sort

↓

$limit
```

---

## Banking

Average account balance

```
$group

↓

$avg
```

---

## School

Students in each course

```
$group

↓

$sum
```

---

## Hospital

Average patient age

```
$group

↓

$avg
```

---

# Common Beginner Mistakes

## ❌ Forgetting []

Wrong

```javascript
aggregate({

})
```

Correct

```javascript
aggregate([

])

```

Aggregation always uses an array.

---

## ❌ Forgetting $

Wrong

```javascript
group
```

Correct

```javascript
$group
```

---

## ❌ Forgetting field reference

Wrong

```javascript
course
```

Correct

```javascript
"$course"
```

Inside `$group`, field names must begin with `$`.

---

# Interview Questions

### What is Aggregation?

Aggregation is a framework that processes documents through multiple stages to calculate, summarize, and transform data.

---

### What is an Aggregation Pipeline?

An Aggregation Pipeline is a sequence of stages where the output of one stage becomes the input of the next stage.

---

### Difference between `find()` and `aggregate()`?

- `find()` retrieves documents.
- `aggregate()` analyzes and processes documents.

---

### Which stage filters documents?

```
$match
```

---

### Which stage selects fields?

```
$project
```

---

### Which stage groups documents?

```
$group
```

---

### Which operator calculates total?

```
$sum
```

---

### Which operator calculates average?

```
$avg
```

---

### Which operator finds the highest value?

```
$max
```

---

### Which operator finds the lowest value?

```
$min
```

---

### Which stage counts documents?

```
$count
```

---

# Quick Revision

| Stage | Purpose |
|---------|----------|
| `$match` | Filter documents |
| `$project` | Select fields |
| `$sort` | Arrange documents |
| `$limit` | Return limited documents |
| `$skip` | Skip documents |
| `$group` | Group documents |
| `$sum` | Calculate total |
| `$avg` | Calculate average |
| `$min` | Smallest value |
| `$max` | Largest value |
| `$count` | Count documents |

---

# Summary

- **Aggregation** is used to process and analyze data instead of simply retrieving it.
- An **Aggregation Pipeline** passes documents through multiple stages.
- **`$match`** filters documents.
- **`$project`** selects the required fields.
- **`$sort`**, **`$limit`**, and **`$skip`** organize the results.
- **`$group`** combines related documents for calculations.
- **`$sum`**, **`$avg`**, **`$min`**, **`$max`**, and **`$count`** perform statistical operations.
- Aggregation is widely used for dashboards, reports, analytics, sales summaries, and business intelligence.

---

# ✅ Part 5A Completed

You now know the **core Aggregation Pipeline** used in almost every MongoDB backend project.

**Next:** **Part 5B – Indexing**, where you'll learn how MongoDB searches millions of documents in milliseconds and why indexes are one of the most important interview topics.
