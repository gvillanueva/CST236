Lab 1 Write-up 
==============

What was the hardest part of this lab?
--------------------------------------

The hardest part of this lab for me was getting failed tests to abort a commit.  I strong-armed a few possibilities and had to undo a few test commits before I got it working.  I was trying to find “FAILED” within stdout, but it turned out it was actually in stderr.  It took me a while before I thought of possibility.

During the course of this lab, why did we exclude .pyc files?
-------------------------------------------------------------

We exclude .pyc files because they are binary files, and binary files cause problems for git repositories.

Name three files which would likely need to have a gitignore added?
-------------------------------------------------------------------

Three other files which would likely need a .gitignore line are object files (.o), file-based databases like SQLite (.db), and libraries (.lib/.dll)

What is a pyunit TestCase?
--------------------------

A TestCase is a class that inherits from the pyunit TestCase base class.  It groups test steps which test units of the source code.  A successful test provide the expected output for a given input(s).  In order for a test step to be run automatically, it needs to be a function with a name starting with "test``_``".

What is the difference between a git cherry pick and a rebase?
--------------------------------------------------------------

A rebase operation replays all changes from a branch into its upstream, and it changes the branch base to the tip of the upstream.  This makes it appear as though all work occurred on the same branch.  A cherry pick merges one or more change(s) from a branch and does not affect the source branch’s history.

How could you use git to output just the author name of a given file for the current version of the repo?
------------------------------------------------------------------------------------------------------------

git log --format=format:%an -- <filename>

During this lab did you explore Tortoise Git or GIT Extensions? If not take a look at them, they probably would be useful for the remainder of the class.
---------------------------------------------------------------------------------------------------------------------------------------------------------

I have not explored them yet.  For the lab I used git within bash on Chrubuntu.

Did you find the second issue in get_triangle_type? Did you choose to test the code as is or fix the code in get_triangle_type.
-------------------------------------------------------------------------------------------------------------------------------

I did find the second issue in get_triangle_type.  I chose to fix the code in get_triangle type since its original form did not reflect the apparent intent of a, based on the len(a) == 3 conditional.
