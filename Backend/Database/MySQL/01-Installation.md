# MySQL Installation Guide

**Version:** 1.0
**Last Updated:** July 2026

---

# Table of Contents

1. Introduction
2. System Requirements
3. Installation Methods
4. Windows Installation
5. macOS Installation
6. Linux Installation

   * Ubuntu/Debian
   * Fedora
   * CentOS/RHEL
   * Arch Linux
7. Docker Installation
8. Verify Installation
9. Start, Stop and Restart MySQL
10. Login to MySQL
11. Secure MySQL Installation
12. Create Your First Database
13. Common MySQL Commands
14. Environment Variables
15. Troubleshooting
16. Uninstall MySQL
17. Useful Resources

---

# Introduction

MySQL is one of the most popular open-source Relational Database Management Systems (RDBMS). It stores data in tables and uses SQL (Structured Query Language) to manage databases.

It is widely used in:

* Web Development
* Enterprise Applications
* Backend APIs
* Data Analytics
* E-commerce Systems
* CMS Platforms
* Cloud Applications

---

# System Requirements

## Minimum

| Component        | Requirement           |
| ---------------- | --------------------- |
| RAM              | 2 GB                  |
| Storage          | 1 GB Free Space       |
| CPU              | Dual Core             |
| Operating System | Windows, macOS, Linux |

## Recommended

| Component | Recommendation |
| --------- | -------------- |
| RAM       | 8 GB or More   |
| SSD       | Recommended    |
| CPU       | Quad Core      |

---

# Installation Methods

MySQL can be installed using:

* Official Installer
* Package Manager
* Homebrew (macOS)
* Docker
* ZIP Archive
* Linux Package Repository

---

# Windows Installation

## Step 1: Download MySQL Installer

Visit the official MySQL downloads page.

Download:

```
MySQL Installer for Windows
```

Choose either:

* Web Installer (small download)
* Full Installer (offline)

---

## Step 2: Launch Installer

Run:

```
mysql-installer-community.exe
```

Choose:

```
Yes
```

if Windows asks for Administrator permission.

---

## Step 3: Choose Setup Type

Available options:

### Developer Default

Installs:

* MySQL Server
* MySQL Workbench
* Shell
* Connectors
* Documentation
* Sample Data

Recommended for developers.

---

### Server Only

Installs only:

* MySQL Server

Suitable for production servers.

---

### Client Only

Installs:

* Workbench
* Shell
* Connectors

No database server.

---

### Full

Installs everything.

---

### Custom

Allows selecting individual components.

---

## Step 4: Install Required Dependencies

Installer may ask to install:

* Microsoft Visual C++ Redistributable

Install it before continuing.

---

## Step 5: Install Components

Click:

```
Execute
```

Wait until all products show:

```
Complete
```

---

## Step 6: Configure MySQL Server

Click:

```
Next
```

to begin configuration.

---

## Step 7: Configuration Type

Choose:

```
Development Computer
```

for learning and development.

Other options:

* Server Computer
* Dedicated Computer

---

## Step 8: Connectivity

Default settings:

```
Port:
3306
```

Protocol:

```
TCP/IP
```

Keep default unless another service already uses the port.

---

## Step 9: Authentication Method

Choose:

```
Use Strong Password Encryption
```

Recommended.

---

## Step 10: Set Root Password

Example:

```
Username:
root

Password:
********
```

Remember this password.

---

## Step 11: Windows Service

Recommended settings:

```
Service Name:
MySQL80

Start Automatically:
Enabled
```

---

## Step 12: Apply Configuration

Click:

```
Execute
```

Configuration tasks include:

* Creating configuration file
* Starting MySQL Service
* Creating system tables
* Applying security settings

---

## Step 13: Finish Installation

Click:

```
Finish
```

MySQL is now installed.

---

# Verify Windows Installation

Open Command Prompt:

```cmd
mysql --version
```

Example:

```text
mysql  Ver 8.4.x for Win64
```

---

# macOS Installation

There are two common methods.

---

# Method 1 — Homebrew

Install Homebrew if not already installed.

Update Homebrew:

```bash
brew update
```

Install MySQL:

```bash
brew install mysql
```

Start MySQL:

```bash
brew services start mysql
```

Verify:

```bash
mysql --version
```

---

# Method 2 — Official DMG Installer

Download the MySQL DMG package.

Open:

```
MySQL.pkg
```

Follow the installation wizard.

During installation:

* Accept License
* Install Components
* Set Root Password
* Complete Installation

After installation:

Open:

```
System Settings
```

↓

```
MySQL
```

Start the MySQL Server.

---

# Linux Installation

---

# Ubuntu / Debian

Update packages:

```bash
sudo apt update
```

Install MySQL:

```bash
sudo apt install mysql-server
```

Verify installation:

```bash
mysql --version
```

Start service:

```bash
sudo systemctl start mysql
```

Enable at boot:

```bash
sudo systemctl enable mysql
```

Check status:

```bash
sudo systemctl status mysql
```

---

# Fedora

Install:

```bash
sudo dnf install community-mysql-server
```

Start:

```bash
sudo systemctl start mysqld
```

Enable:

```bash
sudo systemctl enable mysqld
```

---

# CentOS / RHEL

Install repository:

```bash
sudo dnf install mysql-server
```

Start:

```bash
sudo systemctl start mysqld
```

Enable:

```bash
sudo systemctl enable mysqld
```

---

# Arch Linux

Install:

```bash
sudo pacman -S mysql
```

Initialize:

```bash
sudo mysql_install_db --user=mysql --basedir=/usr --datadir=/var/lib/mysql
```

Start:

```bash
sudo systemctl start mysqld
```

Enable:

```bash
sudo systemctl enable mysqld
```

---

# Docker Installation

Pull MySQL image:

```bash
docker pull mysql:latest
```

Run container:

```bash
docker run \
--name mysql-server \
-e MYSQL_ROOT_PASSWORD=password \
-p 3306:3306 \
-d mysql
```

Check running containers:

```bash
docker ps
```

Connect:

```bash
docker exec -it mysql-server mysql -u root -p
```

---

# Verify Installation

Check version:

```bash
mysql --version
```

Login:

```bash
mysql -u root -p
```

Successful login shows:

```text
mysql>
```

---

# Start, Stop and Restart MySQL

## Windows

Start:

```cmd
net start MySQL80
```

Stop:

```cmd
net stop MySQL80
```

Restart:

```cmd
net stop MySQL80
net start MySQL80
```

---

## macOS

Start:

```bash
brew services start mysql
```

Stop:

```bash
brew services stop mysql
```

Restart:

```bash
brew services restart mysql
```

---

## Linux

Start:

```bash
sudo systemctl start mysql
```

Stop:

```bash
sudo systemctl stop mysql
```

Restart:

```bash
sudo systemctl restart mysql
```

Status:

```bash
sudo systemctl status mysql
```

---

# Login to MySQL

```bash
mysql -u root -p
```

Enter password:

```text
********
```

Exit:

```sql
exit;
```

or

```sql
quit;
```

---

# Secure MySQL Installation

Run:

```bash
mysql_secure_installation
```

This helps:

* Remove anonymous users
* Disable remote root login
* Remove test database
* Reload privilege tables
* Improve security

---

# Create Your First Database

Create database:

```sql
CREATE DATABASE college;
```

Show databases:

```sql
SHOW DATABASES;
```

Use database:

```sql
USE college;
```

Create table:

```sql
CREATE TABLE students(
    id INT PRIMARY KEY,
    name VARCHAR(100)
);
```

Insert:

```sql
INSERT INTO students
VALUES
(1,'John');
```

Retrieve:

```sql
SELECT * FROM students;
```

---

# Common MySQL Commands

Show databases:

```sql
SHOW DATABASES;
```

Use database:

```sql
USE database_name;
```

Show tables:

```sql
SHOW TABLES;
```

Describe table:

```sql
DESCRIBE table_name;
```

Current database:

```sql
SELECT DATABASE();
```

Current user:

```sql
SELECT USER();
```

Version:

```sql
SELECT VERSION();
```

---

# Environment Variables

Sometimes the MySQL executable is not added to the system PATH.

Typical installation directories:

## Windows

```
C:\Program Files\MySQL\MySQL Server 8.x\bin
```

Add this directory to the **Path** environment variable.

Verify:

```cmd
mysql --version
```

## macOS

Typical Homebrew path:

```
/opt/homebrew/bin
```

or

```
/usr/local/bin
```

## Linux

Usually available in:

```
/usr/bin
```

or

```
/usr/local/mysql/bin
```

---

# Troubleshooting

## mysql command not found

Cause:

* PATH variable missing
* MySQL not installed correctly

Solution:

* Verify installation
* Add MySQL `bin` directory to PATH
* Restart terminal

---

## Port 3306 Already in Use

Check which process uses the port.

Windows:

```cmd
netstat -ano | findstr 3306
```

Linux/macOS:

```bash
sudo lsof -i :3306
```

Stop the conflicting service or configure MySQL to use a different port.

---

## Access Denied for User root

Possible causes:

* Incorrect password
* Authentication plugin mismatch

Solutions:

* Verify credentials
* Reset the root password if necessary
* Check authentication method

---

## MySQL Service Won't Start

Check service status.

Windows:

```cmd
services.msc
```

Linux:

```bash
sudo systemctl status mysql
```

Inspect MySQL error logs for detailed diagnostics.

---

## Workbench Cannot Connect

Verify:

* MySQL service is running
* Correct hostname (`localhost`)
* Correct port (`3306`)
* Username and password are correct
* Firewall is not blocking the connection

---

# Uninstall MySQL

## Windows

1. Open **Control Panel**
2. Open **Programs and Features**
3. Select **MySQL**
4. Click **Uninstall**
5. Remove remaining data directory if no longer needed

---

## macOS

Homebrew:

```bash
brew uninstall mysql
```

Official installer:

Remove MySQL using the provided uninstall instructions or package receipts, then delete remaining data directories if desired.

---

## Ubuntu

```bash
sudo apt remove mysql-server
```

Remove configuration:

```bash
sudo apt purge mysql-server
```

Remove unused packages:

```bash
sudo apt autoremove
```

---

# Useful Resources

* Official MySQL Documentation
* MySQL Downloads
* MySQL Workbench Documentation
* MySQL Reference Manual

---

# Summary

This guide covered:

* Installing MySQL on Windows, macOS, Linux, and Docker
* Configuring the MySQL server
* Starting and managing the service
* Logging in to MySQL
* Securing the installation
* Creating your first database and table
* Basic SQL commands
* Environment variable configuration
* Common troubleshooting steps
* Uninstallation procedures

You are now ready to begin working with MySQL databases for application development and database management.
