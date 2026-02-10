#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  logx.py
 #
 #  File Description:
 #      The Python script, logx.py, contains generic Python functions for writing 
 #      information to log files.  Here is the list:
 #
 #  set_log_mode
 #  set_image_mode
 #  set_program_designation
 #
 #  set_logs_directory_path
 #  set_images_directory_path
 #  set_resources_directory_path
 #  set_sql_directory_path
 #  set_visualization_directory_path
 #  set_models_directory_path
 #  set_backups_directory_path
 #
 #  set_base_log_file_name
 # 
 #  get_log_mode
 #  get_image_mode
 #  get_program_designation
 #
 #  get_logs_directory_path
 #  get_images_directory_path
 #  get_resources_directory_path
 #  get_sql_directory_path
 #  get_visualization_directory_path
 #  get_models_directory_path
 #  get_backups_directory_path
 #
 #  get_base_log_file_name
 #
 #  get_image_file_path
 #
 #  current_date_as_text
 #  current_timestamp_as_text
 #  current_timepoint_with_message
 #
 #  return_styler_save_png
 #
 #  begin_program
 #  end_program
 #
 #  log_write_obj
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
 #  02/09/2026      Abbreviated variable names and added global configuration
 #                  dictionary                              Nicholas J. George
 #  02/10/2026      Added functions for returning global values
 #                                                          Nicholas J. George
 #
 #******************************************************************************************/

import os
import copy

import dataframe_image as dfi
import matplotlib.pyplot as plt

import hvplot.pandas

from datetime import date
from datetime import datetime


# In[2]:


CONSTANT_LOCAL_FILE_NAME = 'logx.py'


# In[3]:


logs_config_dict \
    = {'logs_folder': './logs',
       'images_folder': './images',
       'resources_folder': './resources',
       'sql_folder': './sql',
       'visual_folder': './visualization',
       'models_folder': './models',
       'backups_folder': './backups',
       'base_log_name': '_log.txt',
       'log_folder': '',
       'log_txt_file': None,
       'prgrm_dsgn': '',
       'log_bool': False,
       'image_bool': False}


# In[4]:


#*******************************************************************************************
 #
 #  Function Name:  set_log_mode
 #
 #  Function Description:
 #      The function sets the value for the global log flag (True/False).
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  boolean mode_bool       The parameter is the desired Boolean value 
 #                          for the global log flag.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_log_mode(mode_bool = True):

    global logs_config_dict

    logs_config_dict['log_bool'] = mode_bool


# In[5]:


#*******************************************************************************************
 #
 #  Function Name:  set_image_mode
 #
 #  Function Description:
 #      The function sets the value for the global image flag (True/False).
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  boolean mode_bool       The parameter is the desired Boolean value 
 #                          for the global image flag.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_image_mode(mode_bool = True):

    global logs_config_dict

    logs_config_dict['image_bool'] = mode_bool


# In[6]:


#*******************************************************************************************
 #
 #  Function Name:  set_program_designation
 #
 #  Function Description:
 #      The function sets the value for the global program designation string.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  string  prgrm_desig     The parameter is the text for the global program designation.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_program_designation(prgrm_desig = ''):

    global logs_config_dict

    logs_config_dict['prgrm_dsgn'] = prgrm_desig


# In[7]:


#*******************************************************************************************
 #
 #  Function Name:  set_logs_directory_path
 #
 #  Function Description:
 #      The function sets the logs directory path.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  string  directory_path  The parameter is the new directory path.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_logs_directory_path(directory_path):

    global logs_config_dict

    logs_config_dict['logs_folder'] = directory_path


# In[8]:


#*******************************************************************************************
 #
 #  Function Name:  set_images_directory_path
 #
 #  Function Description:
 #      The function sets the images directory path.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  string  directory_path  The parameter is the new directory path.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_images_directory_path(directory_path):

    global logs_config_dict

    logs_config_dict['images_folder'] = directory_path


# In[9]:


#*******************************************************************************************
 #
 #  Function Name:  set_resources_directory_path
 #
 #  Function Description:
 #      The function sets the resources directory path.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  string  directory_path  The parameter is the new directory path.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_resources_directory_path(directory_path):

    global logs_config_dict

    logs_config_dict['resources_folder'] = directory_path


# In[10]:


#*******************************************************************************************
 #
 #  Function Name:  set_sql_directory_path
 #
 #  Function Description:
 #      The function sets the sql directory path.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  string  directory_path  The parameter is the new directory path.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_sql_directory_path(directory_path):

    global logs_config_dict

    logs_config_dict['sql_folder'] = directory_path


# In[11]:


#*******************************************************************************************
 #
 #  Function Name:  set_visualzation_directory_path
 #
 #  Function Description:
 #      The function sets the visualzation directory path.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  string  directory_path  The parameter is the new directory path.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_visualzation_directory_path(directory_path):

    global logs_config_dict

    logs_config_dict['visual_folder'] = directory_path


# In[12]:


#*******************************************************************************************
 #
 #  Function Name:  set_models_directory_path
 #
 #  Function Description:
 #      The function sets the models directory path.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  string  directory_path  The parameter is the new directory path.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_models_directory_path(directory_path):

    global logs_config_dict

    logs_config_dict['models_folder'] = directory_path


# In[13]:


#*******************************************************************************************
 #
 #  Function Name:  set_backups_directory_path
 #
 #  Function Description:
 #      The function sets the backups directory path.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  string  directory_path  The parameter is the new directory path.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_backups_directory_path(directory_path):

    global logs_config_dict

    logs_config_dict['backups_folder'] = directory_path


# In[14]:


#*******************************************************************************************
 #
 #  Function Name:  set_base_log_file_name
 #
 #  Function Description:
 #      The function sets the base log file name.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  string  base_file_path  The parameter is the base file name.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_base_log_file_name(base_file_path):

    global logs_config_dict

    logs_config_dict['base_log_name'] = base_file_path


# In[15]:


#*******************************************************************************************
 #
 #  Function Name:  get_log_mode
 #
 #  Function Description:
 #      The function returns the value of the global log flag (True/False).
 #
 #
 #  Return Type: bool
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
 #  02/10/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_log_mode():

    return logs_config_dict['log_bool']


# In[16]:


#*******************************************************************************************
 #
 #  Function Name:  get_image_mode
 #
 #  Function Description:
 #      The function returns the value of the global image flag (True/False).
 #
 #
 #  Return Type: bool
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
 #  02/10/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_image_mode():

    return logs_config_dict['image_bool']


# In[17]:


#*******************************************************************************************
 #
 #  Function Name:  get_program_designation
 #
 #  Function Description:
 #      The function returns the value for the global program designation.
 #
 #
 #  Return Type: string
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
 #  02/10/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_program_designation():

    return logs_config_dict['prgrm_dsgn']


# In[18]:


#*******************************************************************************************
 #
 #  Function Name:  get_logs_directory_path
 #
 #  Function Description:
 #      The function returns the logs directory path.
 #
 #
 #  Return Type: string
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
 #  02/10/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_logs_directory_path():

    return logs_config_dict['logs_folder']


# In[19]:


#*******************************************************************************************
 #
 #  Function Name:  get_images_directory_path
 #
 #  Function Description:
 #      The function returns the images directory path.
 #
 #
 #  Return Type: string
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
 #  02/10/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_images_directory_path():

    return logs_config_dict['images_folder']


# In[20]:


#*******************************************************************************************
 #
 #  Function Name:  get_resources_directory_path
 #
 #  Function Description:
 #      The function returns the resources directory path.
 #
 #
 #  Return Type: string
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
 #  02/10/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_resources_directory_path():

    return logs_config_dict['resources_folder']


# In[21]:


#*******************************************************************************************
 #
 #  Function Name:  get_sql_directory_path
 #
 #  Function Description:
 #      The function returns the sql directory path.
 #
 #
 #  Return Type: string
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
 #  02/10/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_sql_directory_path():

    return logs_config_dict['sql_folder']


# In[22]:


#*******************************************************************************************
 #
 #  Function Name:  get_visualzation_directory_path
 #
 #  Function Description:
 #      The function returns the visualzation directory path.
 #
 #
 #  Return Type: string
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
 #  02/10/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_visualzation_directory_path():

    return logs_config_dict['visual_folder']


# In[23]:


