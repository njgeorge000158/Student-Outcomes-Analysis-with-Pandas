#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  log_subroutines.py
 #
 #  File Description:
 #      This Python script, log_subroutines.py, contains generic Python subroutines
 #      for writing information to log files.  Here is the list:
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
 #  02/19/2024      Initial Development                     Nicholas J. George
 #
 #******************************************************************************************/

import log_constants
import log_functions

import matplotlib.pyplot as plt
import hvplot.pandas

import os
import copy


# In[2]:


CONSTANT_LOCAL_FILE_NAME = 'log_subroutines.py'


# In[3]:


#*******************************************************************************************
 #
 #  Subroutine Name:  begin_program
 #
 #  Subroutine Description:
 #      This subroutine prints an announcement for the start of program execution, creates
 #      the appropriate folders, and writes the same announcement to the log file.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  string
 #          program_designation_string
 #                          This parameter is the program designation.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/19/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def begin_program(program_designation_string = ''):
    
    try:

        create_directory(log_constants.LOGS_DIRECTORY_PATH)
        
        create_directory(log_constants.IMAGES_DIRECTORY_PATH)


        set_program_designation(program_designation_string)
        

        open_log_file()


        message_string = 'Program execution begins...\n'

        
        if log_constants.LOG_FLAG == True:
    
            print_and_log_text(message_string)

    except:
        
        print \
            (f'The subroutine, begin_program, in file {CONSTANT_LOCAL_FILE_NAME}, ' \
             + f'could not begin program execution: {program_designation_string}')    


# In[4]:


#*******************************************************************************************
 #
 #  Subroutine Name:  end_program
 #
 #  Subroutine Description:
 #      This subroutine prints an end of program execution announcement, creates the 
 #      appropriate folders, and writes the same announcement to the log file.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  n/a     n/a             n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/19/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def end_program():
    
    try:
        
        current_timestamp_string \
            = log_functions.current_timestamp_as_string()
                
        message_string \
            = f'Program execution ends at {current_timestamp_string}.\n\n\n\n'
        
        
        if log_constants.LOG_FLAG == True:
            
            print_and_log_text(message_string)

            log_constants.log_txt_file.close()

    except:
        
        print \
            (f'The subroutine, end_program, in file {CONSTANT_LOCAL_FILE_NAME}, ' \
             + 'could not close the log file.')   


# In[5]:


#*******************************************************************************************
 #
 #  Subroutine Name:  set_log_mode
 #
 #  Subroutine Description:
 #      This subroutine sets the value for the global log flag (True/False).
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  boolean
 #          mode_boolean
 #                          This parameter is the desired Boolean value 
 #                          for the global log flag.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/19/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_log_mode(mode_boolean = True):
    
    log_constants.LOG_FLAG = mode_boolean


# In[6]:


#*******************************************************************************************
 #
 #  Subroutine Name:  set_image_mode
 #
 #  Subroutine Description:
 #      This subroutine sets the value for the global image flag (True/False).
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  boolean
 #          mode_boolean
 #                          This parameter is the desired Boolean value 
 #                          for the global image flag.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/19/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_image_mode(mode_boolean = True):
    
    log_constants.IMAGE_FLAG = mode_boolean


# In[7]:


#*******************************************************************************************
 #
 #  Subroutine Name:  set_program_designation
 #
 #  Subroutine Description:
 #      This subroutine sets the value for the global program designation string.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  string
 #          program_designation_string
 #                          This parameter is the text for the global program designation.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/19/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_program_designation(program_designation_string = ''):
    
    log_constants.PROGRAM_DESIGNATION = program_designation_string


# In[8]:


#*******************************************************************************************
 #
 #  Function Name:  log_write_object
 #
 #  Function Description:
 #      This function takes an object as a parameter, and, if the global debug flag is true, 
 #      writes it to a debug file.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  object
 #          input_object
 #                          This parameter is the object to be written to the log file.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/19/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def log_write_object(input_object):
    
    message_string = f'\n\n' + str(input_object) + f'\n\n'
    
    if log_constants.LOG_FLAG == True:
        
        log_constants.log_txt_file.write(message_string)


# In[9]:


#*******************************************************************************************
 #
 #  Subroutine Name:  create_directory
 #
 #  Subroutine Description:
 #      This subroutine creates a folder if it does not exist.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  string
 #          directory_string
 #                          This parameter is the directory name.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/19/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def create_directory(directory_string):
    
    try:
    
        exist_boolean \
            = os.path.exists(directory_string)
    
    
        if exist_boolean == False:
        
            os.makedirs(directoryNameStringParameter)
            
            print \
                (f'The script created directory, {directory_string}.\n')
    
    except:
        
        print \
            (f'The subroutine, create_directory, in file {CONSTANT_LOCAL_FILE_NAME}, ' \
             + f'could not create the directory, {directory_string}.')


# In[10]:


#*******************************************************************************************
 #
 #  Subroutine Name:  open_log_file
 #
 #  Subroutine Description:
 #      This subroutine opens the log file for appending.  If it does not exist, the 
 #      subroutine creates it.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  n/a     n/a             n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/19/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def open_log_file():
    
    try:

        current_date_string \
            = log_functions \
                .current_date_as_string()

       
        program_designation_string \
            = log_constants \
                .PROGRAM_DESIGNATION \

       
        log_constants.LOG_FILE_PATH \
            = log_constants.LOGS_DIRECTORY_PATH \
                + '/' \
                + current_date_string \
                + program_designation_string \
                + log_constants.BASE_LOG_FILE_NAME

      
        if log_constants.LOG_FLAG == True:
        
            log_constants.log_txt_file \
                = open(log_constants.LOG_FILE_PATH, 'a')
       

    except:
        
        print \
            (f'The subroutine, open_log_file, in file {CONSTANT_LOCAL_FILE_NAME}, ' \
             + f'could not open the log file: {log_constants.LOG_FILE_PATH}.')


# In[11]:


#*******************************************************************************************
 #
 #  Subroutine Name:  print_and_log_text
 #
 #  Subroutine Description:
 #      This subroutine prints the received message then writes the message to the log file.
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  string
 #          message_string
 #                          This parameter is the input message text string.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/19/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def print_and_log_text(message_string = ''):
    
    print(message_string)
    
    timepoint_message_string \
        = log_functions.current_timepoint_with_message(message_string)
    
    if log_constants.LOG_FLAG == True:
    
        log_constants.log_txt_file.write(timepoint_message_string)    


# In[12]:


#*******************************************************************************************
 #
 #  Subroutine Name:  save_plot_image
 #
 #  Subroutine Description:
 #      This subroutine saves the image of a matplotlib plot to a file.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  string
 #          caption_string
 #                          This parameter is the plot title.
 #  integer
 #          dpi_integer
 #                          This parameter is the dots per square inch for the image.
 #  float
 #          pad_inches_float
 #                          This parameter is the buffer around the plot in inches.
 #  string
 #          image_format_string
 #                          This parameter is the image format (png, html, etc.).
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/19/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def save_plot_image \
        (caption_string = '',
         dpi_integer = 300,
         pad_inches_float = 0.5,
         image_format_string = 'png'):

    try:
        
        if log_constants.IMAGE_FLAG == True:

            image_file_path_string \
                = log_functions.get_image_file_path \
                    (caption_string,
                     image_format_string)

            plt.savefig \
                (image_file_path_string, 
                 dpi = dpi_integer, 
                 bbox_inches = 'tight', 
                 pad_inches = pad_inches_float)

    except:
        
        print \
            (f'The subroutine, save_plot_image, in file {CONSTANT_LOCAL_FILE_NAME}, ' \
             + f'could not save a plot to a file for caption, {caption_string}.')   


# In[13]:


#*******************************************************************************************
 #
 #  Subroutine Name:  save_hvplot_image_to_html
 #
 #  Subroutine Description:
 #      This subroutine saves an hvplot to an html file.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  object
 #          hvplot_overlay
 #                          This parameter is the input hvplot overlay object.
 #  string
 #          caption_string
 #                          This parameter is the plot title.
 #  integer
 #          height_integer
 #                          This parameter is the plot's height.
 #  integer
 #          width_integer
 #                          This parameter is the plot's width.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/19/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def save_hvplot_image_to_html \
        (hvplot_overlay,
         caption_string = '',
         height_integer = 550,
         width_integer = 1100):
    
    try:
        
        if log_constants.IMAGE_FLAG == True:

            temp_overlay = copy.copy(hvPlotOverlayParameter)
    
            temp_overlay.opts \
                (width = width_integer, 
                 height = height_integer)
        
            image_file_path_string \
                = log_functions.get_image_file_path(captionStringParameter, 'html')
            
            hvplot.save(temp_overlay, image_file_path_string)
    
    except:
        
        print \
            (f'The subroutine, save_hvplot_image_to_html, in file {CONSTANT_LOCAL_FILE_NAME}, ' \
             + f'could not save an hvplot to an HTML file for caption, {caption_string}.') 


# In[14]:


#*******************************************************************************************
 #
 #  Subroutine Name:  save_plotly_image
 #
 #  Subroutine Description:
 #      This subroutine saves a Plotly image to the images folder.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  object
 #          plotly_figure
 #                          This parameter is the Plotly Figure Object.
 #  string
 #          figure_title_string
 #                          This parameter is the figure title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/19/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def save_plotly_image \
        (plotly_figure,
         caption_string):

    try:
        
        if log_constants.IMAGE_FLAG == True:

            image_file_path_string \
                = log_functions.get_image_file_path(caption_string, 'png')

            plotly_figure.write_image(image_file_path_string)

    except:
        
        print \
            (f'The subroutine, save_plotly_image, in file {CONSTANT_LOCAL_FILE_NAME}, ' \
             + f'could not save a Plotly image to a file for caption, {caption_string}.')   


# In[ ]:




