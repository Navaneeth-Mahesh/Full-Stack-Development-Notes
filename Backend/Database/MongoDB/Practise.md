# MongoDB Practice - Level 1 & Level 2
> Author: Navaneeth
> Goal: Master MongoDB Queries through Practice

---

# Setup

```javascript
use("PracticeDB")

db.students.insertMany([
{
    name:"Navaneeth",
    age:19,
    city:"Kakinada",
    course:"CSE",
    marks:88
},
{
    name:"Rahul",
    age:21,
    city:"Hyderabad",
    course:"ECE",
    marks:72
},
{
    name:"Priya",
    age:20,
    city:"Vizag",
    course:"CSE",
    marks:95
},
{
    name:"Kiran",
    age:22,
    city:"Chennai",
    course:"EEE",
    marks:60
},
{
    name:"Anjali",
    age:18,
    city:"Hyderabad",
    course:"CSE",
    marks:81
}
])
```

---

# 🟢 Level 1 (Easy)

---

## Q1. Find all students.

### Solution

```javascript
db.students.find()
```

---

## Q2. Find the student named Rahul.

### Solution

```javascript
db.students.findOne({
    name:"Rahul"
})
```

---

## Q3. Find students whose age is greater than 20.

### Solution

```javascript
db.students.find({
    age:{
        $gt:20
    }
})
```

---

## Q4. Find all CSE students.

### Solution

```javascript
db.students.find({
    course:"CSE"
})
```

---

## Q5. Find students whose marks are above 80.

### Solution

```javascript
db.students.find({
    marks:{
        $gt:80
    }
})
```

---

## Q6. Find students from Hyderabad.

### Solution

```javascript
db.students.find({
    city:"Hyderabad"
})
```

---

## Q7. Find students from Hyderabad who are studying CSE.

### Solution

```javascript
db.students.find({
    city:"Hyderabad",
    course:"CSE"
})
```

---

## Q8. Find students younger than 20.

### Solution

```javascript
db.students.find({
    age:{
        $lt:20
    }
})
```

---

## Q9. Find students whose marks are at least 80.

### Solution

```javascript
db.students.find({
    marks:{
        $gte:80
    }
})
```

---

## Q10. Display only name and marks.

### Solution

```javascript
db.students.find(
{},
{
    _id:0,
    name:1,
    marks:1
})
```

---

# 🟡 Level 2 (Easy+)

---

## Q11. Find students whose age is between 19 and 21 (inclusive).

### Solution

```javascript
db.students.find({
    age:{
        $gte:19,
        $lte:21
    }
})
```

---

## Q12. Find students who are NOT studying CSE.

### Solution

```javascript
db.students.find({
    course:{
        $ne:"CSE"
    }
})
```

---

## Q13. Find students from Hyderabad or Vizag.

### Solution

```javascript
db.students.find({
    city:{
        $in:[
            "Hyderabad",
            "Vizag"
        ]
    }
})
```

---

## Q14. Find students whose marks are not less than 70.

### Solution

```javascript
db.students.find({
    marks:{
        $gte:70
    }
})
```

---

## Q15. Display students sorted by marks (Ascending).

### Solution

```javascript
db.students.find().sort({
    marks:1
})
```

---

## Q16. Display students sorted by marks (Descending).

### Solution

```javascript
db.students.find().sort({
    marks:-1
})
```

---

## Q17. Display the top 3 students by marks.

### Solution

```javascript
db.students.find()
.sort({
    marks:-1
})
.limit(3)
```

---

## Q18. Count all students.

### Solution

```javascript
db.students.countDocuments()
```

---

## Q19. Count all CSE students.

### Solution

```javascript
db.students.countDocuments({
    course:"CSE"
})
```

---

## Q20. Find students who are NOT from Hyderabad and whose marks are greater than 75.

### Solution

```javascript
db.students.find({
    city:{
        $ne:"Hyderabad"
    },
    marks:{
        $gt:75
    }
})
```

---

# 🟠 Level 3 (Intermediate)

---

## Q21. Find students whose course is either CSE or ECE.

### Solution

```javascript
db.students.find({
    $or:[
        {
            course:"CSE"
        },
        {
            course:"ECE"
        }
    ]
})
```

Alternative

```javascript
db.students.find({
    course:{
        $in:["CSE","ECE"]
    }
})
```

---

## Q22. Find students whose age is NOT between 19 and 21.

### Solution

```javascript
db.students.find({
    $or:[
        {
            age:{
                $lt:19
            }
        },
        {
            age:{
                $gt:21
            }
        }
    ]
})
```

---

## Q23. Find students whose marks are between 70 and 90.

### Solution

```javascript
db.students.find({
    marks:{
        $gte:70,
        $lte:90
    }
})
```

---

## Q24. Display only name and course sorted alphabetically by name.

### Solution

```javascript
db.students.find(
{},
{
    _id:0,
    name:1,
    course:1
})
.sort({
    name:1
})
```

---

## Q25. Find the student with the highest marks.

### Solution

```javascript
db.students.find()
.sort({
    marks:-1
})
.limit(1)
```

---

## Q26. Find the student with the lowest marks.

### Solution

```javascript
db.students.find()
.sort({
    marks:1
})
.limit(1)
```

---

## Q27. Find students whose city is neither Hyderabad nor Chennai.

### Solution

```javascript
db.students.find({
    city:{
        $nin:[
            "Hyderabad",
            "Chennai"
        ]
    }
})
```

---

## Q28. Skip the first 2 students and display the next 2.

### Solution

```javascript
db.students.find()
.skip(2)
.limit(2)
```

---

## Q29. Find students whose name starts with "P".

### Solution

```javascript
db.students.find({
    name:{
        $regex:"^P"
    }
})
```

---

## Q30. Find CSE students whose marks are greater than 85 and display only name and marks.

### Solution

```javascript
db.students.find(
{
    course:"CSE",
    marks:{
        $gt:85
    }
},
{
    _id:0,
    name:1,
    marks:1
})
```

---

# 📚 Operators Covered

- `find()`
- `findOne()`
- `$gt`
- `$gte`
- `$lt`
- `$lte`
- `$eq`
- `$ne`
- `$in`
- `$nin`
- `$or`
- Projection
- `sort()`
- `limit()`
- `skip()`
- `countDocuments()`
- `$regex`

---

# Progress

- ✅ CRUD Basics
- ✅ Comparison Operators
- ✅ Logical Operators
- ✅ Projection
- ✅ Sorting
- ✅ Limiting
- ✅ Skipping
- ✅ Counting
- ✅ Regular Expressions

**Completed: 30 MongoDB Practice Questions**