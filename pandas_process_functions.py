#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  pandas_process_functions.py
 #
 #  File Description:
 #      This Python script, pandas_process_functions.py, contains Python functions
 #      for processing Pandas data structures. Here is the list:
 #
 #      return_standard_format_styler
 #      save_image_and_return_styler
 #      return_formatted_table
 #      return_summary_statistics_as_dataframe
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  03/04/2024      Initial Development                     Nicholas J. George
 #
 #******************************************************************************************/

import error_handle_functions
import log_constants
import log_functions
import log_subroutines

import dataframe_image

import pandas as pd

pd.options.mode.chained_assignment = None


# In[2]:


CONSTANT_LOCAL_FILE_NAME = 'pandas_process_functions.py'


# In[3]:


#*******************************************************************************************
 #
 #  Function Name:  return_standard_format_styler
 #
 #  Function Description:
 #      This function returns a styler object in standard format from a dataframe.
 #
 #
 #  Return Type: styler
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  dataframe
 #          input_dataframe
 #                          The parameter is the input dataframe.
 #  string
 #          caption_string
 #                          The parameter is the table caption.
 #  integer
 #          precision_integer
 #                          This optional parameter is the decimal place 
 #                          precision of the displayed numbers.
 #  boolean
 #          hide_index_boolean
 #                          This optional parameter indicates whether the
 #                          index column is hidden or not.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  03/04/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_standard_format_styler \
        (input_dataframe,
         caption_string,
         precision_integer = 2,
         hide_index_boolean = True):
    
    try:
        
        error_check_dictionary \
            = {'input_dataframe': [input_dataframe, pd.DataFrame, pd.DataFrame],
               'caption_string': [caption_string, str, str],
               'precision_integer': [precision_integer, int, int],
               'hide_index_boolean': [hide_index_boolean, bool, bool]}
    
        if error_handle_functions.check_parameters_for_errors(error_check_dictionary):
        
            log_subroutines \
                .print_and_log_text \
                    ('\033[1m'
                     + 'The function, return_standard_format_styler, ' 
                     + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, ' 
                     + f'received invalid or empty function parameters.\n\n'
                     + '\033[0m')
        
            return None
        
        
        temp_dataframe = input_dataframe.copy()
        
        
        if hide_index_boolean == True:
            
            return \
                temp_dataframe \
                    .style \
                    .set_caption \
                        (caption_string) \
                    .set_table_styles \
                        ([dict \
                             (selector = 'caption',
                              props = [('color', 'black'),
                                       ('font-size', '20px'),
                                       ('font-style', 'bold'),
                                       ('text-align', 'center')])]) \
                    .set_properties \
                         (**{'text-align':
                            'center',
                            'border':
                            '1.3px solid red',
                            'color':
                            'blue'}) \
                    .format \
                        (precision \
                            = precision_integer, 
                         thousands \
                            = ',', 
                         decimal \
                            = '.') \
                    .hide()
            
        else:
            
            return \
                temp_dataframe \
                    .style \
                    .set_caption \
                        (caption_string) \
                    .set_table_styles \
                        ([dict \
                             (selector = 'caption',
                              props = [('color', 'black'),
                                       ('font-size', '20px'),
                                       ('font-style', 'bold'),
                                       ('text-align', 'center')])]) \
                    .set_properties \
                         (**{'text-align':
                            'center',
                            'border':
                            '1.3px solid red',
                            'color':
                            'blue'}) \
                    .format \
                        (precision \
                            = precision_integer, 
                         thousands \
                            = ',', 
                         decimal \
                            = '.')
        
    except:
            
        log_subroutines \
            .print_and_log_text \
                (f'The function, return_standard_format_styler, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to format a dataframe as a styler object.')
        
        return None


# In[4]:


#*******************************************************************************************
 #
 #  Function Name:  save_image_and_return_styler
 #
 #  Function Description:
 #      This function saves the styler object as a png image then returns the object.
 #
 #
 #  Return Type: styler
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  styler
 #          input_styler
 #                          The parameter is the input styler object.
 #  string
 #          caption_string
 #                          The parameter is the table caption.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  03/04/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def save_image_and_return_styler \
        (input_styler,
         caption_string):
    
    try:
        
        if log_constants.IMAGE_FLAG == True:

            image_file_path_string \
                = log_functions.get_image_file_path(caption_string, 'png')
        
            dataframe_image.export(input_styler, image_file_path_string)
        
        return input_styler
        
    except:
        
        log_subroutines \
            .print_and_log_text \
                (f'The function, save_image_and_return_styler, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + 'cannot save an image of a styler object ' \
                 + 'then return it to the caller.')
        
        return None


# In[5]:


#*******************************************************************************************
 #
 #  Function Name:  return_formatted_table
 #
 #  Function Description:
 #      This function returns a formatted table from a dataframe.
 #
 #
 #  Return Type: styler
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  dataframe
 #          input_dataframe
 #                          The parameter is the input dataframe.
 #  string
 #          caption_string
 #                          The parameter is the table caption.
 #  integer
 #          line_count_integer
 #                          The parameter is the number of displayed records.
 #  boolean
 #          hide_index_boolean
 #                          The parameter indicates whether the index is present.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  03/12/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_formatted_table \
        (input_dataframe,
         caption_string,
         line_count_integer = 10,
         hide_index_boolean = True):

    current_styler \
        = return_standard_format_styler \
            (input_dataframe.head(line_count_integer),
             caption_string, 
             hide_index_boolean = hide_index_boolean)

    return \
        save_image_and_return_styler \
            (current_styler,
             caption_string)


# In[6]:


#*******************************************************************************************
 #
 #  Function Name:  return_summary_statistics_as_dataframe
 #
 #  Function Description:
 #      This function converts a data series into summary statistics, assigns
 #      the statistics to a dataframe, and returns it.
 #
 #
 #  Return Type: dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  series
 #          data_series
 #                          The parameter is the input series.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  03/12/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_summary_statistics_as_dataframe(data_series):

    try:
        
        # This line of code allocates the distribution for the quartiles.
        quartiles_series = data_series.quantile([0.25, 0.50, 0.75])
    
        # These lines of code establish the lower quartile and the upper quartile.
        lower_quartile_float = quartiles_series[0.25]

        upper_quartile_float = quartiles_series[0.75]
    
        # This line of code calculates the interquartile range (IQR).
        interquartile_range_float = upper_quartile_float - lower_quartile_float

        # These line of code calculate the lower bound and upper bound 
        # of the distribution.
        lower_bound_float = lower_quartile_float - (1.5*interquartile_range_float)
    
        upper_bound_float = upper_quartile_float + (1.5*interquartile_range_float)
    
        # This line of code establishes a list of outliers.
        outliers_series \
            = data_series \
                .loc[(data_series < lower_bound_float) \
                        | (data_series > upper_bound_float)]
        
        # This line of code finds the number of outliers.
        number_of_outliers_integer = len(outliers_series)
  
        # These lines of code create a list of all the summary statistics and store
        # the data in a DataFrame.
        statistics_dictionary_list \
            = [{'Lower Quartile': lower_quartile_float,
                'Upper Quartile': upper_quartile_float,
                'Interquartile Range': interquartile_range_float,
                'Median': quartiles_series[0.5],
                'Lower Boundary': lower_bound_float,
                'Upper Boundary': upper_bound_float,
                'Number of Outliers': number_of_outliers_integer}]
  
        return pd.DataFrame(statistics_dictionary_list)
        
    except:
            
        log_subroutines \
            .print_and_log_text \
                (f'The function, return_summary_statistics_as_dataframe, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + 'cannot return summary statistics as a dataframe.')
            
        return None


# In[ ]:




