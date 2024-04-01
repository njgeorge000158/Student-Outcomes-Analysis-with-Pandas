#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  error_handle_functions.py
 #
 #  File Description:
 #      This Python script, error_handle_functions.py, contains generic Python functions
 #      for handling and checking for errors.  Here is the list:
 #
 #  find_min_max_from_enumeration
 #  check_parameter_data_type
 #  check_parameter_length
 #  check_enumeration_parameter_range
 #  check_parameters_for_errors
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  02/21/2024      Initial Development                     N. James George
 #
 #******************************************************************************************/
    
import log_subroutines
    
import pandas as pd

from enum import Enum
from enum import EnumType
    
pd.options.mode.chained_assignment = None


# In[2]:


CONSTANT_LOCAL_FILE_NAME = 'error_handle_functions.py'


# In[3]:


#*******************************************************************************************
 #
 #  Function Name:  find_min_max_from_enumeration
 #
 #  Function Description:
 #      This function returns the minimum and maximum enumeration constants.
 #
 #
 #  Return Type: integer
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  enum.Enum
 #          input_enumeration
 #                          This parameter is the input enumeration data structure.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/21/2024          Initial Development                         N. James George
 #
 #******************************************************************************************/

def find_min_max_from_enumeration(input_enumeration):
    
    enumeration_range_integer_list \
        = sorted(list(map(lambda x: x.value, list(input_enumeration))))
            
    minimum_value_integer \
        = enumeration_range_integer_list[0]
            
    maximum_value_integer \
        = enumeration_range_integer_list \
            [len(enumeration_range_integer_list)-1]
    
    return minimum_value_integer, maximum_value_integer


# In[4]:


#*******************************************************************************************
 #
 #  Function Name:  check_parameter_data_type
 #
 #  Function Description:
 #      This function checks for invalid function parameter data types.
 #
 #
 #  Return Type: boolean
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  dictionary
 #          input_dictionary)
 #                          This parameter is the input dictionary and has the following
 #                          structure: {'parameter_name': 
 #                                         [parameter, data_type, enumeration or data_type].
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/21/2024          Initial Development                         N. James George
 #
 #******************************************************************************************/

def check_parameter_data_type(input_dictionary):
    
    for value_list in input_dictionary.values():
        
        if isinstance(value_list[0], value_list[1]) == False:
            
            return True
        
    return False


# In[5]:


#*******************************************************************************************
 #
 #  Function Name:  check_parameter_length
 #
 #  Function Description:
 #      This function checks for invalid function parameter string, enumeration, Series, 
 #      or DataFrame lengths.
 #
 #
 #  Return Type: boolean
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  dictionary
 #          input_dictionary
 #                          This parameter is the input dictionary and has the following
 #                          structure: {'parameter_name': 
 #                                         [parameter, data_type, enumeration or data_type].
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/21/2024          Initial Development                         N. James George
 #
 #******************************************************************************************/

def check_parameter_length(input_dictionary):
    
    for value_list in input_dictionary.values():
        
        if value_list[1] != int \
            and value_list[1] != float \
            and value_list[1] != bool:
            
            if len(value_list[0]) <= 0:
            
                return True
        
    return False


# In[6]:


#*******************************************************************************************
 #
 #  Function Name:  check_enumeration_parameter_range
 #
 #  Function Description:
 #      This function checks for invalid function parameter enumeration constants.
 #
 #
 #  Return Type: boolean
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  dictionary
 #          input_dictionary
 #                          This parameter is the input dictionary and has the following
 #                          structure: {'parameter_name': 
 #                                         [parameter, data_type, enumeration or data_type].
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/21/2024          Initial Development                         N. James George
 #
 #******************************************************************************************/

def check_enumeration_parameter_range(input_dictionary):
    
    for key, value in input_dictionary.items():
    
        if type(value[2]) == EnumType:
            
            minimum_value_integer, maximum_value_integer \
                = find_min_max_from_enumeration \
                    (value[2])
            
            if value[0] > maximum_value_integer \
                or value[0] <= minimum_value_integer:
                
                return True
            
    return False


# In[7]:


#*******************************************************************************************
 #
 #  Function Name:  check_parameters_for_errors
 #
 #  Function Description:
 #      This function checks for invalid function parameters.
 #
 #
 #  Return Type: boolean
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  dictionary
 #          input_dictionary
 #                          This parameter is the input dictionary and has the following
 #                          structure: {'parameter_name': 
 #                                         [parameter, data_type, enumeration or data_type].
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/21/2024          Initial Development                         N. James George
 #
 #******************************************************************************************/

def check_parameters_for_errors(input_dictionary):
    
    invalid_boolean = False
    
    if check_parameter_data_type(input_dictionary):
        
        message_string = 'received invalid function parameter data types:\n'
        
        invalid_boolean = True
    
    elif check_parameter_length(input_dictionary):
        
        message_string = 'received empty function parameters:\n'
        
        invalid_boolean = True
    
    elif check_enumeration_parameter_range(input_dictionary):
        
        message_string \
            = 'received out-of-range enumeration constants as function parameters:\n'
        
        invalid_boolean = True
        
        
    if invalid_boolean == True:
        
        log_subroutines \
            .print_and_log_text \
                ('\033[1m'
                 + '\nThe function, check_parameters_for_errors, ' 
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, ' 
                 + f'{message_string}'
                 + '\033[0m')
        
        for key, value in input_dictionary.items():
            
            log_subroutines \
                .print_and_log_text \
                    ('\033[1m'
                     + f'{key} / {value[0]} / {value[1]} / {value[2]}\n\n' 
                     + '\033[0m')

            
    return invalid_boolean


# In[ ]:




