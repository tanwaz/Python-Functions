# -*- coding: utf-8 -*-
"""
Spyder Editor

Author: Zhenying Tan-Wasielewski
"""
######################################################################################
## This function allows users to import all data (either csv or sas7bdat or xlsx) OR #
#  a single data with data_name specified from a directory                           #
######################################################################################

import pandas as pd
import os
import glob
import csv

def getdata(path,data_name=None, excel_index_col=None):
    ######################################################################################
    ##path: user enters the directory where data files are                              ##
    ##data_name (optional): user can enter the speicifc data file in the path directory ##
    ##excel_index_col (optional): if xlsx file, user enters to specify the sheet number ##
    ######################################################################################
    
    #make a list of all paths if data_name is not specified
    if data_name is None:
        all_files = [f for f in glob.glob(path+'\\*', recursive=True)]
    #make a list of one single path if data_name is specified
    else:
        all_files = [f for f in glob.glob(path+'\\'+data_name+'*', recursive=True)]
    #define a dictionary with keys as the data names and values are variables
    data_storage={}
    for file in all_files:
        #file_name is a tuple: 0=data name; 1=extension(csv or sas7bdat)
        file_name=os.path.splitext(os.path.basename(file))
        
        #if it is a csv file 
        if 'csv' in file_name[1]:
            #able to open only non-empty csv files
            with open (file) as csvfile:
                csv_dict=[row for row in csv.DictReader(csvfile)]
                if len(csv_dict) != 0:
                    df=pd.read_csv(file)
                    data_storage[file_name[0]] = df
                    
        #if it is a sas file
        elif 'sas7bdat' in file_name[1]: 
        	df=pd.read_sas(file)
        	data_storage[file_name[0]] = df
            
        #if it is an excel file
        elif 'xlsx' in file_name[1]:
            df=pd.read_excel(file, excel_index_col)
            data_storage[file_name[0]] = df
    if data_name is None:
        return data_storage
    else:
        return data_storage[data_name]

        
