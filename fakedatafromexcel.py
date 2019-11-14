#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 14:31:51 2019

@author: ubuntu
"""

from faker import Faker
import pandas as pd
import numpy as np
import random
import re
import os

class fakedata:
    
    def normal(self, repeat=100, loc=1, scale=100):
        datalist=[]
        for i in range(repeat):
            datalist.append(abs(int(np.random.normal(loc, scale))))
        return datalist
    
    def fakedatagenarator(self, in_path, repeat=1000, start_id=1, out_path='output'):
        fake = Faker()
        df_new=pd.DataFrame()
        xl = pd.ExcelFile(in_path)
        sheetsList = xl.sheet_names
        sheetsList.remove('List Table')
        
        for sheet in sheetsList:
            df = xl.parse(sheet)
            for row in range(len(df.iloc[:, 1])):
                FieldName, DataType = df.iloc[row, 0].upper(), re.sub(r'[^A-z]', '', df.iloc[row, 1].upper())
                if DataType=='NUMBER':
                    if FieldName == 'AGE':
                        df_new[FieldName]=[random.choice(list(range(1,100))) for i in range(repeat)]
                    else:
                        df_new[FieldName]=self.normal(repeat)
            
                elif DataType=='TIMESTAMP' or DataType=='DATE':
                    df_new[FieldName]=[fake.date() for i in range(repeat)]
            
                elif DataType=='VARCHAR':
                    if FieldName == 'SEX' or FieldName == 'GENDER':
                        df_new[FieldName]=[random.choice(['M', 'F']) for i in range(repeat)]
                    elif FieldName == 'AREA_CODE' or FieldName =='PINCODE':
                        df_new[FieldName]=[fake.profile()['residence'].split()[-1] for i in range(repeat)]
                    else:
                        df_new[FieldName]=[fake.name() for i in range(repeat)]
            
            df_new.index=list(np.array(df_new.index)+start_id)
            
            if not os.path.exists(out_path):
                os.makedirs(out_path)
                
            df_new.to_csv(out_path+'/'+sheet+'.csv', index=True, header=True)
            df_new = pd.DataFrame()