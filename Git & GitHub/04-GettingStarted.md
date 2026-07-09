# Git - Getting Started

## Introduction

Before Git can track your project, you need to create a project folder and initialize it as a Git repository.

Once initialized, Git starts monitoring the project and allows you to track every change made to your files.

---

# Prerequisites

Before starting, make sure:

- Git is installed on your computer.
- Git is configured with your username and email.
- You have a terminal (Git Bash, Command Prompt, PowerShell, or Terminal).

---

# Step 1: Create a Project Folder

Create a new folder for your project.

```bash
mkdir myproject
```

### What does `mkdir` do?

`mkdir` stands for **Make Directory**.

It creates a new folder.

---

# Step 2: Move Into the Project Folder

Navigate inside the folder you just created.

```bash
cd myproject
```

### What does `cd` do?

`cd` stands for **Change Directory**.

It moves your terminal into another folder.

You should now be inside your project folder.

---

# Windows Users

Instead of opening Git Bash and navigating manually:

1. Open File Explorer.
2. Open your project folder.
3. Right-click inside the folder.
4. Click **Git Bash Here**.

Git Bash will open directly inside that folder.

---

# Step 3: Initialize Git

Run:

```bash
git init
```

Example output:

```text
Initialized empty Git repository in /Users/user/myproject/.git/
```

Congratulations!

You have created your first Git repository.

---

# What is a Git Repository?

A **Git Repository (Repo)** is a project folder that Git tracks.

It stores:

- Project files
- Change history
- Commits
- Branches
- Configuration

Think of it as a database that remembers everything about your project.

---

# What Happens After Running `git init`?

Git creates a hidden folder called:

```text
.git
```

This folder contains everything Git needs to manage your project.

It stores:

- Commit history
- Branch information
- Configuration
- Staging area
- References

**Never delete the `.git` folder** unless you want to remove Git from the project.

---

# View Hidden Files

### Linux / macOS

```bash
ls -a
```

Example:

```text
.
..
.git
```

### Windows

Enable **Show Hidden Files** in File Explorer to see the `.git` folder.

---

# Creating Your First File

A Git repository starts empty.

Let's create a simple HTML file.

Create a file named:

```text
index.html
```

Example:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Hello World</title>
</head>
<body>

<h1>Hello World!</h1>
<p>This is my first Git project.</p>

</body>
</html>
```

Save this file inside your project folder.

---

# List Files

To see all files inside the current directory:

```bash
ls
```

Output:

```text
index.html
```

### What does `ls` do?

`ls` stands for **List**.

It displays all files and folders in the current directory.

---

# Check Git Status

Run:

```bash
git status
```

Example:

```text
On branch master

No commits yet

Untracked files:
  (use "git add ..." to include in what will be committed)

        index.html

nothing added to commit but untracked files present
```

Git has detected your file, but it is **not tracking it yet**.

---

# Understanding File States

Git keeps files in different states.

## 1. Untracked Files

An **Untracked File** is a file that exists in your project folder but Git is not monitoring.

Example:

```text
index.html
```

Git knows the file exists, but it will not save its history until you tell Git to track it.

---

## 2. Tracked Files

A **Tracked File** is a file that Git is monitoring.

Git watches every change made to tracked files.

To make a file tracked, it must first be added to the staging area using:

```bash
git add filename
```

Example:

```bash
git add index.html
```

or

```bash
git add .
```

This topic is covered in the next chapter.

---

# Repository Workflow

```text
Create Project
      │
      ▼
git init
      │
      ▼
Create Files
      │
      ▼
git status
      │
      ▼
Untracked Files
      │
      ▼
git add
      │
      ▼
Tracked Files
```

---

# Common Commands

| Command | Description |
|----------|-------------|
| `mkdir project` | Create a new folder |
| `cd project` | Enter the folder |
| `git init` | Initialize Git repository |
| `ls` | List files |
| `ls -a` | Show hidden files |
| `git status` | Check repository status |

---

# Troubleshooting

## `git: command not found`

### Cause

Git is not installed or not added to the system PATH.

### Solution

- Install Git.
- Restart your terminal.
- Verify installation:

```bash
git --version
```

---

## Permission Denied

### Solution

Windows:

Run Git Bash or Command Prompt as **Administrator**.

Linux/macOS:

Use:

```bash
sudo
```

only when necessary.

---

## File Not Showing in `ls`

Possible reasons:

- File wasn't saved.
- You're in the wrong directory.

Check your current location:

```bash
pwd
```

---

## File Not Appearing in `git status`

Possible reasons:

- You're inside the wrong folder.
- The file hasn't been saved yet.

Verify:

```bash
pwd
ls
```

---

# Summary

By the end of this chapter, you learned how to:

- Create a project folder.
- Navigate into the folder.
- Initialize a Git repository.
- Understand what a repository is.
- Learn what the `.git` folder does.
- Create your first file.
- List project files.
- Check repository status.
- Understand the difference between tracked and untracked files.