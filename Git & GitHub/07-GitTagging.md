# Git Tagging

Git tags are used to mark important points in your project's history. They act like permanent labels for specific commits, making it easy to identify releases, milestones, or stable versions of your project.

---

# What is a Git Tag?

A **Git Tag** is a reference that points to a specific commit.

Think of it as placing a bookmark inside a book. Instead of searching through hundreds of pages (commits), you can instantly jump to an important location.

Tags are commonly used for:

-  Software Releases (v1.0, v2.0)
-  Production Deployments
-  Project Milestones
-  Hotfix Versions
-  Stable Builds

---

# Why Use Tags?

Without tags, finding the exact commit of a previous release can be difficult.

With tags, you can:

- Easily identify releases
- Return to older versions anytime
- Share release versions with your team
- Deploy a specific version confidently
- Keep project history organized

---

# Types of Git Tags

Git provides two types of tags:

## 1. Lightweight Tag

A lightweight tag is simply a name that points to a commit.

It does **not** store:

- Author
- Date
- Message

Think of it as a simple bookmark.

### Syntax

```bash
git tag <tagname>
```

### Example

```bash
git tag v1.0
```

This creates a lightweight tag named **v1.0**.

---

## 2. Annotated Tag

Annotated tags contain additional metadata.

They store:

- Author Name
- Email
- Date
- Tag Message

Annotated tags are recommended for releases because they provide useful information.

### Syntax

```bash
git tag -a <tagname> -m "message"
```

### Example

```bash
git tag -a v1.0 -m "Version 1.0 Release"
```

---

# Lightweight vs Annotated Tags

| Feature | Lightweight | Annotated |
|----------|-------------|------------|
| Stores metadata | ❌ No | ✅ Yes |
| Stores message | ❌ No | ✅ Yes |
| Stores author | ❌ No | ✅ Yes |
| Recommended for releases | ❌ No | ✅ Yes |
| Best for personal bookmarks | ✅ Yes | ❌ Not necessary |

---

# Create a Tag

## Lightweight Tag

```bash
git tag v1.0
```

---

## Annotated Tag

```bash
git tag -a v1.0 -m "Version 1.0 Release"
```

---

# Tag a Specific Commit

You can attach a tag to any previous commit using its commit hash.

### Syntax

```bash
git tag <tagname> <commit-hash>
```

### Example

```bash
git tag v1.1 1a2b3c4d
```

Replace `1a2b3c4d` with the desired commit hash.

---

# List All Tags

To see every tag in your repository:

```bash
git tag
```

### Example Output

```text
v1.0
v1.1
v2.0
```

---

# View Tag Details

Use `git show` to inspect a tag.

### Syntax

```bash
git show <tagname>
```

### Example

```bash
git show v1.0
```

Example output:

```text
tag v1.0
Tagger: Navaneeth
Date: Tue Jul 8 20:15:10 2026

Version 1.0 Release

commit a4d6b8c...
Author: Navaneeth
Date: Tue Jul 8 19:30:44 2026

Initial Stable Release
```

---

# Push Tags to Remote

Tags are created **only on your local machine**.

They are **not automatically uploaded** when you push commits.

---

## Push a Single Tag

```bash
git push origin v1.0
```

---

## Push All Tags

```bash
git push --tags
```

This uploads every local tag to the remote repository.

> **Note:** `git push` only pushes commits. Tags must be pushed separately.

---

# Delete a Local Tag

### Syntax

```bash
git tag -d <tagname>
```

### Example

```bash
git tag -d v1.0
```

---

# Delete a Remote Tag

### Syntax

```bash
git push origin --delete tag <tagname>
```

### Example

```bash
git push origin --delete tag v1.0
```

This removes the tag from the remote repository.

---

# Update or Replace a Tag

Sometimes a tag points to the wrong commit.

You can move it to another commit.

### Step 1

Force update the local tag.

```bash
git tag -f v1.0 <new-commit-hash>
```

### Step 2

Force push the updated tag.

```bash
git push --force origin v1.0
```

> **Warning:** Force pushing tags changes history for everyone using the repository. Use it carefully.

---

# Common Workflow

Suppose you've completed Version 1.0 of your project.

### Commit your changes

```bash
git add .
git commit -m "Finish Version 1.0"
```

### Create an annotated tag

```bash
git tag -a v1.0 -m "Version 1.0 Release"
```

### Push commits

```bash
git push origin main
```

### Push the tag

```bash
git push origin v1.0
```

Your release is now available to everyone.

---

# Best Practices

- Use annotated tags for releases.
- Keep tag names meaningful.
- Follow semantic versioning (`v1.0.0`, `v1.1.0`, `v2.0.0`).
- Tag only tested and stable commits.
- Push tags after creating them.
- Avoid modifying published tags unless absolutely necessary.

---

# Common Version Naming

```text
v1.0.0
v1.1.0
v1.2.0
v2.0.0
```

Meaning:

- First number → Major release
- Second number → New features
- Third number → Bug fixes

Example:

```text
v1.0.0
│ │ │
│ │ └── Patch
│ └──── Minor
└────── Major
```

---

# Troubleshooting

## Tag Already Exists

Delete the old tag and create a new one.

```bash
git tag -d v1.0
git tag -a v1.0 -m "Version 1.0 Release"
```

---

## Wrong Tag Was Pushed

Delete it locally:

```bash
git tag -d v1.0
```

Delete it remotely:

```bash
git push origin --delete tag v1.0
```

Create the correct tag:

```bash
git tag -a v1.0 -m "Correct Release"
```

Push it again:

```bash
git push origin v1.0
```

---

## Tag Not Showing on GitHub

Remember:

```bash
git push
```

Only pushes commits.

To push tags:

```bash
git push origin v1.0
```

or

```bash
git push --tags
```

---

# Quick Reference

| Command | Description |
|----------|-------------|
| `git tag v1.0` | Create a lightweight tag |
| `git tag -a v1.0 -m "Release"` | Create an annotated tag |
| `git tag` | List all tags |
| `git show v1.0` | Show tag details |
| `git tag v1.0 <commit>` | Tag a specific commit |
| `git push origin v1.0` | Push one tag |
| `git push --tags` | Push all tags |
| `git tag -d v1.0` | Delete local tag |
| `git push origin --delete tag v1.0` | Delete remote tag |
| `git tag -f v1.0 <commit>` | Replace a tag |
| `git push --force origin v1.0` | Force update remote tag |

---

# Summary

Git tags provide a simple and reliable way to mark important commits in your project's history.

Use **lightweight tags** for quick personal bookmarks and **annotated tags** for official releases, deployments, and version tracking.

Following consistent tagging practices makes collaboration easier, simplifies deployments, and helps you quickly return to any important version of your project.