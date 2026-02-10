#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  timex
 #
 #  File Description:
 #      This Python script, timex.py, contains generic Python functions for manipulating 
 #      dates and times.  Here is the list:
 #
 #  return_prior_date_days
 #  return_future_date
 #
 #  return_normalized_date_index
 #  return_normalized_series_list_as_df
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  04/11/2024      Initial Development                     Nicholas J. George
 #  02/09/2026      Abbreviated variable names              Nicholas J. George
 #
 #******************************************************************************************/

import pandas as pd

from datetime import datetime as dt
from datetime import timedelta

pd.options.mode.chained_assignment = None


# In[2]:


#*******************************************************************************************
 #
 #  Function Name:  return_prior_date_days
 #
 #  Function Description:
 #      This function returns the prior date based on the number of days.
 #
 #
 #  Return Type: string
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  string  date            The parameter is the date.
 #  integer days_int        The parameter is the number of days
 #  string  date_format     The parameter is the date format.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_prior_date_days \
        (date, 
         days_int = 365, 
         date_format = '%Y-%m-%d'):

    current_date = dt.strptime(date, date_format)

    prior_date = current_date.date() - timedelta(days = days_int)

    prior_date = dt.strftime(prior_date, date_format)


    return prior_date


# In[3]:


#*******************************************************************************************
 #
 #  Function Name:  return_future_date_days
 #
 #  Function Description:
 #      This function returns the future date based on the number of days.
 #
 #
 #  Return Type: string
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  string  date            The parameter is the date.
 #  integer days_int        The parameter is the number of days
 #  string  date_format     The parameter is the date format.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_future_date_days \
        (date, 
         days_int, 
         date_format = '%Y-%m-%d'):

    current_date = dt.strptime(date, date_format)

    future_date = current_date.date() + timedelta(days = days_int)

    future_date = dt.strftime(prior_date, date_format)


    return future_date


# In[4]:


#*******************************************************************************************
 #
 #  Function Name:  return_normalized_date_index
 #
 #  Function Description:
 #      This function returns a list of series where the all the series share 
 #      a common index.
 #
 #
 #  Return Type: list
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  list    input_series_list     
 #                          The parameter is the unsorted input series list 
 #                          of date strings with the format, yyyy-mm-dd.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_normalized_date_index(input_series_list):

    current_series_list = sorted(input_series_list, key = len)


    for i, series in enumerate(current_series_list):

        index_list = [x[5:] for x in series.index.tolist()]

        if i >= 1:

            temp_index_list = [x for x in temp_index_list if x in index_list]

        else:

            temp_index_list = index_list 


    return temp_index_list


# In[5]:


#*******************************************************************************************
 #
 #  Function Name:  return_normalized_series_list_as_df
 #
 #  Function Description:
 #      This function returns a dataframe from a series list normalized 
 #      from a common index with a date string format, yyyy-mm-dd.
 #
 #
 #  Return Type: styler
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  list    input_series_list     
 #                         The parameter is a input series list.
 #  list    omit_index_int_list
 #                          The parameter is the list of omitted series list indices.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_normalized_series_list_as_df \
        (input_series_list,
         omit_index_int_list = None):

    current_series_list = input_series_list.copy()

    if omit_index_int_list != None:

        current_series_list \
            = [x for i, x in enumerate(current_series_list) if i not in omit_index_int_list]


    normalized_index_list = return_normalized_date_index(current_series_list)

    normalized_series_list = []


    for index, series in enumerate(current_series_list):

        index_list = [x[5:] for x in current_series_list[index].index.tolist()]

        current_series_list[index] = current_series_list[index].set_axis(index_list)


        temp_list = []

        for j, x in enumerate(current_series_list[index]):

            if str(current_series_list[index].index[j]) in normalized_index_list:

                temp_list.append(x)


        normalized_series = pd.Series(temp_list, index = normalized_index_list)

        normalized_series.name = current_series_list[index].name

        normalized_series_list.append(normalized_series)


    return pd.DataFrame(normalized_series_list).transpose()


# In[ ]:




