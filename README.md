![city_schools](https://github.com/njgeorge000158/Student-Outcomes-Analysis-with-Pandas/assets/137228821/2b8ccf0f-f02d-4b5f-a08b-bcf55dc9f06d)

----

# PyCitySchools Analysis

----

As the chief data scientist for the city’s school district, I analyzed high school standardized test results as well as other information to understand trends in school performance.  Although the data was sufficient to establish a picture of the current situation, it also produced additional questions regarding the underlying reasons for various conclusions.

An cursory examination of the school district’s summary yielded useful insights: its 15 high schools have an annual total operating budget of \$24.7 million for their mission to educate 39,000 students; average test scores range from 79 to 82; and average passing rates fall between 75\% to 85\%.  While there is certainly room for improvement, these metrics did not explain the 65\% overall passage rate, leading me to take a closer look at the data.

The two types of district high schools cannot be more different.  Out of its 15 schools, seven are district and eight are public.  In this analysis, I weigh per student spending more heavily than total budget, and this approach reveals contrasting circumstances:  the public high schools' average \$644 per capita outlay, above the district wide average of \$633, dwarfs the charter schools’ average expenditure per capita of \$600.  Moreover, all seven public schools are large while there are one large, five medium, and two small charter schools.  In terms of academic performance, the five highest-performing schools are all charter and the five lowest-performing schools are all public.  Further examination conveys even more alarming news: passing rates for charter schools exceed 90\% while public school passing rates lag significantly at 65\%.

There are two notable observations from the test scores and passage rates by grade for each high school. Variations are remarkably small for all schools, and the difference between mean and median values is, for the most part, negligible.  Unchanging scores can indicate that, from one grade to another, each high school has a group of students who previously passed exams then fail them only to have another group of students approximately equal in number who previously failed exams pass them, a highly improbable hypothetical situation.  It is far more plausible that students who are successful in ninth grade are consistently successful for the next three grades and vice versa.  Although the reasons are unclear, these conditions can signify that school practices have led to consistency in student performance.  For all schools, the close mean and median values for scores and passing rates suggest symmetrical distributions; this occurrence coupled with the relatively unchanging scores and passing rates is unusual and suggests that the datasets may be artificial, even, computer generated.

In summary, I established the existence of several trends: despite higher per capita spending, the public schools trail behind charter schools in performance and lower the district-wide averages for test scores and passing rates; more spending per student does not translate into better performance, especially in math (Table 10.1); small and medium-sized schools are comparable in performance, yet large schools are lagging (Table 12.1); test scores and passing rates for math and reading do not vary much between grades for any one school possibly implying consistency in student outcomes (Table 8.2.1 and Table 8.3.1); mean and median scores are not significantly different for each school suggesting a symmetrical distribution of scores and passage rates (Table 8.2.3 and Table 8.3.3).  Although there are many possible reasons for these observations, the culprit is likely either public school practices, social problems, or a combination of both.  As such, I suggest additional studies to root out the fundamental causes behind these conclusions.

----

## Copyright

Nicholas J. George © 2023. All Rights Reserved.
