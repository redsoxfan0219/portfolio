---
title: "Introduction to the Command Line for Technical Writers"
description: ""
lead: ""
date: 2022-10-28T09:08:22-04:00
lastmod: 2022-10-28T09:08:22-04:00
draft: false
images: []
menu:
  docs:
    parent: "articles-and-guides"
weight: 60
toc: true
---

This guide is intended for technical writers who have no or limited experience with the command line.

Windows, Mac, and Linux computers have slightly different command line interfaces (CLIs). Below, I include separate instructions for all three. Focus on the sections that apply to the system you're using.

Note: for Linux, I base my instructions on the Ubuntu distribution. There may be minor differences for you if are using a different distribution.

## What Is the Command Line?

The command line is a program that makes an operating system perform actions. It works by processing textual commands written by a user. In this respect, it differs from most programs, which which take their directions from a user's mouse clicks. These other programs are known as "graphical user interfaces" (GUIs).

The command line goes by different names. Mac and Linux calls it **Terminal**. Windows has two CLIs, one called **Command Prompt** and one called **PowerShell**. Powershell is more versatile, and it is the Windows CLI I will use for instructions below.

## Opening the Command Line

The command line can be found the same way you find your other programs. 

### For Mac 

1. Open a Finder window.
2. Use the search bar to search for **Terminal**.
3. In the search returns, locate **Terminal** and double-click to open it.

I recommend adding **Terminal**  to your MacOS Dock. Click and drag the **Terminal** icon from your search returns and drop it in your Dock.

### For Windows 

1. Open the Start Menu.
2. Search for **PowerShell** in the search bar.
3. When the **PowerShell** icon appears, double-click to open the program.

### For Linux 


## Understanding the Terminal Window

When first opened, a command line info will display some information. This section explains what you're seeing.

### For Mac 

Here's a newly opened Terminal window. Your color schema may be different.

![Mac Terminal Home Directory](mac-terminal-home-directory.png)

Here's what you're seeing:

- "Last login" gives a timestamp for the last time you opened a Terminal window. If you open a new window (⌘ + N), the timestamp will change.
- The next three lines relate to the "shell," which is the invisible program used to convert your textual commands into computer actions. Don't worry about this for now.
- The last line tells you five things:
  - `(base) Macbook Pro:`. This tells you the machine you're working on. It'll differ for your machine, unless you're on a Macbook Pro.
  - `~`. This indicates your home directory. Terminal will start in your home directory when you open a new window.
  - `benjaminmoran`. This indicates your "relative working directory." "Relative" here means "short form," and "working directory" indicates where the terminal is currently "looking." More on this soon.
  - `$`. This is the prompt. It may be a `%` for you. It indicates where you will start entering your commands.
  - `▮`. This is the cursor. It's likely flashing. It tells you where you're typing. It will move as you type something.

### For Windows 


### For Linux 




