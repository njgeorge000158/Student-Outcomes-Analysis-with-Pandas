# **Student Outcomes Analysis with Pandas**

----

### **Installation:**

----

If the computer has Anaconda, Jupyter Notebook, and a recent version of Python, the IPython notebook already has the following dependencies installed: datetime, io, json, matplotlib, numpy, pandas, pathlib, os, pandas, requests, requests_html, and scipy.

In addition to those modules, the Jupyter Notebook requires the following to execute: holoviews, hvplot, geoviews, geopy, aspose-words, dataframe-image.

Here are the requisite Terminal commands for the installation of these peripheral modules:

python3 -m pip install holoviews

python3 -m pip install hvplot

python3 -m pip install geoviews

python3 -m pip install geopy

python3 -m pip install aspose-words

python3 -m pip install dataframe-image

----

### **Usage:**

----

The IPython notebook, city_schools_analysis.ipynb, uses the CSV files, schools_data.csv and students_data.csv, as input and will not run without them.  The interactive Python notebook must have the following Python scripts in the same folder with it:

city_schools_constants.py

error_handle_functions.py

log_functions.py

log_subroutines.py

pandas_process_functions.py

If the folders, resources and logs are not present, the IPython notebook will create them.  The folder, resources, holds input files for the IPython Notebook; the folder, logs, contains log files from testing the IPython Notebook; and the folder, images, has the PNG image files of the IPython Notebook's tables and plots.

To place the IPython notebook in Log Mode or Image Mode set the parameter for the appropriate subroutine in coding cell #2 to True. In Log Mode, the notebook sends log information to a log file. If the program is in Image Mode, it writes all DataFrames, hvplot maps, and matplotlib plots to PNG files in the Images Folder.

----

### **Resource Summary:**

----

#### Source code

city_schools_analysis.ipynb, city_schools_constants.py, error_handle_functions.py, log_constants.py, log_functions.py, log_subroutines.py, pandas_process_functions.py

#### Input files

schools_data.csv, students_data.csv

#### Output files

n/a

#### SQL script

n/a

#### Software

Jupyter Notebook, Pandas, Python 3.11.4