#*******************************************************************************************
 #
 #  Function Name:  get_models_directory_path
 #
 #  Function Description:
 #      The function returns the models directory path.
 #
 #
 #  Return Type: string
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
 #  02/10/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_models_directory_path():

    return logs_config_dict['models_folder']


# In[24]:


#*******************************************************************************************
 #
 #  Function Name:  get_backups_directory_path
 #
 #  Function Description:
 #      The function returns the backups directory path.
 #
 #
 #  Return Type: string
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
 #  02/10/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_backups_directory_path():

    return logs_config_dict['backups_folder']


# In[25]:


#*******************************************************************************************
 #
 #  Function Name:  get_base_log_file_name
 #
 #  Function Description:
 #      The function returns the base log file name.
 #
 #
 #  Return Type: string
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
 #  02/10/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_base_log_file_name():

    return logs_config_dict['base_log_name']


# In[26]:


#*******************************************************************************************
 #
 #  Function Name:  get_image_file_path
 #
 #  Function Description:
 #      The function uses a plot's caption to determine the image file path.
 #
 #
 #  Return Type: string
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  string  caption         The parameter is the plot title.
 #  string  image_format    The parameter is the image format file suffix.    
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_image_file_path \
        (caption = 'test',
         image_format = ''):

    temp = ''.join(filter(str.isalnum, caption))

    image_file_path \
        = logs_config_dict['images_folder'] + '/' + logs_config_dict['prgrm_dsgn'] + temp

    if image_format != '':

        image_file_path += '.' + image_format

    return image_file_path


# In[27]:


#*******************************************************************************************
 #
 #  Function Name:  current_date_as_text
 #
 #  Function Description:
 #      The function returns the current date as a formatted string for the names
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
 #  string  string_format   The parameter is optional and specifies the date format.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def current_date_as_text(string_format = '%Y%m%d'):

    todays_date = date.today()

    return todays_date.strftime(string_format)


# In[28]:


#*******************************************************************************************
 #
 #  Function Name:  current_timestamp_as_text
 #
 #  Function Description:
 #      The function returns the current date and time as a formatted string
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
 #  string  string_format   The parameter is optional and specifies the datetime format.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def current_timestamp_as_text(string_format = '%Y/%m/%d %H:%M:%S'):

    current_datetime = datetime.now()

    return current_datetime.strftime(string_format)


# In[29]:


#*******************************************************************************************
 #
 #  Function Name:  current_timepoint_with_message
 #
 #  Function Description:
 #      The function takes a message, formats it with a timestamp, and returns it 
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
 #  string  message         The parameter is the optional message with the timepoint.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def current_timepoint_with_message(message = ''):

    current_timestamp = current_timestamp_as_text()

    timepoint = f'\nTimepoint: {current_timestamp}\n' + message + '\n\n'

    return timepoint


# In[30]:


#*******************************************************************************************
 #
 #  Function Name:  save_png_return_styler
 #
 #  Function Description:
 #      The function saves the styler object as a png image file then returns it.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  styler  input_styler    The parameter is the input styler object.
 #  string  caption         The parameter is the styler caption.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def save_png_return_styler \
        (input_styler,
         caption):

    if logs_config_dict['image_bool'] == True:

        image_file_path = get_image_file_path(caption, 'png')

        dfi.export(input_styler, image_file_path)


    return input_styler


# In[31]:


#*******************************************************************************************
 #
 #  Function Name:  begin_program
 #
 #  Function Description:
 #      The function prints an announcement for the start of program execution, creates
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
 #  string  prgrm_desig     The parameter is the program designation.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def begin_program(prgrm_desig = ''):

    create_directory(logs_config_dict['logs_folder'])

    create_directory(logs_config_dict['images_folder'])

    set_program_designation(prgrm_desig)


    open_log_file()


    message = 'Program execution begins...\n'

    if logs_config_dict['log_bool'] == True:

        print_and_log_text(message) 


# In[32]:


#*******************************************************************************************
 #
 #  Function Name:  end_program
 #
 #  Function Description:
 #      The function prints an end of program execution announcement, creates the 
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

    current_timestamp = current_timestamp_as_text()

    message = f'Program execution ends at {current_timestamp}.\n\n\n\n'

    if logs_config_dict['log_bool'] == True:

        print_and_log_text(message)

        logs_config_dict['log_txt_file'].close() 


