#!/usr/bin/env python3
# -*- coding: latin-1 -*-
"""
Created on Fri Mar 25 15:37:50 2022

@author: nalle
"""
from urllib.request import urlopen
import pandas as pd
import json
import math
import numpy as np
import zipfile
import shutil
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

! pip install -q kaggle
pip install -U kaggle==1.5.3
!chmod 600 ~/.kaggle/kaggle.json
! kaggle datasets list
            
#ExtracciÃ³n de datos de API kaggle
! kaggle datasets download -d prasertk/public-holidays-in-every-country-in-2022
! kaggle datasets download -d berkeleyearth/climate-change-earth-surface-temperature-data
! kaggle datasets download -d rtatman/iris-dataset-json-version
ruta_zip="/home/nalle/iris-dataset-json-version.zip"
ruta_extraccion = "/home/nalle/Escritorio/Caso_Práctico/iris-dataset-json-version.zip"
password = None
archivo_zip = zipfile.ZipFile(ruta_zip, "r")
try:
    print(archivo_zip.namelist())
    archivo_zip.extractall(pwd=password, path=ruta_extraccion)
except:
    pass
archivo_zip.close()
shutil.move("/home/nalle/Escritorio/Caso_Práctico/iris-dataset-json-version.zip/iris.json","/home/nalle/Escritorio/Caso_Práctico/iris.json")

#Estructurando datos en un dataframe
df=pd.read_json("/home/nalle/Escritorio/Caso_Práctico/iris.json",orient='columns')
df.head(10)

#Explorando datos
df.columns
df.shape
df.dtypes
df.head()
df.tail()
df.describe()
df.describe(include="all")
df.info
pd.isna(df)
pd.isnull(df)
df.isnull().values.any()
df.isna().values.any()


#Manipulando datos perdidos
nfila={'sepalLength':5.0,'sepalWidth':3.1,'petalLength':1.5,'petalWidth':0.2}
nfil2={"sepalLength":5.0,"petalLength":1.5,"petalWidth":0.2,"species":"setosa"}
df=df.append(nfila,ignore_index=True)
df=df.append(nfil2,ignore_index=True)
df
print(pd.unique(df['species']))
df['species'].describe()
x=df.groupby('species')
x.describe()
x.mean()
df['sepalWidth'].replace(np.nan,3.4,inplace=True)
df['species'].replace(np.nan,"setosa",inplace=True)

#Guarda el dataframe en archivo .csv
df.to_csv('iris.csv')

!git init 
!git status
!git add .
!git status
!git commit -m "segunda carga"
!git push -u origin nalle@nalle-HP-Pavilion-Notebook

