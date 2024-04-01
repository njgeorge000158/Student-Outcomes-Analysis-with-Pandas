#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  log_functions.py
 #
 #  File Description:
 #      This Python script, log_functions.py, contains generic Python functions
 #      for writing information to log files.  Here is the list:
 #
 #      current_date_as_string
 #      current_timestamp_as_string
 #      current_timepoint_with_message
 #
 #      get_image_file_path
 #
 #      return_styler_save_png
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  02/19/2024      Initial Development                     N. James George
 #
 #******************************************************************************************/

import log_constants
import log_subroutines

import dataframe_image

from datetime import date
from datetime import datetime


# In[2]:


CONSTANT_LOCAL_FILE_NAME = 'log_functions.py'


# In[3]:


#*******************************************************************************************
 #
 #  Function Name:  current_date_as_string
 #
 #  Function Description:
 #      This function returns the current date as a formatted string for the names
 #      of log files.
 #
 #
 #  Return Type: string
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  string
 #          format_string
 #                          This parameter is optional and specifies the date format.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/19/2024          Initial Development                         N. James George
 #
 #******************************************************************************************/

def current_date_as_string(format_string = '%Y%m%d'):
    
    todays_date = date.today()
    
    return todays_date.strftime(format_string)


# In[4]:


#*******************************************************************************************
 #
 #  Function Name:  current_timestamp_as_string
 #
 #  Function Description:
 #      This function returns the current date and time as a formatted string
 #      for timepoint entries in log files.
 #
 #
 #  Return Type: string
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  string
 #          format_string
 #                          This parameter is optional and specifies the datetime format.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/19/2024          Initial Development                         N. James George
 #
 #******************************************************************************************/

def current_timestamp_as_string(format_string = '%Y/%m/%d %H:%M:%S'):
    
    current_datetime = datetime.now()
    
    return current_datetime.strftime(format_string)


# In[5]:


#*******************************************************************************************
 #
 #  Function Name:  current_timepoint_with_message
 #
 #  Function Description:
 #      This function takes a message, formats it with a timestamp, and returns it 
 #      to the caller.
 #
 #
 #  Return Type: string
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  string
 #          message_string
 #                          This parameter is the optional message with the timepoint.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/19/2024          Initial Development                         N. James George
 #
 #******************************************************************************************/

def current_timepoint_with_message(message_string = ''):
    
    current_timestamp_string = current_timestamp_as_string()
    
    timepoint_string \
        = f'\nTimepoint: {current_timestamp_string}\n' \
            + message_string \
            + '\n\n'

    return timepoint_string


# In[6]:


#*******************************************************************************************
 #
 #  Function Name:  get_image_file_path
 #
 #  Function Description:
 #      This function uses a plot's caption to determine the image file path.
 #
 #
 #  Return Type: string
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  string
 #          caption_string
 #                          This parameter is the plot title.
 #  string
 #          image_format_string
 #                          This parameter is the image format file suffix.    
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/19/2024          Initial Development                         N. James George
 #
 #******************************************************************************************/
    
def get_image_file_path \
        (caption_string = 'test',
         image_format_string = ''):
    
    temp_string = ''.join(filter(str.isalnum, caption_string))
    
    
    image_file_path \
        = log_constants.IMAGES_DIRECTORY_PATH \
            + '/' \
            + log_constants.PROGRAM_DESIGNATION \
            + temp_string
    
    
    if image_format_string != '':
    
        image_file_path += '.' + image_format_string
        
    
    return image_file_path


# In[7]:


#*******************************************************************************************
 #
 #  Subroutine Name:  save_png_return_styler
 #
 #  Subroutine Description:
 #      This subroutine saves the styler object as a png image file then returns it.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  styler
 #          input_styler
 #                          This parameter is the input styler object.
 #  string
 #          caption_string
 #                          This parameter is the styler caption.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/19/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def save_png_return_styler \
        (input_styler,
         caption_string):
    
    try:
        
        if log_constants.IMAGE_FLAG == True:

            image_file_path_string \
                = get_image_file_path(caption_string, 'png')
        
            dataframe_image.export(input_styler, image_file_path_string)

        
        return input_styler

    except:
        
        log_subroutines \
            .print_and_log_text \
                (f'The function, save_png_return_styler, in file {CONSTANT_LOCAL_FILE_NAME}, ' \
                 + f'could not save the image and return the styler for caption, {caption_string}.')

        return None


# In[ ]:




