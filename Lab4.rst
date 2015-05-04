Lab 4 Write-up
==============

1. What observations did you make while performing the analysis on the system?

The code is pretty solid due to low CC and MI values.

Stage 2 addressed almost all problems with the original code. It is debatable, but #0017 may still be exceding the requirements. It adds a space between the converted value and 'miles', though this is not called for in the requirements.

Stage 2 also introduced a lot more pathways into the code that were not covered under my original tests.

2. What are the advantages/disadvantages of performing this analysis?

Analyzing test results build confidence, be it positive or negative, in the code. Without regular assessment, a tester is just guessing at the integrity of the software. It also expresses direction of development, up or down, and can aide estimation, scheduling, and other project management tasks.

3. What are the advantages of data mutation? Did you use any of these tools?

Data mutation helps ensure that your tests are capable of failure. Tests that cannot fail are worthless.  Data mutation changes the behavior of the function under test. If the FUT's behavior changes and your test still passes, this is a bad test. Your expected outcome is probably too broad, or you're not actually testing the function.

4. What did you use Mock for in this lab?

I used mock to fake the network server and traffic. Initially I used one class with fixed results for each call to _socketobject's methods. This tracks the ip, port, and message arguments to test requirement #0025. The class also returns a formatted string containing a list of users to test #0024/#0026. When I saw #0027, I simply subclassed my original mock class and altered the return value for recv to make it return None. 

5. How long did this lab take to complete?

About 5 hours. Mocking was a huge headache for me as I couldn't get it to behave. For a long time it seemed every member of the class I wanted to mock was itself a Mock instance. I couldn't assign to return_value and I ran in circles for a long time.