![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

----

### **GitHub Repository Branches:**

----

#### main branch

|&rarr; [./city_schools_analysis.ipynb](./city_schools_analysis.ipynb)

|&rarr; [./city_schools_constants.py](./city_schools_constants.py)

|&rarr; [./error_handle_functions.py](./error_handle_functions.py)

|&rarr; [./log_constants.py](./log_constants.py)

|&rarr; [./log_functions.py](./log_functions.py)

|&rarr; [./log_subroutines.py](./log_subroutines.py)

|&rarr; [./pandas_process_functions.py](./pandas_process_functions.py)

|&rarr; [./README.TECHNICAL.md](./README.TECHNICAL.md)

|&rarr; [./README.md](./README.md)

|&rarr; [./table-of-contents.md](./table-of-contents.md)

|&rarr; [./images/](./images/)

  &emsp; |&rarr; [./images/city_schools_analysisTable12CompleteSchoolDataSet.png](./images/city_schools_analysisTable12CompleteSchoolDataSet.png)
  
  &emsp; |&rarr; [./images/city_schools_analysisTable23SchoolDistrictMetrics.png](./images/city_schools_analysisTable23SchoolDistrictMetrics.png)
  
  &emsp; |&rarr; [./images/city_schools_analysisTable33SchoolMetrics.png](./images/city_schools_analysisTable33SchoolMetrics.png)
  
  &emsp; |&rarr; [./images/city_schools_analysisTable41HighestPerformingSchools.png](./images/city_schools_analysisTable41HighestPerformingSchools.png)
  
  &emsp; |&rarr; [./images/city_schools_analysisTable42LowestPerformingSchools.png](./images/city_schools_analysisTable42LowestPerformingSchools.png)
  
  &emsp; |&rarr; [./images/city_schools_analysisTable62SchoolMetricswithSpendingRanges.png](./images/city_schools_analysisTable62SchoolMetricswithSpendingRanges.png)
  
  &emsp; |&rarr; [./images/city_schools_analysisTable74TestScoresPassingRatesMeanbySpendingRanges.png](./images/city_schools_analysisTable74TestScoresPassingRatesMeanbySpendingRanges.png)
  
  &emsp; |&rarr; [./images/city_schools_analysisTable75TestScoresPassingRatesMedianbySpendingRanges.png](./images/city_schools_analysisTable75TestScoresPassingRatesMedianbySpendingRanges.png)

  &emsp; |&rarr; [./images/city_schools_analysisTable76TestScoresPassingRatesMeanMedianbySpendingRanges.png](./images/city_schools_analysisTable76TestScoresPassingRatesMeanMedianbySpendingRanges.png)
  
  &emsp; |&rarr; [./images/city_schools_analysisTable82SchoolMetricswithSchoolSizeCategories.png](./images/city_schools_analysisTable82SchoolMetricswithSchoolSizeCategories.png)
  
  &emsp; |&rarr; [./images/city_schools_analysisTable94FinancialMetricsbySchoolSizeMean.png](./images/city_schools_analysisTable94FinancialMetricsbySchoolSizeMean.png)
  
  &emsp; |&rarr; [./images/city_schools_analysisTable95FinancialMetricsbySchoolSizeMedian.png](./images/city_schools_analysisTable95FinancialMetricsbySchoolSizeMedian.png)

  &emsp; |&rarr; [./images/city_schools_analysisTable96FinancialMetricsbySchoolSizeMeanMedian.png](./images/city_schools_analysisTable96FinancialMetricsbySchoolSizeMeanMedian.png)
  
  &emsp; |&rarr; [./images/city_schools_analysisTable104TestScoresPassingRatesMeanbySchoolSize.png](./images/city_schools_analysisTable104TestScoresPassingRatesMeanbySchoolSize.png)

  &emsp; |&rarr; [./images/city_schools_analysisTable105TestScoresPassingRatesMedianbySchoolSize.png](./images/city_schools_analysisTable105TestScoresPassingRatesMedianbySchoolSize.png)
  
  &emsp; |&rarr; [./images/city_schools_analysisTable106TestScoresPassingRatesMeanMedianbySchoolSize.png](./images/city_schools_analysisTable106TestScoresPassingRatesMeanMedianbySchoolSize.png)
  
  &emsp; |&rarr; [./images/city_schools_analysisTable114FinancialMetricsbySchoolTypeMean.png](./images/city_schools_analysisTable114FinancialMetricsbySchoolTypeMean.png)
  
  &emsp; |&rarr; [./images/city_schools_analysisTable115FinancialMetricsbySchoolTypeMedian.png](./images/city_schools_analysisTable115FinancialMetricsbySchoolTypeMedian.png)
  
  &emsp; |&rarr; [./images/city_schools_analysisTable116FinancialMetricsbySchoolTypeMeanMedian.png](./images/city_schools_analysisTable116FinancialMetricsbySchoolTypeMeanMedian.png)
  
  &emsp; |&rarr; [./images/city_schools_analysisTable124DisplayTestScoresPassingRatesMeanbySchoolType.png](./images/city_schools_analysisTable124DisplayTestScoresPassingRatesMeanbySchoolType.png)

  &emsp; |&rarr; [./images/city_schools_analysisTable124DisplayTestScoresPassingRatesMeanbySchoolType.png](./images/city_schools_analysisTable124DisplayTestScoresPassingRatesMeanbySchoolType.png)
  
  &emsp; |&rarr; [./images/city_schools_analysisTable125DisplayTestScoresPassingRatesMedianbySchoolType.png](./images/city_schools_analysisTable125DisplayTestScoresPassingRatesMedianbySchoolType.png)
  
  &emsp; |&rarr; [./images/city_schools_analysisTable126DisplayTestScoresPassingRatesMeanMedianbySchoolType.png](./images/city_schools_analysisTable126DisplayTestScoresPassingRatesMeanMedianbySchoolType.png)

  &emsp; |&rarr; [./images/city_schools_analysisTable521MathScoresMeanbyGrade.png](./images/city_schools_analysisTable521MathScoresMeanbyGrade.png)

  &emsp; |&rarr; [./images/city_schools_analysisTable522MathScoresMedianbyGrade.png](./images/city_schools_analysisTable522MathScoresMedianbyGrade.png)

  &emsp; |&rarr; [./images/city_schools_analysisTable523MathScoresMeanMedianbyGrade.png](./images/city_schools_analysisTable523MathScoresMeanMedianbyGrade.png)

  &emsp; |&rarr; [./images/city_schools_analysisTable531ReadingScoresMeanbyGrade.png](./images/city_schools_analysisTable531ReadingScoresMeanbyGrade.png)

  &emsp; |&rarr; [./images/city_schools_analysisTable532ReadingScoresMedianbyGrade.png](./images/city_schools_analysisTable532ReadingScoresMedianbyGrade.png)

  &emsp; |&rarr; [./images/city_schools_analysisTable533ReadingScoresMeanMedianbyGrade.png](./images/city_schools_analysisTable533ReadingScoresMeanMedianbyGrade.png)
 
  &emsp; |&rarr; [./images/README.md](./images/README.md)

|&rarr; [./logs/](./logs/)

  &emsp; |&rarr; [./logs/20240401city_schools_analysis_log.txt](./logs/20240401city_schools_analysis_log.txt)

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
