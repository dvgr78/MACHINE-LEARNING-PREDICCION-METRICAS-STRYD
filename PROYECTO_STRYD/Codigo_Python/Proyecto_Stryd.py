import pandas                       as pd
import matplotlib.pyplot            as plt
import pandas                       as pd
import numpy                        as np
import seaborn                      as sns
from    sklearn.model_selection     import train_test_split
from    sklearn.linear_model        import LinearRegression
from    sklearn.metrics             import r2_score
from    sklearn.metrics             import mean_squared_error
import  statsmodels.api             as sm
import  statsmodels.formula.api     as smf
from    statsmodels.stats.anova     import anova_lm

# Cargamos los datos contenidos en "SEGMENTOS_csv.csv"
data = pd.read_csv('SEGMENTOS_csv.csv')
print(data)
# **************************************
# *****   ANÁLISIS DE LOS DATOS    *****
# **************************************

# Mediante head(15) visualizaremos los 15 primeros
# registros para hacernos una idea
print(data.head(15))
# Mediante shape() sabremos las filas y columnas
# que componen nuestro dataframe
print(data.shape)
# Mediante dtypes conoceremos los tipos de datos de
# las diferentes características
print(data.dtypes)
# Formato de los datos
print(f"Cantidad de filas y columnas: {data.shape}")
print(f"Nombre de las columnas: {data.columns}")
print(data.info())

# Descripción de los datos y de diferentes métricas
# como media, varianza, percentiles,
# mínimos, máximos, etc.....
pd.set_option('display.width',      100)
pd.set_option('display.precision',  3)
print(data.describe())

# Buscamos datos nulos o faltantes
print(data.isnull().sum())
# Completamos los datos nulos con la media de cada uno
data['DESNIVEL']        = data['DESNIVEL'].fillna(data['DESNIVEL'].median())
print(data.isnull().sum())

#   SEGMENTAMOS POR CARACTERÍSTICA O ATRIBUTO
por_cp          = data['POR_CP']
distancia       = data['DISTANCIA']
duracion        = data['DURACION']
frec_cardiaca   = data['FREC_CARDIACA']
cadencia        = data['CADENCIA']
tsc             = data['TSC']
fp              = data['FP']
lss             = data['LSS']
osc_vertical    = data['OSC_VERTICAL']
l_zancada       = data['L_ZANCADA']
rfp             = data['RFP']
rlss            = data['RLSS']
rov             = data['ROV']
re              = data['RE']
aire            = data['AIRE']
pendiente       = data['PENDIENTE']
altitud         = data['ALTITUD']
desnivel        = data['DESNIVEL']
rss             = data['RSS']
ritmo           = data['RITMO']

# **********************************************************************************
# *********        CORRELACIÓN ENTRE LAS DIFERENTES CARACTERÍSTICAS        *********
# **********************************************************************************
# COEFICIENTE DE PEARSON
pearson     = data.corr(method="pearson")
print("******************* COEFICIENTE DE PEARSON *******************")
print(pearson)
#   Graficamos la matriz de correlación (Pearson)
plt.figure(figsize=(14,8))
sns.heatmap(pearson, vmax =1, annot=True, cmap='viridis')
plt.title("COEFICIENTES DE PEARSON")
plt.tight_layout()
plt.show()
# COEFICIENTE DE SPEARMAN
spearman    = data.corr(method= "spearman", min_periods = 2)
print("******************* COEFICIENTE DE SPEARMAN *******************")
print(spearman)
#   Graficamos la matriz de correlación (Spearman)
plt.figure(figsize=(14, 8))
sns.heatmap(spearman, vmax =1, annot=True, cmap='viridis')
plt.title("COEFICIENTES DE SPEARMAN")
plt.tight_layout()
plt.show()
print("******************* SKEW O SESGO *******************")
print(data.skew())

# **********************************************************************************
# *******************              VISUALIZACIONES               *******************
# **********************************************************************************
#   Visualizamos histograma de distribución y densidad
f, axes = plt.subplots(4,5, figsize =(14,10))
sns.distplot(por_cp,                ax= axes [0,0])
sns.distplot(distancia,             ax= axes [0,1])
sns.distplot(duracion,              ax= axes [0,2])
sns.distplot(frec_cardiaca,         ax= axes [0,3])
sns.distplot(cadencia,              ax= axes [0,4])
sns.distplot(tsc,                   ax= axes [1,0])
sns.distplot(fp,                    ax= axes [1,1])
sns.distplot(lss,                   ax= axes [1,2])
sns.distplot(osc_vertical,          ax= axes [1,3])
sns.distplot(l_zancada,             ax= axes [1,4])
sns.distplot(rfp,                   ax= axes [2,0])
sns.distplot(rlss,                  ax= axes [2,1])
sns.distplot(rov,                   ax= axes [2,2])
sns.distplot(re,                    ax= axes [2,3])
sns.distplot(aire,                  ax= axes [2,4])
sns.distplot(pendiente,             ax= axes [3,0])
sns.distplot(altitud,               ax= axes [3,1])
sns.distplot(desnivel,              ax= axes [3,2])
sns.distplot(rss,                   ax= axes [3,3])
sns.distplot(ritmo,                 ax= axes [3,4])
plt.tight_layout()
plt.show()

# Visualizacion de boxplot con matplotlib
fig = plt.figure(figsize=(14,10))
ax = fig.gca()
data.plot(ax= ax, kind="box", subplots =True, layout =(4,5), sharex=False)
plt.show()

# Visualizacion de boxplot con seaborn
f, axes = plt.subplots(4,5, figsize =(14,10))
sns.boxplot(por_cp,                ax= axes [0,0])
sns.boxplot(distancia,             ax= axes [0,1])
sns.boxplot(duracion,              ax= axes [0,2])
sns.boxplot(frec_cardiaca,         ax= axes [0,3])
sns.boxplot(cadencia,              ax= axes [0,4])
sns.boxplot(tsc,                   ax= axes [1,0])
sns.boxplot(fp,                    ax= axes [1,1])
sns.boxplot(lss,                   ax= axes [1,2])
sns.boxplot(osc_vertical,          ax= axes [1,3])
sns.boxplot(l_zancada,             ax= axes [1,4])
sns.boxplot(rfp,                   ax= axes [2,0])
sns.boxplot(rlss,                  ax= axes [2,1])
sns.boxplot(rov,                   ax= axes [2,2])
sns.boxplot(re,                    ax= axes [2,3])
sns.boxplot(aire,                  ax= axes [2,4])
sns.boxplot(pendiente,             ax= axes [3,0])
sns.boxplot(altitud,               ax= axes [3,1])
sns.boxplot(desnivel,              ax= axes [3,2])
sns.boxplot(rss,                   ax= axes [3,3])
sns.boxplot(ritmo,                 ax= axes [3,4])
plt.tight_layout()
plt.show()

