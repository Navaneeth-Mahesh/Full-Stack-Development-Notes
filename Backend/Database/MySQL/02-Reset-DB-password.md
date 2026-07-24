# Resetting the MySQL Root Password

## Introduction

If you forget the **root password** for your MySQL Server, you can reset it without reinstalling MySQL. The process involves temporarily starting MySQL with authentication disabled, logging in without a password, setting a new password, and restarting the server normally.

> **Note:** This guide is intended for **your own MySQL server** where you have administrator access to the operating system.

---

# Prerequisites

Before starting, ensure that:

* You have administrator (Windows) or sudo (Linux/macOS) privileges.
* You can stop and start the MySQL service.
* No important database operations are currently running.

---

# Method 1: Reset Root Password on Windows

## Step 1: Stop the MySQL Service

Open **Command Prompt** as **Administrator**.

Stop the MySQL service:

```cmd
net stop MySQL80
```

If your service has a different name, first list all services:

```cmd
sc query type= service | findstr MySQL
```

Example output:

```text
SERVICE_NAME: MySQL80
```

---

## Step 2: Open Command Prompt in the MySQL Bin Directory

Navigate to your MySQL installation.

Example:

```cmd
cd "C:\Program Files\MySQL\MySQL Server 8.0\bin"
```

Your version number may be different.

---

## Step 3: Start MySQL Without Password Authentication

Run:

```cmd
mysqld --skip-grant-tables --skip-networking
```

Leave this Command Prompt window open.

Do **not** close it.

---

## Step 4: Open a New Command Prompt

Open another Command Prompt as Administrator.

Again navigate to:

```cmd
cd "C:\Program Files\MySQL\MySQL Server 8.0\bin"
```

Login without a password:

```cmd
mysql -u root
```

Since authentication is disabled, MySQL allows access without asking for the password.

---

## Step 5: Select the MySQL System Database

```sql
USE mysql;
```

---

## Step 6: Reset the Root Password

For MySQL 8.x:

```sql
ALTER USER 'root'@'localhost'
IDENTIFIED BY 'NewStrongPassword';
```

Replace:

```text
NewStrongPassword
```

with your own secure password.

Example:

```sql
ALTER USER 'root'@'localhost'
IDENTIFIED BY 'MySecure@123';
```

---

## Step 7: Reload Privileges

```sql
FLUSH PRIVILEGES;
```

---

## Step 8: Exit MySQL

```sql
EXIT;
```

---

## Step 9: Close the MySQL Server

Return to the first Command Prompt running:

```text
mysqld --skip-grant-tables --skip-networking
```

Stop it by pressing:

```text
Ctrl + C
```

---

## Step 10: Start MySQL Normally

Start the service again:

```cmd
net start MySQL80
```

---

## Step 11: Verify the New Password

Login:

```cmd
mysql -u root -p
```

Enter your newly created password.

If login succeeds, the password has been reset successfully.

---

# Method 2: Reset Root Password on Linux (Ubuntu/Debian)

## Step 1: Stop MySQL

```bash
sudo systemctl stop mysql
```

---

## Step 2: Start MySQL Without Authentication

```bash
sudo mysqld_safe --skip-grant-tables --skip-networking &
```

Wait until MySQL starts.

---

## Step 3: Login Without Password

```bash
mysql -u root
```

---

## Step 4: Select the MySQL Database

```sql
USE mysql;
```

---

## Step 5: Reset the Password

```sql
ALTER USER 'root'@'localhost'
IDENTIFIED BY 'NewStrongPassword';
```

---

## Step 6: Reload Privileges

```sql
FLUSH PRIVILEGES;
```

---

## Step 7: Exit

```sql
EXIT;
```

---

## Step 8: Stop the Temporary Server

Find the MySQL process:

```bash
ps aux | grep mysqld
```

Terminate it:

```bash
sudo kill -9 process_id
```

Replace `process_id` with the actual process ID.

---

## Step 9: Start MySQL Normally

```bash
sudo systemctl start mysql
```

---

## Step 10: Verify Login

```bash
mysql -u root -p
```

Enter the new password.

---

# Method 3: Reset Root Password on macOS

## Step 1: Stop MySQL

If installed using Homebrew:

```bash
brew services stop mysql
```

---

## Step 2: Start Without Authentication

```bash
mysqld_safe --skip-grant-tables --skip-networking &
```

---

## Step 3: Login

```bash
mysql -u root
```

---

## Step 4: Change Password

```sql
USE mysql;

ALTER USER 'root'@'localhost'
IDENTIFIED BY 'NewStrongPassword';

FLUSH PRIVILEGES;
```

---

## Step 5: Exit

```sql
EXIT;
```

---

## Step 6: Stop Temporary Server

```bash
pkill mysqld
```

---

## Step 7: Start MySQL Normally

```bash
brew services start mysql
```

---

## Step 8: Verify Login

```bash
mysql -u root -p
```

---

# If ALTER USER Does Not Work

Some older MySQL versions use different authentication methods.

Check existing users:

```sql
SELECT User, Host FROM mysql.user;
```

If necessary, use:

```sql
SET PASSWORD FOR 'root'@'localhost'
= PASSWORD('NewStrongPassword');
```

> This command is only supported on older MySQL versions and is deprecated in MySQL 8.x.

---

# Common Errors

## ERROR 1045 (28000): Access denied

Possible causes:

* Incorrect username
* Wrong password
* MySQL not started with `--skip-grant-tables`
* Authentication plugin mismatch

---

## mysqld is not recognized

The MySQL `bin` directory is not in your PATH.

Navigate to the installation directory:

```cmd
cd "C:\Program Files\MySQL\MySQL Server 8.0\bin"
```

Or add the directory to the system `PATH` environment variable.

---

## Service Will Not Start

Check the MySQL service status.

Windows:

```cmd
services.msc
```

Linux:

```bash
sudo systemctl status mysql
```

Review the MySQL error log for more information.

---

## Unknown MySQL Service Name

List available services.

Windows:

```cmd
sc query type= service | findstr MySQL
```

Use the returned service name in the `net stop` and `net start` commands.

---

# Security Best Practices

* Use a strong password containing uppercase letters, lowercase letters, numbers, and special characters.
* Never leave MySQL running with `--skip-grant-tables` after resetting the password.
* Restart the server normally immediately after the password change.
* Store your password securely using a password manager.
* Avoid using the `root` account for everyday application development. Create separate users with only the permissions they need.

---

# Quick Command Summary

### Windows

```cmd
net stop MySQL80

cd "C:\Program Files\MySQL\MySQL Server 8.0\bin"

mysqld --skip-grant-tables --skip-networking
```

Open another Command Prompt:

```cmd
mysql -u root
```

```sql
USE mysql;

ALTER USER 'root'@'localhost'
IDENTIFIED BY 'NewStrongPassword';

FLUSH PRIVILEGES;

EXIT;
```

Back in the first Command Prompt:

```text
Ctrl + C
```

Start MySQL normally:

```cmd
net start MySQL80
```

Verify:

```cmd
mysql -u root -p
```

---

# Summary

This guide covered:

* Resetting the MySQL root password on Windows
* Resetting the MySQL root password on Linux
* Resetting the MySQL root password on macOS
* Troubleshooting common password reset issues
* Security best practices after resetting the password

Following these steps allows you to safely regain administrative access to your MySQL server without reinstalling MySQL or losing your existing databases.
