# JavaScript Server-Side

## What is Server-Side JavaScript?

Server-side JavaScript is JavaScript that runs on a **server** instead of a web browser.

The server receives requests from users, processes them, communicates with databases if needed, and sends a response back to the browser.

The most popular runtime for server-side JavaScript is **Node.js**.

---

# How It Works

```text
+-------------------+
|   Web Browser     |
| (HTML, CSS, JS)   |
+-------------------+
          |
          | HTTP Request
          ▼
+-------------------+
|      Server       |
|     (Node.js)     |
+-------------------+
          |
          ▼
+-------------------+
| Handle Request    |
+-------------------+
          |
          ▼
+-------------------+
| Handle Logic      |
| (Business Logic)  |
+-------------------+
          |
          ▼
+-------------------+
| Database          |
| CRUD Operations   |
+-------------------+
          |
          ▼
+-------------------+
| Send Response     |
+-------------------+
          |
          ▼
+-------------------+
|   Web Browser     |
+-------------------+
```

---

# Step-by-Step Explanation

## 1. User Opens a Website

The user visits a website in a browser like:

- Chrome
- Edge
- Firefox

The browser sends an **HTTP Request** to the server.

Example:

```
GET /users
```

---

## 2. Server Receives the Request

The Node.js server receives the request.

Example:

```js
app.get("/users", (req, res) => {
    // request received
});
```

This is called **handling the request**.

---

## 3. Handle Logic

The server decides what to do.

Examples:

- Check if the user exists
- Validate login
- Calculate totals
- Process payments
- Fetch data

Example:

```js
if (userExists) {
    // continue
}
```

This is called **Business Logic**.

---

## 4. Database CRUD Operations

If data is needed, the server talks to the database.

CRUD stands for:

| Operation | Meaning |
|-----------|---------|
| Create | Add new data |
| Read | Get existing data |
| Update | Modify data |
| Delete | Remove data |

Example:

```text
User Registration
↓

Create User

-------------------

Login
↓

Read User

-------------------

Edit Profile
↓

Update User

-------------------

Delete Account
↓

Delete User
```

---

## 5. Send Response

After processing everything, the server sends a response back to the browser.

Example:

```js
res.json({
    message: "Success"
});
```

The browser then displays the result to the user.

---

# Complete Flow

```text
Browser
   │
   │ Request
   ▼
Server (Node.js)
   │
   ▼
Handle Request
   │
   ▼
Business Logic
   │
   ▼
Database (CRUD)
   │
   ▼
Response
   │
   ▼
Browser
```

---

# Real-Life Example

Imagine you're ordering food online.

### Browser

You click **Order Now**.

↓

### Server

The server receives your order.

↓

### Handle Logic

The server checks:

- Is the restaurant open?
- Is the item available?
- Is payment successful?

↓

### Database

The server:

- Reads menu items
- Creates a new order
- Updates stock

↓

### Response

The server sends:

```
Order Placed Successfully!
```

The browser shows the confirmation to you.

---

# Key Points

- HTML, CSS, and JavaScript run in the browser (client-side).
- Node.js allows JavaScript to run on the server.
- The server handles requests from clients.
- Business logic determines what the server should do.
- Databases store and manage data using CRUD operations.
- The server sends a response back to the browser.

---

# Summary

```text
Browser
    │
Request
    │
    ▼
Server (Node.js)
    │
Handle Request
    │
Business Logic
    │
Database (CRUD)
    │
Response
    │
    ▼
Browser
```

This is the basic request-response cycle used in most web applications.