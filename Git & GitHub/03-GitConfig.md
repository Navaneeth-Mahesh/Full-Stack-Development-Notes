# Git Configuration 

Git Configuration tells Git **who you are** and **how Git should behave**.

Whenever you create a commit, Git saves information like:

* Who created the commit
* Email of the author
* Date and time
* Commit message

Without configuration, Git doesn't know who you are.

---

# What is Git Configuration?

Git stores settings called **configuration**.

These settings tell Git things like:

* Your name
* Your email
* Default branch name
* Preferred editor
* Aliases
* Many other preferences

Think of it like your profile settings.

```
Git
│
├── Name
├── Email
├── Default Branch
├── Editor
└── Other Preferences
```

---

# Why do we configure Git?

Imagine you work in a company with 100 developers.

Everyone pushes code.

Git needs to know:

> Who made this change?

So every commit contains:

```
Author: Navaneeth
Email : navaneeth@gmail.com

Commit:
Added Login Page
```

Without this information Git cannot identify the author correctly.

---

# Configure User Name

This tells Git your name.

### Command

```bash
git config --global user.name "Navaneeth"
```

### Explanation

```
git
```

Git command.

```
config
```

Open Git configuration.

```
--global
```

Save this setting for **all repositories** on your computer.

```
user.name
```

The setting you want to change.

```
"Navaneeth"
```

The value you are assigning.

---

### Result

Now every commit will show

```
Author: Navaneeth
```

---

# Configure Email

Git also stores your email.

### Command

```bash
git config --global user.email "your@example.com"
```

Now commits will contain

```
Author:
Navaneeth

Email:
your@example.com
```

---

# Why Email?

GitHub uses your email to:

* Identify you
* Link commits to your GitHub account
* Show contribution graphs

Example

```
Commit

Name:
Navaneeth

Email:
navaneeth@gmail.com
```

GitHub sees that email and attaches the commit to your account.

---

# What does `--global` mean?

This is one of the most important concepts.

When you write

```bash
git config --global user.name "Navaneeth"
```

Git saves it for **every project**.

Example

```
Computer

├── Portfolio
├── Ecommerce
├── College Project
├── Todo App
└── AI Project
```

All these projects automatically use

```
Name:
Navaneeth

Email:
your@gmail.com
```

You configure it once.

No need to configure again.

---

# What happens if you make a mistake?

Suppose you typed

```bash
git config --global user.name "Navneth"
```

Oops.

Simply run

```bash
git config --global user.name "Navaneeth"
```

The old value is replaced.

No extra steps needed.

---

# Viewing All Configuration

To see every Git setting

```bash
git config --list
```

Example output

```text
user.name=Navaneeth
user.email=navaneeth@gmail.com
core.editor=code --wait
init.defaultbranch=main
```

Meaning

```
user.name
↓

Navaneeth

user.email
↓

navaneeth@gmail.com

core.editor
↓

VS Code

default branch
↓

main
```

---

# View Only One Setting

Instead of everything, you can ask for one value.

Example

```bash
git config user.name
```

Output

```text
Navaneeth
```

Another example

```bash
git config user.email
```

Output

```text
navaneeth@gmail.com
```

---

# Changing a Configuration

Simply run the command again.

Old value

```bash
git config --global user.name "Nav"
```

Change it

```bash
git config --global user.name "Navaneeth"
```

Now Git stores

```
Navaneeth
```

Old value is overwritten.

---

# Removing a Configuration

Use

```bash
git config --global --unset user.name
```

Now

```
user.name
```

is removed.

You can also remove other settings.

Example

```bash
git config --global --unset core.editor
```

---

# Setting Default Branch

When creating a new repository

Old Git versions created

```
master
```

Nowadays

```
main
```

is the standard.

To make Git always create

```
main
```

run

```bash
git config --global init.defaultBranch main
```

Now every new repository starts like

```
Project

main
```

instead of

```
Project

master
```

---

# Configuration Levels

Git has **3 configuration levels**.

```
System
↓

Global
↓

Local
```

Let's understand each one.

---

# 1. System Configuration

Command

```bash
git config --system
```

Applies to

```
Entire Computer

All Users
```

Imagine a family computer

```
Computer

├── User A
├── User B
├── User C
```

System configuration affects

```
Everyone
```

Usually only administrators use this.

---

# 2. Global Configuration

Command

```bash
git config --global
```

Applies to

```
Current User
```

Example

```
Windows

Computer

├── Navaneeth
├── Brother
└── Sister
```

If you're logged into **Navaneeth's** account,

```bash
git config --global user.name "Navaneeth"
```

only affects **Navaneeth's** Git settings.

This is the level most developers use.

---

# 3. Local Configuration

Command

```bash
git config --local
```

or simply

```bash
git config
```

inside a repository.

Local configuration affects **only the current project**.

Example

```
Projects

├── Portfolio
├── Company Project
└── College Project
```

Suppose your global name is

```
Navaneeth
```

But for one project you want

```
Company Bot
```

Go inside that repository

```bash
cd company-project
```

Then

```bash
git config user.name "Company Bot"
```

Only this project uses

```
Company Bot
```

All other repositories still use

```
Navaneeth
```

---

# Order of Precedence (Priority)

Suppose Git finds different values at different levels.

Example

```
System

Name = System User

↓

Global

Name = Navaneeth

↓

Local

Name = College Project
```

Which one wins?

Git follows this priority:

```
Local
↑ Highest Priority

Global

System
↓ Lowest Priority
```

So Git uses

```
College Project
```

because Local overrides Global and System.

---

# Example

Suppose

System

```text
user.name=Admin
```

Global

```text
user.name=Navaneeth
```

Local

```text
user.name=Backend Team
```

When committing inside that repository

Git uses

```
Backend Team
```

because Local has the highest priority.

---

# Real-Life Analogy

Imagine you work in a company.

**System (Office Rule)**

Everyone wears an ID card.

**Global (Your Personal Preference)**

You always wear a blue shirt.

**Local (Special Event)**

Today the project team requires everyone to wear black.

Which shirt do you wear today?

**Black**, because the project-specific rule overrides your normal preference.

Git works the same way: **Local > Global > System**.

---

# Summary

| Command                                              | Purpose                                               |
| ---------------------------------------------------- | ----------------------------------------------------- |
| `git config --global user.name "Name"`               | Set your name for all repositories                    |
| `git config --global user.email "email@example.com"` | Set your email for all repositories                   |
| `git config --list`                                  | Show all Git settings                                 |
| `git config user.name`                               | Show only your configured name                        |
| `git config user.email`                              | Show only your configured email                       |
| `git config --global --unset user.name`              | Remove the global user name                           |
| `git config --global init.defaultBranch main`        | Make `main` the default branch for new repositories   |
| `git config --system`                                | Configure settings for all users on the computer      |
| `git config --global`                                | Configure settings for the current user (most common) |
| `git config --local` or `git config`                 | Configure settings only for the current repository    |

### Key Takeaways

* `git config` is used to view and change Git settings.
* `user.name` and `user.email` identify you as the author of commits.
* `--global` applies settings to all repositories for your user account.
* `--local` applies settings only to the current repository.
* `--system` applies settings to every user on the computer.
* If the same setting exists at multiple levels, Git uses this priority:
  **Local → Global → System**.
* You can view all settings with `git config --list` and update or remove them at any time.
