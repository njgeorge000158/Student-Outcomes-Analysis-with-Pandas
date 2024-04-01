![1680105043870](https://github.com/njgeorge000158/Student-Outcomes-Analysis-in-Jupyter-Notebook/assets/137228821/bf8bce8b-3e80-40e6-a16a-7e0514455542)

----

# PyCitySchools Analysis

----

As the Chief Data Scientist for the city’s school district, I analyzed district-wide standardized test results as well as other information to understand trends in school performance.  Although the data was sufficient to establish a picture of the current situation, it also produced additional questions regarding its underlying reasons.  The following trends summarize my conclusions.

-	More spending per student does not translate into better performance, especially in math (Table 10.1).

-	Charter schools significantly outperform district schools (Table 13.1).  

-	Small and medium schools are comparable in performance with large schools falling behind (Table 12.1).

-	Test scores and passing rates for math and reading do not vary much between grades for any one school possibly implying consistency in student outcomes (Table 8.2.1 and Table 8.3.1).

-	Mean and median scores are not significantly different for each school suggesting a symmetrical distribution of scores and passage rates (Table 8.2.3 and Table 8.3.3).

An cursory examination of the school district’s summary yielded useful insights: its 15 high schools have an annual total operating budget of \$24.7 million for their mission to educate 39,000 students; average test scores range from 79 to 82, and average passing rates fall between 75\% to 85\%.  While there is certainly room for improvement, these metrics are not as significant when one sees the discrepancy of an overall passage rate of 65\%: this inconsistency led me to take a closer look at the data.

The two types of high schools in this school district cannot be more different.  Out of its 15 schools, seven are district and eight are charter.  In this analysis, I weigh per student spending more heavily than total budget, and this approach reveals contrasting circumstances:  the district high schools' average \$644 per capita outlay, above the district wide average of \$633, dwarfs the charter schools’ average expenditure per capita of \$600.  Moreover, school size is also a distinctive consideration: all seven district schools are large while there are one large, five medium, and two small charter schools.  In terms of academic performance, a sorting of the school summary dataset based on overall passing rates reveals the five highest-performing schools to be all charter and the five lowest-performing schools to be all district.  Further examination conveys even more alarming news: all passing rates for charter schools exceed 90\% while district school passing rates lag significantly behind with the overall rate at 65\%.

There are two notable observations from the test scores and passage rates by grade for each high school: variations are remarkably small for all schools; and the difference between mean and median values is, for the most part, negligible.  Unchanging scores can indicate that, from one grade to another, each high school has a group of students who previously passed exams then fail them only to have another group of students approximately equal in number who previously failed exams pass them: this hypothetical situation is highly unlikely.  It is far more plausible that students who are successful in ninth grade are consistently successful for the next three grades and vice versa.  Although the reasons are unclear, these conditions can signify that school practices have led to consistency in student performance.  For all schools, the close mean and median values for scores and passing rates suggest symmetrical distributions; this occurrence coupled with the relatively unchanging scores and passing rates is unusual and suggests that the datasets may be artificial, even, computer generated.

In conclusion, the school district includes seven large district high schools and eight smaller charter high schools.  Despite higher per capita spending, the district schools trail behind the charter schools in performance and bring down the district-wide averages for test scores and passing rates.  Thus, this disparity in school performance is a catalyst for further investigation.  Although there are many possibilities, the culprit is likely either district and school practices, social problems, or a combination of both.  As such, I suggest an additional study to root out the fundamental causes behind these conclusions.

----

## Copyright

Nicholas J. George © 2023. All Rights Reserved.
