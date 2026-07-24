# Creating and Managing Databases in MySQL

## Creating a Database

A database is a collection of related tables used to store and organize data.

### Step 1: Open MySQL Workbench

Launch **MySQL Workbench** and connect to your MySQL Server by selecting your connection and entering the **root password** (or the password for your MySQL user account).

Once connected, open a new SQL query tab.

### Step 2: Create a New Database

Execute the following SQL statement:

```sql
CREATE DATABASE database_name;
```

Replace `database_name` with the name you want to give your database.

### Example

```sql
CREATE DATABASE college;
```

If the command executes successfully, MySQL creates a new database named `college`.

### Verify the Database

To display all available databases on the server, run:

```sql
SHOW DATABASES;
```

You should see your newly created database in the list.

---

# Selecting (Using) a Database

Before creating tables or inserting data, you must tell MySQL which database you want to work with.

Use the following command:

```sql
USE database_name;
```

### Example

```sql
USE college;
```

After executing this command, the `college` database becomes the active database, and all subsequent SQL operations (such as creating tables, inserting records, or querying data) will be performed within it.

### Check the Currently Selected Database

To verify which database is currently in use:

```sql
SELECT DATABASE();
```

---

# Deleting (Dropping) a Database

If a database is no longer needed, you can permanently remove it using the `DROP DATABASE` statement.

```sql
DROP DATABASE database_name;
```

### Example

```sql
DROP DATABASE college;
```

### Important

* This command permanently deletes the database.
* All tables, records, views, stored procedures, and other objects inside the database are also deleted.
* This action **cannot be undone**, so use it carefully.

To avoid errors if the database does not exist, you can use:

```sql
DROP DATABASE IF EXISTS database_name;
```

---

# Setting a Database to Read-Only

Some database systems (such as Microsoft SQL Server) allow an entire database to be placed in **read-only mode**, preventing any modifications while still allowing users to view data.

The syntax is:

```sql
ALTER DATABASE database_name
READ ONLY = 1;
```

### Example

```sql
ALTER DATABASE college
READ ONLY = 1;
```

In read-only mode:

* Users can execute `SELECT` queries.
* `INSERT`, `UPDATE`, and `DELETE` operations are blocked.
* No structural changes can be made to the database.

---

# Making a Database Writable Again

To allow modifications again, disable read-only mode.

```sql
ALTER DATABASE database_name
READ ONLY = 0;
```

### Example

```sql
ALTER DATABASE college
READ ONLY = 0;
```

After executing this command, users can once again:

* Insert new records
* Update existing records
* Delete records
* Modify tables and other database objects

---

# Important Note

The following commands:

```sql
ALTER DATABASE database_name READ ONLY = 1;

ALTER DATABASE database_name READ ONLY = 0;
```

**are not supported in MySQL.** They are used in database systems such as **Microsoft SQL Server**.

In MySQL, if you want to prevent changes to a database, common approaches include:

* Granting users **read-only privileges** using `GRANT`.
* Starting the MySQL server in **read-only mode** (`--read-only`).
* Using **transaction and permission management** to restrict modifications.

---

# Summary

| Command                                  | Description                                          |
| ---------------------------------------- | ---------------------------------------------------- |
| `CREATE DATABASE database_name;`         | Creates a new database.                              |
| `SHOW DATABASES;`                        | Displays all databases on the server.                |
| `USE database_name;`                     | Selects a database for the current session.          |
| `SELECT DATABASE();`                     | Shows the currently selected database.               |
| `DROP DATABASE database_name;`           | Permanently deletes a database and all its contents. |
| `DROP DATABASE IF EXISTS database_name;` | Deletes the database only if it exists.              |
| `ALTER DATABASE ... READ ONLY`           | Not supported in MySQL; available in SQL Server.     |
