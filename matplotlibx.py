#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  matplotlibx.py
 #
 #  File Description:
 #      The Python script, matplotlibx.py, contains generic Python functions
 #      for matplotlib charts and processing.  Here is the list:
 #
 #  display_linear_regression_line
 #  display_regression_line
 #
 #  display_line_chart_from_xy_series
 #  display_line_chart_from_dataframe
 #  display_stacked_line_subplots
 #
 #  display_boxplots_from_series_list
 #  display_boxplot_from_dataframe
 #
 #  display_bar_chart_from_series
 #  display_bar_chart_from_dataframe
 #  
 #  display_scatter_plot_from_xy_series
 #  display_multiple_scatter_plots_from_xy_series_list
 #
 #  display_pie_chart_from_series
 #  display_multiple_pie_charts_from_dataframe
 #
 #  display_histogram_from_series
 #  display_histograms_from_series_list
 #  display_multiple_histograms_from_dataframe
 #
 #  display_plot_from_series
 #  display_plots_from_series_list
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  08/18/2023      Initial Development                     Nicholas J. George
 #
 #******************************************************************************************/

import logx
import mathx

import math

import matplotlib.pyplot as plt
import pandas as pd

from scipy import stats

pd.options.mode.chained_assignment = None


# In[2]:


CONSTANT_LOCAL_FILE_NAME = 'matplotlibx.py'


# In[3]:


#*******************************************************************************************
 #
 #  Function Name:  display_linear_regression_line
 #
 #  Function Description:
 #      The function displays a linear regression line.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  series  x_series        The parameter is the x-axis series.
 #  series  y_series        The parameter is the y-axis series.
 #  float   x_coordinate_float
 #                          The parameter is the x-coordinate of the text.   
 #  float   y_coordinate_float
 #                          The parameter is the y-coordinate of the text.  
 #  string  line_color_string
 #                          The parameter is the line color.
 #  string  line_width_float
 #                          The parameter is the line type.
 #  float   alpha_float     The parameter is the alpha (transparency) value.  
 #  integer coefficient_precision_integer
 #                          The parameter is the equation coefficient precision. 
 #  float   font_size_float The parameter is the equation's font size. 
 #  string  font_weight_string
 #                          The parameter is the equation's font weight.
 #  string  font_color_string
 #                          The parameter is the equation's font color.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def display_linear_regression_line \
        (x_series,
         y_series,
         x_coordinate_float,
         y_coordinate_float,
         line_color_string = 'red',
         line_width_float = 3.0,
         alpha_float = 1.0,
         coefficient_precision_integer = 4,
         font_size_float = 16.0,
         font_weight_string = 'bold',
         font_color_string = 'blue'):

    (slope, intercept, rvalue, pvalue, stderr) = stats.linregress(x_series, y_series)

    linear_regression_series = (x_series * slope) + intercept

    r_squared_float = rvalue * rvalue


    plt.plot \
        (x_series,
         linear_regression_series,
         color = line_color_string,
         linewidth = line_width_float,
         alpha = alpha_float)

    linear_equation_string \
        = 'y = ' + str(round(slope, coefficient_precision_integer)) \
          + 'x + ' + str(round(intercept, coefficient_precision_integer))

    plt.annotate \
        (linear_equation_string,
         (x_coordinate_float, y_coordinate_float),
         fontsize = font_size_float,
         fontweight = font_weight_string,
         color = font_color_string)   


    logx.print_and_log_text('r-value:     {:.4f}'.format(rvalue))

    logx.print_and_log_text('r-squared:   {:.4f}\n'.format(r_squared_float))


# In[4]:


#*******************************************************************************************
 #
 #  Function Name:  display_polynomial_regression_line
 #
 #  Function Description:
 #      The function displays a single line chart from an x and y series and criteria.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  series  x_series        The parameter is the x-axis series.
 #  series  y_series        The parameter is the y-axis series.
 #  float   x_coordinate_float
 #                          The parameter is the x-coordinate of the text.   
 #  float   y_coordinate_float
 #                          The parameter is the y-coordinate of the text.
 #  integer degree_integer  The parameter is the regression polynomial degree.
 #  string  line_color_string
 #                          The parameter is the line color.
 #  string  line_width_float
 #                          The parameter is the line type.
 #  float   alpha_float     The parameter is the alpha (transparency) value.  
 #  integer coefficient_precision_integer
 #                          The parameter is the equation coefficient precision. 
 #  float   font_size_float The parameter is the equation's font size. 
 #  string  font_weight_string
 #                          The parameter is the equation's font weight.
 #  string  font_color_string
 #                          The parameter is the equation's font color.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def display_polynomial_regression_line \
        (x_series,
         y_series,
         x_coordinate_float,
         y_coordinate_float,
         degree_integer,
         line_color_string = 'red',
         line_width_float = 3.0,
         alpha_float = 1.0,
         coefficient_precision_integer = 4,
         font_size_float = 16.0,
         font_weight_string = 'bold',
         font_color_string = 'blue'):

    model_equation_list \
        = mathx.return_regression_model_equation_coefficients \
            (x_series, y_series, degree_integer)

    polynomial_line_series = mathx.return_polynomial_line_series(x_series, y_series)

    plt.plot \
        (polynomial_line_series, 
         model_equation_list(polynomial_line_series),
         color = line_color_string,
         linewidth = line_width_float,
         alpha = alpha_float)


    equation_label_string = mathx.return_equation_as_string(model_equation_list)

    plt.annotate \
        (equation_label_string,
         (x_coordinate_float, y_coordinate_float),
          fontsize = font_size_float,
          fontweight = font_weight_string,
          color = font_color_string)


    r_squared_float = mathx.return_r_squared_value(x_series, y_series, degree_integer)

    r_value_float = math.sqrt(r_squared_float)


    logx.print_and_log_text('r-value:     {:.4f}'.format(r_value_float))

    logx.print_and_log_text('r-squared:   {:.4f}'.format(r_squared_float))


# In[5]:


#*******************************************************************************************
 #
 #  Function Name:  display_line_chart_from_xy_series
 #
 #  Function Description:
 #      The function displays a single line chart from an x and y series and criteria.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  series  x_series        The parameter is the x-axis series.
 #  series  y_series        The parameter is the y-axis series.
 #  string  title_string    The parameter is the chart title.
 #  string  xlabel_string   The parameter is the x-axis label.
 #  string  ylabel_string   The parameter is the y-axis label.
 #  string  line_color_string
 #                          The parameter is the line color.
 #  string  line_type_string
 #                          The parameter is the line type.
 #  float   alpha_float     The parameter is the alpha (transparency) value.
 #  string  fill_style_string
 #                          The parameter is the line fills style.
 #  float   line_width_float
 #                          The parameter is the line width.       
 #  string  marker_string   The parameter is the marker type.
 #  string  marker_face_color_string
 #                          The parameter is the marker face color.
 #  string  marker_edge_color_string
 #                          The parameter is the marker edge color.
 #  float   marker_size_float
 #                          The parameter is the marker size.
 #  float   marker_edge_width_float
 #                          The parameter is the marker edge width. 
 #  float   title_font_size_float
 #                          The parameter is the title font size. 
 #  string  title_font_style_string
 #                          The parameter is the title font style.
 #  float   title_pad_float The parameter is the title space pad value. 
 #  float   xlabel_font_size_float
 #                          The parameter is the x-axis font size. 
 #  string  xlabel_font_style_string
 #                          The parameter is the x-axis font style.
 #  float   xlabel_pad_float
 #                          The parameter is the x-axis space pad value. 
 #  float   ylabel_font_size_float
 #                          The parameter is the y-axis font size. 
 #  string  ylabel_font_style_string
 #                          The parameter is the y-axis font style.
 #  float   ylabel_pad_float
 #                          The parameter is the y-axis space pad value. 
 #  float   xticks_font_size_float
 #                          The parameter is the x-axis tick font size. 
 #  float   yticks_font_size_float
 #                          The parameter is the y-axis tick font size. 
 #  float   figure_width_float
 #                          The parameter is the figure width. 
 #  float   figure_length_float
 #                          The parameter is the figure length. 
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def display_line_chart_from_xy_series \
        (x_series,
         y_series,
         title_string,
         xlabel_string,
         ylabel_string,
         line_color_string = 'darkslategray',
         line_type_string = 'solid',
         alpha_float = 1.0,
         fill_style_string = 'full',
         line_width_float = 3.0,
         marker_string = 'o',
         marker_face_color_string = 'red',
         marker_edge_color_string = 'black',
         marker_size_float = 10.0,
         marker_edge_width_float = 1.0,
         title_font_size_float = 20.0,
         title_font_style_string = 'normal',
         title_pad_float = 20.0,
         xlabel_font_size_float = 16.0,
         xlabel_font_style_string = 'normal',
         xlabel_pad_float = 10.0,
         ylabel_font_size_float = 16.0,
         ylabel_font_style_string = 'normal',
         ylabel_pad_float = 10.0,
         xticks_font_size_float = 14.0,
         xticks_rotation_float = 0.0,
         yticks_font_size_float = 14.0,
         yticks_rotation_float = 0.0,
         figure_width_float = 9.708,
         figure_length_float = 6.0):

    plt.figure(figsize = (figure_width_float, figure_length_float))

    plt.plot \
        (x_series,
         y_series,
         alpha = alpha_float,
         color = line_color_string,
         fillstyle = fill_style_string,
         linewidth = line_width_float,
         marker = marker_string,
         markerfacecolor = marker_face_color_string,
         markeredgecolor = marker_edge_color_string,
         markersize = marker_size_float,
         markeredgewidth = marker_edge_width_float,
         linestyle = line_type_string)

    plt.title \
        (title_string,
         fontdict = {'fontsize': title_font_size_float, 
                     'fontstyle': title_font_style_string},
         pad = title_pad_float)

    plt.xlabel \
        (xlabel_string,
         fontdict = {'fontsize': xlabel_font_size_float,
                     'fontstyle': xlabel_font_style_string},
         labelpad = xlabel_pad_float)

    plt.ylabel \
        (ylabel_string,
         fontdict = {'fontsize': ylabel_font_size_float,
                     'fontstyle': ylabel_font_style_string},
         labelpad = ylabel_pad_float)

    plt.xticks(fontsize = xticks_font_size_float, rotation = xticks_rotation_float)

    plt.yticks(fontsize = yticks_font_size_float, rotation = yticks_rotation_float)


    plt.grid()

    logx.save_plot_image(title_string)

    plt.show()


# In[6]:


#*******************************************************************************************
 #
 #  Function Name:  display_line_chart_from_dataframe
 #
 #  Function Description:
 #      The function displays a chart from a dataframe and criteria.
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
 #  string  title_string    The parameter is the chart title.
 #  list    colors_string_list
 #                          The parameter is the list of colors for the subplots.
 #  string  xlabel_string   The parameter is the x-axis label.
 #  string  ylabel_string   The parameter is the y-axis label.
 #  float   alpha_float     The parameter is the alpha (transparency) value.
 #  string  fill_style_string
 #                          The parameter is the line fills style.
 #  float   line_width_float
 #                          The parameter is the line width.       
 #  string  marker_string   The parameter is the marker type.
 #  string  marker_face_color_string
 #                          The parameter is the marker face color.
 #  string  marker_edge_color_string
 #                          The parameter is the marker edge color.
 #  float   marker_edge_width_float
 #                          The parameter is the marker size.
 #  boolean grid_boolean    The parameter indicates whether the chart displays a grid.
 #  boolean display_legend_boolean
 #                          The parameter indicates whether the legend will be present.
 #  float   title_font_size_float
 #                          The parameter is the title font size. 
 #  string  title_font_style_string
 #                          The parameter is the title font style.
 #  float   title_pad_float The parameter is the title space pad value. 
 #  float   xlabel_font_size_float
 #                          The parameter is the x-axis font size. 
 #  string  xlabel_font_style_string
 #                          The parameter is the x-axis font style.
 #  float   xlabel_pad_float
 #                          The parameter is the x-axis space pad value. 
 #  float   ylabel_font_size_float
 #                          The parameter is the y-axis font size. 
 #  string  ylabel_font_style_string
 #                          The parameter is the y-axis font style.
 #  float   ylabel_pad_float
 #                          The parameter is the y-axis space pad value. 
 #  float   xticks_font_size_float
 #                          The parameter is the subplot's x-tick label's font size.
 #  float   xticks_rotation_float
 #                          The parameter is the subplot's x-tick label's rotation in degrees.
 #  float   yticks_font_size_float
 #                          The parameter is the subplot's y-tick label's font size.
 #  float   yticks_rotation_float
 #                          The parameter is the subplot's y-tick label's rotation in degrees.
 #  string  legend_loc_string
 #                          The parameter is the legend's general location.
 #  float   legend_font_size_float
 #                          The parameter is legend's font size.
 #  tuple   legend_bbox_to_anchor_float_tuple
 #                          The parameter is the legend's xy-coordinates. 
 #  float   figure_width_float
 #                          The parameter is the figure width. 
 #  float   figure_length_float
 #                          The parameter is the figure length. 
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def display_line_chart_from_dataframe \
        (input_dataframe,
         title_string,
         colors_string_list,
         xlabel_string = None,
         ylabel_string = None,
         alpha_float = 0.8,
         fill_style_string = 'full',
         line_width_float = 3.0,
         marker_string = 'o',
         marker_face_color_string = 'red',
         marker_edge_color_string = 'black',
         marker_size_float = 0.0,
         marker_edge_width_float = 1.0,
         grid_boolean = True,
         display_legend_boolean = False,
         title_font_size_float = 16.0,
         title_font_style_string = 'normal',
         title_pad_float = 10.0,
         xlabel_font_size_float = 16.0,
         xlabel_font_style_string = 'normal',
         xlabel_pad_float = 10.0,
         ylabel_font_size_float = 16.0,
         ylabel_font_style_string = 'normal',
         ylabel_pad_float = 10.0,
         xticks_font_size_float = 14.0,
         xticks_rotation_float = 90.0,
         yticks_font_size_float = 14.0,
         yticks_rotation_float = 0.0,
         legend_loc_string = 'center right',
         legend_font_size_float = 14.0,
         legend_bbox_to_anchor_float_tuple = (1.5, 0.5),
         figure_width_float = 9.708,
         figure_length_float = 6.0):

    plt.figure(figsize = (figure_width_float, figure_length_float))

    input_dataframe \
        .plot.line \
            (label = [],
             color = colors_string_list,
             alpha = alpha_float,
             marker = marker_string,
             markerfacecolor = marker_face_color_string,
             markeredgecolor = marker_edge_color_string ,
             markersize = marker_size_float,
             grid = grid_boolean,
             legend = display_legend_boolean)

    plt.title \
        (title_string,
         fontdict = {'fontsize': title_font_size_float, 
                     'fontstyle': title_font_style_string},
         pad = title_pad_float)

    if xlabel_string != None:

        plt.xlabel \
            (xlabel_string,
             fontdict = {'fontsize': xlabel_font_size_float,
                         'fontstyle': xlabel_font_style_string},
             labelpad = xlabel_pad_float)

    if ylabel_string != None:

        plt.ylabel \
            (ylabel_string,
             fontdict = {'fontsize': ylabel_font_size_float,
                         'fontstyle': ylabel_font_style_string},
             labelpad = ylabel_pad_float)

    plt.xticks(fontsize = xticks_font_size_float, rotation = xticks_rotation_float)

    plt.yticks(fontsize = yticks_font_size_float, rotation = yticks_rotation_float)

    if display_legend_boolean == True:

        plt.legend \
            (loc = legend_loc_string,
             fontsize = legend_font_size_float,
             bbox_to_anchor = legend_bbox_to_anchor_float_tuple)


    logx.save_plot_image(title_string)

    plt.show()


# In[7]:


#*******************************************************************************************
 #
 #  Function Name:  display_stacked_line_subplots
 #
 #  Function Description:
 #      The function receives a dictionary of series and formatting parameters 
 #      for the display of stacked line subplots.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  dictionary
 #          input_frame_dictionary
 #                          The parameter is the input dictionary of plot series
 #  string  suptitle_string The parameter is the chart title.
 #  list    colors_string_list
 #                          The parameter is the list of colors for the subplots.
 #  string  supxlabel_string
 #                          The parameter is the title for the figure's x-axis.
 #  string  supylabel_string
 #                          The parameter is the title for the figure's y-axis.
 #  string  xlabel_string   The parameter is the title for the plot's x-axis.
 #  string  ylabel_string   The parameter is the title for the plot's y-axis.
 #  boolean first_ylabel_pad_boolean
 #                          The parameter indicates whether the first subplot 
 #                          should have a different pad value.
 #  float   first_ylabel_pad_float
 #                          The parameter is first subplot pad value.
 #  boolean ylabel_default_boolean
 #                          The parameter indicates whether the y label will 
 #                          have the default value.
 #  boolean display_legend_boolean
 #                          The parameter indicates whether the legend will be present.
 #  string  legend_loc_string
 #                          The parameter is the legend's general location.
 #  float   legend_font_size_float
 #                          The parameter is legend's font size.
 #  tuple   legend_bbox_to_anchor_float_tuple
 #                          The parameter is the legend's xy-coordinates. 
 #  float   suptitle_x_float
 #                          The parameter is the figure title's x-coordinate padding.
 #  float   suptitle_y_float
 #                          The parameter is the figure title's y-coordinate padding.
 #  float   suptitle_font_size_float
 #                          The parameter is the figure title's font size.
 #  string  suptitle_font_weight_string
 #                          The parameter is the figure title's font weight.
 #  float   supxlabel_x_float
 #                          The parameter is the figure's x-axis label's 
 #                          x-coordinate padding.
 #  float   supxlabel_y_float
 #                          The parameter is the figure's x-axis label's 
 #                          y-coordinate padding.
 #  float   supxlabel_font_size_float
 #                          The parameter is the figure's x-axis label's font size.
 #  string  supxlabel_font_weight_string
 #                          The parameter is the figure's x-axis label's font weight.
 #  float   supylabel_x_float
 #                          The parameter is the figure's y-axis label's 
 #                          x-coordinate padding.
 #  float   supylabel_y_float
 #                          The parameter is the figure's y-axis label's 
 #                          y-coordinate padding.
 #  float   supylabel_font_size_float
 #                          The parameter is the figure's y-axis label's font size.
 #  string  supylabel_font_weight_string
 #                          The parameter is the figure's y-axis label's font weight.
 #  float   xlabel_pad_float  
 #                          The parameter is the subplot's x-axis label's padding.
 #  float   xlabel_font_size_float
 #                          The parameter is the subplot's x-axis label's font size.
 #  string  xlabel_loc_string
 #                          The parameter is the subplot's x-axis label's general location.
 #  string  xlabel_font_weight_string
 #                          The parameter is the subplot's x-axis label's font weight.
 #  float   ylabel_pad_float  
 #                          The parameter is the subplot's y-axis label's padding.
 #  float   ylabel_font_size_float
 #                          The parameter is the subplot's y-axis label's font size.
 #  string  ylabel_loc_string
 #                          The parameter is the subplot's y-axis label's general location.
 #  string  ylabel_font_weight_string
 #                          The parameter is the subplot's y-axis label's font weight.
 #  float   xtick_label_size_float
 #                          The parameter is the subplot's x-tick label's font size.
 #  float   xtick_label_rotation_float
 #                          The parameter is the subplot's x-tick label's rotation in degrees.
 #  float   ytick_label_size_float
 #                          The parameter is the subplot's y-tick label's font size.
 #  float   ytick_label_rotation_float
 #                          The parameter is the subplot's y-tick label's rotation in degrees.
 #  float   subplot_width_space_float
 #                          The parameter is the width of the space between subplots.
 #  float   subplot_height_space_float
 #                          The parameter is the width of the space between subplots.
 #  float   figure_width_float
 #                          The parameter is the figure width. 
 #  float   figure_length_float
 #                          The parameter is the figure length. 
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/  

def display_stacked_line_subplots \
        (input_frame_dictionary,
         suptitle_string,
         colors_string_list,
         supxlabel_string = None,
         supylabel_string = None,
         xlabel_string = None,
         ylabel_string = None,
         first_ylabel_pad_boolean = False,
         first_ylabel_pad_float = 4.0,
         ylabel_default_boolean = True,
         display_legend_boolean = True,
         legend_loc_string = 'center right',
         legend_font_size_float = 14.0,
         legend_bbox_to_anchor_float_tuple = (1.12, 0.5),
         suptitle_x_float = 0.5,  
         suptitle_y_float = 1.0,  
         suptitle_font_size_float = 20.0,
         suptitle_font_weight_string = 'normal',
         supxlabel_x_float = 0.5,  
         supxlabel_y_float = -0.15,
         supxlabel_font_size_float = 16.0,
         supxlabel_font_weight_string = 'normal',
         supylabel_x_float = 0.0,  
         supylabel_y_float = 0.5,  
         supylabel_font_size_float = 16.0,
         supylabel_font_weight_string = 'normal',
         xlabel_pad_float = 4.0,
         xlabel_font_size_float = 16.0,
         xlabel_loc_string = 'center',
         xlabel_font_weight_string = 'normal',
         ylabel_pad_float = 4.0,
         ylabel_font_size_float = 16.0,
         ylabel_loc_string = 'center',
         ylabel_font_weight_string = 'normal',
         xtick_label_size_float = 14.0,
         xtick_label_rotation_float = 90.0,
         ytick_label_size_float = 14.0,
         ytick_label_rotation_float = 0.0,
         subplot_width_space_float = None,
         subplot_height_space_float = None,
         figure_width_float = 9.708,
         figure_length_float = 6.0):

    input_dataframe = pd.DataFrame(input_frame_dictionary)

    subplot_count_integer = len(input_dataframe.keys())


    if xlabel_string == None:

        xlabel_string = ''


    fig, axs \
        = plt.subplots \
            (subplot_count_integer, figsize = (figure_width_float, figure_length_float))

    fig.suptitle \
        (suptitle_string,
         x = suptitle_x_float,
         y = suptitle_y_float,
         fontsize = suptitle_font_size_float, 
         fontweight = suptitle_font_weight_string)

    if supxlabel_string != None:

        fig.supxlabel \
            (supxlabel_string,
             x = supxlabel_x_float,
             y = supxlabel_y_float,
             fontsize = supxlabel_font_size_float, 
             fontweight = supxlabel_font_weight_string)

    if supylabel_string != None:

        fig.supylabel \
            (supylabel_string,
             x = supylabel_x_float,
             y = supylabel_y_float,
             fontsize = supylabel_font_size_float, 
             fontweight = supylabel_font_weight_string)


    legend_line_plot_list = []

    legend_line_names_string_list = []


    for index, subplot in enumerate(axs):

        line_subplot, \
            = subplot.plot \
                (input_dataframe.iloc[:,index], color = colors_string_list[index])

        legend_line_plot_list.append(line_subplot)

        legend_line_names_string_list.append(input_dataframe.iloc[:,index].name)

        subplot.grid()


        if index == (subplot_count_integer - 1):

            subplot.set_xlabel \
                (xlabel_string, 
                 labelpad = xlabel_pad_float, 
                 fontsize = xlabel_font_size_float, 
                 loc = xlabel_loc_string, 
                 fontweight = xlabel_font_weight_string)

        else:

            subplot.set_xticklabels(labels = [])


        if ylabel_string == None:

            ylabel_string = input_dataframe.iloc[:,index].name


        if index == 0 and first_ylabel_pad_boolean == True:

            subplot.set_ylabel \
                (ylabel_string, 
                 labelpad = first_ylabel_pad_float, 
                 fontsize = ylabel_font_size_float, 
                 loc = ylabel_loc_string, 
                 fontweight = ylabel_font_weight_string)

        else:

            subplot.set_ylabel \
                (ylabel_string, 
                 labelpad = ylabel_pad_float, 
                 fontsize = ylabel_font_size_float, 
                 loc = ylabel_loc_string, 
                 fontweight = ylabel_font_weight_string)


        subplot.tick_params \
            (axis = 'x', 
             labelrotation = xtick_label_rotation_float, 
             labelsize = xtick_label_size_float)

        subplot.tick_params \
            (axis = 'y', 
             labelrotation = ytick_label_rotation_float, 
             labelsize = ytick_label_size_float)


    if display_legend_boolean == True:

        fig.legend \
            (legend_line_plot_list, 
             legend_line_names_string_list, 
             loc = legend_loc_string,
             fontsize = legend_font_size_float,
             bbox_to_anchor = legend_bbox_to_anchor_float_tuple)


    plt.subplots_adjust \
        (wspace = subplot_width_space_float, 
         hspace = subplot_height_space_float)


    logx.save_plot_image(suptitle_string)

    plt.show()


# In[8]:


#*******************************************************************************************
 #
 #  Function Name:  display_boxplots_from_series_list
 #
 #  Function Description:
 #      The function displays a box plot from a list of series.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  list    input_series_list
 #                          The parameter is the input series list.
 #  list    xticks_label_string_list
 #                          The parameter is the list of a-axis tick labels.
 #  string  title_string    The parameter is the chart title.
 #  string  xlabel_string   The parameter is the x-axis label.
 #  string  ylabel_string   The parameter is the y-axis label.
 #  float   box_widths_float
 #                          The parameter is the width of boxes in the chart.    
 #  boolean mean_line_boolean
 #                          The parameter indicates whether the mean lines are present.
 #  boolean show_means_boolean
 #                          The parameter indicates whether the means are present.
 #  boolean vertical_boolean
 #                          The parameter indicates whether the boxplot is vertical.
 #  float   title_font_size_float
 #                          The parameter is the title font size. 
 #  string  title_font_style_string
 #                          The parameter is the title font style.
 #  float   title_pad_float The parameter is the title space pad value. 
 #  float   xlabel_font_size_float
 #                          The parameter is the x-axis font size. 
 #  string  xlabel_font_style_string
 #                          The parameter is the x-axis font style.
 #  float   xlabel_pad_float
 #                          The parameter is the x-axis space pad value. 
 #  float   ylabel_font_size_float
 #                          The parameter is the y-axis font size. 
 #  string  ylabel_font_style_string
 #                          The parameter is the y-axis font style.
 #  float   ylabel_pad_float
 #                          The parameter is the y-axis space pad value. 
 #  float   xticks_font_size_float
 #                          The parameter is the x-axis tick font size. 
 #  float   xticks_rotation_float
 #                          The parameter is the x-axis tick rotation in degrees.
 #  float   figure_width_float
 #                          The parameter is the figure width. 
 #  float   figure_length_float
 #                          The parameter is the figure length. 
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def display_boxplots_from_series_list \
        (input_series_list,
         xticks_label_string_list,
         title_string,
         xlabel_string = '',
         ylabel_string = '',
         box_widths_float = 0.45,
         mean_line_boolean = True,
         show_means_boolean = True,
         vertical_boolean = True,
         title_font_size_float = 20.0,
         title_font_style_string = 'normal',
         title_pad_float = 20.0,
         xlabel_font_size_float = 16.0,
         xlabel_font_style_string = 'normal',
         xlabel_pad_float = 10.0,
         ylabel_font_size_float = 16.0,
         ylabel_font_style_string = 'normal',
         ylabel_pad_float = 10.0,
         xticks_font_size_float = 14.0,
         xticks_rotation_float = 0.0,
         figure_width_float = 9.708,
         figure_length_float = 6.0):

    fig1, axs = plt.subplots(figsize = (figure_width_float, figure_length_float))

    axs.boxplot \
        (input_series_list,
         vert = vertical_boolean,
         widths = box_widths_float,
         meanline = mean_line_boolean, 
         showmeans = show_means_boolean)

    axs.set_title \
        (title_string,
         fontdict = {'fontsize': title_font_size_float, 
                     'fontstyle': title_font_style_string},
         pad = title_pad_float)

    axs.set_xlabel \
        (xlabel_string,
         fontdict = {'fontsize': xlabel_font_size_float, 
                     'fontstyle': xlabel_font_style_string},
         labelpad = xlabel_pad_float)

    axs.set_ylabel \
        (ylabel_string,
         fontdict = {'fontsize': ylabel_font_size_float, 
                     'fontstyle': ylabel_font_style_string},
         labelpad = ylabel_pad_float)


    ticks_index_integer_list = []

    for index, regimen in enumerate(xticks_label_string_list):

        ticks_index_integer_list.append(index + 1)


    axs.set_xticks \
        (ticks_index_integer_list, 
         xticks_label_string_list,
         fontsize = xticks_font_size_float,
         rotation = xticks_rotation_float)


    if vertical_boolean == True:

        plt.grid(axis = 'y')

    else:

        plt.grid(axis = 'x')


    logx.save_plot_image(title_string)

    plt.show()


# In[9]:


#*******************************************************************************************
 #
 #  Function Name:  display_boxplot_from_dataframe
 #
 #  Function Description:
 #      The function displays a box plot from a dataframe.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  list    input_dataframe The parameter is the input dataframe.
 #  string  x_column_string The parameter is the dataframe column with the x-variable data.
 #  string  y_column_string The parameter is the dataframe column with the y-variable data.
 #  string  suptitle_string The parameter is the figure title.
 #  string  title_string    The parameter is the chart title.
 #  string  xlabel_string   The parameter is the x-axis label.
 #  string  ylabel_string   The parameter is the y-axis label.
 #  float   box_widths_float
 #                          The parameter is the width of boxes in the chart.    
 #  boolean mean_line_boolean
 #                          The parameter indicates whether the mean lines are present.
 #  boolean show_means_boolean
 #                          The parameter indicates whether the means are present.
 #  boolean vertical_boolean
 #                          The parameter indicates whether the boxplot is vertical.
 #  boolean grid_boolean    The parameter indicates whether the boxplot displays a grid.
 #  float   suptitle_x_float
 #                          The parameter is the figure title's x-coordinate padding.
 #  float   suptitle_y_float
 #                          The parameter is the figure title's y-coordinate padding.
 #  float   suptitle_font_size_float
 #                          The parameter is the figure title's font size.
 #  string  suptitle_font_weight_string
 #                          The parameter is the figure title's font weight.
 #  float   title_font_size_float
 #                          The parameter is the title font size. 
 #  string  title_font_style_string
 #                          The parameter is the title font style.
 #  float   title_pad_float The parameter is the title space pad value. 
 #  float   xlabel_font_size_float
 #                          The parameter is the x-axis font size. 
 #  string  xlabel_font_style_string
 #                          The parameter is the x-axis font style.
 #  float   xlabel_pad_float
 #                          The parameter is the x-axis space pad value. 
 #  float   ylabel_font_size_float
 #                          The parameter is the y-axis font size. 
 #  string  ylabel_font_style_string
 #                          The parameter is the y-axis font style.
 #  float   ylabel_pad_float
 #                          The parameter is the y-axis space pad value. 
 #  float   xticks_font_size_float
 #                          The parameter is the x-axis tick font size. 
 #  float   xticks_rotation_float
 #                          The parameter is the x-axis tick rotation in degrees. 
 #  float   yticks_font_size_float
 #                          The parameter is the y-axis tick font size. 
 #  float   yticks_rotation_float
 #                          The parameter is the y-axis tick rotation in degrees. 
 #  float   figure_width_float
 #                          The parameter is the figure width. 
 #  float   figure_length_float
 #                          The parameter is the figure length. 
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def display_boxplot_from_dataframe \
        (input_dataframe,
         x_column_string,
         y_column_string,
         suptitle_string = '',
         title_string = '',
         xlabel_string = '',
         ylabel_string = '',
         box_widths_float = 0.45,
         mean_line_boolean = True,
         show_means_boolean = True,
         vertical_boolean = True,
         grid_boolean = True,
         suptitle_x_float = 0.5,  
         suptitle_y_float = 1.01, 
         suptitle_font_size_float = 20.0,
         suptitle_font_style_string = 'normal',
         title_font_size_float = 16.0,
         title_font_style_string = 'normal',
         title_pad_float = 10.0,
         xlabel_font_size_float = 16.0,
         xlabel_font_style_string = 'normal',
         xlabel_pad_float = 10.0,
         ylabel_font_size_float = 16.0,
         ylabel_font_style_string = 'normal',
         ylabel_pad_float = 10.0,
         xticks_font_size_float = 14.0,
         xticks_rotation_float = 90.0,
         yticks_font_size_float = 14.0,
         yticks_rotation_float = 0.0,
         figure_width_float = 9.708,
         figure_length_float = 6.0):


    box_plot_axes \
        = input_dataframe \
            .boxplot \
                (by = x_column_string,
                 column = [y_column_string], 
                 fontsize = xticks_font_size_float,
                 widths = box_widths_float,
                 meanline = mean_line_boolean,
                 showmeans = show_means_boolean,
                 vert = vertical_boolean,
                 grid = grid_boolean,
                 figsize = (figure_width_float, figure_length_float))

    plt.suptitle \
        (suptitle_string,
         x = suptitle_x_float,
         y = suptitle_y_float,
         fontsize = suptitle_font_size_float, 
         fontstyle = suptitle_font_style_string)

    plt.title \
        (title_string,
         fontdict = {'fontsize': title_font_size_float, 
                     'fontstyle': title_font_style_string},
         pad = title_pad_float)

    plt.xlabel \
        (xlabel_string,
         fontdict = {'fontsize': xlabel_font_size_float, 
                     'fontstyle': xlabel_font_style_string},
         labelpad = xlabel_pad_float)

    plt.ylabel \
        (ylabel_string,
         fontdict = {'fontsize': ylabel_font_size_float, 
                     'fontstyle': ylabel_font_style_string},
         labelpad = ylabel_pad_float)


    plt.xticks(fontsize = xticks_font_size_float, rotation = xticks_rotation_float)

    plt.yticks(fontsize = yticks_font_size_float, rotation = yticks_rotation_float)


    logx.save_plot_image(suptitle_string)

    plt.show()


# In[10]:


#*******************************************************************************************
 #
 #  Function Name:  display_bar_chart_from_series
 #
 #  Function Description:
 #      The function displays a bar chart from a series.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  series  input_series    The parameter is the input series.
 #  string  title_string    The parameter is the chart title.
 #  string  xlabel_string   The parameter is the x-axis label.
 #  string  ylabel_string   The parameter is the y-axis label.
 #  list    bar_colors_string_list
 #                          The parameter is the list of bar chart bar colors.
 #  boolean horizontal_boolean
 #                          The parameter indicates whether the bar chart is horizontal.
 #  string  bar_align_string
 #                          The parameter is bar alignment.
 #  string  edge_color_string
 #                          The parameter is the bar edge color.
 #  float   line_width_float
 #                          The parameter is the bar line width.       
 #  float   alpha_float     The parameter is the bar transparency level (0-1.0).
 #  float   bar_width_float The parameter is the bar width.
 #  float   title_font_size_float
 #                          The parameter is the title font size. 
 #  string  title_font_style_string
 #                          The parameter is the title font style.
 #  float   title_pad_float The parameter is the title space pad value. 
 #  float   xlabel_font_size_float
 #                          The parameter is the x-axis font size. 
 #  string  xlabel_font_style_string
 #                          The parameter is the x-axis font style.
 #  float   xlabel_pad_float
 #                          The parameter is the x-axis space pad value. 
 #  float   ylabel_font_size_float
 #                          The parameter is the y-axis font size. 
 #  string  ylabel_font_style_string
 #                          The parameter is the y-axis font style.
 #  float   ylabel_pad_float
 #                          The parameter is the y-axis space pad value. 
 #  float  xtick_label_rotation_float
 #                          The parameter is the x-axis tick rotation. 
 #  float  xtick_font_size_float
 #                          The parameter is the x-axis tick font size.
 #  float  ytick_label_rotation_float
 #                          The parameter is the y-axis tick rotation. 
 #  float  ytick_font_size_float
 #                          The parameter is the y-axis tick font size. 
 #  float  figure_width_float
 #                          The parameter is the figure width. 
 #  float  figure_length_float
 #                          The parameter is the figure length. 
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def display_bar_chart_from_series \
        (input_series,
         title_string,
         xlabel_string,
         ylabel_string,
         bar_colors_string_list,
         horizontal_boolean = False,
         bar_align_string = 'center',
         edge_color_string = 'black',
         line_width_float = 1.5,
         bar_width_float = 0.5,
         alpha_float = 1.0,
         title_font_size_float = 20.0,
         title_font_style_string = 'normal',
         title_pad_float = 20.0,
         xlabel_font_size_float = 16.0,
         xlabel_font_style_string = 'normal',
         xlabel_pad_float = 10.0,
         ylabel_font_size_float = 16.0,
         ylabel_font_style_string = 'normal',
         ylabel_pad_float = 10.0,
         xtick_label_rotation_float = 80.0,
         xtick_font_size_float = 14.0,
         ytick_label_rotation_float = 0.0,
         ytick_font_size_float = 14.0,        
         figure_width_float = 9.708,
         figure_length_float = 6.0):

    plt.figure(figsize = (figure_width_float, figure_length_float))


    if horizontal_boolean == False:

        plt.bar \
            (input_series.keys(),
             input_series,
             align = bar_align_string,
             color = bar_colors_string_list,
             edgecolor = edge_color_string,
             linewidth = line_width_float,
             alpha = alpha_float,
             width = bar_width_float)

    else:

        plt.barh \
            (input_series.keys(),
             input_series,
             align = bar_align_string,
             color = bar_colors_string_list,
             edgecolor = edge_color_string,
             linewidth = line_width_float,
             alpha = alpha_float)


    plt.title \
        (title_string,
         fontdict = {'fontsize': title_font_size_float, 
                     'fontstyle': title_font_style_string},
         pad = title_pad_float)


    plt.xlabel \
        (xlabel_string,
         fontdict = {'fontsize': xlabel_font_size_float, 
                     'fontstyle': xlabel_font_style_string},
         labelpad = xlabel_pad_float)

    plt.ylabel \
        (ylabel_string,
         fontdict = {'fontsize': ylabel_font_size_float, 
                     'fontstyle': ylabel_font_style_string},
         labelpad = ylabel_pad_float)


    plt.xticks \
        (rotation = xtick_label_rotation_float,
         fontsize = xtick_font_size_float)

    plt.yticks \
        (rotation = ytick_label_rotation_float,
         fontsize = ytick_font_size_float)


    plt.grid(axis = 'y')


    logx.save_plot_image(title_string)

    plt.show()


# In[11]:


#*******************************************************************************************
 #
 #  Function Name:  display_bar_chart_from_dataframe
 #
 #  Function Description:
 #      The function displays a bar chart from a dataframe.
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
 #  string  title_string    The parameter is the chart title.
 #  string  xlabel_string   The parameter is the x-axis label.
 #  string  ylabel_string   The parameter is the y-axis label.
 #  list    bar_colors_string_list
 #                          The parameter is the list of bar colors.
 #  boolean stacked_boolean The parameter indicates whether the bar chart is stacked.
 #  boolean legend_boolean  The parameter indicates whether the legend is present.
 #  tuple   legend_bbox_to_anchor_float_tuple
 #                          The parameter is the legend's xy-coordinates. 
 #  string  bar_align_string
 #                          The parameter is bar alignment.
 #  string  edge_color_string
 #                          The parameter is the bar edge color.
 #  float   line_width_float
 #                          The parameter is the bar line width.       
 #  float   alpha_float     The parameter is the bar transparency level (0-1.0).
 #  float   bar_width_float The parameter is the bar width.
 #  float   title_font_size_float
 #                          The parameter is the title font size. 
 #  string  title_font_style_string
 #                          The parameter is the title font style.
 #  float   title_pad_float The parameter is the title space pad value. 
 #  float   xlabel_font_size_float
 #                          The parameter is the x-axis font size. 
 #  string  xlabel_font_style_string
 #                          The parameter is the x-axis font style.
 #  float   xlabel_pad_float
 #                          The parameter is the x-axis space pad value. 
 #  float   ylabel_font_size_float
 #                          The parameter is the y-axis font size. 
 #  string  ylabel_font_style_string
 #                          The parameter is the y-axis font style.
 #  float   ylabel_pad_float
 #                          The parameter is the y-axis space pad value. 
 #  float   xtick_label_rotation_float
 #                          The parameter is the x-axis tick rotation. 
 #  float   xtick_font_size_float
 #                          The parameter is the x-axis tick font size.
 #  float   ytick_label_rotation_float
 #                          The parameter is the y-axis tick rotation. 
 #  float   ytick_font_size_float
 #                          The parameter is the y-axis tick font size. 
 #  float   figure_width_float
 #                          The parameter is the figure width. 
 #  float   figure_length_float
 #                          The parameter is the figure length. 
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def display_bar_chart_from_dataframe \
        (input_dataframe,
         title_string,
         xlabel_string,
         ylabel_string,
         bar_colors_string_list,
         stacked_boolean = False,
         legend_boolean = False,
         legend_bbox_to_anchor_float_tuple = (1.1, 1.05),
         bar_align_string = 'center',
         edge_color_string = 'black',
         line_width_float = 1.5,
         bar_width_float = 0.5,
         alpha_float = 1.0,
         title_font_size_float = 20.0,
         title_font_style_string = 'normal',
         title_pad_float = 20.0,
         xlabel_font_size_float = 16.0,
         xlabel_font_style_string = 'normal',
         xlabel_pad_float = 10.0,
         ylabel_font_size_float = 16.0,
         ylabel_font_style_string = 'normal',
         ylabel_pad_float = 10.0,
         xtick_label_rotation_float = 80.0,
         xtick_font_size_float = 14.0,
         ytick_label_rotation_float = 0.0,
         ytick_font_size_float = 14.0,
         figure_width_float = 9.708,
         figure_length_float = 6.0):

    input_dataframe.plot.bar \
        (stacked = stacked_boolean,
         align = bar_align_string,
         color = bar_colors_string_list,
         edgecolor = edge_color_string,
         linewidth = line_width_float,
         alpha = alpha_float,
         width = bar_width_float, 
         legend = legend_boolean,
         figsize = (figure_width_float, figure_length_float))

    if legend_boolean == True:

        plt.legend \
            (bbox_to_anchor \
                 = (legend_bbox_to_anchor_float_tuple[0], legend_bbox_to_anchor_float_tuple[1]))


    plt.title \
        (title_string,
         fontdict = {'fontsize': title_font_size_float, 
                     'fontstyle': title_font_style_string},
         pad = title_pad_float)

    plt.xlabel \
        (xlabel_string,
         fontdict = {'fontsize': xlabel_font_size_float,
                     'fontstyle': xlabel_font_style_string},
         labelpad = xlabel_pad_float)

    plt.ylabel \
        (ylabel_string,
         fontdict = {'fontsize': ylabel_font_size_float,
                     'fontstyle': ylabel_font_style_string},
         labelpad = ylabel_pad_float)

    plt.xticks \
        (rotation = xtick_label_rotation_float,
         fontsize = xtick_font_size_float)

    plt.yticks \
        (rotation = ytick_label_rotation_float,
         fontsize = ytick_font_size_float)


    plt.grid(axis = 'y')

    logx.save_plot_image(title_string)

    plt.show()


# In[12]:


#*******************************************************************************************
 #
 #  Function Name:  display_scatter_plot_from_xy_series
 #
 #  Function Description:
 #      The function displays a scatter plot from x-y series.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  series  x_series        The parameter is the x-axis series.
 #  series  y_series        The parameter is the y-axis series.
 #  string  title_string    The parameter is the chart title.
 #  string  xlabel_string   The parameter is the x-axis label.
 #  string  ylabel_string   The parameter is the y-axis label.
 #  integer degree_integer  The parameter is the degree of the regression line polynomial.
 #  float   equation_x_coordinate_float
 #                          The parameter is the equation's x-coordinate.  
 #  float   equation_y_coordinate_float
 #                          The parameter is the equation's y-coordinate.  
 #  string  marker_shape_string
 #                          The parameter is marker shape.
 #  float   marker_size_float
 #                          The parameter is the marker size.       
 #  string  marker_color_string
 #                          The parameter is the marker color.
 #  float   line_width_float
 #                          The parameter is line width of the scatter points.
 #  string  edge_colors_string
 #                          The parameter is the edge color for the scatter points.
 #  float   alpha_float
 #                          The parameter is the bar transparency level (0-1.0).
 #  float   title_font_size_float
 #                          The parameter is the title font size. 
 #  string  title_font_style_string
 #                          The parameter is the title font style.
 #  float   title_pad_float
 #                          The parameter is the title space pad value. 
 #  float   xlabel_font_size_float
 #                          The parameter is the x-axis font size. 
 #  string  xlabel_font_style_string
 #                          The parameter is the x-axis font style.
 #  float   xlabel_pad_float
 #                          The parameter is the x-axis space pad value. 
 #  float   ylabel_font_size_float
 #                          The parameter is the y-axis font size. 
 #  string  ylabel_font_style_string
 #                          The parameter is the y-axis font style.
 #  float   ylabel_pad_float
 #                          The parameter is the y-axis space pad value. 
 #  float   xtick_label_rotation_float
 #                          The parameter is the x-axis tick rotation. 
 #  float   xtick_font_size_float
 #                          The parameter is the x-axis tick font size.
 #  float   ytick_label_rotation_float
 #                          The parameter is the y-axis tick rotation. 
 #  float   ytick_font_size_float
 #                          The parameter is the y-axis tick font size. 
 #  float   figure_width_float
 #                          The parameter is the figure width. 
 #  float   figure_length_float
 #                          The parameter is the figure length. 
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def display_scatter_plot_from_xy_series \
        (x_series, 
         y_series, 
         title_string,
         xlabel_string,
         ylabel_string,
         degree_integer = 0,
         equation_x_coordinate_float = 0.0,
         equation_y_coordinate_float = 0.0,
         marker_shape_string = 'o',
         marker_size_float = 80.0,
         marker_color_string = 'lime',
         line_width_float = 1.5,
         edge_colors_string = 'black',
         alpha_float = 0.8,
         title_font_size_float = 20.0,
         title_font_style_string = 'normal',
         title_pad_float = 20.0,
         xlabel_font_size_float = 16.0,
         xlabel_font_style_string = 'normal',
         xlabel_pad_float = 10.0,
         ylabel_font_size_float = 16.0,
         ylabel_font_style_string = 'normal',
         ylabel_pad_float = 10.0,
         xtick_label_rotation_float = 0.0,
         xtick_font_size_float = 14.0,
         ytick_label_rotation_float = 0.0,
         ytick_font_size_float = 14.0,        
         figure_width_float = 9.708,
         figure_length_float = 6.0):

    plt.figure(figsize = (figure_width_float, figure_length_float))

    plt.scatter \
        (x_series, 
         y_series, 
         marker = marker_shape_string,
         s = marker_size_float,
         color = marker_color_string, 
         linewidth = line_width_float,
         edgecolors = edge_colors_string,
         alpha = alpha_float)

    plt.title \
        (title_string, 
         fontdict = {'fontsize': title_font_size_float, 
                     'fontstyle': title_font_style_string},
         pad = title_pad_float)

    plt.xlabel \
        (xlabel_string,
         fontdict = {'fontsize': xlabel_font_size_float, 
                     'fontstyle': xlabel_font_style_string},
         labelpad = xlabel_pad_float)

    plt.ylabel \
        (ylabel_string,
         fontdict = {'fontsize': ylabel_font_size_float, 
                     'fontstyle': ylabel_font_style_string},
         labelpad = ylabel_pad_float)

    plt.xticks \
        (rotation = xtick_label_rotation_float,
         fontsize = xtick_font_size_float)

    plt.yticks \
        (rotation = ytick_label_rotation_float,
         fontsize = ytick_font_size_float)

    plt.grid()


    if degree_integer == 1:

        display_linear_regression_line \
            (x_series, y_series,
             equation_x_coordinate_float,
             equation_y_coordinate_float)

    elif degree_integer > 1:

        display_polynomial_regression_line \
            (x_series, y_series,
             equation_x_coordinate_float,
             equation_y_coordinate_float,
             degree_integer)


    logx.save_plot_image(title_string)

    plt.show()


# In[13]:


#*******************************************************************************************
 #
 #  Function Name:  display_multiple_scatter_plots_from_xy_series_list
 #
 #  Function Description:
 #      The function displays multiple scatter plots from x-y series lists.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  series  x_series_list   The parameter is the x-axis series list.
 #  series  y_series_list   The parameter is the y-axis series list.
 #  string  titles_string_list
 #                          The parameter is the chart title list.
 #  string  suptitle_string The parameter is the figure title.
 #  string  xlabel_string   The parameter is the x-axis label.
 #  string  ylabel_string   The parameter is the y-axis label.
 #  integer degree_integer  The parameter is the degree of the regression line polynomial.
 #  float   equation_x_coordinate_float_list
 #                          The parameter is the list of equation's x-coordinates.  
 #  float   equation_y_coordinate_float_list
 #                          The parameter is the list of equation's y-coordinate.  
 #  string  marker_shape_string
 #                          The parameter is marker shape.
 #  float   marker_size_float
 #                          The parameter is the marker size.       
 #  string  marker_color_string
 #                          The parameter is the marker color.
 #  float   line_width_float
 #                          The parameter is line width of the scatter points.
 #  string  edge_colors_string
 #                          The parameter is the edge color for the scatter points.
 #  float   alpha_float     The parameter is the bar transparency level (0-1.0).
 #  float   suptitle_font_size_float
 #                          The parameter is the figure title font size. 
 #  string  suptitle_font_style_string
 #                          The parameter is the figure title font style.
 #  float   suptitle_pad_float
 #                          The parameter is the figure title space pad value. 
 #  float   title_font_size_float
 #                          The parameter is the title font size. 
 #  string  title_font_style_string
 #                          The parameter is the title font style.
 #  float   title_pad_float The parameter is the title space pad value. 
 #  float   xlabel_font_size_float
 #                          The parameter is the x-axis font size. 
 #  string  xlabel_font_style_string
 #                          The parameter is the x-axis font style.
 #  float   xlabel_pad_float
 #                          The parameter is the x-axis space pad value. 
 #  float   ylabel_font_size_float
 #                          The parameter is the y-axis font size. 
 #  string  ylabel_font_style_string
 #                          The parameter is the y-axis font style.
 #  float   ylabel_pad_float
 #                          The parameter is the y-axis space pad value. 
 #  float   xtick_label_rotation_float
 #                          The parameter is the x-axis tick rotation. 
 #  float   xtick_font_size_float
 #                          The parameter is the x-axis tick font size.
 #  float   ytick_label_rotation_float
 #                          The parameter is the y-axis tick rotation. 
 #  float   ytick_font_size_float
 #                          The parameter is the y-axis tick font size. 
 #  float   tight_layout_pad_float
 #                          The parameter is the figure tight layout padding. 
 #  float   figure_width_float
 #                          The parameter is the figure width. 
 #  float   figure_length_float
 #                          The parameter is the figure length. 
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def display_multiple_scatter_plots_from_xy_series_list \
        (x_series_list,
         y_series_list,
         titles_string_list,
         suptitle_string,
         xlabel_string,
         ylabel_string,
         degree_integer = 0,
         equation_x_coordinate_float_list = 0.0,
         equation_y_coordinate_float_list = 0.0,
         marker_shape_string = 'o',
         marker_size_float = 80.0,
         marker_color_string = 'lime',
         line_width_float = 1.5,
         edge_colors_string = 'black',
         alpha_float = 0.8,
         suptitle_font_size_float = 20.0,
         suptitle_font_weight_string = 'normal',
         suptitle_pad_float = 1.0,         
         title_font_size_float = 20.0,
         title_font_style_string = 'normal',
         title_pad_float = 20.0,
         xlabel_font_size_float = 16.0,
         xlabel_font_style_string = 'normal',
         xlabel_pad_float = 10.0,
         ylabel_font_size_float = 16.0,
         ylabel_font_style_string = 'normal',
         ylabel_pad_float = 10.0,
         xtick_label_rotation_float = 0.0,
         xtick_font_size_float = 14.0,
         ytick_label_rotation_float = 0.0,
         ytick_font_size_float = 14.0,
         tight_layout_pad_float = 3.0,
         figure_width_float = 15.0,
         figure_length_float = 5.5181):

    scatter_plot_count_integer = len(x_series_list)

    if scatter_plot_count_integer != len(y_series_list):

        logx.print_and_log_text \
            ('The function, display_multiple_scatter_plots_from_xy_series_list, '
              + f'in source file, {CONSTANT_LOCAL_FILE_NAME},'
              + f'with the caption, {suptitle_string},'
              + 'was unable to display scatter plots '
              + 'because the number of x and y series did not match.')


    plt.subplots(figsize = (figure_width_float, figure_length_float))

    plt.clf()


    x_length_integer, y_length_integer \
        = mathx.calculate_closest_factors(scatter_plot_count_integer)


    for index in range(0, scatter_plot_count_integer):

        plt.subplot(x_length_integer, y_length_integer, index + 1)

        plt.scatter \
            (x_series_list[index], 
             y_series_list[index], 
             marker = marker_shape_string,
             s = marker_size_float,
             color = marker_color_string, 
             linewidth = line_width_float,
             edgecolors = edge_colors_string,
             alpha = alpha_float)

        plt.title \
            (titles_string_list[index], 
             fontdict = {'fontsize': title_font_size_float, 
                         'fontstyle': title_font_style_string},
             pad = title_pad_float)

        plt.xlabel \
            (xlabel_string,
             fontdict = {'fontsize': xlabel_font_size_float, 
                        'fontstyle': xlabel_font_style_string},
             labelpad = xlabel_pad_float)

        plt.ylabel \
            (ylabel_string,
             fontdict = {'fontsize': ylabel_font_size_float, 
                         'fontstyle': ylabel_font_style_string},
             labelpad = ylabel_pad_float)

        plt.xticks \
            (rotation = xtick_label_rotation_float,
             fontsize = xtick_font_size_float)

        plt.yticks \
            (rotation = ytick_label_rotation_float,
             fontsize = ytick_font_size_float)

        plt.grid()


        if degree_integer == 1:

            logx.print_and_log_text(titles_string_list[index] + ':')

            display_linear_regression_line \
                (x_series_list[index],
                 y_series_list[index],
                 equation_x_coordinate_float_list[index],
                 equation_y_coordinate_float_list[index])

        elif degree_integer > 1:

            logx.print_and_log_text(titles_string_list[index] + ':')

            display_polynomial_regression_line \
                (x_series_list[index],
                 y_series_list[index],
                 equation_x_coordinate_float_list[index],
                 equation_y_coordinate_float_list[index],
                 degree_integer)

        plt.tight_layout(pad = tight_layout_pad_float)

        plt.suptitle \
            (suptitle_string, 
             fontsize = suptitle_font_size_float,
             fontweight = suptitle_font_weight_string,
             y = suptitle_pad_float)

        logx.save_plot_image(suptitle_string)

        plt.show()


# In[14]:


#*******************************************************************************************
 #
 #  Function Name:  display_pie_chart_from_series
 #
 #  Function Description:
 #      The function displays a pie chart from a series.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  series  input_series    The parameter is the input series.
 #  string  title_string    The parameter is the figure title.
 #  list    colors_string_list
 #                          The parameter is the list of pie wedge colors.
 #  tuple   explode_float_tuple   
 #                          The parameter is the degree of separation for each pie wedge.
 #  boolean shadow_boolean  The parameter indicates whether the pie chart is shadowed.
 #  float   pct_distance_float
 #                          The parameter is the percent distance between pie wedges.  
 #  float   start_angle_float
 #                          The parameter is the pie chart's start angle.
 #  string  auto_pct_string
 #                          The parameter is percent format for pie wedges.
 #  float   label_distance_float
 #                          The parameter is the label's distance from the center.
 #  float   chart_font_size_float
 #                          The parameter is the chart text font size.       
 #  float   title_font_size_float
 #                          The parameter is the title font size. 
 #  string  title_font_style_string
 #                          The parameter is the title font style.
 #  float   title_pad_float
 #                          The parameter is the title space pad value. 
 #  float   figure_width_float
 #                          The parameter is the figure width. 
 #  float   figure_length_float
 #                          The parameter is the figure length. 
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def display_pie_chart_from_series \
        (input_series,
         title_string,
         colors_string_list,
         explode_float_tuple,
         shadow_boolean = True,
         pct_distance_float = 0.75,
         start_angle_float = 45.0,
         auto_pct_string = '%1.1f%%',
         label_distance_float = 1.1,
         chart_font_size_float = 14.0,
         title_font_size_float = 20.0,
         title_font_style_string = 'normal',
         title_pad_float = 5.0,
         figure_width_float = 9.708,
         figure_length_float = 6.0):

    temp_series = input_series.copy()

    temp_series.rename(None, inplace = True)


    plt.figure(figsize = (figure_width_float, figure_length_float))

    plt.pie \
        (temp_series,
         labels = temp_series.index, 
         colors = colors_string_list,   
         explode = explode_float_tuple, 
         shadow = shadow_boolean,
         pctdistance = pct_distance_float,
         startangle = start_angle_float,
         autopct = auto_pct_string,
         labeldistance = label_distance_float,
         textprops = {'fontsize': chart_font_size_float})

    plt.title \
        (title_string,
         fontdict = {'fontsize': title_font_size_float, 
                     'fontstyle': title_font_style_string},
         pad = title_pad_float)   


    logx.save_plot_image(title_string)

    plt.show()


# In[15]:


#*******************************************************************************************
 #
 #  Function Name:  display_multiple_pie_charts_from_dataframe
 #
 #  Function Description:
 #      The function receives a dataframe and formatting parameters for the display
 #      of multiple pie charts.
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
 #          input_dataframe The parameter is the input dataframe
 #  string  suptitle_string The parameter is the chart title.
 #  list    colors_string_list
 #                          The parameter is the list of pie wedge colors.
 #  tuple   explode_float_tuple   
 #                          The parameter is the degree of separation for each pie wedge.
 #  boolean shadow_boolean  The parameter indicates whether the pie chart is shadowed.
 #  float   pct_distance_float
 #                          The parameter is the percent distance between pie wedges.  
 #  float   start_angle_float
 #                          The parameter is the pie chart's start angle.
 #  string  auto_pct_string
 #                          The parameter is percent format for pie wedges.
 #  float   label_distance_float
 #                          The parameter is the label's distance from the center.
 #  float   chart_font_size_float
 #                          The parameter is the chart text font size.  
 #  float   suptitle_x_float
 #                          The parameter is the figure title's x-coordinate padding.
 #  float   suptitle_y_float
 #                          The parameter is the figure title's y-coordinate padding.
 #  float   suptitle_font_size_float
 #                          The parameter is the figure title's font size.
 #  string  suptitle_font_weight_string
 #                          The parameter is the figure title's font weight.
 #  string  titles_string_list
 #                          The parameter is the list of chart titles.
 #  float   title_font_size_float
 #                          The parameter is the title font size. 
 #  string  title_font_style_string
 #                          The parameter is the title font style.
 #  float   title_pad_float
 #                          The parameter is the title space pad value. 
 #  float   title_y_float
 #                          The parameter is the title's y-axis displacement.
 #  string  xlabel_string
 #                          The parameter is the subplot's x-axis label.
 #  float   xlabel_pad_float  
 #                          The parameter is the subplot's x-axis label's padding.
 #  float   xlabel_font_size_float
 #                          The parameter is the subplot's x-axis label's font size.
 #  string  xlabel_loc_string
 #                          The parameter is the subplot's x-axis label's general location.
 #  string  xlabel_font_weight_string
 #                          The parameter is the subplot's x-axis label's font weight.
 #  string  ylabel_string
 #                          The parameter is the subplot's y-axis label.
 #  float   ylabel_pad_float  
 #                          The parameter is the subplot's y-axis label's padding.
 #  float   ylabel_font_size_float
 #                          The parameter is the subplot's y-axis label's font size.
 #  string  ylabel_loc_string
 #                          The parameter is the subplot's y-axis label's general location.
 #  string  ylabel_font_weight_string
 #                          The parameter is the subplot's y-axis label's font weight.
 #  float   subplot_width_space_float
 #                          The parameter is the width of the space between subplots.
 #  float   subplot_height_space_float
 #                          The parameter is the width of the space between subplots.
 #  float   figure_width_float
 #                          The parameter is the figure width. 
 #  float   figure_length_float
 #                          The parameter is the figure length. 
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/  

def display_multiple_pie_charts_from_dataframe \
        (input_dataframe,
         suptitle_string,
         colors_string_list,
         explode_float_tuple,
         shadow_boolean = True,
         pct_distance_float = 0.75,
         start_angle_float = 45.0,
         auto_pct_string = '%1.1f%%',
         label_distance_float = 1.2,
         chart_font_size_float = 12.0,
         suptitle_x_float = 0.5,  
         suptitle_y_float = 0.9,  
         suptitle_font_size_float = 20.0,
         suptitle_font_weight_string = 'normal',
         titles_string_list = [],
         title_font_size_float = 18.0,
         title_font_style_string = 'normal',
         title_pad_float = 5.0,
         title_y_float = 1.05,
         xlabel_string = '',
         xlabel_pad_float = 4.0,
         xlabel_font_size_float = 16.0,
         xlabel_loc_string = 'center',
         xlabel_font_weight_string = 'normal',
         ylabel_string = '',
         ylabel_pad_float = 4.0,
         ylabel_font_size_float = 16.0,
         ylabel_loc_string = 'center',
         ylabel_font_weight_string = 'normal',
         subplot_width_space_float = 1.1,
         subplot_height_space_float = None,
         figure_width_float = 15.0,
         figure_length_float = 5.5181):

    chart_count_integer = len(input_dataframe.columns)

    row_count_integer, column_count_integer \
        = mathx.calculate_closest_factors(chart_count_integer)

    index = 0


    fig, axs \
        = plt.subplots \
            (nrows = row_count_integer, ncols = column_count_integer,
             figsize = (figure_width_float, figure_length_float),
             tight_layout = True)

    fig.suptitle \
        (suptitle_string,
         x = suptitle_x_float,
         y = suptitle_y_float,
         fontsize = suptitle_font_size_float, 
         fontweight = suptitle_font_weight_string)


    for row in range(row_count_integer):
        for column in range(column_count_integer):

            input_dataframe.iloc[:, index].plot.pie \
                (ax = axs[index],
                 colors = colors_string_list, 
                 shadow = shadow_boolean,
                 pctdistance = pct_distance_float,
                 startangle = start_angle_float, 
                 autopct = auto_pct_string,
                 labeldistance = label_distance_float,
                 textprops = {'fontsize': chart_font_size_float},
                 subplots = True)


            if len(titles_string_list) <= 0:

                title_string = input_dataframe.iloc[:, index].name

            else:

                title_string = titles_string_list[index]


            axs[index].set_title \
                (title_string,
                 fontdict = {'fontsize': title_font_size_float, 
                             'fontstyle': title_font_style_string},
                 pad = title_pad_float,
                 y = title_y_float)


            axs[index].set_xlabel \
                (xlabel_string, 
                 labelpad = xlabel_pad_float, 
                 fontsize = xlabel_font_size_float, 
                 loc = xlabel_loc_string, 
                 fontweight = xlabel_font_weight_string)

            axs[index].set_ylabel \
                (ylabel_string, 
                 labelpad = ylabel_pad_float, 
                 fontsize = ylabel_font_size_float, 
                 loc = ylabel_loc_string, 
                 fontweight = ylabel_font_weight_string)


            index += 1


    plt.subplots_adjust \
        (wspace = subplot_width_space_float, 
         hspace = subplot_height_space_float)


    logx.save_plot_image(suptitle_string)

    plt.show()


# In[16]:


#*******************************************************************************************
 #
 #  Function Name:  display_histogram_from_series
 #
 #  Function Description:
 #      The function displays a histogram from a series and criteria.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  series
 #          input_series    The parameter is the input series.
 #  string  title_string    The parameter is the chart title.
 #  list    color_string    The parameter is the color of the histogram.
 #  string  xlabel_string   The parameter is the x-axis label.
 #  string  ylabel_string   The parameter is the y-axis label.
 #  integer bins_count_integer
 #                          The parameter is the number of histogram bins.
 #  float   alpha_float     The parameter is the alpha (transparency) value.
 #  boolean grid_boolean    The parameter indicates whether the boxplot displays a grid.
 #  string  fill_style_string
 #                          The parameter is the line fills style.
 #  float   line_width_float
 #                          The parameter is the line width around a histogram box.       
 #  string  edge_color_string
 #                          The parameter is the histogram box edge color.
 #  boolean display_legend_boolean
 #                          The parameter indicates whether the legend will be present.
 #  float   title_font_size_float
 #                          The parameter is the title font size. 
 #  string  title_font_style_string
 #                          The parameter is the title font style.
 #  float   title_pad_float The parameter is the title space pad value. 
 #  float   xlabel_font_size_float
 #                          The parameter is the x-axis font size. 
 #  string  xlabel_font_style_string
 #                          The parameter is the x-axis font style.
 #  float   xlabel_pad_float
 #                          The parameter is the x-axis space pad value. 
 #  float   ylabel_font_size_float
 #                          The parameter is the y-axis font size. 
 #  string  ylabel_font_style_string
 #                          The parameter is the y-axis font style.
 #  float   ylabel_pad_float
 #                          The parameter is the y-axis space pad value. 
 #  float   xticks_font_size_float
 #                          The parameter is the subplot's x-tick label's font size.
 #  float   xticks_rotation_float
 #                          The parameter is the subplot's x-tick label's rotation in degrees.
 #  float   yticks_font_size_float
 #                          The parameter is the subplot's y-tick label's font size.
 #  float   yticks_rotation_float
 #                          The parameter is the subplot's y-tick label's rotation in degrees.
 #  string  legend_loc_string
 #                          The parameter is the legend's general location.
 #  float   legend_font_size_float
 #                          The parameter is legend's font size.
 #  tuple   legend_bbox_to_anchor_float_tuple
 #                          The parameter is the legend's xy-coordinates. 
 #  float   figure_width_float
 #                          The parameter is the figure width. 
 #  float   figure_length_float
 #                          The parameter is the figure length. 
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def display_histogram_from_series \
        (input_series,
         title_string,
         color_string,
         xlabel_string = None,
         ylabel_string = None,
         bins_count_integer = 20,
         alpha_float = 1.0,
         grid_boolean = True,
         line_width_float = 1.5,
         edge_color_string = 'black',
         display_legend_boolean = False,
         title_font_size_float = 20.0,
         title_font_style_string = 'normal',
         title_pad_float = 20.0,
         xlabel_font_size_float = 16.0,
         xlabel_font_style_string = 'normal',
         xlabel_pad_float = 10.0,
         ylabel_font_size_float = 16.0,
         ylabel_font_style_string = 'normal',
         ylabel_pad_float = 10.0,
         xticks_font_size_float = 14.0,
         xticks_rotation_float = 90.0,
         yticks_font_size_float = 14.0,
         yticks_rotation_float = 0.0,
         legend_loc_string = 'center right',
         legend_font_size_float = 14.0,
         legend_bbox_to_anchor_float_tuple = (1.5, 0.5),
         figure_width_float = 9.708,
         figure_length_float = 6.0):

    input_series \
        .plot.hist \
            (bins = bins_count_integer, 
             alpha = alpha_float, 
             color = color_string, 
             linewidth = line_width_float, 
             edgecolor = edge_color_string, 
             legend = display_legend_boolean,
             figsize = (figure_width_float, figure_length_float))


    plt.title \
        (title_string,
         fontdict = {'fontsize': title_font_size_float, 
                     'fontstyle': title_font_style_string},
         pad = title_pad_float)


    if xlabel_string != None:

        plt.xlabel \
            (xlabel_string,
             fontdict = {'fontsize': xlabel_font_size_float,
                         'fontstyle': xlabel_font_style_string},
             labelpad = xlabel_pad_float)

    if ylabel_string != None:

        plt.ylabel \
            (ylabel_string,
             fontdict = {'fontsize': ylabel_font_size_float,
                         'fontstyle': ylabel_font_style_string},
             labelpad = ylabel_pad_float)


    plt.xticks(fontsize = xticks_font_size_float, rotation = xticks_rotation_float)

    plt.yticks(fontsize = yticks_font_size_float, rotation = yticks_rotation_float)


    if display_legend_boolean == True:

        plt.legend \
            (loc = legend_loc_string,
             fontsize = legend_font_size_float,
             bbox_to_anchor = legend_bbox_to_anchor_float_tuple)


    logx.save_plot_image(title_string)


# In[17]:


#*******************************************************************************************
 #
 #  Function Name:  display_histograms_from_series_list
 #
 #  Function Description:
 #      The function receives a series list and formatting parameters for the display
 #      of multiple histograms in a single figure.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  series
 #          input_series    The parameter is the input dataframe
 #  string  suptitle_string The parameter is the chart title.
 #  string  supxlabel_string
 #                          The parameter is the title for the figure's x-axis.
 #  string  supylabel_string
 #                          The parameter is the title for the figure's y-axis.
 #  string  xlabel_string   The parameter is the x-axis label.
 #  string  ylabel_string   The parameter is the y-axis label.
 #  list    color_string    The parameter is the histogram color.
 #  boolean reverse_dimensions_boolean 
 #                          The parameter indicates whether the histograms share the x-axis.
 #  boolean share_x_boolean The parameter indicates whether the histograms share the x-axis.
 #  boolean share_y_boolean The parameter indicates whether the histograms share the y-axis.
 #  boolean tight_layout_boolean  
 #                          The parameter indicates whether the figure has a tight layout.
 #  integer bins_count_integer
 #                          The parameter is the number of histogram bins.
 #  float   alpha_float     The parameter is the alpha (transparency) value.
 #  boolean grid_boolean    The parameter indicates whether the boxplot displays a grid.
 #  float   line_width_float
 #                          The parameter is the line width around a histogram box.       
 #  string  edge_color_string
 #                          The parameter is the histogram box edge color.
 #  float   suptitle_x_float
 #                          The parameter is the figure title's x-coordinate padding.
 #  float   suptitle_y_float
 #                          The parameter is the figure title's y-coordinate padding.
 #  float   suptitle_font_size_float
 #                          The parameter is the figure title's font size.
 #  string  suptitle_font_style_string
 #                          The parameter is the figure title's font style.
 #  float   supxlabel_x_float
 #                          The parameter is the figure's x-axis label's 
 #                          x-coordinate padding.
 #  float   supxlabel_y_float
 #                          The parameter is the figure's x-axis label's 
 #                          y-coordinate padding.
 #  float   supxlabel_font_size_float
 #                          The parameter is the figure's x-axis label's font size.
 #  string  supxlabel_font_style_string
 #                          The parameter is the figure's x-axis label's font style.
 #  float   supylabel_x_float
 #                          The parameter is the figure's y-axis label's 
 #                          x-coordinate padding.
 #  float   supylabel_y_float
 #                          The parameter is the figure's y-axis label's 
 #                          y-coordinate padding.
 #  float   supylabel_font_size_float
 #                          The parameter is the figure's y-axis label's font size.
 #  string  supylabel_font_style_string
 #                          The parameter is the figure's y-axis label's font style.
 #  string  titles_string_list
 #                          The parameter is the list of chart titles.
 #  float   title_font_size_float
 #                          The parameter is the title font size. 
 #  string  title_font_style_string
 #                          The parameter is the title font style.
 #  float   title_pad_float
 #                          The parameter is the title space pad value. 
 #  float   title_y_float
 #                          The parameter is the title's y-axis displacement.
 #  string  xlabel_string
 #                          The parameter is the subplot's x-axis label.
 #  float   xlabel_pad_float  
 #                          The parameter is the subplot's x-axis label's padding.
 #  float   xlabel_font_size_float
 #                          The parameter is the subplot's x-axis label's font size.
 #  string  xlabel_loc_string
 #                          The parameter is the subplot's x-axis label's general location.
 #  string  xlabel_font_style_string
 #                          The parameter is the subplot's x-axis label's font style.
 #  string  ylabel_string
 #                          The parameter is the subplot's y-axis label.
 #  float   ylabel_pad_float  
 #                          The parameter is the subplot's y-axis label's padding.
 #  float   ylabel_font_size_float
 #                          The parameter is the subplot's y-axis label's font size.
 #  string  ylabel_loc_string
 #                          The parameter is the subplot's y-axis label's general location.
 #  string  ylabel_font_style_string
 #                          The parameter is the subplot's y-axis label's font style.
 #  float   figure_width_float
 #                          The parameter is the figure width. 
 #  float   figure_length_float
 #                          The parameter is the figure length. 
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/  

def display_histograms_from_series_list \
        (input_series_list,
         suptitle_string,
         supxlabel_string = None,
         supylabel_string = None,
         xlabel_string = '',
         ylabel_string = '',
         color_string = 'firebrick',
         reverse_dimensions_boolean = True,
         share_x_boolean = True,
         share_y_boolean = True,
         tight_layout_boolean = True,
         bins_count_integer = 20,
         alpha_float = 1.0,
         grid_boolean = True,
         line_width_float = 1.5,
         edge_color_string = 'black',
         suptitle_x_float = 0.5,  
         suptitle_y_float = 0.9,  
         suptitle_font_size_float = 20.0,
         suptitle_font_weight_string = 'normal',
         supxlabel_x_float = 0.5,  
         supxlabel_y_float = 0.0,  
         supxlabel_font_size_float = 16.0,
         supxlabel_font_weight_string = 'normal',
         supylabel_x_float = 0.0,  
         supylabel_y_float = 0.5,  
         supylabel_font_size_float = 16.0,
         supylabel_font_weight_string = 'normal',
         title_font_size_float = 20.0,
         title_font_style_string = 'normal',
         title_pad_float = 20.0,
         xlabel_font_size_float = 16.0,
         xlabel_font_style_string = 'normal',
         xlabel_pad_float = 10.0,
         ylabel_font_size_float = 16.0,
         ylabel_font_style_string = 'normal',
         ylabel_pad_float = 10.0,
         tight_layout_float = 3.0,
         figure_width_float = 15.0,
         figure_length_float = 7.5):

    chart_count_integer = len(input_series_list)

    colors_string_list = [color_string] * chart_count_integer


    row_count_integer, column_count_integer \
        = mathx.calculate_closest_factors(chart_count_integer)

    if reverse_dimensions_boolean == True:

        row_count_integer, column_count_integer = column_count_integer, row_count_integer       


    fig, axs \
        = plt.subplots \
            (row_count_integer, 
             column_count_integer, 
             figsize = (figure_width_float, figure_length_float),
             sharex = share_x_boolean,
             sharey = share_y_boolean, 
             tight_layout = tight_layout_boolean)


    plt.clf()


    fig.suptitle \
        (suptitle_string,
         x = suptitle_x_float,
         y = suptitle_y_float,
         fontsize = suptitle_font_size_float, 
         fontweight = suptitle_font_weight_string)


    for index in range(chart_count_integer):

        plt.subplot(row_count_integer, column_count_integer, index + 1)


        input_series_list[index] \
            .plot.hist \
                (bins = bins_count_integer, 
                 alpha = alpha_float,
                 grid = grid_boolean,
                 color = colors_string_list[index], 
                 linewidth = line_width_float, 
                 edgecolor = edge_color_string,
                 legend = False)


        plt.title \
            (input_series_list[index].name,
             fontdict = {'fontsize': title_font_size_float, 
                         'fontstyle': title_font_style_string},
             pad = title_pad_float)


        plt.xlabel \
            (xlabel_string,
             fontdict = {'fontsize': xlabel_font_size_float,
                         'fontstyle': xlabel_font_style_string},
             labelpad = xlabel_pad_float)

        plt.ylabel \
            (ylabel_string,
             fontdict = {'fontsize': ylabel_font_size_float,
                         'fontstyle': ylabel_font_style_string},
             labelpad = ylabel_pad_float)


        plt.tight_layout(pad = 3.0)


    if supxlabel_string != None:

        fig.supxlabel \
            (supxlabel_string,
             x = supxlabel_x_float,
             y = supxlabel_y_float,
             fontsize = supxlabel_font_size_float, 
             fontweight = supxlabel_font_weight_string)

    if supylabel_string != None:

            fig.supylabel \
                (supylabel_string,
                 x = supylabel_x_float,
                 y = supylabel_y_float,
                 fontsize = supylabel_font_size_float, 
                 fontweight = supylabel_font_weight_string)


    logx.save_plot_image(suptitle_string)

    plt.show()


# In[18]:


#*******************************************************************************************
 #
 #  Function Name:  display_multiple_histograms_from_dataframe
 #
 #  Function Description:
 #      The function receives a dataframe and formatting parameters for the display
 #      of multiple histograms.
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
 #          input_dataframe The parameter is the input dataframe
 #  string  suptitle_string The parameter is the chart title.
 #  list    colors_string_list
 #                          The parameter is the list of histogram colors.
 #  string  supxlabel_string
 #                          The parameter is the title for the figure's x-axis.
 #  string  supylabel_string
 #                          The parameter is the title for the figure's y-axis.
 #  boolean share_x_boolean The parameter indicates whether the histograms share the x-axis.
 #  boolean share_y_boolean The parameter indicates whether the histograms share the y-axis.
 #  boolean tight_layout_boolean  
 #                          The parameter indicates whether the figure has a tight layout.
 #  integer bins_count_integer
 #                          The parameter is the number of histogram bins.
 #  float   alpha_float     The parameter is the alpha (transparency) value.
 #  boolean grid_boolean    The parameter indicates whether the boxplot displays a grid.
 #  float   suptitle_x_float
 #                          The parameter is the figure title's x-coordinate padding.
 #  float   suptitle_y_float
 #                          The parameter is the figure title's y-coordinate padding.
 #  float   suptitle_font_size_float
 #                          The parameter is the figure title's font size.
 #  string  suptitle_font_weight_string
 #                          The parameter is the figure title's font weight.
 #  float   supxlabel_x_float
 #                          The parameter is the figure's x-axis label's 
 #                          x-coordinate padding.
 #  float   supxlabel_y_float
 #                          The parameter is the figure's x-axis label's 
 #                          y-coordinate padding.
 #  float   supxlabel_font_size_float
 #                          The parameter is the figure's x-axis label's font size.
 #  string  supxlabel_font_weight_string
 #                          The parameter is the figure's x-axis label's font weight.
 #  float   supylabel_x_float
 #                          The parameter is the figure's y-axis label's 
 #                          x-coordinate padding.
 #  float   supylabel_y_float
 #                          The parameter is the figure's y-axis label's 
 #                          y-coordinate padding.
 #  float   supylabel_font_size_float
 #                          The parameter is the figure's y-axis label's font size.
 #  string  supylabel_font_weight_string
 #                          The parameter is the figure's y-axis label's font weight.
 #  string  titles_string_list
 #                          The parameter is the list of chart titles.
 #  float   title_font_size_float
 #                          The parameter is the title font size. 
 #  string  title_font_style_string
 #                          The parameter is the title font style.
 #  float   title_pad_float
 #                          The parameter is the title space pad value. 
 #  float   title_y_float
 #                          The parameter is the title's y-axis displacement.
 #  string  xlabel_string
 #                          The parameter is the subplot's x-axis label.
 #  float   xlabel_pad_float  
 #                          The parameter is the subplot's x-axis label's padding.
 #  float   xlabel_font_size_float
 #                          The parameter is the subplot's x-axis label's font size.
 #  string  xlabel_loc_string
 #                          The parameter is the subplot's x-axis label's general location.
 #  string  xlabel_font_weight_string
 #                          The parameter is the subplot's x-axis label's font weight.
 #  string  ylabel_string
 #                          The parameter is the subplot's y-axis label.
 #  float   ylabel_pad_float  
 #                          The parameter is the subplot's y-axis label's padding.
 #  float   ylabel_font_size_float
 #                          The parameter is the subplot's y-axis label's font size.
 #  string  ylabel_loc_string
 #                          The parameter is the subplot's y-axis label's general location.
 #  string  ylabel_font_weight_string
 #                          The parameter is the subplot's y-axis label's font weight.
 #  float   xtick_label_size_float
 #                          The parameter is the subplot's x-tick label's font size.
 #  float   xtick_label_rotation_float
 #                          The parameter is the subplot's x-tick label's rotation in degrees.
 #  float   ytick_label_size_float
 #                          The parameter is the subplot's y-tick label's font size.
 #  float   ytick_label_rotation_float
 #                          The parameter is the subplot's y-tick label's rotation in degrees.
 #  float   subplot_width_space_float
 #                          The parameter is the width of the space between subplots.
 #  float   subplot_height_space_float
 #                          The parameter is the width of the space between subplots.
 #  float   figure_width_float
 #                          The parameter is the figure width. 
 #  float   figure_length_float
 #                          The parameter is the figure length. 
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/  

def display_multiple_histograms_from_dataframe \
        (input_dataframe,
         suptitle_string,
         colors_string_list,
         supxlabel_string = None,
         supylabel_string = None,
         share_x_boolean = False,
         share_y_boolean = True,
         tight_layout_boolean = True,
         bins_count_integer = 20,
         alpha_float = 0.8,
         grid_boolean = True,
         suptitle_x_float = 0.5,  
         suptitle_y_float = 1.0,  
         suptitle_font_size_float = 20.0,
         suptitle_font_weight_string = 'normal',
         supxlabel_x_float = 0.5,  
         supxlabel_y_float = 0.0,  
         supxlabel_font_size_float = 16.0,
         supxlabel_font_weight_string = 'normal',
         supylabel_x_float = 0.0,  
         supylabel_y_float = 0.5,  
         supylabel_font_size_float = 16.0,
         supylabel_font_weight_string = 'normal',
         titles_string_list = [],
         title_font_size_float = 18.0,
         title_font_style_string = 'normal',
         title_pad_float = 5.0,
         title_y_float = 1.05,
         xlabel_string = '',
         xlabel_pad_float = 4.0,
         xlabel_font_size_float = 16.0,
         xlabel_loc_string = 'center',
         xlabel_font_weight_string = 'normal',
         ylabel_string = '',
         ylabel_pad_float = 4.0,
         ylabel_font_size_float = 16.0,
         ylabel_loc_string = 'center',
         ylabel_font_weight_string = 'normal',
         xtick_label_size_float = 14.0,
         xtick_label_rotation_float = 0.0,
         ytick_label_size_float = 14.0,
         ytick_label_rotation_float = 0.0,
         subplot_width_space_float = 1.1,
         subplot_height_space_float = None,
         figure_width_float = 9.708,
         figure_length_float = 6.0):

    chart_count_integer = len(input_dataframe.columns)

    row_count_integer, column_count_integer \
        = mathx.calculate_closest_factors(chart_count_integer)

    index = 0


    fig, axs \
        = plt.subplots \
            (nrows = row_count_integer, ncols = column_count_integer,
             figsize = (figure_width_float, figure_length_float),
             sharex = share_x_boolean,
             sharey = share_y_boolean, 
             tight_layout = tight_layout_boolean)

    fig.suptitle \
        (suptitle_string,
         x = suptitle_x_float,
         y = suptitle_y_float,
         fontsize = suptitle_font_size_float, 
         fontweight = suptitle_font_weight_string)


    ax = axs.ravel()


    for row in range(row_count_integer):
        for column in range(column_count_integer):

            input_dataframe.iloc[:, index].hist \
                (ax = ax[index],
                 color = colors_string_list[index], 
                 bins = bins_count_integer,
                 alpha = alpha_float,
                 grid = grid_boolean)


            if len(titles_string_list) <= 0:

                title_string = input_dataframe.keys()[index]

            else:

                title_string = titles_string_list[index]


            ax[index].set_title \
                (title_string,
                 fontdict = {'fontsize': title_font_size_float, 
                             'fontstyle': title_font_style_string},
                 pad = title_pad_float,
                 y = title_y_float)

            ax[index].set_xlabel \
                (xlabel_string, 
                 labelpad = xlabel_pad_float, 
                 fontsize = xlabel_font_size_float, 
                 loc = xlabel_loc_string, 
                 fontweight = xlabel_font_weight_string)

            ax[index].set_ylabel \
                (ylabel_string, 
                 labelpad = ylabel_pad_float, 
                 fontsize = ylabel_font_size_float, 
                 loc = ylabel_loc_string, 
                 fontweight = ylabel_font_weight_string)

            ax[index].tick_params \
                (axis = 'x', 
                 labelrotation = xtick_label_rotation_float, 
                 labelsize = xtick_label_size_float)

            ax[index].tick_params \
                (axis = 'y', 
                 labelrotation = ytick_label_rotation_float, 
                 labelsize = ytick_label_size_float)

            index += 1


    if supxlabel_string != None:

        fig.supxlabel \
            (supxlabel_string,
             x = supxlabel_x_float,
             y = supxlabel_y_float,
             fontsize = supxlabel_font_size_float, 
             fontweight = supxlabel_font_weight_string)

    if supylabel_string != None:

            fig.supylabel \
                (supylabel_string,
                 x = supylabel_x_float,
                 y = supylabel_y_float,
                 fontsize = supylabel_font_size_float, 
                 fontweight = supylabel_font_weight_string)


    plt.subplots_adjust \
        (wspace = subplot_width_space_float, 
         hspace = subplot_height_space_float)


    logx.save_plot_image(suptitle_string)

    plt.show()


# In[19]:


#*******************************************************************************************
 #
 #  Function Name:  display_plot_from_series
 #
 #  Function Description:
 #      The function displays a plot from a series and criteria.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  series
 #          input_series    The parameter is the input series.
 #  string  title_string    The parameter is the chart title.
 #  list    color_string    The parameter is the color of the histogram.
 #  string  xlabel_string   The parameter is the x-axis label.
 #  string  ylabel_string   The parameter is the y-axis label.
 #  float   alpha_float     The parameter is the alpha (transparency) value.
 #  boolean grid_boolean    The parameter indicates whether the boxplot displays a grid.
 #  boolean display_legend_boolean
 #                          The parameter indicates whether the legend will be present.
 #  nparray display_legend_boolean
 #                          The parameter is the positions of peaks in the graph.
 #  string  peaks_marker_size_float
 #                          The parameter is the size of the peaks markers.
 #  float   peaks_label_y_offset_float
 #                          The parameter is the y-axis offset of the label
 #                          from the peaks marker. 
 #  list   peaks_color_string_list
 #                          The parameter is the peaks marker and label colors. 
 #  float   title_font_size_float
 #                          The parameter is the title font size. 
 #  string  title_font_style_string
 #                          The parameter is the title font style.
 #  float   title_pad_float The parameter is the title space pad value. 
 #  float   xlabel_font_size_float
 #                          The parameter is the x-axis font size. 
 #  string  xlabel_font_style_string
 #                          The parameter is the x-axis font style.
 #  float   xlabel_pad_float
 #                          The parameter is the x-axis space pad value. 
 #  float   ylabel_font_size_float
 #                          The parameter is the y-axis font size. 
 #  string  ylabel_font_style_string
 #                          The parameter is the y-axis font style.
 #  float   ylabel_pad_float
 #                          The parameter is the y-axis space pad value. 
 #  float   xticks_font_size_float
 #                          The parameter is the subplot's x-tick label's font size.
 #  float   xticks_rotation_float
 #                          The parameter is the subplot's x-tick label's rotation in degrees.
 #  float   yticks_font_size_float
 #                          The parameter is the subplot's y-tick label's font size.
 #  float   yticks_rotation_float
 #                          The parameter is the subplot's y-tick label's rotation in degrees.
 #  string  legend_loc_string
 #                          The parameter is the legend's general location.
 #  float   legend_font_size_float
 #                          The parameter is legend's font size.
 #  tuple   legend_bbox_to_anchor_float_tuple
 #                          The parameter is the legend's xy-coordinates. 
 #  float   figure_width_float
 #                          The parameter is the figure width. 
 #  float   figure_length_float
 #                          The parameter is the figure length. 
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def display_plot_from_series \
        (input_series,
         title_string,
         color_string,
         xlabel_string = None,
         ylabel_string = None,
         alpha_float = 1.0,
         grid_boolean = True,
         display_legend_boolean = False,
         peaks_nparray = [],
         peaks_marker_size_float = 15.0,
         peaks_font_size_float = 12.0,
         peaks_label_y_offset_float = 5.0,
         peaks_color_string_list = ['red', 'blue'],
         title_font_size_float = 20.0,
         title_font_style_string = 'normal',
         title_pad_float = 20.0,
         xlabel_font_size_float = 16.0,
         xlabel_font_style_string = 'normal',
         xlabel_pad_float = 10.0,
         ylabel_font_size_float = 16.0,
         ylabel_font_style_string = 'normal',
         ylabel_pad_float = 10.0,
         xticks_font_size_float = 14.0,
         xticks_rotation_float = 90.0,
         yticks_font_size_float = 14.0,
         yticks_rotation_float = 0.0,
         legend_loc_string = 'center right',
         legend_font_size_float = 14.0,
         legend_bbox_to_anchor_float_tuple = (1.5, 0.5),
         figure_width_float = 9.708,
         figure_length_float = 6.0):

    plt.figure(figsize = (figure_width_float, figure_length_float))

    plt.clf()


    input_series \
        .plot \
            (color = color_string,
             alpha = alpha_float,
             grid = grid_boolean,
             legend = display_legend_boolean)

    if len(peaks_nparray) > 0:

        plt.plot \
            (input_series.index[peaks_nparray], 
             input_series.iloc[peaks_nparray], 
             'x', 
             markersize = peaks_marker_size_float, 
             color = peaks_color_string_list[0])

        for i, j in zip(input_series.index[peaks_nparray], input_series.iloc[peaks_nparray]):

            y_coordinate_float = j + peaks_label_y_offset_float

            plt.annotate \
                (i, xy = (i, y_coordinate_float), 
                 size = peaks_font_size_float, 
                 color = peaks_color_string_list[1])


    plt.title \
        (title_string,
         fontdict = {'fontsize': title_font_size_float, 
                     'fontstyle': title_font_style_string},
         pad = title_pad_float)


    if xlabel_string != None:

        plt.xlabel \
            (xlabel_string,
             fontdict = {'fontsize': xlabel_font_size_float,
                         'fontstyle': xlabel_font_style_string},
             labelpad = xlabel_pad_float)

    if ylabel_string != None:

        plt.ylabel \
            (ylabel_string,
             fontdict = {'fontsize': ylabel_font_size_float,
                         'fontstyle': ylabel_font_style_string},
             labelpad = ylabel_pad_float)


    plt.xticks(fontsize = xticks_font_size_float, rotation = xticks_rotation_float)

    plt.yticks(fontsize = yticks_font_size_float, rotation = yticks_rotation_float)


    if display_legend_boolean == True:

        plt.legend \
            (loc = legend_loc_string,
             fontsize = legend_font_size_float,
             bbox_to_anchor = legend_bbox_to_anchor_float_tuple)


    logx.save_plot_image(title_string)


# In[20]:


#*******************************************************************************************
 #
 #  Function Name:  display_plots_from_series_list
 #
 #  Function Description:
 #      The function receives a series list and formatting parameters for the display
 #      of plots in a single figure.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  series
 #          input_series    The parameter is the input dataframe
 #  string  suptitle_string The parameter is the chart title.
 #  string  supxlabel_string
 #                          The parameter is the title for the figure's x-axis.
 #  string  supylabel_string
 #                          The parameter is the title for the figure's y-axis.
 #  string  xlabel_string   The parameter is the x-axis label.
 #  string  ylabel_string   The parameter is the y-axis label.
 #  list    color_string    The parameter is the histogram color.
 #  boolean reverse_dimensions_boolean 
 #                          The parameter indicates whether the histograms share the x-axis.
 #  boolean share_x_boolean The parameter indicates whether the histograms share the x-axis.
 #  boolean share_y_boolean The parameter indicates whether the histograms share the y-axis.
 #  boolean tight_layout_boolean  
 #                          The parameter indicates whether the figure has a tight layout.
 #  float   alpha_float     The parameter is the alpha (transparency) value.
 #  boolean grid_boolean    The parameter indicates whether the boxplot displays a grid.
 #  float   suptitle_x_float
 #                          The parameter is the figure title's x-coordinate padding.
 #  float   suptitle_y_float
 #                          The parameter is the figure title's y-coordinate padding.
 #  float   suptitle_font_size_float
 #                          The parameter is the figure title's font size.
 #  string  suptitle_font_style_string
 #                          The parameter is the figure title's font style.
 #  float   supxlabel_x_float
 #                          The parameter is the figure's x-axis label's 
 #                          x-coordinate padding.
 #  float   supxlabel_y_float
 #                          The parameter is the figure's x-axis label's 
 #                          y-coordinate padding.
 #  float   supxlabel_font_size_float
 #                          The parameter is the figure's x-axis label's font size.
 #  string  supxlabel_font_style_string
 #                          The parameter is the figure's x-axis label's font style.
 #  float   supylabel_x_float
 #                          The parameter is the figure's y-axis label's 
 #                          x-coordinate padding.
 #  float   supylabel_y_float
 #                          The parameter is the figure's y-axis label's 
 #                          y-coordinate padding.
 #  float   supylabel_font_size_float
 #                          The parameter is the figure's y-axis label's font size.
 #  string  supylabel_font_style_string
 #                          The parameter is the figure's y-axis label's font style.
 #  string  titles_string_list
 #                          The parameter is the list of chart titles.
 #  float   title_font_size_float
 #                          The parameter is the title font size. 
 #  string  title_font_style_string
 #                          The parameter is the title font style.
 #  float   title_pad_float
 #                          The parameter is the title space pad value. 
 #  float   title_y_float
 #                          The parameter is the title's y-axis displacement.
 #  string  xlabel_string
 #                          The parameter is the subplot's x-axis label.
 #  float   xlabel_pad_float  
 #                          The parameter is the subplot's x-axis label's padding.
 #  float   xlabel_font_size_float
 #                          The parameter is the subplot's x-axis label's font size.
 #  string  xlabel_loc_string
 #                          The parameter is the subplot's x-axis label's general location.
 #  string  xlabel_font_style_string
 #                          The parameter is the subplot's x-axis label's font style.
 #  string  ylabel_string
 #                          The parameter is the subplot's y-axis label.
 #  float   ylabel_pad_float  
 #                          The parameter is the subplot's y-axis label's padding.
 #  float   ylabel_font_size_float
 #                          The parameter is the subplot's y-axis label's font size.
 #  string  ylabel_loc_string
 #                          The parameter is the subplot's y-axis label's general location.
 #  string  ylabel_font_style_string
 #                          The parameter is the subplot's y-axis label's font style.
 #  float   figure_width_float
 #                          The parameter is the figure width. 
 #  float   figure_length_float
 #                          The parameter is the figure length. 
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/  

def display_plots_from_series_list \
        (input_series_list,
         suptitle_string,
         supxlabel_string = None,
         supylabel_string = None,
         xlabel_string = '',
         ylabel_string = '',
         color_string = 'darkgreen',
         reverse_dimensions_boolean = True,
         share_x_boolean = True,
         share_y_boolean = True,
         tight_layout_boolean = True,
         alpha_float = 1.0,
         grid_boolean = True,
         suptitle_x_float = 0.5,  
         suptitle_y_float = 0.9,  
         suptitle_font_size_float = 20.0,
         suptitle_font_weight_string = 'normal',
         supxlabel_x_float = 0.5,  
         supxlabel_y_float = 0.0,  
         supxlabel_font_size_float = 16.0,
         supxlabel_font_weight_string = 'normal',
         supylabel_x_float = 0.0,  
         supylabel_y_float = 0.5,  
         supylabel_font_size_float = 16.0,
         supylabel_font_weight_string = 'normal',
         title_font_size_float = 20.0,
         title_font_style_string = 'normal',
         title_pad_float = 20.0,
         xlabel_font_size_float = 16.0,
         xlabel_font_style_string = 'normal',
         xlabel_pad_float = 10.0,
         ylabel_font_size_float = 16.0,
         ylabel_font_style_string = 'normal',
         ylabel_pad_float = 10.0,
         xticks_font_size_float = 14.0,
         xticks_rotation_float = 90.0,
         yticks_font_size_float = 14.0,
         yticks_rotation_float = 0.0,
         tight_layout_float = 3.0,
         figure_width_float = 15.0,
         figure_length_float = 10.0):

    chart_count_integer = len(input_series_list)

    colors_string_list = [color_string] * chart_count_integer


    row_count_integer, column_count_integer \
        = mathx.calculate_closest_factors(chart_count_integer)

    if reverse_dimensions_boolean == True:

        row_count_integer, column_count_integer = column_count_integer, row_count_integer       


    fig, axs \
        = plt.subplots \
            (row_count_integer, 
             column_count_integer, 
             figsize = (figure_width_float, figure_length_float),
             sharex = share_x_boolean,
             sharey = share_y_boolean, 
             tight_layout = tight_layout_boolean)


    plt.clf()


    fig.suptitle \
        (suptitle_string,
         x = suptitle_x_float,
         y = suptitle_y_float,
         fontsize = suptitle_font_size_float, 
         fontweight = suptitle_font_weight_string)


    for index in range(chart_count_integer):

        plt.subplot(row_count_integer, column_count_integer, index + 1)


        input_series_list[index] \
            .plot \
                (color = colors_string_list[index], 
                 alpha = alpha_float, 
                 grid = grid_boolean,
                 legend = False)


        plt.title \
            (input_series_list[index].name,
             fontdict = {'fontsize': title_font_size_float, 
                         'fontstyle': title_font_style_string},
             pad = title_pad_float)


        plt.xlabel \
            (xlabel_string,
             fontdict = {'fontsize': xlabel_font_size_float,
                         'fontstyle': xlabel_font_style_string},
             labelpad = xlabel_pad_float)

        plt.ylabel \
            (ylabel_string,
             fontdict = {'fontsize': ylabel_font_size_float,
                         'fontstyle': ylabel_font_style_string},
             labelpad = ylabel_pad_float)

        plt.xticks(fontsize = xticks_font_size_float, rotation = xticks_rotation_float)

        plt.yticks(fontsize = yticks_font_size_float, rotation = yticks_rotation_float)


        plt.tight_layout(pad = 3.0)


    if supxlabel_string != None:

        fig.supxlabel \
            (supxlabel_string,
             x = supxlabel_x_float,
             y = supxlabel_y_float,
             fontsize = supxlabel_font_size_float, 
             fontweight = supxlabel_font_weight_string)

    if supylabel_string != None:

            fig.supylabel \
                (supylabel_string,
                 x = supylabel_x_float,
                 y = supylabel_y_float,
                 fontsize = supylabel_font_size_float, 
                 fontweight = supylabel_font_weight_string)


    logx.save_plot_image(suptitle_string)

    plt.show()


# In[ ]:




