#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  pandasx.py
 #
 #  File Description:
 #      This Python script, pandasx.py, contains Python functions for processing
 #      Pandas data structures. Here is the list:
 #
 #      get_google_colab
 #      set_google_colab
 #
 #      get_table_conversion
 #      set_table_conversion
 #
 #      get_format_dict
 #      set_format_dict
 #
 #      get_style_dict
 #      set_style_dict
 #
 #      get_hvplot_dict
 #      set_hvplot_dict
 #
 #      fmt_df_from_dict
 #      sv_img_rtn_styler
 #
 #      rtn_std_fmt_styler
 #      rtn_fmt_tbl
 #      rtn_fmt_rows
 #      rtn_df_desc
 #      rtn_fmt_desc
 #
 #      disp_df_col_cnts
 #      disp_df_col_unq_val
 #      disp_series_unq_val_cnts
 #      disp_series_list_stats
 #      disp_df_hvplot
 #
 #      rtn_stats_list
 #      rtn_smry_stats_as_df
 #      rtn_stats_styler_from_series
 #      rtn_stats_styler_from_series_list
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #  02/18/2026          Upgraded Module                             Nicholas J. George
 #
 #******************************************************************************************/

import logx

import hvplot.pandas

import dataframe_image as dfi
import numpy as np
import pandas as pd

pd.options.mode.chained_assignment = None


# In[2]:


CONSTANT_LOCAL_FILE_NAME = 'pandasx.py'


# In[3]:


config_dict \
    = {'google_colab': False,
       'table_conversion': 'selenium'}

fmt_dict \
    = {'text': '{:}',
       'int': '{:,}',
       'flt': '{:,.2f}',
       'flt_int': '{:,.0f}',
       'pct': '{:,.2%}',
       'pct_flt': '{:,.2f}%',
       'pct_int': '{:,}%',
       'curr_int': '${:,}',
       'curr_flt': '${:,.2f}',
       'curr_flt_int': '${:,.0f}',
       'tmpf_int': '{:,}° F',
       'tmpc_int': '{:,}° C',
       'tmpf_flt': '{:,.2f}° F',
       'tmpc_flt': '{:,.2f}° C',
       'eqn_coeff_prec': 4}

style_dict \
    = {'table_styles': [{'selector': 'caption',
                         'props': [('color', 'black'),
                                   ('font-size', '20px'),
                                   ('font-style', 'bold'),
                                   ('text-align', 'center')]}],
       'properties': {'text-align': 'center',
                      'border': '1.3px solid red',
                      'color': 'blue'},
       'format': {'precision': 2,
                  'thousands': ',',
                  'decimal': '.'}}

hvplot_dict \
    = {'lng_col': 'longitude',
       'lat_col': 'latitude',
       'color_col': 'city',
       'size_col': 'humidity',
       'x_lbl': '',
       'y_lbl': '',
       'geo': True,
       'x_lmt': (-180, 180),
       'y_lmt': (-55, 75),
       'alpha': 0.7,
       'tiles': 'OSM',
       'hover_cols': []}

stats_dict \
    = {'idx': np.array(['mean', 'median', 'mode', 'variance', 'std_dev', 'sem',
                        'minimum', '25%', '50%', '75%', 'maximum', 'count']),
       'format': {'mean': lambda x: f'{x:.4f}',
                  'median': lambda x: f'{x:.4f}',
                  'mode': lambda x: f'{x:.4f}',
                  'variance': lambda x: f'{x:.4f}',
                  'std_dev': lambda x: f'{x:.4f}',
                  'sem': lambda x: f'{x:.4f}',
                  'minimum': lambda x: f'{x:.2f}',
                  '25%': lambda x: f'{x:.2f}',
                  '50%': lambda x: f'{x:.2f}',
                  '75%': lambda x: f'{x:.2f}',
                  'maximum': lambda x: f'{x:.2f}',
                  'count': lambda x: f'{x:.0f}'},
       'desc': {'count': lambda x: f'{x:,.0f}',
                'mean': lambda x: f'{x:,.2f}',
                'std': lambda x: f'{x:,.2f}',
                'min': lambda x: f'{x:,.0f}',
                '25%': lambda x: f'{x:,.2f}',
                '50%': lambda x: f'{x:,.2f}',
                '75%': lambda x: f'{x:,.2f}',
                'max': lambda x: f'{x:,.0f}'}}


