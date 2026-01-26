#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  mathx.py
 #
 #  File Description:
 #      This Python script, mathx.py, contains Python functions for math calculations. 
 #      Here is the list:
 #
 #  return_regression_model_equation_coefficients
 #  return_polynomial_line_series
 #  return_equation_as_string
 #  return_r_squared_value
 #
 #  is_perfect_square
 #  calculate_closest_factors
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  03/04/2024      Initial Development                     Nicholas J. George
 #
 #******************************************************************************************/

import math

import numpy as np
import pandas as pd

pd.options.mode.chained_assignment = None


# In[2]:


CONSTANT_LOCAL_FILE_NAME = 'mathx.py'


# In[3]:


#*******************************************************************************************
 #
 #  Function Name:  return_regression_model_equation_coefficients
 #
 #  Function Description:
 #      This function returns the coefficients for a regression equation using x-y series.
 #
 #
 #  Return Type: list
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  series  x_series        The parameter is the series holding the x values.
 #  series  y_series        The parameter is the series holding the y values.
 #  integer degree_integer  This parameter is the degree of the polynomial.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  03/04/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_regression_model_equation_coefficients \
        (x_series, 
         y_series,
         degree_integer):

    equation_list = np.poly1d(np.polyfit(x_series, y_series, degree_integer))

    return equation_list


# In[4]:


#*******************************************************************************************
 #
 #  Function Name:  return_polynomial_line_series
 #
 #  Function Description:
 #      This function returns a polynomial line as an np array.
 #
 #
 #  Return Type: np array
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  series  x_series        The parameter is the series holding the x values.
 #  series  y_series        The parameter is the series holding the y values.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  03/04/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_polynomial_line_series \
        (x_series, 
         y_series):

    sample_number_integer = abs(int((x_series.max() - y_series.min()) / 2))

    return np.linspace(x_series.min(), x_series.max(), sample_number_integer)


# In[5]:


#*******************************************************************************************
 #
 #  Function Name:  return_equation_as_string
 #
 #  Function Description:
 #      This function returns the model equation as a string.
 #
 #
 #  Return Type: string
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  list    model_equation_list
 #                          The parameter is a list of coefficients for a polynomial.
 #  integer coefficient_precision_integer
 #                          The parameter is the precision of the equation's coefficients.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  03/04/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_equation_as_string \
        (model_equation_list,
         coefficient_precision_integer = 4):

    degree_integer = len(model_equation_list)


    for index, term in enumerate(model_equation_list):

        temp_string = str(round(float(term), coefficient_precision_integer))

        if degree_integer > 1:

            temp_string = temp_string + 'x' + '^' + str(degree_integer)

        elif degree_integer == 1:

            temp_string = temp_string + 'x'

        if degree_integer == len(model_equation_list):

            equation_string = temp_string

        else:

            equation_string = equation_string + ' + ' + temp_string

        degree_integer -= 1


    equation_string = 'y = ' + equation_string


    return equation_string


# In[6]:


#*******************************************************************************************
 #
 #  Function Name:  return_r_squared_value
 #
 #  Function Description:
 #      This function returns the r-squared value from x-y series.
 #
 #
 #  Return Type: float
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  series  x_series        The parameter is the series holding the x values.
 #  series  y_series        The parameter is the series holding the y values.
 #  integer degree_integer  This parameter is the degree of the polynomial.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  03/04/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_r_squared_value \
        (x_series, 
         y_series, 
         degree_integer):

    coefficients_float_nparray = np.polyfit(x_series, y_series, degree_integer)

    pPoly1D = np.poly1d(coefficients_float_nparray)


    yhatList = pPoly1D(x_series)

    ybar_float = y_series.sum() / len(y_series)


    ssreg_float = ((yhatList - ybar_float) ** 2).sum()

    sstot_float = ((y_series - ybar_float) ** 2).sum()


    return ssreg_float / sstot_float


# In[7]:


#*******************************************************************************************
 #
 #  Function Name:  is_perfect_square
 #
 #  Function Description:
 #      This function indicates whether the input is a perfect square.
 #
 #
 #  Return Type: boolean
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  integer positive_integer
 #                          The parameter is the input integer.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  03/04/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def is_perfect_square(positive_integer):

    positive_integer = int(positive_integer)


    if positive_integer < 0:

        return False

    elif positive_integer >= 0 and positive_integer <= 1:

        return True


    x_integer = positive_integer // 2

    seen = set([x_integer])


    while x_integer * x_integer != positive_integer:

        x_integer = (x_integer + (positive_integer // x_integer)) // 2

        if x_integer in seen: 

            return False

        seen.add(x_integer)


    return True


# In[8]:


#*******************************************************************************************
 #
 #  Function Name:  calculate_closest_factors
 #
 #  Function Description:
 #      This function calculates the closest factors of an integer.
 #
 #
 #  Return Type: boolean
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  integer
 #          positive_integer
 #                          The parameter is the input integer.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  03/04/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def calculate_closest_factors(positive_integer):

    positive_integer = int(positive_integer)

    if positive_integer <= 0:

        return [0, 0]


    a_integer, b_integer, i_integer = 1, positive_integer, 0


    while a_integer < b_integer:

        i_integer += 1

        if positive_integer % i_integer == 0:

            a_integer = i_integer

            b_integer = positive_integer // a_integer


    if positive_integer > 2 and a_integer > b_integer:

        a_integer, b_integer = b_integer, a_integer


    return [b_integer, a_integer]


# In[ ]:




