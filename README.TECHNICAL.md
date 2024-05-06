# **Student Outcomes Analysis with Pandas**

----

### **Installation:**

----

If the computer has Anaconda, Jupyter Notebook, and a recent version of Python, the IPython notebook already has the following dependencies installed: datetime, io, json, matplotlib, numpy, pandas, pathlib, os, pandas, requests, requests_html, and scipy.

In addition to those modules, the Jupyter Notebook requires the following to execute: holoviews, hvplot, geoviews, geopy, aspose-words, dataframe-image.

Here are the requisite Terminal commands for the installation of these peripheral modules:

pip3 install -U holoviews

pip3 install -U hvplot

pip3 install -U geoviews

pip3 install -U geopy

pip3 install -U aspose-words

pip3 install -U dataframe-image

----

### **Usage:**

----

The IPython notebook, city_schools.ipynb, uses the CSV files, schools_data.csv and students_data.csv, as input and will not run without them.  The interactive Python notebook must have the following Python scripts in the same folder with it:

logx.py

pandasx.py

timex.py

If the folders, resources and logs are not present, the IPython notebook will create them.  The folder, resources, holds input files for the IPython Notebook; the folder, logs, contains log files from testing the IPython Notebook; and the folder, images, has the PNG image files of the IPython Notebook's tables and plots.

To place the IPython notebook in Log Mode or Image Mode set the parameter for the appropriate subroutine in coding cell #2 to True. In Log Mode, the notebook writes log information to a log file in the folder, logs. If the program is in Image Mode, it writes all DataFrames, hvplot maps, and matplotlib plots to PNG files to the folder, images.

----

### **Resource Summary:**

----

#### Source code

city_schools.ipynb, logx.py, pandasx.py, timex.py

#### Input files

schools_data.csv, students_data.csv

#### Output files

n/a

#### SQL script

n/a

#### Software

Jupyter Notebook, Pandas, Python 3.11.5

![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

----

### **GitHub Repository Branches:**

----

#### main branch

|&rarr; [./city_schools_constants.py](./city_schools_constants.py)

|&rarr; [./README.TECHNICAL.md](./README.TECHNICAL.md)

|&rarr; [./README.md](./README.md)

|&rarr; [./table-of-contents.md](./table-of-contents.md)

|&rarr; [./images/](./images/)

  &emsp; |&rarr; [./images/city_schoolsTable12CompleteSchoolDataSet.png](./images/city_schoolsTable12CompleteSchoolDataSet.png)
  
  &emsp; |&rarr; [./images/city_schoolsTable23SchoolDistrictMetrics.png](./images/city_schoolsTable23SchoolDistrictMetrics.png)
  
  &emsp; |&rarr; [./images/city_schoolsTable33SchoolMetrics.png](./images/city_schoolsTable33SchoolMetrics.png)
  
  &emsp; |&rarr; [./images/city_schoolsTable41HighestPerformingSchools.png](./images/city_schoolsTable41HighestPerformingSchools.png)
  
  &emsp; |&rarr; [./images/city_schoolsTable42LowestPerformingSchools.png](./images/city_schoolsTable42LowestPerformingSchools.png)
  
  &emsp; |&rarr; [./images/city_schoolsTable62SchoolMetricswithSpendingRanges.png](./images/city_schoolsTable62SchoolMetricswithSpendingRanges.png)
  
  &emsp; |&rarr; [./images/city_schoolsTable74TestScoresPassingRatesMeanbySpendingRanges.png](./images/city_schoolsTable74TestScoresPassingRatesMeanbySpendingRanges.png)
  
  &emsp; |&rarr; [./images/city_schoolsTable75TestScoresPassingRatesMedianbySpendingRanges.png](./images/city_schoolsTable75TestScoresPassingRatesMedianbySpendingRanges.png)

  &emsp; |&rarr; [./images/city_schoolsTable76TestScoresPassingRatesMeanMedianbySpendingRanges.png](./images/city_schoolsTable76TestScoresPassingRatesMeanMedianbySpendingRanges.png)
  
  &emsp; |&rarr; [./images/city_schoolsTable82SchoolMetricswithSchoolSizeCategories.png](./images/city_schoolsTable82SchoolMetricswithSchoolSizeCategories.png)
  
  &emsp; |&rarr; [./images/city_schoolsTable94FinancialMetricsbySchoolSizeMean.png](./images/city_schoolsTable94FinancialMetricsbySchoolSizeMean.png)
  
  &emsp; |&rarr; [./images/city_schoolsTable95FinancialMetricsbySchoolSizeMedian.png](./images/city_schoolsTable95FinancialMetricsbySchoolSizeMedian.png)

  &emsp; |&rarr; [./images/city_schoolsTable96FinancialMetricsbySchoolSizeMeanMedian.png](./images/city_schoolsTable96FinancialMetricsbySchoolSizeMeanMedian.png)
  
  &emsp; |&rarr; [./images/city_schoolsTable104TestScoresPassingRatesMeanbySchoolSize.png](./images/city_schoolsTable104TestScoresPassingRatesMeanbySchoolSize.png)

  &emsp; |&rarr; [./images/city_schoolsTable105TestScoresPassingRatesMedianbySchoolSize.png](./images/city_schoolsTable105TestScoresPassingRatesMedianbySchoolSize.png)
  
  &emsp; |&rarr; [./images/city_schoolsTable106TestScoresPassingRatesMeanMedianbySchoolSize.png](./images/city_schoolsTable106TestScoresPassingRatesMeanMedianbySchoolSize.png)
  
  &emsp; |&rarr; [./images/city_schoolsTable114FinancialMetricsbySchoolTypeMean.png](./images/city_schoolsTable114FinancialMetricsbySchoolTypeMean.png)
  
  &emsp; |&rarr; [./images/city_schoolsTable115FinancialMetricsbySchoolTypeMedian.png](./images/city_schoolsTable115FinancialMetricsbySchoolTypeMedian.png)
  
  &emsp; |&rarr; [./images/city_schoolsTable116FinancialMetricsbySchoolTypeMeanMedian.png](./images/city_schoolsTable116FinancialMetricsbySchoolTypeMeanMedian.png)
  
  &emsp; |&rarr; [./images/city_schoolsTable124DisplayTestScoresPassingRatesMeanbySchoolType.png](./images/city_schoolsTable124DisplayTestScoresPassingRatesMeanbySchoolType.png)

  &emsp; |&rarr; [./images/city_schoolsTable124DisplayTestScoresPassingRatesMeanbySchoolType.png](./images/city_schoolsTable124DisplayTestScoresPassingRatesMeanbySchoolType.png)
  
  &emsp; |&rarr; [./images/city_schoolsTable125DisplayTestScoresPassingRatesMedianbySchoolType.png](./images/city_schoolsTable125DisplayTestScoresPassingRatesMedianbySchoolType.png)
  
  &emsp; |&rarr; [./images/city_schoolsTable126DisplayTestScoresPassingRatesMeanMedianbySchoolType.png](./images/city_schoolsTable126DisplayTestScoresPassingRatesMeanMedianbySchoolType.png)

  &emsp; |&rarr; [./images/city_schoolsTable521MathScoresMeanbyGrade.png](./images/city_schoolsTable521MathScoresMeanbyGrade.png)

  &emsp; |&rarr; [./images/city_schoolsTable522MathScoresMedianbyGrade.png](./images/city_schoolsTable522MathScoresMedianbyGrade.png)

  &emsp; |&rarr; [./images/city_schoolsTable523MathScoresMeanMedianbyGrade.png](./images/city_schoolsTable523MathScoresMeanMedianbyGrade.png)

  &emsp; |&rarr; [./images/city_schoolsTable531ReadingScoresMeanbyGrade.png](./images/city_schoolsTable531ReadingScoresMeanbyGrade.png)

  &emsp; |&rarr; [./images/city_schoolsTable532ReadingScoresMedianbyGrade.png](./images/city_schoolsTable532ReadingScoresMedianbyGrade.png)

  &emsp; |&rarr; [./images/city_schoolsTable533ReadingScoresMeanMedianbyGrade.png](./images/city_schoolsTable533ReadingScoresMeanMedianbyGrade.png)
 
  &emsp; |&rarr; [./images/README.md](./images/README.md)

|&rarr; [./logs/](./logs/)

  &emsp; |&rarr; [./logs/20240419city_schools_log.txt](./logs/20240419city_schools_log.txt)

  &emsp; |&rarr; [./logs/README.md](./logs/README.md)

|&rarr; [./resources/](./resources/)

  &emsp; |&rarr; [./resources/README.md](./resources/README.md)

  &emsp; |&rarr; [./resources/schools_data.csv](./resources/schools_data.csv)

  &emsp; |&rarr; [./resources/students_data.csv](./resources/students_data.csv)

----

### **References:**

----

[Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/en/stable/)

[Pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html)

[Python Documentation](https://docs.python.org/3/contents.html)

----

### **Authors and Acknowledgment:**

----

### Copyright

Nicholas J. George © 2023. All Rights Reserved.
