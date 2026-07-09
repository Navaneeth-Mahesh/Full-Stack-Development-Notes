# Git Installation Guide

> A complete guide to installing Git on Windows, macOS, and Linux.

---

# What is Git?

Git is a **Version Control System (VCS)** used to:

- Track changes in code
- Collaborate with developers
- Maintain project history
- Revert mistakes
- Work with GitHub, GitLab, and Bitbucket

---

# Before Installing

## Check if Git is Already Installed

Open your terminal or command prompt.

### Windows

```bash
git --version
```

### Linux

```bash
git --version
```

### macOS

```bash
git --version
```

Example output:

```bash
git version 2.50.1
```

If you receive something like:

```bash
'git' is not recognized...
```

or

```bash
command not found: git
```

Git is not installed.

---

# Installing Git on Windows

## Method 1 (Recommended)

Download Git from:

https://git-scm.com/downloads

The download usually starts automatically.

---

## Installation Steps

Run the installer.

Most options can be left as **Default**.

Recommended settings:

### Select Components

✔ Git Bash

✔ Git GUI

✔ Git LFS (optional)

✔ Windows Explorer Integration

Leave the remaining options as default.

---

### Choosing Default Editor

Recommended:

- Visual Studio Code
- Vim (default)
- Nano

If you use VS Code, select:

```
Use Visual Studio Code as Git's default editor
```

---

### PATH Environment

Choose:

```
Git from the command line and also from 3rd-party software
```

This allows Git to work from:

- CMD
- PowerShell
- VS Code Terminal
- Windows Terminal

---

### HTTPS Transport Backend

Choose:

```
Use the OpenSSL Library
```

(Default)

---

### Line Ending Conversion

Recommended:

```
Checkout Windows-style, commit Unix-style line endings
```

(Default)

---

### Terminal Emulator

Choose:

```
Use MinTTY
```

(Default)

---

### Git Pull Behavior

Choose:

```
Fast-forward or merge
```

(Default)

---

### Credential Helper

Choose:

```
Git Credential Manager
```

This securely stores GitHub credentials.

---

### Extra Options

Leave defaults.

Click:

```
Install
```

Wait until installation completes.

Click:

```
Finish
```

---

# Installing Git on macOS

## Method 1 (Recommended)

Install using Homebrew:

```bash
brew install git
```

---

## Method 2

Download installer:

https://git-scm.com/download/mac

---

## Method 3

Install Xcode Command Line Tools

```bash
xcode-select --install
```

This also installs Git.

---

# Installing Git on Linux

---

## Ubuntu / Debian

```bash
sudo apt update

sudo apt install git
```

---

## Fedora

```bash
sudo dnf install git
```

---

## CentOS

```bash
sudo yum install git
```

---

## Arch Linux

```bash
sudo pacman -S git
```

---

## openSUSE

```bash
sudo zypper install git
```

---

# Verify Installation

Run:

```bash
git --version
```

Example:

```bash
git version 2.50.1
```

Git is now installed successfully.

---

# First-Time Git Setup

Git needs to know who you are.

---

## Set Username

```bash
git config --global user.name "Your Name"
```

Example

```bash
git config --global user.name "Navaneeth"
```

---

## Set Email

Use the email associated with your GitHub account.

```bash
git config --global user.email "you@example.com"
```

Example

```bash
git config --global user.email "navaneeth@gmail.com"
```

---

## Verify Configuration

```bash
git config --list
```

or

```bash
git config --global --list
```

Expected output:

```text
user.name=Navaneeth
user.email=navaneeth@gmail.com
```

---

# Set Default Branch Name

Git now recommends using **main**.

```bash
git config --global init.defaultBranch main
```

Verify:

```bash
git config --global init.defaultBranch
```

Output:

```text
main
```

---

# Enable Colored Output

```bash
git config --global color.ui auto
```

---

# Set VS Code as Default Editor

If VS Code is installed:

```bash
git config --global core.editor "code --wait"
```

Verify:

```bash
git config --global core.editor
```

---

# View All Global Settings

```bash
git config --global --list
```

---

# Where Git Stores Configuration

## Windows

```text
C:\Users\<YourUsername>\.gitconfig
```

---

## Linux

```text
~/.gitconfig
```

---

## macOS

```text
~/.gitconfig
```

---

# Git Configuration Levels

Git has three configuration levels.

## System

Applies to every user.

```bash
git config --system
```

---

## Global

Applies to your account.

```bash
git config --global
```

---

## Local

Applies only to the current repository.

```bash
git config --local
```

---

# Check Configuration Values

Username

```bash
git config user.name
```

Email

```bash
git config user.email
```

Global Username

```bash
git config --global user.name
```

Global Email

```bash
git config --global user.email
```

---

# Update Username

```bash
git config --global user.name "New Name"
```

---

# Update Email

```bash
git config --global user.email "new@email.com"
```

---

# Remove Configuration

Remove username:

```bash
git config --global --unset user.name
```

Remove email:

```bash
git config --global --unset user.email
```

---

# Test Git

Create a test folder.

```bash
mkdir git-test
```

Move inside it.

```bash
cd git-test
```

Initialize Git.

```bash
git init
```

Output:

```text
Initialized empty Git repository...
```

Check repository status.

```bash
git status
```

If you see:

```text
On branch main

No commits yet
```

Git is working correctly.

---

# Common Installation Problems

## Git command not found

Restart your terminal.

If it still doesn't work:

- Reinstall Git.
- Ensure Git is added to the system PATH.
- Run `git --version` again.

---

## VS Code doesn't recognize Git

Restart VS Code.

Open a new terminal and run:

```bash
git --version
```

If it works in the terminal but not in VS Code:

- Restart VS Code.
- Check that Git is installed and accessible in your PATH.

---

## Permission Denied

On Linux/macOS:

```bash
sudo apt install git
```

or use the appropriate package manager with administrator privileges.

---

# Recommended Tools

- Git
- Git Bash (Windows)
- Visual Studio Code
- GitHub Desktop (optional)
- Windows Terminal (Windows)
- Homebrew (macOS)

---

# Next Step After Installing Git

Once Git is installed and configured, you should learn these commands in order:

1. `git init`
2. `git status`
3. `git add`
4. `git commit`
5. `git log`
6. `git branch`
7. `git checkout`
8. `git switch`
9. `git merge`
10. `git clone`
11. `git remote`
12. `git push`
13. `git pull`
14. `git fetch`
15. `git stash`
16. `git reset`
17. `git restore`
18. `git tag`
19. `git rebase`
20. `.gitignore`

---

# Summary

After installing Git:

- Install Git for your operating system.
- Verify the installation with `git --version`.
- Configure your username and email.
- Set the default branch to `main`.
- Optionally set VS Code as the default editor.
- Verify your configuration.
- Create a test repository using `git init`.
- Start learning core Git commands before working with GitHub.