adass-proceedings
=================

Helpful tools to prepare and produce the ADASS proceedings, including
an ASCL index. First tried out for the 2012 proceedings, which took
place in Urbana, Nov 5-9.  Editors Friedel with ASCL contributions by
Allen & Teuben.

Formalized for the 2013 proceedings that took place in Kona, Sep 30-Oct 3.


INSTALLATION:
=============

   git clone https://github.com/teuben/adass-proceedings
   cd adass-proceedings
   ./configure
   source ap_start.csh

GIT:
====


Here's a super simple "git for dummies" (there are more advanced
(better?) ways to work with git, cloning, working on a branch, and
sending a pull request to the master etc.)

1) this will get you a new clean copy:

   git clone https://github.com/teuben/adass-proceedings

   and it will create a new subdirectory called 'ADASS'. If 
   you already had one, git will nicely complain.

2) this will get you the latest updates from the others:


   cd adass-proceedings
   git pull

3) make a change and give it back to the others.   Pick your favorite editor,
   and the -m flag is for those who don't want/need the editor at that stage.

   cd adass-proceedings
   edit README.md
   git add README.md
   git commit README.md
       -- or if you don't like your choice of unix editors (vi in particular)
   git commit -m "reasons of changes to file"  README.md
   git push


4.) if you have made changes to a file that has been changed upstream,
    a pull will fail. You will have to stash the file (git help stash)
    before you can pull the updated version down.

    If you have stashed a file that you no longer want, you apparently
    have to delete it before you can push the file you are currently
    working on.

5.) I have deleted a file, did a pull, and did not get the file; in this case, the file was README.md. 
    Peter suggested I type:

   git checkout -- README.md 
   
I then pulled again and got the file. 

6.) To set the alias so I don't have to type the whole path to the git comment, type:

   alias git=/usr/local/git/bin/git to 

   (that's for mac users who don't know how to set their $PATH)

7.) use :q! to get out of the editor when dumped into it 
    (if the editor is called 'vi')

8.) Can change editor to, for example, emacs with: 

   git config --global core.editor emacs

9.) git push will normally ask for a username/password, but some recommended practices Peter 
    found to set credentials (once) are:

   git config --global user.email teuben@gmail.com
   git config --global user.name "Peter Teuben"
   
   (which didn't seem to work for me all the time, and even when it does, 
    I get "error: git-credential-osxkeychain died of signal 11" message twice after a push, 
    but at least I don't have to type my user name and password!)

   Also useful: 
   
   git config --global credential.helper 'cache --timeout 3600'

10.) The most commonly used git commands are:
   add		Add file contents to the index
   bisect		Find by binary search the change that introduced a bug
   branch     	List, create, or delete branches
   checkout	Checkout a branch or paths to the working tree
   clone      	Clone a repository into a new directory
   commit     	Record changes to the repository
   diff       		Show changes between commits, commit and working tree, etc
   fetch      		Download objects and refs from another repository
   grep       		Print lines matching a pattern
   init       		Create an empty git repository or reinitialize an existing one
   log        		Show commit logs
   merge      	Join two or more development histories together
   mv         		Move or rename a file, a directory, or a symlink
   pull       		Fetch from and merge with another repository or a local branch
   push       	Update remote refs along with associated objects
   rebase     	Forward-port local commits to the updated upstream head
   reset      		Reset current HEAD to the specified state
   rm         		Remove files from the working tree and from the index
   show      		Show various types of objects
   status     		Show the working tree status
   tag        		Create, list, delete or verify a tag object signed with GPG

   
11.) When pushing, I get: 
push.default is unset; its implicit value is changing in
Git 2.0 from 'matching' to 'simple'. To squelch this message
and maintain the current behavior after the default changes, use:

  git config --global push.default matching

To squelch this message and adopt the new behavior now, use:

  git config --global push.default simple

See 'git help config' and search for 'push.default' for further information.
(the 'simple' mode was introduced in Git 1.7.11. Use the similar mode
'current' instead of 'simple' if you sometimes use older versions of Git)



   
