Lab 5 Write-up
==============

1. What was the hardest part of this lab?

The Fibonacci generator thread bit me hard. A big reason why this was such a disaster was the cost of time in waiting for my test to evaluate.  I knew going in to the test that the 1000th digit would take a while to compute.  Through testing in isolation I knew it was going to take at least 30 seconds.  The test also completed in isolation.  But through nose it was taking a long time. So I waited.

It took me a very long time to realize what was happening.  An earlier test stopped the generator thread.  Once the generator is stopped, there isn't an easy way to reset the threading event that stopped it.  Then, in my Fibonacci test, I looped until it returned something other than the processing messages.  But, of course, since the thread was not running, the 1000th digit was never reached.  AFter I changed tearDown to better clean up my threads, the tests passed.

I also had a lot of trouble debugging the results of one of my tests. It was throwing an exception because I was trying to access __stopEvent, the old name for _stopEvent. pyTona's execution, however, returns an exception like "Passed too many arguments!".  So I searched high and low for where I could be passing too many parameters, or where a function was defined that accepted too few.

I also object some to writing 4 new answers.  It's difficult to invent new code in the context of the lab's system and under the
requirements of threading and 6 kinds of performance testing.

2. What is the difference between performance testing and performance measurement?

Performance testing is a category of testing that measures performance.  Each performance test measures a specific performance aspect and returns pass/fail.  A performance measurement could be a time limit on a function's completion, the maximum supported data size, or some other constraint on unit under test.  These constraints are usually found in the system's requirements.

3. What new bugs did you encounter with the new code?

I found that on occasion the retrieval method took longer than 5ms.

4. Did you mock anything to speed up performance testing? Do you see any issues with this?

No.  Aside from a few exceptions, mocking would seem to defeat the purpose of performance testing.  Mocks that fake a 1,000,000 user connection done poorly might not test correctly.  For instance, just setting the user count to 1,000,000 would be insufficient.  You would have to mock the actual simultaneous connection of a million users.  The actual user could be mocked though. 

5. Generate at least 5 performance measurement value sets and graphs (these sets must be worthwhile)

See file attached to lab submission.

6. Explain Load Testing, stress testing, endurance testing, spike testing configuration testing and isolation testing. How did you implement each of these?

**Load testing**
  The ability for the system to perform under a given load (typical, minimum, maximum).

I tested this for my weather prediction question, which rejected additional prediction models once 4 were processing already.

**Stress testing**
  Similar to load testing, typically with respect to hardware.

I tested this with my read_data function, where I started 10 other processes to write to disk while attempting to read a data file and maintain 10 characters per second.

**Endurance testing**
  This is the ability for a system to perform as specified over time.

I implemented this for my woodchuck test.  I included the requirement that my woodchuck would never tire. This means that it's wood chuck performance shall remain constant.  If it degrades over time, this would be a performance failure.

**Spike testing**
  The ability for the system to perform while certain conditions are spiking up and down.

I didn't really see a good opportunity to implement this.

**Configuration testing**
  The ability for the system to perform when the configuration is not as expected.

I tested this in my read_data function, where it returns 'Unknown' if data.txt is missing.

**Isolation testing**
  The ability for components of the system to perform alone.

I ran into this manually when I was testing the Fibonacci sequence generator.  It required me to change my test procedure.

7. How long did this lab take to accomplish?

About 12 hours.  The trickiest part was coming up with new QA's to meet the requirements of the lab.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| | **Issue Number:** 1                                                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| | **Brief:**                                                                                                                                                                                                                   |
| | Answer retrieval occassionally takes longer than 5ms                                                                                                                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| | **Steps to Reproduce:**                                                                                                                                                                                                      |
| | 1. Create a pyTona.main.Interface object.                                                                                                                                                                                    |
| | 2. Ask pyTona a new question.                                                                                                                                                                                                |
| | 3. Teach pyTona a new answer.                                                                                                                                                                                                |
| | 4. Get the current clock using time.clock().                                                                                                                                                                                 |
| | 5. Ask pyTona the new question.                                                                                                                                                                                              |
| | 6. Calculate elapsed = time.clock() - start                                                                                                                                                                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| | **Comments:**                                                                                                                                                                                                                |
| | OUTCOME: On occasion, elapsed is greater than 5ms.                                                                                                                                                                           |
| | EXPECTED: elapsed is always less than 5ms.                                                                                                                                                                                   |
| | I wrote an additional test to determine whether retrieval was affected by an answer's position in the list of answers.  It does not appear to be a factor.                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