# In[4]:


#*******************************************************************************************
 #
 #  Function Name:  get_google_colab
 #
 #  Function Description:
 #      This function returns the global boolean for google colaboratory.
 #
 #
 #  Return Type: bool
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  n/a            n/a              n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_google_colab(): 

    return config_dict['google_colab']


# In[5]:


#*******************************************************************************************
 #
 #  Function Name:  set_google_colab
 #
 #  Function Description:
 #      This function sets the global boolean for google colaboratory.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  boolean        input_bool       The parameter is the input boolean value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_google_colab(input_bool):

  global config_dict

  config_dict['google_colab'] = input_bool


# In[6]:


#*******************************************************************************************
 #
 #  Function Name:  get_table_conversion
 #
 #  Function Description:
 #      This function returns the global table conversion specifier.
 #
 #
 #  Return Type: string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  n/a            n/a              n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_table_conversion(): 

    return config_dict['table_conversion']


# In[7]:


#*******************************************************************************************
 #
 #  Function Name:  set_table_conversion
 #
 #  Function Description:
 #      This function sets the global table conversion specifier.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         tbl_conv         The parameter is the new table conversion specifier.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_table_conversion(tbl_conv):

  global config_dict

  config_dict['table_conversion'] = tbl_conv


# In[8]:


#*******************************************************************************************
 #
 #  Function Name:  get_format_dict
 #
 #  Function Description:
 #      This function returns the global format dictionary for objects.
 #
 #
 #  Return Type: dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  n/a            n/a              n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_format_dict(): 

    return fmt_dict


# In[9]:


#*******************************************************************************************
 #
 #  Function Name:  set_format_dict
 #
 #  Function Description:
 #      This function sets the global format dictionary for objects.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     upd_fmt_dict     The parameter is the updated format dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_format_dict(upd_fmt_dict):

  global fmt_dict

  fmt_dict = upd_fmt_dict


# In[10]:


#*******************************************************************************************
 #
 #  Function Name:  get_style_dict
 #
 #  Function Description:
 #      This function returns the global style dictionary for dataframes and stylers.
 #
 #
 #  Return Type: dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  n/a            n/a              n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_style_dict(): 

    return style_dict


# In[11]:


#*******************************************************************************************
 #
 #  Function Name:  set_style_dict
 #
 #  Function Description:
 #      This function sets the global style dictionary for pandas dataframes and stylers.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dict           upd_style_dict   The parameter is the updated style dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_style_dict(upd_style_dict):

  global style_dict

  style_dict = upd_style_dict


# In[12]:


#*******************************************************************************************
 #
 #  Function Name:  get_hvplot_dict
 #
 #  Function Description:
 #      This function returns the global hvplot parameters dictionary.
 #
 #
 #  Return Type: dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  n/a            n/a              n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_hvplot_dict(): 

    return hvplot_dict


# In[13]:


#*******************************************************************************************
 #
 #  Function Name:  set_hvplot_dict
 #
 #  Function Description:
 #      This function sets the global hvplot parameters dictionary.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     upd_hvplot_dict  The parameter is the updated hvplot dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_hvplot_dict(upd_hvplot_dict): 

    global hvplot_dict

    hvplot_dict = upd_hvplot_dict


# In[14]:


#*******************************************************************************************
 #
 #  Function Name:  get_stats_dict
 #
 #  Function Description:
 #      This function returns the global statistics format dictionary for dataframes 
 #      and stylers.
 #
 #
 #  Return Type: dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  n/a            n/a              n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_stats_dict(): 

    return stats_dict


# In[15]:


#*******************************************************************************************
 #
 #  Function Name:  set_stats_dict
 #
 #  Function Description:
 #      This function sets the global statistics format dictionary for dataframes 
 #      and stylers.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     upd_stats_dict   The parameter is the updated statistics dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_stats_dict(upd_stats_dict):

  global stats_dict

  stats_dict = upd_stats_dict


# In[16]:


#*******************************************************************************************
 #
 #  Function Name:  fmt_df_from_dict
 #
 #  Function Description:
 #      This function formats a dataframe based on a format dictionary 
 #      and returns a styler.
 #
 #
 #  Return Type: styler
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dataframe      input_df         The parameter is the input dataframe.
 #  dictionary     input_dict       The parameter is the format dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def fmt_df_from_dict \
        (input_df,
         input_dict):

    input_styler = input_df.style

    nmbr_cols = len(input_styler.columns)


    for idx, fmt in input_dict.items():

        row = input_styler.index.get_loc(idx)

        for col in range(nmbr_cols):

            input_styler._display_funcs[(row, col)] = fmt


    return input_styler


# In[17]:


#*******************************************************************************************
 #
 #  Function Name:  sv_img_rtn_styler
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
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  styler         input_styler     The parameter is the input styler object.
 #  string         title            The parameter is the table title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def sv_img_rtn_styler \
        (input_styler,
         title):

    if logx.logs_config_dict['img_mode'] == True:

        img_file_path = logx.curr_img_file_path(title, 'png')

        dfi.export \
            (input_styler,
             img_file_path,
             table_conversion = config_dict['table_conversion'],
             max_rows = -1, max_cols = -1)

    return input_styler


# In[18]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_std_fmt_styler
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
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dataframe      input_df         The parameter is the input dataframe.
 #  string         title            The parameter is the table title.
 #  boolean        hide_idx_bool    The optional parameter indicates whether the index
 #                                  column is hidden or not.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_std_fmt_styler \
        (input_df,
         title,
         hide_idx_bool = True):

    fmt_styler \
        = input_df \
            .style \
            .set_caption(title) \
            .set_table_styles \
                (style_dict['table_styles']) \
            .set_properties \
                (**style_dict['properties']) \
            .format \
                (style_dict['format'])

    if hide_idx_bool == True:

        return fmt_styler.hide()

    else:

        return fmt_styler


# In[19]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_fmt_tbl
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
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dataframe      input_df         The parameter is the input dataframe.
 #  string         title            The parameter is the table title.
 #  integer        line_cnt_int     The parameter is the number of displayed records.
 #  boolean        hide_idx_bool    The parameter indicates whether the index is present.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_fmt_tbl \
        (input_df,
         title,
         line_cnt_int = 10,
         hide_idx_bool = True):

    curr_styler \
        = rtn_std_fmt_styler \
            (input_df.head(line_cnt_int),
             title,
             hide_idx_bool)

    return sv_img_rtn_styler(curr_styler, title)


# In[20]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_fmt_rows
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
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  styler         input_styler     The parameter is the input styler.
 #  dictionary     input_dict       The parameter is the dicitionary with the format 
 #                                  specifications.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_fmt_rows \
        (input_styler,
         input_dict):

    for k, v in input_dict.items():

        row = input_styler.index.get_loc(k)

        for col in range(len(input_styler.columns)):

            input_styler._display_funcs[(row, col)] = v


    return input_styler


# In[21]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_df_desc
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
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dataframe      input_df         The parameter is the input dataframe.
 #  string         title            The parameter is the description title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_df_desc \
        (input_df,
         title):

    desc_df \
        = input_df.describe()

    desc_styler \
        = rtn_fmt_rows(desc_df.style, stats_dict['desc'])

    return \
        desc_styler \
            .set_caption(title) \
            .set_table_styles \
                (style_dict['table_styles']) \
            .set_properties \
                (**style_dict['properties'])


# In[22]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_fmt_desc
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
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dataframe      input_df         The parameter is the input dataframe.
 #  string         title            The parameter is the description title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_fmt_desc \
        (input_df,
         title):

    curr_styler = rtn_df_desc(input_df, title)

    return sv_img_rtn_styler(curr_styler, title)


# In[23]:


#*******************************************************************************************
 #
 #  Function Name:  disp_df_col_cnts
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
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dataframe      input_df         The parameter is the input dataframe.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def disp_df_col_cnts(input_df):

    for i, col in enumerate(input_df.columns):

        cnt_int = input_df[col].nunique()

        logx.print_and_log_text \
            ('\033[1m' + f'{col}: ' + '{:,}\n'.format(cnt_int) + '\033[0m')


# In[24]:


#*******************************************************************************************
 #
 #  Function Name:  disp_df_col_unq_val
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
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dataframe      input_df         The parameter is the input dataframe.
 #  boolean        rvs_bool         The parameter indicates whether the script sorts 
 #                                  the list in reverse order or not.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def disp_df_col_unq_val \
        (input_df,
         rvs_bool = False):

    for i, col in enumerate(input_df.columns):

        value_list = input_df[col].unique().tolist()

        logx.print_and_log_text \
            ('\033[1m' + f'{col}:\n'
             + f'{sorted(value_list, reverse = rvs_bool)}\n\n'
             + '\033[0m')


# In[25]:


#*******************************************************************************************
 #
 #  Function Name:  disp_series_unq_val_cnts
 #
 #  Function Description:
 #      This function displays the sorted unique value count of a series then returns
 #      the sorted series.
 #
 #
 #  Return Type: series
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         input_series    The parameter is the input series.
 #  string         series_name     The parameter is the sorted series name.
 #  boolean        asc_bool        The parameter indicates wheher the script sorts the
 #                                 series in ascending order or not.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def disp_series_unq_val_cnts \
        (input_series,
         series_name = 'output_series',
         asc_bool = False):

    srtd_series \
        = input_series \
            .value_cnts() \
            .sort_values \
                (ascending = asc_bool)

    srtd_series.name = series_name


    for k, v in srtd_series.items():

        logx.print_and_log_text('\033[1m' + str(k) + '\t' + str(v) + '\n' + '\033[0m')


    return srtd_series


# In[26]:


#*******************************************************************************************
 #
 #  Function Name:  disp_series_list_stats
 #
 #  Function Description:
 #      This subroutine calculates and displays summary statistics for each drug
 #      in the series list.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  list           input_list       The parameter is the input series list.
 #  array          title_array      The parameter is the list of drug regimen names.
 #  string         section_name     The parameter is the section name.
 #  string         stats_type       The parameter is the statistics type.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def disp_series_list_stats \
        (input_list,
         title_array,
         section_name,
         stats_type):

    for idx, title in enumerate(title_array):

        stats_df \
            = rtn_smry_stats_as_df \
                (input_list[idx])

        caption \
            = 'Table ' \
              + section_name \
              + f'.{idx + 1}: ' \
              + stats_type \
              + f' Statistics for {title}'

        curr_styler \
            = rtn_std_fmt_styler \
                (stats_df, caption)

        curr_styler \
            = sv_img_rtn_styler \
                (curr_styler, caption)


        display(curr_styler)


# In[27]:


#******************************************************************************************
 #
 #  Function Name:  disp_df_hvplot
 #
 #  Function Description:
 #      This function receives a dataframe and displays a formatted hvplot. This function
 #      uses the global dictionary hvplot_dict for its remaining parameters.
 #
 #
 #  Return Type: hvplot overlay
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dataframe      input_df         The parameter is the input dataframe.
 #  string         title            The parameter is the plot's title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def disp_df_hvplot \
        (input_df,
         title):

    hvplot_overlay \
        = input_df \
            .hvplot \
            .points \
                (hvplot_dict['lng_col'],
                 hvplot_dict['lat_col'],
                 xlabel = hvplot_dict['x_lbl'],
                 ylabel = hvplot_dict['y_lbl'],
                 geo = hvplot_dict['geo'],
                 color = hvplot_dict['color_col'],
                 size = hvplot_dict['size_col'],
                 xlim = hvplot_dict['x_lmt'],
                 ylim = hvplot_dict['y_lmt'],
                 alpha = hvplot_dict['alpha'],
                 tiles = hvplot_dict['tiles'],
                 title = title,
                 hover_cols = hvplot_dict['hover_cols'])

    logx.save_hvplot_image_to_html(hvplot_overlay, title)

    return hvplot_overlay


# In[28]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_stats_list
 #
 #  Function Description:
 #      This function returns the statistics for a series as a list.
 #
 #
 #  Return Type: dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         input_series     The parameter is the input series.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_stats_list(input_series):

    stats_list \
        = [input_series.mean(),
           input_series.median(),
           input_series.mode()[0],
           input_series.var(),
           input_series.std(),
           input_series.sem(),
           input_series.min(),
           input_series.describe().loc['25%'],
           input_series.describe().loc['50%'],
           input_series.describe().loc['75%'],
           input_series.max(),
           input_series.count()]

    return stats_list


# In[29]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_smry_stats_as_df
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
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         input_series     The parameter is the input series.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_smry_stats_as_df(input_series):

    quartiles_series = input_series.quantile([0.25, 0.50, 0.75])


    lower_quartile_flt = quartiles_series[0.25]

    upper_quartile_flt = quartiles_series[0.75]


    interquartile_range_flt = upper_quartile_flt - lower_quartile_flt


    lower_bound_flt = lower_quartile_flt - (1.5 * interquartile_range_flt)

    upper_bound_flt = upper_quartile_flt + (1.5 * interquartile_range_flt)


    outliers_series \
        = input_series.loc \
            [(input_series < lower_bound_flt) | (input_series > upper_bound_flt)]


    outlier_count_int = len(outliers_series)

    stats_dict_list \
        = [{'lower_quartile': lower_quartile_flt,
            'upper_quartile': upper_quartile_flt,
            'interquartile_range': interquartile_range_flt,
            'median': quartiles_series[0.5],
            'lower_boundary': lower_bound_flt,
            'upper_boundary': upper_bound_flt,
            'outlier_count': outlier_count_int}]

    return pd.DataFrame(stats_dict_list)


# In[30]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_stats_styler_from_series
 #
 #  Function Description:
 #      This function receives a series, calculates its statistical values, places them
 #      in a dataframe, formats the dataframe as a syler and returns it to the caller.
 #
 #
 #  Return Type: dataframe
 #
 #
 #  Function Parameters:
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         input_series     The parameter is the input series.
 #  string         title            The parameter is the title of the styler.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_stats_styler_from_series \
        (input_series,
         title):

    stats_list \
        = rtn_stats_list(input_series)

    stats_df \
        = pd.DataFrame \
            (stats_list,
             columns = [input_series.name],
             index = stats_dict['idx'])

    stats_styler \
        = fmt_df_from_dict \
             (stats_df, stats_dict['format'])

    stats_styler \
        .set_caption(title) \
        .set_table_styles \
            (style_dict['table_styles']) \
        .set_properties \
            (**style_dict['properties'])


    return sv_img_rtn_styler(stats_styler, title)


# In[31]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_stats_styler_from_series_list
 #
 #  Function Description:
 #      This function receives a series list, calculates the statistical values 
 #      of each series, places them in a dataframe, and returns the styler to 
 #      the caller.
 #
 #
 #  Return Type: styler
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  list           input_list       The parameter is the input series list.
 #  string         title            The parameter is the title for the styler.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_stats_styler_from_series_list \
        (input_list,
         title):

    for idx, series in enumerate(input_list):

        stats_flt_array \
            = rtn_stats_as_array(series)

        temp_df \
            = pd.DataFrame \
                (stats_flt_array,
                 columns = [series.name],
                 index = stats_dict['idx'])

        if idx != 0:

            stats_df \
                = pd.concat([stats_df, temp_df], axis = 1)

        else:

            stats_df = temp_df.copy()


    stats_styler \
        = fmt_df_from_dict \
             (stats_df, stats_dict['format'])

    stats_styler \
        .set_caption(title) \
        .set_table_styles \
            (style_dict['table_styles']) \
        .set_properties \
            (**style_dict['properties'])


    return stats_styler


# In[ ]:




