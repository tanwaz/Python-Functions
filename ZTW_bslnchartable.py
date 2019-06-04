#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 15:53:44 2019

@author: Zhenying Tan-Wasielewski
"""

########################################################################################################
# NOTE: this function z needs to be updated. Due to the deadlines at this moment, this will do for now #
# FUTURE PLAN: make a class with function (including this) that outputs to the excel as a table        #
########################################################################################################

###############################################################################################################
# This function creates a baseline characteristics frequency table from a data set or columns from a data set #
###############################################################################################################


import pandas as pd

def table (data, count_name, *args):
    
    ###################################################################################################
    ## data: the name of the data set                                                                ##
    ## count_name: the name for the count column of the final table                                  ##
    ## *args: optional multiple arguments, here, they are the columns names if specification needed  ##
    ###################################################################################################

    argCount=len(args)
    finaldf = pd.DataFrame()
    append_df=[]
    
    #if arguments are given
    if argCount > 0:
        for column in args:
            #frequency table (df)
            table_df=pd.crosstab(data[column], columns="count")
            #calculate percent
            table_df=pd.merge(table_df, table_df.apply(lambda x: round(x/x.sum()*100)), on=column, how='left')
            #formatting the table
            table_df[count_name]=table_df[["count_x", "count_y"]].apply(lambda x: '('.join(x.astype(int).astype(str))+'%)', axis=1)
            table_df["Category"] = column
            table_df["SubCategory"] = table_df.index
            table_df=pd.DataFrame(table_df[['Category',"SubCategory",count_name]])
            #append tables together into a list
            append_df.append(table_df)
            #concatenate tables from the list into one whole table
            finaldf=pd.concat(append_df)
            finaldf = finaldf.set_index(['Category'])
            finaldf.groupby(level=0)
            
    else:
        for column in data:
            table_df=pd.crosstab(data[column], columns="count")
            table_df=pd.merge(table_df, table_df.apply(lambda x: round(x/x.sum()*100)), on=column, how='left')
            table_df[count_name]=table_df[["count_x", "count_y"]].apply(lambda x: '('.join(x.astype(int).astype(str))+'%)', axis=1)
            table_df["Category"] = column
            table_df["SubCategory"] = table_df.index
            table_df=pd.DataFrame(table_df[['Category',"SubCategory",count_name]])
            append_df.append(table_df)
            finaldf=pd.concat(append_df)
            finaldf = finaldf.set_index(['Category'])
            finaldf.groupby(level=0)
        
    return finaldf
