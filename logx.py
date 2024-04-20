#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  logx.py
 #
 #  File Description:
 #      This Python script, logx.py, contains generic Python functions for writing 
 #      information to log files.  Here is the list:
 #
 #  current_date_as_string
 #  current_timestamp_as_string
 #  current_timepoint_with_message
 #
 #  get_image_file_path
 #
 #  return_styler_save_png
 #
 #  begin_program
 #  end_program
 #  set_log_mode
 #  set_image_mode
 #  set_program_designation
 #
 #  log_write_object
 #  create_directory
 #  open_log_file
 #  print_and_log_text
 #
 #  save_plot_image
 #  save_hvplot_image_to_html
 #  save_plotly_image
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  04/11/2024      Initial Development                     Nicholas J. George
 #
 #******************************************************************************************/

import logx_constants

import dataframe_image
import os
import copy

import matplotlib.pyplot as plt
import hvplot.pandas

from datetime import date
from datetime import datetime


# In[2]:


CONSTANT_LOCAL_FILE_NAME = 'logx.py'


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
 #  string  format_string   This parameter is optional and specifies the date format.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
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
 #  string  format_string   This parameter is optional and specifies the datetime format.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
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
 #  string  message_string  This parameter is the optional message with the timepoint.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def current_timepoint_with_message(message_string = ''):
    
    current_timestamp_string = current_timestamp_as_string()
    
    timepoint_string = f'\nTimepoint: {current_timestamp_string}\n' + message_string + '\n\n'

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
 #  string  caption_string  This parameter is the plot title.
 #  string  image_format_string
 #                          This parameter is the image format file suffix.    
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/
    
def get_image_file_path \
        (caption_string = 'test',
         image_format_string = ''):
    
    temp_string = ''.join(filter(str.isalnum, caption_string))
    
    image_file_path \
        = logx_constants.IMAGES_DIRECTORY_PATH \
            + '/' \
            + logx_constants.PROGRAM_DESIGNATION \
            + temp_string
    
    if image_format_string != '':
    
        image_file_path += '.' + image_format_string
        
    return image_file_path


# In[7]:


#*******************************************************************************************
 #
 #  Function Name:  save_png_return_styler
 #
 #  Function Description:
 #      This function saves the styler object as a png image file then returns it.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  styler  input_styler    This parameter is the input styler object.
 #  string  caption_string  This parameter is the styler caption.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def save_png_return_styler \
        (input_styler,
         caption_string):
    
    if logx_constants.IMAGE_FLAG == True:

        image_file_path_string = get_image_file_path(caption_string, 'png')
        
        dataframe_image.export(input_styler, image_file_path_string)

        
    return input_styler


# In[8]:


#*******************************************************************************************
 #
 #  Function Name:  begin_program
 #
 #  Function Description:
 #      This function prints an announcement for the start of program execution, creates
 #      the appropriate folders, and writes the same announcement to the log file.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  string  program_designation_string
 #                          This parameter is the program designation.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def begin_program(program_designation_string = ''):
    
    create_directory(logx_constants.LOGS_DIRECTORY_PATH)
        
    create_directory(logx_constants.IMAGES_DIRECTORY_PATH)

    set_program_designation(program_designation_string)

    
    open_log_file()

    
    message_string = 'Program execution begins...\n'
        
    if logx_constants.LOG_FLAG == True:
    
        print_and_log_text(message_string) 


# In[9]:


#*******************************************************************************************
 #
 #  Function Name:  end_program
 #
 #  Function Description:
 #      This function prints an end of program execution announcement, creates the 
 #      appropriate folders, and writes the same announcement to the log file.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  n/a     n/a             n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def end_program():
    
    current_timestamp_string = current_timestamp_as_string()
                
    message_string = f'Program execution ends at {current_timestamp_string}.\n\n\n\n'
        
    if logx_constants.LOG_FLAG == True:
            
        print_and_log_text(message_string)

        logx_constants.log_txt_file.close() 


# In[10]:


#*******************************************************************************************
 #
 #  Function Name:  set_log_mode
 #
 #  Function Description:
 #      This function sets the value for the global log flag (True/False).
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  boolean mode_boolean    This parameter is the desired Boolean value for the global 
 #                          log flag.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_log_mode(mode_boolean = True):
    
    logx_constants.LOG_FLAG = mode_boolean


# In[11]:


#*******************************************************************************************
 #
 #  Function Name:  set_image_mode
 #
 #  Function Description:
 #      This function sets the value for the global image flag (True/False).
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  boolean mode_boolean    This parameter is the desired Boolean value for the global 
 #                          image flag.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_image_mode(mode_boolean = True):
    
    logx_constants.IMAGE_FLAG = mode_boolean


# In[12]:


#*******************************************************************************************
 #
 #  Function Name:  set_program_designation
 #
 #  Function Description:
 #      This function sets the value for the global program designation string.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  string  program_designation_string
 #                          This parameter is the text for the global program designation.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_program_designation(program_designation_string = ''):
    
    logx_constants.PROGRAM_DESIGNATION = program_designation_string


# In[13]:


#*******************************************************************************************
 #
 #  Function Name:  log_write_object
 #
 #  Function Description:
 #      This function takes an object as a parameter, and, if the global debug flag is true, 
 #      writes it to a debug file.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  object  input_object    This parameter is the object to be written to the log file.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def log_write_object(input_object):
    
    message_string = f'\n\n' + str(input_object) + f'\n\n'
    
    if logx_constants.LOG_FLAG == True:
        
        logx_constants.log_txt_file.write(message_string)


# In[14]:


#*******************************************************************************************
 #
 #  Function Name:  create_directory
 #
 #  Function Description:
 #      This function creates a folder if it does not exist.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  string  directory_string
 #                          This parameter is the directory name.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def create_directory(directory_string):
    
    exist_boolean = os.path.exists(directory_string)
    
    if exist_boolean == False:
        
        os.makedirs(directory_string)
            
        print(f'The script created directory, {directory_string}.\n')


# In[15]:


#*******************************************************************************************
 #
 #  Function Name:  open_log_file
 #
 #  Function Description:
 #      This function opens the log file for appending.  If it does not exist, the 
 #      function creates it.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  n/a     n/a             n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def open_log_file():
    
    current_date_string = current_date_as_string()

    program_designation_string = logx_constants.PROGRAM_DESIGNATION \

    logx_constants.LOG_FILE_PATH \
        = logx_constants.LOGS_DIRECTORY_PATH \
            + '/' \
            + current_date_string \
            + program_designation_string \
            + logx_constants.BASE_LOG_FILE_NAME

    if logx_constants.LOG_FLAG == True:
        
        logx_constants.log_txt_file = open(logx_constants.LOG_FILE_PATH, 'a')


# In[16]:


#*******************************************************************************************
 #
 #  Function Name:  print_and_log_text
 #
 #  Function Description:
 #      This function prints the received message then writes the message to the log file.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  string  message_string  This parameter is the input message text string.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def print_and_log_text(message_string = ''):
    
    print(message_string)
    
    timepoint_message_string = current_timepoint_with_message(message_string)
    
    if logx_constants.LOG_FLAG == True:
    
        logx_constants.log_txt_file.write(timepoint_message_string)    


# In[17]:


#*******************************************************************************************
 #
 #  Function Name:  save_plot_image
 #
 #  Function Description:
 #      This function saves the image of a matplotlib plot to a file.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  string  caption_string  This parameter is the plot title.
 #  integer dpi_integer     This parameter is the dots per square inch for the image.
 #  float   pad_inches_float
 #                          This parameter is the buffer around the plot in inches.
 #  string  image_format_string
 #                          This parameter is the image format (png, html, etc.).
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def save_plot_image \
        (caption_string = '',
         dpi_integer = 300,
         pad_inches_float = 0.5,
         image_format_string = 'png'):

    if logx_constants.IMAGE_FLAG == True:

        image_file_path_string \
            = get_image_file_path(caption_string, image_format_string)

        plt.savefig \
            (image_file_path_string, 
             dpi = dpi_integer, 
             bbox_inches = 'tight', 
             pad_inches = pad_inches_float)


# In[18]:


#*******************************************************************************************
 #
 #  Function Name:  save_hvplot_image_to_html
 #
 #  Function Description:
 #      This function saves an hvplot to an html file.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  object  hvplot_overlay  This parameter is the input hvplot overlay object.
 #  string  caption_string  This parameter is the plot title.
 #  integer height_integer  This parameter is the plot's height.
 #  integer width_integer   This parameter is the plot's width.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def save_hvplot_image_to_html \
        (hvplot_overlay,
         caption_string = '',
         height_integer = 550,
         width_integer = 1100):
    
    if logx_constants.IMAGE_FLAG == True:

        temp_overlay = copy.copy(hvplot_overlay)
    
        temp_overlay.opts(width = width_integer, height = height_integer)
        
        image_file_path_string = get_image_file_path(caption_string, 'html')
            
        hvplot.save(temp_overlay, image_file_path_string)


# In[19]:


#*******************************************************************************************
 #
 #  Function Name:  save_plotly_image
 #
 #  Function Description:
 #      This function saves a Plotly image to the images folder.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  object  plotly_figure   This parameter is the Plotly Figure Object.
 #  string  figure_title_string
 #                          This parameter is the figure title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def save_plotly_image \
        (plotly_figure,
         caption_string):

    if logx_constants.IMAGE_FLAG == True:

        image_file_path_string = get_image_file_path(caption_string, 'png')

        plotly_figure.write_image(image_file_path_string)


# In[ ]:




