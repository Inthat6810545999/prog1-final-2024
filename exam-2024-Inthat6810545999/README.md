[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/vpndk05z)
# 01219114/5 Laboratory Examination

Department of Computer Engineering \
Faculty of Engineering, Kasetsart University \
**THIS IS AN EXAMINATION**: all regulations regarding examinations apply \
FRI 06 DEC 2024 09:00-12:00 (*time shared with other parts*)

## Problem Author

This section (task) authored by Chawanat Nakasan.

Inquiries should be asked directly to the author.

## Friendly Reminder

The exam also has other parts. Don't forget to do all parts, beyond this one.

## Directions (meta)

1. There is only one task with multiple class files. Make sure to check ALL
   class files before starting your work.
2. It is necessary to work on the `Item` class in `item.py` first. Otherwise,
   it will be difficult to get graded in the other classes.
3. Implement classes and instructions as blanks are provided or as indicated
   by `TODO` or `pass` instructions. Don't forget to fix the method headers
   if necessary.
4. Type hints are considered correct but not necessarily complete. Also,
   compound types like `List` may sometimes lack the definition of what's
   inside (such as `List[Int]`), so inspect carefully as you work.
5. Doctests are provided but not part of grading. Feel free to use them
   creatively, add more, change them as you need. The provided doctests are
   correct but not necessarily complete. Again, modifying the doctests is
   completely OPTIONAL.
6. The grader is finicky. If your code passes the provided pytest file, then
   you can assume that you received the scores you need.
7. **IMPORTANT** Tag the final commit that you are about to submit as `v0.2`.
   In the command line, type `git tag v0.2` to tag. Type `git tag -d v0.2`
   if you want to delete tag. Remember that you must move to the correct
   commit first before tagging.

## IMPORTANT: AVOID OPENING HTML HELP!

* In Git, you SHOULD use `git <command> -h` to open in terminal. DO NOT USE
  ~~`git <command> --help`~~ as this WILL open a web browser AND MAY RESULT IN
  EXAM INTEGRITY TRIGGER! (At the time of writing the exam information page we
  did not include Git Online/HTML Help as a valid browser destination.)
* In Python, you should always use the internal help function `help()` to
  access help. Avoid using even the Python manual website if possible.

## Protected Files that must not be modified

You MUST NOT modify any of the following files.

1. main.py
2. exceptions.py
3. test_*.py (only those provided)
4. README.md

If you modified them, GitHub classroom will flag them. If you do not revert
the files back, your points will be deducted (see below in Repository Check).

## Repository Check (10 points)

Repository cleanliness and correctness is part of the examination.

Your repo starts with 6 points out of 10. The following factors will change
the score:

* (+1) Your user name is set to your real name.
* (+1) You have at least two commits.
* (+1) You have at least four commits. (Stacks with the above.)
* (+1) You tagged `v0.2` in the final commit to submit AND it is on `master`.
* (+2) For creating another branch AND merging it back into `master`.
* (-1) For each commit without a meaningful commit message.
* (-1) For each Protected File (above) you modified that you shouldn't.
* (-1) For each excess file.
* (-3) For not having exactly either `main` or `master` branch.
       You MUST have one, but not neither, and not both.

The template repo comes with `master` branch but you may choose to eliminate
it entirely and use `main` instead. Your choice.

Since you START WITH 6 points, you only have to do just 4 points' worth of
tasks to reach the maximum possible score.

To maintain a clean repo, you may modify the `.gitignore` file if you wish.

## Task Scoring (80 points)

There are 3 levels of subtasks in this examination, each successively harder
but also more rewarding.

* Level 1 (40p) tasks are the basics. Highly guided, individually tested, and
  have very clear doctest. Pytest file is given and autograded.
* Level 2 (20p) tasks are similar to Level 1 but less guided and clear.
  Doctests are less complete. Alternatively, they might have specific
  requirements like attribute privacy. Pytest file is not given.
* Level 3 (20p) tasks are more complex and you might encounter a blank sheet,
  like an entire class with just the instructions and the word `pass`. Or, they
  could be test about interaction between multiple classes. Good luck.

In case text of two levels seem to conflict or mention the same thing, if you
want a higher score, just follow the instruction of the harder level. For
example:

* Level 1: Implement f(x, y) where result is sum of both arguments
* Level 2: Implement f(x, y, z=0) where result is sum of all arguments

Doing Level 2 will mean Level 1 is satisfied and you will get scores for both.

## Pylint scoring (10 points)

Pylint is not part of autograding as it kinda sucks in GitHub Classroom. Just
run it locally on the latest version, and you can estimate score from that.

## Scoring Summary

 | No. | Score | Criteria                                                     |
 | --- | ----- | ------------------------------------------------------------ |
 |  1  |   10  | pylint (default settings, score = max(0,(pylintscore-5) * 2) |
 |  2  |   10  | Repository Correctness, see above                            |
 |  3  |   40  | Autograded Pytest (test\_1.py) (Level 1)                     |
 |  4  |   20  | (Manual) Level 2                                             |
 |  5  |   20  | (Manual) Level 3                                             |
 |     |  100  | Total                                                        |

## Story

In the fictional territory of Zaklusia, there is a strange convention where not
only people do a lot of work in the Mine, they also are engaged in the Craft.

The Craft is a very simple concept. It's just a magic where you draw a grid on
something like a table or floor, like a 3x3 grid, then place objects on it in
a specific pattern and hope it turns into something else.

In this task, you will implement Python classes that represent how the people
in the Mine should Craft things. The Craft is best practiced in the Mine,
therefore people in the Mine tend to Craft a lot there. While some people can
Mine and some people can Craft, people who both Mine and Craft tend to be the
most prosperous, wealthy, and successful, so yes, you should learn also to Mine
and Craft, or Craft in the Mine, or Mine as you Craft, or somehow put them
together and make it work.

In short, do You Craft, bro?

(Obviously this is NOT related to a blocky game of a similar name.)

## Hints

* Math is not difficult. If it's too difficult, you're probably messing up.
* Be very mindful of data types.
* Doctest is correct but not necessarily complete.
* You CAN implement try/except liberally. Unnecessary try/excepts do not deduct
  points.
* Use private attributes with @property for the best scores.
* Use getter/setter methods ONLY when told.
* You might want to cut comment lines and paste them where you can work
  conveniently, such as close to where you actually implement the method or
  class. The examiner already puts the comments with TODO where they should
  roughly be, but ultimately it's your decision.

## Corrections

If any changes are made to the protected files during the examination, we will
let you know and ask you to pull the changes using `git pull`. This is why you
SHOULD NOT modify the protected files.

Changes to the protected files made in this way will not be penalized.


## LICENSE

Due to the nature of the examination, this file is ALL RIGHTS RESERVED by the
author. Redistribution is NOT PERMITTED on fear of ACADEMIC DISHONESTY penalty
and INTELLECTUAL PROPERTY INFRINGEMENT legal action by Faculty of Engineering,
Kasetsart University.

Should there be updates or declassification of the exam material, there will be
a general notification given to you later. (Assume none.)