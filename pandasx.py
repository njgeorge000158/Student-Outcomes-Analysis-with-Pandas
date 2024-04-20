#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#*******************************************************************************************
 #
 #  File Name:  pandasx.py
 #
 #  File Description:
 #      This Python script, pandasx.py, contains Python functions for processing 
 #      Pandas data structures. Here is the list:
 #
 #      return_standard_format_styler
 #      save_image_and_return_styler
 #      return_formatted_table
 #      return_summary_statistics_as_dataframe
 #      return_formatted_rows
 #      return_dataframe_description
 #      return_formatted_description
 #
 #      display_dataframe_column_counts
 #      display_dataframe_column_unique_values
 #      display_series_unique_value_counts
 #
 #      display_dataframe_hvplot
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  04/11/2024      Initial Development                     Nicholas J. George
 #
 #******************************************************************************************/

import logx_constants
import logx

import hvplot.pandas
import dataframe_image

import pandas as pd

pd.options.mode.chained_assignment = None


# In[ ]:


CONSTANT_LOCAL_FILE_NAME = 'pandasx.py'


# In[ ]:


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
 #          input_dataframe The parameter is the input dataframe.
 #  string  caption_string  The parameter is the table caption.
 #  integer precision_integer
 #                          This optional parameter is the decimal place 
 #                          precision of the displayed numbers.
 #  boolean hide_index_boolean
 #                          This optional parameter indicates whether the
 #                          index column is hidden or not.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_standard_format_styler \
        (input_dataframe,
         caption_string,
         precision_integer = 2,
         hide_index_boolean = True):
    
    temp_dataframe = input_dataframe.copy()
        
        
    if hide_index_boolean == True:
            
        return \
            temp_dataframe \
                .style \
                .set_caption(caption_string) \
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
                    (precision = precision_integer, 
                     thousands = ',', 
                     decimal = '.') \
                .hide()
            
    else:
            
        return \
            temp_dataframe \
                .style \
                .set_caption(caption_string) \
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
                    (precision = precision_integer, 
                     thousands = ',', 
                     decimal = '.')


# In[ ]:


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
 #  styler  input_styler    The parameter is the input styler object.
 #  string  caption_string  The parameter is the table caption.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def save_image_and_return_styler \
        (input_styler,
         caption_string):
    
    if logx_constants.IMAGE_FLAG == True:

        image_file_path_string = logx.get_image_file_path(caption_string, 'png')
            
        dataframe_image.export \
            (input_styler, image_file_path_string, max_rows = -1, max_cols = -1)
        
    return input_styler


# In[ ]:


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
 #          input_dataframe The parameter is the input dataframe.
 #  string  caption_string  The parameter is the table caption.
 #  integer line_count_integer
 #                          The parameter is the number of displayed records.
 #  boolean hide_index_boolean
 #                          The parameter indicates whether the index is present.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
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

    return save_image_and_return_styler(current_styler, caption_string)


# In[ ]:


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
 #  series  data_series     The parameter is the input series.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_summary_statistics_as_dataframe(data_series):

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
        = data_series.loc[(data_series < lower_bound_float) | (data_series > upper_bound_float)]
        
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


# In[ ]:


#*******************************************************************************************
 #
 #  Function Name:  return_formatted_rows
 #
 #  Function Description:
 #      This function formats the rows in a pandas styler and returns it.
 #
 #
 #  Return Type: styler
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  styler  input_styler    The parameter is the input styler.
 #  dictionary
 #          format_dictionary
 #                          The parameter is the dicitionary with the format specifications.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_formatted_rows \
        (input_styler, 
         format_dictionary):
    
    for key, value in format_dictionary.items():
        
        row_number = input_styler.index.get_loc(key)

        for column_number in range(len(input_styler.columns)):
            
            input_styler._display_funcs[(row_number, column_number)] = value
            
            
    return input_styler


# In[ ]:


#*******************************************************************************************
 #
 #  Function Name:  return_dataframe_description
 #
 #  Function Description:
 #      This function takes a dataframe and returns the its formatted data statistics.
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
 #          input_dataframe The parameter is the input dataframe.
 #  string  caption_string  The parameter is the text for the caption.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_dataframe_description \
        (input_dataframe,
         caption_string):
    
    description_dataframe = input_dataframe.describe()
    
    format_dictionary \
        = {'count': lambda x: f'{x:,.0f}',
           'mean': lambda x: f'{x:,.2f}',
           'std': lambda x: f'{x:,.2f}',
           'min': lambda x: f'{x:,.0f}',
           '25%': lambda x: f'{x:,.2f}',
           '50%': lambda x: f'{x:,.2f}',
           '75%': lambda x: f'{x:,.2f}',
           'max': lambda x: f'{x:,.0f}'}

    description_styler \
        = return_formatted_rows(description_dataframe.style, format_dictionary)
        
    description_styler \
        .set_caption(caption_string) \
        .set_table_styles \
            ([{'selector': 'caption', 
               'props': [('color', 'black'), 
                         ('font-size', '16px'),
                         ('font-style', 'bold'),
                         ('text-align', 'center')]}]) \
        .set_properties \
            (**{'text-align': 'center',
                'border': '1.3px solid red',
                'color': 'blue'})
            
    return description_styler


# In[ ]:


#*******************************************************************************************
 #
 #  Function Name:  return_formatted_description
 #
 #  Function Description:
 #      This function returns a formatted dataframe description.
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
 #          input_dataframe The parameter is the input dataframe.
 #  string  caption_string  The parameter is the text for the caption.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_formatted_description \
        (input_dataframe,
         caption_string):

    current_styler = return_dataframe_description(input_dataframe, caption_string)

    return save_image_and_return_styler(current_styler, caption_string)


# In[ ]:


#*******************************************************************************************
 #
 #  Function Name:  display_dataframe_column_counts
 #
 #  Function Description:
 #      This function displays a dataframe's column counts.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  dataframe
 #          input_dataframe The parameter is the input dataframe.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def display_dataframe_column_counts(input_dataframe):

    for i, column in enumerate(student_loan_dataframe.columns):
        
        count_integer = student_loan_dataframe[column].nunique()
        
        logx.print_and_log_text \
            ('\033[1m' + f'{column}: ' + '{:,}\n'.format(count_integer) + '\033[0m')


# In[ ]:


#*******************************************************************************************
 #
 #  Function Name:  display_dataframe_column_unique_values
 #
 #  Function Description:
 #      This function displays the dataframe column unique values.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  dataframe
 #          input_dataframe The parameter is the input dataframe.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def display_dataframe_column_unique_values(input_dataframe):

    for i, column in enumerate(input_dataframe.columns):
        
        value_string_list = input_dataframe[column].unique().tolist()
        
        logx.print_and_log_text \
            ('\033[1m' + f'{column}:\n'
             + f'{sorted(value_string_list, reverse = False)}\n\n'
             + '\033[0m')


# In[ ]:


#*******************************************************************************************
 #
 #  Function Name:  display_series_unique_value_counts
 #
 #  Function Description:
 #      This function displays the sorted unique value count of a series then returns
 #      the sorted series.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  dataframe
 #          input_dataframe The parameter is the input dataframe.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def display_series_unique_value_counts \
        (input_series,
         series_name_string = 'output_series'):

    output_series = input_series.value_counts().sort_values(ascending = False)

    output_series.name = series_name_string

    for i, v in output_series.items():

        logx.print_and_log_text('\033[1m' + str(i) + '\t' + str(v) + '\n' + '\033[0m')


    return output_series


# In[ ]:


#******************************************************************************************
 #
 #  Function Name:  display_dataframe_hvplot
 #
 #  Function Description:
 #      This function receives a dataframe and displays a formatted hvplot.
 #
 #
 #  Return Type: hvplot overlay
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  dataframe
 #          input_dataframe The parameter is the input dataframe.
 #  string  caption_string  The parameter is the plot's title.
 #  string  color_column_name_string
 #                          The parameter is the color column name.
 #  string  size_column_name_string
 #                          The parameter is the size column name.
 #  float   longitude_column_string_name
 #                          The parameter is the longitude column name.
 #  float   latitude_column_string_name
 #                          The parameter is the latitude column name.
 #  string  x_label_string  The parameter is the x-axis label.
 #  string  y_label_string  The parameter is the y-axis label.
 #  float tuple
 #          x_limit_float_tuple
 #                          The parameter the HVPlot limits for the x-axis.
 #  float tuple
 #          y_limit_float_tuple
 #                          The parameter the HVPlot limits for the y-axis.
 #  float   alpha_float     The parameter the alpha value for the markers.
 #  string  tiles_string
 #                          The parameter indicates the type of map (OSM, ESRI, etc.).
 #  string list
 #          hover_columns_string_list
 #                          The parameter is the list of column names 
 #                          for the hover message.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def display_dataframe_hvplot \
        (input_dataframe,
         caption_string,
         color_column_name_string,
         size_column_name_string,
         longitude_column_string_name,
         latitude_column_string_name,
         x_label_string = '',
         y_label_string = '',
         x_limit_float_tuple = (-180, 180), 
         y_limit_float_tuple = (-55, 75),
         alpha_float = 0.7,
         tiles_string = 'OSM',
         hover_columns_string_list = []):
    
    hvplot_overlay \
        = input_dataframe \
            .hvplot \
            .points \
                (longitude_column_string_name, 
                 latitude_column_string_name,
                 xlabel = x_label_string, 
                 ylabel = y_label_string,
                 geo = True, 
                 color = color_column_name_string, 
                 size = size_column_name_string,
                 xlim = x_limit_float_tuple, 
                 ylim = y_limit_float_tuple,
                 alpha = alpha_float, 
                 tiles = tiles_string,
                 title = caption_string,
                 hover_cols = hover_columns_string_list)

        
    logx.save_hvplot_image_to_html(hvplot_overlay, caption_string)

    
    return hvplot_overlay


# In[ ]:




