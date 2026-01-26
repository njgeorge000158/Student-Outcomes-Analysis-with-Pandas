#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  pymaceuticalsx.py
 #
 #  File Description:
 #      This Python script, pymaceuticalsx.py, contains generic Python subroutines 
 #      for completing common tasks in the Pymaceuticals animal study.  Here is the list:
 #
 #      display_tumor_volume_statistics
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  08/20/2023      Initial Development                     Nicholas J. George
 #
 #******************************************************************************************/

import logx
import pandasx

import dataframe_image


# In[2]:


CONSTANT_LOCAL_FILE_NAME = 'pymaceuticalsx.py'


# In[3]:


#*******************************************************************************************
 #
 #  Subroutine Name:  display_tumor_volume_statistics
 #
 #  Subroutine Description:
 #      This subroutine calculates and displays summary statistics for each drug.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  list    tumor_volume_series_list
 #                          The parameter is the list of tumor volume series 
 #                          for each drug regimen.
 #  list    regimen_string_list
 #                          The parameter is the list of drug regimen names.
 #  string  section_name_string
 #                          The parameter is the section name.
 #  string  type_string     The parameter is the statistics type.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/19/2023           Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def display_tumor_volume_statistics \
        (tumor_volume_series_list,
         regimen_string_list,
         section_name_string,
         type_string):

    for index, regimen in enumerate(regimen_string_list):

        statistics_dataframe \
            = pandasx.return_summary_statistics_as_dataframe \
                (tumor_volume_series_list[index])

        caption_string \
            = 'Table ' \
              + section_name_string \
              + f'.{index+1}: ' \
              + type_string \
              + f' Statistics for {regimen}'

        current_styler_object \
            = pandasx.return_standard_format_styler \
                (statistics_dataframe, caption_string)

        current_styler_object \
            = pandasx.save_image_and_return_styler \
                (current_styler_object, caption_string)


        display(current_styler_object)


# In[ ]:




