# -*- coding: utf-8 -*-
"""
Created on Fri May 26 11:09:31 2023

@author: 289437
"""

import pandas as pd
data = pd.read_parquet('yellow_tripdata_2023-01.parquet', engine='pyarrow')
print(data.head())
print(data.dtypes)