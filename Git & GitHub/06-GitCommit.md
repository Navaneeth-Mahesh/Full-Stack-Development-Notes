# Git Commit

## What is a Commit?

A **commit** is a snapshot of your project at a specific point in time.

Think of it like **saving your game's progress**. Every commit stores the current state of your tracked files along with a message describing what changed.

### Why are commits important?

- Save your project history
- Track changes over time
- Restore previous versions if something breaks
- Collaborate with other developers
- Understand what changed and why

---

# Basic Workflow

```text
Modify Files
      │
      ▼
git add .
      │
      ▼
git commit -m "Your message"
      │
      ▼
Commit Created
```

---

# Basic Syntax

```bash
git commit -m "commit message"
```

### Example

```bash
git commit -m "Initial project setup"
```

Output:

```text
[main a1b2c3d] Initial project setup
 3 files changed, 120 insertions(+)
 create mode 100644 README.md
 create mode 100644 index.html
 create mode 100644 style.css
```

---

# Commit Message

A commit message explains **what changes were made**.

Example:

```bash
git commit -m "Add login page"
```

Good examples:

```text
Initial project setup
Add navbar
Fix login bug
Update README
Improve UI responsiveness
Create authentication API
```

Bad examples:

```text
Update
Changes
Done
Fix
abc
test
```

Always write meaningful commit messages.

---

# Commit All Tracked Files

Instead of staging tracked files manually:

```bash
git commit -a -m "Update project"
```

This automatically stages:

- Modified files
- Deleted files

It does **NOT** stage:

- New files

Example:

```bash
git commit -a -m "Fix responsive layout"
```

---

# Why Doesn't `-a` Add New Files?

Suppose you created:

```text
app.js
```

If you run:

```bash
git commit -a -m "Add app"
```

Git will show:

```text
Untracked files:
    app.js

nothing added to commit
```

Because Git doesn't know about new files.

First add them:

```bash
git add app.js
```

Then commit:

```bash
git commit -m "Add app.js"
```

---

# Multi-line Commit Messages

Instead of using `-m`, simply run:

```bash
git commit
```

Git opens your default text editor.

Example:

```text
Add authentication system

Implemented JWT authentication.
Added login and signup APIs.
Improved password validation.
```

This is useful for large or important changes.

---

# Commit Message Best Practices

✔ Keep the first line under **50 characters**

✔ Use present tense

Good:

```text
Add dashboard
Fix login issue
Update README
```

Bad:

```text
Added dashboard
Fixed login issue
```

✔ Explain **why** if necessary

Example:

```text
Improve API validation

Prevent invalid user input from reaching the database.
```

---

# Empty Commit

Sometimes you want a commit without changing files.

```bash
git commit --allow-empty -m "Project initialized"
```

Useful for:

- Testing CI/CD
- Starting workflows
- Triggering GitHub Actions

---

# Reuse Previous Commit Message

Reuse the previous commit message:

```bash
git commit --no-edit
```

Useful after amending changes.

---

# Amend the Last Commit

Add more changes to the previous commit without creating a new one.

```bash
git commit --amend --no-edit
```

Or change the commit message:

```bash
git commit --amend -m "Correct commit message"
```

Example:

```bash
git add README.md

git commit --amend --no-edit
```

---

# Forgot to Stage a File?

Example:

```bash
git commit -m "Add login"
```

Oops! Forgot:

```text
config.js
```

Fix:

```bash
git add config.js

git commit --amend --no-edit
```

Now the file is included in the last commit.

---

# Correct a Commit Message

Wrong:

```text
git commit -m "Ad login"
```

Correct it:

```bash
git commit --amend -m "Add login"
```

---

# Undo the Last Commit

Keep your changes but remove the commit:

```bash
git reset --soft HEAD~1
```

Result:

- Commit removed
- Files remain staged

Useful if you committed too early.

---

# View Commit History

## Show Full History

```bash
git log
```

Example:

```text
commit 8f3d2b1...

Author: Navaneeth

Date: July 9

Add login authentication

commit 1ab23cd...

Initial project setup
```

---

## Short History

```bash
git log --oneline
```

Output:

```text
8f3d2b1 Add login authentication
1ab23cd Initial project setup
```

---

## Show Changed Files

```bash
git log --stat
```

Example:

```text
README.md      | 10 +++++-----
app.js         | 22 ++++++++++++++++
style.css      | 8 +++++++
```

Shows how many files changed in each commit.

---

# Useful Commit Commands

| Command | Description |
|----------|-------------|
| `git commit -m "msg"` | Create a commit with a message |
| `git commit -a -m "msg"` | Commit all tracked files |
| `git commit` | Open editor for multi-line message |
| `git commit --allow-empty -m "msg"` | Create an empty commit |
| `git commit --no-edit` | Reuse previous commit message |
| `git commit --amend` | Modify the last commit |
| `git commit --amend --no-edit` | Add changes to the last commit |
| `git commit --amend -m "msg"` | Change the last commit message |
| `git log` | Show complete commit history |
| `git log --oneline` | Show compact commit history |
| `git log --stat` | Show files changed in commits |
| `git reset --soft HEAD~1` | Undo last commit and keep changes |

---

# Example Workflow

```bash
# Check status
git status

# Stage files
git add .

# Create commit
git commit -m "Add user authentication"

# View history
git log --oneline

# Push to GitHub
git push origin main
```

---

# Summary

A Git commit is a saved snapshot of your project.

Basic workflow:

```bash
git add .
git commit -m "Meaningful commit message"
git push origin main
```

Always:

- Write clear commit messages
- Commit small, focused changes
- Commit frequently
- Review your history using `git log`