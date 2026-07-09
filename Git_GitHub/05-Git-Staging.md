# Git Staging Environment 

## What is the Staging Environment?

The **staging environment** (also called the **staging area** or **index**) is a temporary place where Git stores the changes you want to include in your **next commit**.

Think of it like a **shopping cart**:

*  Your project files = Items in the store
*  Staging Area = Shopping cart
*  Commit = Placing the order

You choose which files go into the cart (staging area), and only those files become part of the next commit.

---

# Why Does Git Have a Staging Area?

Without staging, every changed file would automatically be committed.

The staging area gives you **full control** over:

* Which files to commit
* Which changes to leave for later
* Creating clean, meaningful commits

---

# Git Workflow

```text
Working Directory
       │
       │ Edit/Create/Delete Files
       ▼
git add
       ▼
Staging Area
       │
       │ git commit
       ▼
Local Repository
       │
       │ git push
       ▼
GitHub / GitLab / Bitbucket
```

---

# Example

Suppose your project contains:

```text
project/
│
├── index.html
├── style.css
└── script.js
```

You modify:

* index.html
* style.css

Current state:

```text
Working Directory

Modified:
✔ index.html
✔ style.css
```

Nothing is committed yet.

---

## Stage One File

```bash
git add index.html
```

Now only `index.html` is ready for the next commit.

```text
Working Directory

Modified:
✔ style.css

Staging Area

✔ index.html
```

---

## Check Status

```bash
git status
```

Example output:

```bash
On branch main

Changes to be committed:
    modified: index.html

Changes not staged for commit:
    modified: style.css
```

Explanation:

* `index.html` → staged
* `style.css` → not staged

---

# Stage Multiple Files

Instead of adding one by one:

```bash
git add index.html
git add style.css
git add script.js
```

You can stage everything:

```bash
git add --all
```

or

```bash
git add -A
```

or

```bash
git add .
```

### Difference

### `git add .`

Stages changes inside the current directory.

```bash
git add .
```

---

### `git add -A`

Stages **everything**:

* New files
* Modified files
* Deleted files

```bash
git add -A
```

---

### `git add --all`

Exactly the same as:

```bash
git add -A
```

---

# Check What is Staged

```bash
git status
```

Example:

```bash
Changes to be committed:

new file: README.md
modified: style.css
deleted: old.js
```

Everything listed under **Changes to be committed** is staged.

---

# Unstage a File

Suppose you accidentally staged:

```bash
git add style.css
```

But you don't want to commit it yet.

Remove it from the staging area:

```bash
git restore --staged style.css
```

Now:

```text
Working Directory

✔ style.css

Staging Area

(empty)
```

The file is **still modified**, but it won't be included in the next commit.

---

# Older Alternative

Before `git restore` existed, Git used:

```bash
git reset HEAD style.css
```

Both commands unstage the file.

Modern Git recommends:

```bash
git restore --staged <file>
```

---

# Complete Example

### Step 1

Create a project

```text
project/

index.html
style.css
script.js
```

---

### Step 2

Modify two files

```text
Modified:

index.html
style.css
```

---

### Step 3

Check status

```bash
git status
```

Output:

```bash
Modified:
index.html
style.css
```

---

### Step 4

Stage only one file

```bash
git add index.html
```

---

### Step 5

Check again

```bash
git status
```

Output:

```bash
Changes to be committed:

modified: index.html

Changes not staged:

modified: style.css
```

---

### Step 6

Commit

```bash
git commit -m "Update homepage"
```

Only `index.html` is saved in this commit.

`style.css` remains uncommitted.

---

# Common Commands

| Command                         | Purpose                                    |
| ------------------------------- | ------------------------------------------ |
| `git add file.txt`              | Stage one file                             |
| `git add .`                     | Stage changes in the current directory     |
| `git add -A`                    | Stage all changes (new, modified, deleted) |
| `git add --all`                 | Same as `git add -A`                       |
| `git status`                    | Show staged and unstaged changes           |
| `git restore --staged file.txt` | Unstage a file                             |
| `git reset HEAD file.txt`       | Older way to unstage a file                |
| `git commit -m "message"`       | Commit staged changes                      |

---

# Real-Life Analogy

Imagine you're sending documents in an envelope:

*  **Working Directory** → All the papers on your desk.
*  **Staging Area** → The papers you've placed inside the envelope.
*  **Commit** → Sealing the envelope.
*  **Push** → Mailing the envelope to GitHub.

Only the papers inside the envelope (staged files) are sent when you commit.

---

# Summary

* The **Working Directory** contains all your current file changes.
* The **Staging Area** lets you choose exactly which changes will be included in the next commit.
* Use `git add` to move changes to the staging area.
* Use `git status` to inspect what is staged and what isn't.
* Use `git restore --staged <file>` to remove a file from the staging area without losing your changes.
* Only **staged** changes are recorded when you run `git commit`.
