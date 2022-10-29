---
title: "Introduction to Git for Technical Writers"
description: ""
lead: ""
date: 2022-10-28T09:08:22-04:00
lastmod: 2022-10-28T09:08:22-04:00
draft: false
images: []
menu:
  docs:
    parent: "articles-and-guides"
weight: 70
toc: true
---

Increasingly, technical writing jobs require knowledge of something called "version control," and by far the most popular version control system is a program called [Git](https://git-scm.com/). It's commonplace now for TW job posts simply list Git as a required skill, without explain explaining what it is or how it relates to TW.

This page provides an explanation of what Git is and how to use it. I emphasize topics of interests to technical writers, especially those who write or are interested in writing developer documentation.

If you don't want to read the explanation of what Git is, you can jump to the either the [Git Instructions](#git-instructions) or [Git Cheat Sheet](#git-cheat-sheet).

## What Is Version Control?

Version control is simply a way of  tracking changes made to files stored within a directory on a computer. There's a bit more to it than that is a good enough definition for now.

## Why Should I Know Version Control?

Think about instances where you've collaborated on document with a peer using a program like Microsoft Word. Unless you were using a cloud-based version of Word in Microsoft Teams or SharePoint, you inevitably ran into situations where you had to maintain different file version. You probably exchanged several emails with attachments named `Working Document_v2`, `Working Document_v2.1`, or, God forbid, `Working Document_Final`. (And when that `Final` version proved to not really be "final," you may have another version called `Working Document_final_final`. Where does it end?)

If you've experienced situations like the one described above, you've already experienced the reason why version control is necessary. It's inevitable that the system described above will break down at some point. Someone will forget to download the latest version from their email, or someone will download the right version but forget to re-save with a different `_v<>` number. 

The other major headache with this approach is not knowing what changes were made in each file version. Even if you devised a fool-proof method for the suffix-based versioning system, how can you know which changes were associated with which version? Maybe you remember broadly what each version covers. But to version a document properly, you would need a computer-like memory for the details or every version—every paragraph, every word, every comma—and you would need to be able to hold those multiple versions in your head and compare them line-by-line. This is, for all intents and purposes, impossible.

Therefore, we need some way of systematically tracking changes from one version to the next, some way to understand what changes are associated with each version of a file. 

What we need is something called a version control system.

**TL;DR** You'll give yourself headaches (and future you will hate present you) if you manually save multiple versions of a file. 

## What Is a Version Control System?

A version control system (VCS) is a set of computational tools that allow users to systematically track changes to file or set of files within a specific repository. A VCS also allows for users to "roll back" to an earlier version of their file(s) if they so choose.

### What is Distributed Version Control?

There are two primary models of version control: centralized version control and distributed version control. 

With centralized version control, all users on a team save their changes on their personal computers and save their changes to a centralized system of record in a server. (The proper term is "committing" a change; more on this later.)

With distributed version control, each developer on a team maintains a copy of that system of record on their personal computer. When developers want to join their code with others, they submit their system of record to an orchestration system that registers differences between the various systems of record. That orchestration system allows developers to reconcile differences and merge the various systems of record into a single system of record.

Having said all that, distributed version control is what I'll be focused on in the rest of this article. While there are still teams out there that use centralized version control, distributed version control is far more popular because it's faster and it better enables collaboration between team members.

**TL;DR** In all likelihood, you'll only ever use distributed version control, so don't worry about the difference between it and centralized version.

## What is Git?

Git is a distributed VCS. It's by far the most popular VCS in the world.

Unlike many programs technical writers may be familiar with (MS Word, MadCap Flare, etc.), Git is a command line tool. It is directed by textual commands entered in the command line, not by the point-and-click direction of a mouse.

### Aside on the Command Line

For those technical writers that are unfamiliar with the command line, using it can be scary the first few times. You're totally going to break your computer if you enter the wrong character, right? (Nah, not likely.) 

Fear of the command line is completely understandable if you've never used it.But the fact is that the command line is, in many respects, superior to point-and-click direction once you get used to it. It's oftentimes far quicker. You can do things with it that you can't with your mouse. Using it brings you closer to the tools that developers use, helping to break down the barrier that can separate technical writers from their developer partners.

So don't fear the command line. Embrace it.

### Git and GitHub: Related But Distinct

You'll sometimes hear Git used interchangeably with [GitHub](https://github.com/). That's wrong. Git and GitHub are separate entities and do separate things. 

Git, again, is a distributed version control system used for tracking the history and details of various file states. Git is run from the command line.

GitHub, by contrast, is a website and server used for *storing* Git repositories and their files. It also has a few other key functions that I won't get into here.

What makes the distinction between Git and GitHub murkier is that, as their similar names might suggest, they are often used in tandem. Project developers will version control their code—and docs, as I'll describe further below— on their local computer using Git. When they are ready, they will "push" their files and the accompanying Git history to GitHub, where the files and Git history can be accessed by their co-developers.

While I won't describe them in detail here, you should know that GitHub isn't the only Git storage and orchestration website out there. [GitLab](https://about.gitlab.com/) and [Bitbucket](https://bitbucket.org/product) are two other examples.

So, one of the distinctions between Git and GitHub is that you can have Git without GitHub, but you can't have GitHub without Git. 

**TL;DR** Git is a command line tool for versioning code and documentation. GitHub is a website for storing Git repositories. Git and GitHub are often used in combination.

## Git Instructions

If you're ready to start using Git, this section is for you.

### Git Installation

#### For Mac

If you're on a Mac, you will install Git via [Homebrew](https://brew.sh/). To do that,
   
1. Open your Terminal (the command line on Mac).

2. Enter ```/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"```

3. Wait for the downloads to finish. This can take some time.
   
4. When Homebrew has finished installing, enter ```brew install git```.

#### For Windows

If you're on a Windows machine, 

1. Click [here](https://github.com/git-for-windows/git/releases/download/v2.38.1.windows.1/Git-2.38.1-64-bit.exe) to download the Git Installer.

2. Open the installer where you've downloaded it (likely your `Downloads` folder).
   
3. Progress through the installer menu, accepting the defaults.
  
#### For Linux

If you're on a Linux machine, the exact mechanism you'll use will vary by your distribution. 

1. Start by opening the Terminal. You might find this in your distribution by searching for "Shell."
2. Enter the command appropriate to your distribution.
   1. If you are using Fedora, RHEL, or CentOS, enter ```sudo dnf install git-all```.
   2. If you are using Ubuntu or another Debian-based distribution, enter ```sudo apt install git-all```

### Getting Started with Git

This section will cover the basic commands of Git. This section will cover 80% of what you'll need to know to use Git for developer documentation.

#### Setting up GitHub

Further underscoring murky distinctions between Git and GitHub, we'll start our Git journey by setting up a GitHub account. If you already have a GitHub account, skip to the next section. Note that if you're using GitHub for your job, you'll probably use a version of GitHub called GitHub Enterprise. If that's the case, you'll need to set up create a separate work account through GitHub Enterprise.

1. Navigate to [github.com](https://github.com/).
2. Click 'Sign up' in the upper-right.
3. Follow the prompts to set up your account.

### Two Key Non-Git Commands

In just a moment, you'll be using the command line to set up your local Git repository. But before you do that, you need to know a few non-Git commands. 

I'll keep things limited to the very basics here. If you're interested in learning more about the command line, check out my [Introduction to the Command Line for Technical Writers](../commandlineintro).

#### `cd`, Change Working Directory

When you open your command line application, the command line will default to working in some high-level directory (i.e., folder). It's probably not the one you want to be working in, so you'll need to change your directory. You'll need to do this each time you open a new command line window.

When you open your command line, you'll see a screen that looks like the following image. Your command line may look a little different, especially if you are using Windows' `PowerShell`. But functionally this should be the same.

![Command Line Start Screen](command-line-home-directory.png)

The `~ benjaminmoran$` indicates the working directory. You can think of this as communicating the computer's present perspective: it currently sees the `/Users/benjaminmoran` folder and its contents and can perform actions on them.

However, most of the content you interact with is *not* stored in the default working directory that appears when you open a new terminal window (this is know as the "home directory"). If you want to perform actions on another directory's contents, you can either tell the machine where those other contents are or you can move the working directory to that location and perform actions on them there. It's generally easier to do the latter.

To move your working directory, you will enter: `cd <new directory>`, replacing `<new directory>` with the location that you want to work in. For example, I store my Git repositories in within my `Documents` folder. This image shows how I get there from my home directory:

![Changing Directories with the Command Line](command-line-working-directory.png)

I am now in my `GitHub` subfolder within `Documents`. Note that I didn't need to run multiple `cd` commands. I knew my `GitHub` folder was in my `Documents` directory, so I was able to jump two directories down with one command.

#### Tab Completion

There's a handy trick to make changing your directory even quicker: [tab completion](https://www.howtogeek.com/195207/use-tab-completion-to-type-commands-faster-on-any-operating-system/). When writing out a directory, for example, I can enter `TAB` after a couple of characters, and the terminal will fill in the directory. Here, I just typed `Doc` before hitting `TAB`, saving me a little bit of time. When you add up those little bits of time saved, though, you start to realize how much more efficient this is than navigating with your mouse. 

Note that, with tab completion, your computer looks for unique values based on your initial input. If it encounters two file or directory names with the same root, the terminal will stop at the point that the two file names differ. It then expects you to clarify which file or directory you intend to use. For example, imagine I have two subdirectories in my present working directory, one called `Document` and one called `Documents`. If I type `cd Doc` and hit `TAB`, the terminal will fill in `ument`, stopping at `cd Document`, because this is where the two file names differ. The terminal expects me to either hit `Enter` to change directory into `Document` or enter an `s` before entering into the `Documents` directory.

#### `ls`, List Contents of the Working Directory

You've changed into your new directory. How do you know what's there without looking at your File Explorer or Finder?

`ls` is here to help. `ls` lists the contents of your present working directory:

![ls command](command-line-ls.png)

The only thing I want to point out here is that subdirectories and files are both printed when `ls` is entered. Subdirectories do not have a file extension; files do. 


#### Setting Up a Git Repository

You can turn any ordinary folder into a Git repository, because Git repositories are just folders with a hidden `.git` file within them.

##### Cloning from Remote

There are two ways to set up a new Git repository: 

- Initiating a repository on GitHub and cloning it your local computer
- Initiating one on your local computer

I typically do the former, so I'll give those instructions first. 

1. Sign in to GitHub.
2. Click the green "New" button.
3. On the new screen, enter a repository name. I recommend using underscores or hyphens to separate words in a repository name.
4. Keep the accessibility option set to "Public."
5. Click the green "Create repository" button.
6. On the new screen, copy your repository URL, which should appear within the "Quick Setup" pane. The URL will look something like this: `https://github.com/redsoxfan0219/git-demo.git`.
7. We're now going to add a dummy file so this repository is not empty. On the same screen, click the "README" link, which appears beneath the line with the Git URL.
8. On the next screen, you'll see some short text in the window pane. Scroll down and click the green "Commit new file" button".
9. Now, open a new command line window.

  - On Windows, open `PowerShell`.
  - On Mac, open `Terminal`.
  - On Linux, open `Terminal`.

10. `cd` to the directory where you want to store the local copy of your Git repository.
11. Type `git clone`, then paste your the Git URL into the terminal, and hit `Enter`. You'll see some stuff happen:

![Cloning from Git Remote to Local](git-clone.png)

12. Voilà! You've cloned your remote-native Git repository to your local computer. You can `cd` down into the repository and run an `ls` to see what's there:

![Inspecting Git repo contents](inspect-repo.png)

As you can see, our local repository has the `README.md` file we created earlier.

##### Creating a Local Git Repository

We just cloned a remote copy of a Git repository to our local machine. If we don't have a new project already set up, we can start from our local machine instead.

To start a new Git repository on your local machine,

1. Open a terminal window and `cd` to the location where you'd like to create a Git repository.
2. Create a new directory using `mkdir <name of your new folder>`.
3. `cd` into your new directory.
4. Type `git init -b main` and hit `Enter`:

![Git init](git-init.png)

We've turned our new folder `git-test` into a new Git repository, and we've given it a branch (via that `-b` flag) named `main`. More on branches in just a bit.

#### Staging Your Changes

After you've created a new Git repository via `git init`, you need to add some content to the repository before making your first "commit," which essentially saves a snapshot of your Git repository at a given moment in time. Here, I'm going to use the Mac Terminal's `touch <file-name.extension>` command to create a new dummy file (PowerShell users can enter the `New-File <file-name.extension>` command):

![Touch a New File](touch-file.png)

Our `ls` confirms the new file has been created.

Now, we're (almost) ready to commit our work. Unlike in other programs you may be used to, Git "stages" changes before committing them. There's a good reason for that, but I won't get into it here.

To stage your changes, simply run

```sh
git add .
```
The `.` is a shorthand which means "all". Here, that means stage all files that have been changed. If you'd prefer, you can also stage files individually, like so:

```
git add README.md
```

The terminal won't print a confirmation after you stage your content. However, you can run the `git status` command to check if files have been staged. Files listed in green have been staged; files listed in red have not. Here are the results of running `git status` before and staging our file:

![Git staging](git-add.png)

#### Committing Your Contents

Finally, we're now ready to commit our changes. To commit your changes, you will run `git commit -m "some message"`, replacing "some message" with a meaningful description of the changes reflected in this commit. Don't skimp on the message! You may need to use find this commit later, and the message will help you know what this commit captures.

After you hit `Enter`, Git will display a summary of your committed changes.

![git commit](git-commit.png)

To see our most recent commits, you can run `git log` to see your most recent changes, beginning with your latest commit. I've made a few additional commits here for demonstration purposes.

![git log](git-log.png)

That long string of letters and numbers is the "commit hash." Each commit hash is unique. It's what we'll use if we ever need to "roll back" our contents to match the state of the repository reflected in the commit hash.

#### Moving Your Local Git Repository to GitHub

If you've initiated your Git repository on your local machine and you've made at least one commit, you're ready to connect your local Git repository to a remote Git storage system like GitHub.

To do so,

1. Navigate to GitHub and sign-in to your account if necessary. 
   
2.  Click the `+` in the upper-right corner, and select "New repository" from the dropdown.

![Create a repository](repo-create.png)

3. Add a repository name and click the green "Create repository" button. While not strictly required, **it is a very good idea to match this name to the name of your local Git repository.**

4. On the next page, copy the Git URL

5. Switch over to your terminal window.

6. If necessary, `cd` into your local Git repository.
   
7. Enter `git remote add origin`, paste your GitHub URL, and hit `Enter`.
   
8. Verify the connection by entering `git remote -v`. Both the `fetch` and `push` URLs should match the URL you just entered.

![git remote add origin](git-remote-add-origin.png)

### Git Branches

The last major thing I'll discuss in this introduction is what branching is and how it affects how you'll use Git.

Branches are a feature of distributed version control that allow you to store multiple versions of the same Git repository. This allows each developer to work on their own branch before merging their contributions to another branch designated by a team as the primary branch. Nor are you restricted to one branch per person. You might want to perform your testing on a `test` branch, draft your documentation on a `docs-draft` branch, and your save your polished code on a `feature` branch. The names can be whatever they want. However, a developer team may have a "branching strategy" that guides how branches are named and how they interact with one another.

#### Adding a New Branch

A few steps ago, we created our first branch when we initiated a Git repository. The command we used was `git init -b main`. You will use a different Git command for creating subsequent new branches.

There are a few ways of creating new branches, but the one I like most is `git checkout -b <branch-name>`. This step combines two steps: it creates a new branch and changes your working branch to the new branch. You can confirm which branch you are on my entering `git branch`. The following image demonstrates what `git branch` shows before and after running `git checkout -b <branch-name>`.

![git checkout](git-checkout.png)

While Git prints a message after running `git checkout`, you should run `git branch` regularly to ensure you're working on your intended branch.

#### Switching to an Existing Local Branch

While `git checkout -b <branch>` is nice for switching to a new branch, sometimes you'll need to switch to a different branch you previously created. This one is pretty straightforward: use `git switch <existing-branch-name>.

If you can't remember the existing branch name, you can always run a `git branch` to double-check the existing local branches.

#### Pushing a Local Branch to Remote

It's a good practice to send your local branch changes to the remote at least periodically. To do so, after staging and committing your changes, all you need to do is run `git push`. 

#### Getting All Remote Branches on Your Local Repository

Especially when working with collaborators, you will find that your remote repository eventually contains more branches than your local repository. 

Getting all the remote branches and their updates is a bit complicated. You can copy the commands below:

```sh
git branch -r | grep -v '\->' | sed "s,\x1B\[[0-9;]*[a-zA-Z],,g" | while read remote; do git branch --track "${remote#origin/}" "$remote"; done
git fetch --all
git pull --all
```

## Git Cheat Sheet

`git add <. or filename.extension>`

  - Stages your change(s) prior to a commit.

`git commit -m <"commit message">`

  - Commits your changes. `-m` flag + `"commit message"` used to explain what the commit involves.

`git remote add origin <GitHub URL>`

  - Establishes remote Git repository connection for repositories created locally.

`git remote -v`

  - Prints the `fetch` and `push` URLs of the remote Git repository (e.g., GitHub). 

`git fetch`

  - Retrieves the latest metadata from the remote branch. Does NOT change the codebase on the local Git repository.

`git pull`

  - Retrieves the latest metadata from the remote branch AND updates the codebase in the local working branch.

`git push`

  - When a connection to remote has been established and at least one new commit has been made, transmits commit contents and metadata to remote Git repository.

`git checkout -b <branch-name>`

  - Creates a new branch and switches the working branch to it.

`git switch <branch-name>`

  - Changes the working branch.

`git branch`

  - Prints all local branches and identifies the working branch with a `*`.

`git branch -vv`

  - Prints all local branches alongside each branch's most recent commit details (shortform commit hash and commit message). Identifies the working branch with a `*`.

`git branch -a`

  - Prints all local AND remote branches. Identifies the local working branch with a `*`.

`git log`

  - Prints details for the last three commits, including the commit hash, commit author, and the timestamp of the commit.




