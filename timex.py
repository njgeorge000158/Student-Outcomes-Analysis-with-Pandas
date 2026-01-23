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
 #  return_future_date_string
 #
 #  return_normalized_date_index
 #  return_normalized_series_list_as_dataframe
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  04/11/2024      Initial Development                     Nicholas J. George
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
 #  string  date_string     The parameter is the date.
 #  integer days_integer    The parameter is the number of days
 #  string  date_format_string
 #                          The parameter is the date format.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_prior_date_days \
        (date_string, 
         days_integer = 365, 
         date_format_string = '%Y-%m-%d'):

    current_date = dt.strptime(date_string, date_format_string)

    prior_date = current_date.date() - timedelta(days = days_integer)

    prior_date_string = dt.strftime(prior_date, date_format_string)


    return prior_date_string


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
 #  string  date_string     The parameter is the date.
 #  integer days_integer    The parameter is the number of days
 #  string  date_format_string
 #                          The parameter is the date format.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_future_date_days \
        (date_string, 
         days_integer, 
         date_format_string = '%Y-%m-%d'):

    current_date = dt.strptime(date_string, date_format_string)

    future_date = current_date.date() + timedelta(days = days_integer)

    future_date_string = dt.strftime(prior_date, date_format_string)


    return future_date_string


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
 #                          The parameter is an input series list of date strings 
 #                          with the format, yyyy-mm-dd.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_normalized_date_index(input_series_list):

    sorted_series_list = sorted(input_series_list, key = len)


    for index, series in enumerate(sorted_series_list):

        index_string_list = [ele[5:] for ele in series.index.tolist()]

        if index >= 1:

            temp_index_list = [ele for ele in temp_index_list if ele in index_string_list]

        else:

            temp_index_list = index_string_list 


    return temp_index_list


# In[5]:


#*******************************************************************************************
 #
 #  Function Name:  return_normalized_series_list_as_dataframe
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
 #                          The parameter is a input series list.
 #  list    omit_index_integer_list
 #                          The parameter is the list of omitted series list indices.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_normalized_series_list_as_dataframe \
        (input_series_list,
         omit_index_integer_list = None):

    current_series_list = input_series_list.copy()

    if omit_index_integer_list != None:

        current_series_list \
            = [ele for i, ele in enumerate(current_series_list) if i not in omit_index_integer_list]


    normalized_index_string_list = return_normalized_date_index(current_series_list)

    normalized_series_list = []


    for index, series in enumerate(current_series_list):

        index_string_list = [ele[5:] for ele in current_series_list[index].index.tolist()]

        current_series_list[index] = current_series_list[index].set_axis(index_string_list)


        temp_string_list = []

        for i, element in enumerate(current_series_list[index]):

            if str(current_series_list[index].index[i]) in normalized_index_string_list:

                temp_string_list.append(element)


        normalized_series = pd.Series(temp_string_list, index = normalized_index_string_list)

        normalized_series.name = current_series_list[index].name

        normalized_series_list.append(normalized_series)


    normalized_dataframe = pd.DataFrame(normalized_series_list).transpose()

    return normalized_dataframe


# In[ ]:




