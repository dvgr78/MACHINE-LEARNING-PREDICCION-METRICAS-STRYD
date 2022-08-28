# ******************************************************************************
# ***************              LIBRERÍAS A IMPORTAR              ***************
# ******************************************************************************
import pandas                       as pd
import matplotlib.pyplot            as plt
import pandas                       as pd
import numpy                        as np
import seaborn                      as sns

# ******************************************************************************
# ***************           CARGAMOS NUESTO DATAFRAME            ***************
# ******************************************************************************
# Cargamos los datos contenidos en "SEGMENTOS_csv.csv"
data = pd.read_csv('SEGMENTOS_csv.csv')
print(data)

# ******************************************************************************
# ***************             ANÁLISIS DE LOS DATOS              ***************
# ******************************************************************************
# Función head()
print(data.head(15))
# Función shape
print(data.shape)
# Función dtaypes
print(data.dtypes)
# Función describe()
print(data.describe())
# Función describe()
pd.set_option('display.width',      100)
pd.set_option('display.precision',  5)
print(data.corr())
# Función skew()
print(data.skew())
# Buscamos datos nulos o faltantes
print(data.isnull().sum())
# Completamos los datos nulos con la media de cada uno
data['DESNIVEL']        = data['DESNIVEL'].fillna(data['DESNIVEL'].median())
# Buscaremos si hay algún valor nulo o vacío en nuestro DataFrame (data)
print(data.isnull().sum())
