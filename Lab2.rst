Lab 2 Write-up
==============

1. Explain the major differences between TDD and BDD

Test-driven development is straight up code test, code system.  The volume of code required pretty much ensures that TDD will be written by developers, or maybe business analysts.  I believe tests are also typically written in the same language as the software, but this isn’t a necessity for black-box testing.
Behavior-driven development uses job stories rather than user stories.  In python behave, it also uses a natural language syntax to describe features and scenarios.  This makes BDD a little easier for a lay-person to comprehend, but at the cost of a degree of ambiguity.  The test files are also a bit more spread out than TDD, which tends to be more compact.

2. What is a mixin, what challenges can occur when testing them? What order are they initialized in?

A mixin is the pythonic way of specifying multiple inheritence.  Mixins typically provide small, isolated units of functionality that can be tacked on an existing class.

3. In python what does "super" do?

super accesses a python class’s base class.  It allows you to refer to the base class without having to specify its name.

4. Was there any job stories that did not meet the criteria we discussed in class? How did you handle this case?

Some were less than explicit.  Take, for instance, TDD Round 1.3 - “When interfacing with the system I want “X” to quit the program so I can stop this charade.”  Neither “X” nor any system interface had yet been described, so this comes out of nowhere.  Also BDD Round 1.2 - “When researching speeds I want to be able to select an estimated speed so I can see whether the network or driving would be faster.”  Not only does this not specify whether the selected value is estimated driving or network speed, it includes a second requirement, of comparing the results.

5. Which model did you find most challenging? Why?

BDD was more challenging, but simply because I had done TDD in the past.  Using the natural language, and the additional files, took more effort as well.

6. Which model did you find easiest to update/maintain?

I think the BDD was easier to update/maintain.  The purpose of the test is certainly more descriptive without adding comments.  I think that BDD would also take an initial/ongoing investment of time to organize the feature/step files cleanly.

7. How did you test that logging occurred only when desired?

Looking back over my code, I’m not sure I implemented logging in that way.