# In[33]:


#*******************************************************************************************
 #
 #  Function Name:  log_write_obj
 #
 #  Function Description:
 #      The function takes an object as a parameter, and, if the global debug flag is true, 
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
 #  object  input_obj       The parameter is the object to be written to the log file.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def log_write_obj(input_obj):

    message = f'\n\n' + str(input_obj) + f'\n\n'

    if logs_config_dict['log_bool'] == True:

        logs_config_dict['log_txt_file'].write(message)


# In[34]:


#*******************************************************************************************
 #
 #  Function Name:  create_directory
 #
 #  Function Description:
 #      The function creates a folder if it does not exist.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  string  directory       The parameter is the directory name.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def create_directory(directory):

    exist_bool = os.path.exists(directory)

    if exist_bool == False:

        os.makedirs(directory)

        print(f'The script created directory, {directory}.\n')


# In[35]:


#*******************************************************************************************
 #
 #  Function Name:  open_log_file
 #
 #  Function Description:
 #      The function opens the log file for appending.  If it does not exist, the 
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

    global logs_config_dict


    current_date = current_date_as_text()

    prgrm_desig = logs_config_dict['prgrm_dsgn']


    logs_config_dict['log_folder'] \
        = logs_config_dict['logs_folder'] + '/' + current_date \
          + prgrm_desig + logs_config_dict['base_log_name']

    if logs_config_dict['log_bool'] == True:

        logs_config_dict['log_txt_file'] = open(logs_config_dict['log_folder'], 'a')


# In[36]:


#*******************************************************************************************
 #
 #  Function Name:  print_and_log_text
 #
 #  Function Description:
 #      The function prints the received message then writes the message to the log file.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  string  message         The parameter is the input message text.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def print_and_log_text(message = ''):

    print(message)

    timepoint_message = current_timepoint_with_message(message)

    if logs_config_dict['log_bool'] == True:

        logs_config_dict['log_txt_file'].write(timepoint_message)    


# In[37]:


#*******************************************************************************************
 #
 #  Function Name:  save_plot_image
 #
 #  Function Description:
 #      The function saves the image of a matplotlib plot to a file.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  string  caption         The parameter is the plot title.
 #  integer dpi_int         The parameter is the dots per square inch for the image.
 #  float   pad_inches_flt  The parameter is the buffer around the plot in inches.
 #  string  image_format    The parameter is the image format (png, html, etc.).
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def save_plot_image \
        (caption = '',
         dpi_int = 300,
         pad_inches_flt = 0.5,
         image_format = 'png'):

    if logs_config_dict['image_bool'] == True:

        image_file_path \
            = get_image_file_path(caption, image_format)

        plt.savefig \
            (image_file_path, 
             dpi = dpi_int, 
             bbox_inches = 'tight', 
             pad_inches = pad_inches_flt)


# In[38]:


#*******************************************************************************************
 #
 #  Function Name:  save_hvplot_image_to_html
 #
 #  Function Description:
 #      The function saves an hvplot to an html file.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  object  hvplot_overlay  The parameter is the input hvplot overlay object.
 #  string  caption         The parameter is the plot title.
 #  integer height_int      The parameter is the plot's height.
 #  integer width_int       The parameter is the plot's width.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def save_hvplot_image_to_html \
        (hvplot_overlay,
         caption = '',
         height_int = 550,
         width_int = 1100):

    if logs_config_dict['image_bool'] == True:

        temp_overlay = copy.copy(hvplot_overlay)

        temp_overlay.opts(width = width_int, height = height_int)

        image_file_path = get_image_file_path(caption, 'html')

        hvplot.save(temp_overlay, image_file_path)


# In[39]:


#*******************************************************************************************
 #
 #  Function Name:  save_plotly_image
 #
 #  Function Description:
 #      The function saves a Plotly image to the images folder.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  object  plotly_figure   The parameter is the Plotly Figure Object.
 #  string  figure_title    The parameter is the figure title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def save_plotly_image \
        (plotly_figure,
         caption):

    if logs_config_dict['image_bool'] == True:

        image_file_path = get_image_file_path(caption, 'png')

        plotly_figure.write_image(image_file_path)


# In[ ]:




