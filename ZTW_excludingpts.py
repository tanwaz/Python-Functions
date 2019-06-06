# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:17:35 2019

@author: Zhenying Tan-Wasielewski
"""

##################################################################################
## This funciton lets user to exclude patients given an exclusion criteria list ##
## and returns as a dictionary: key=data name; value=new dataframes             ##
##################################################################################

def exclude(*args, col, exc):
    ################################################################################################
    ## *args: user enters one or  multiple dataframes on which they want to perform the exclusion ##
    ## col: column which exlcusion criteria matches, in all of our studies, casenum               ##
    ## exc: the exclusion critreia, in list                                                       ##
    ################################################################################################
    
    df_storage={}
    for data in args:
        data_name =[x for x in globals() if globals()[x] is data][0]
        df=data[~data[col].isin(exc)]
        df_storage[data_name]=df
    return df_storage