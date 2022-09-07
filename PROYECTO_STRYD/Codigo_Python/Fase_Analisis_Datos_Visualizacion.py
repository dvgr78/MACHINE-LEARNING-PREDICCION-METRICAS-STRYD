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
# Completamos los datos nulos con la media de cada uno
data['DESNIVEL']        = data['DESNIVEL'].fillna(data['DESNIVEL'].median())
print(data)

# Univariate Histograms
# **********************************************************************************
# *******************              VISUALIZACIONES               *******************
# **********************************************************************************

#   La ubicación de la media y la mediana
#       Dependiendo de la asimetría de una curva de densidad, podemos saber rápidamente
#       si la media o la mediana es mayor en una distribución dada.
#       En particular:
#           Si se deja sesgada una curva de densidad , entonces la media es menor que la mediana.
#           Si una curva de densidad está sesgada a la derecha , entonces la media es mayor que la mediana.
#           Si una curva de densidad no tiene sesgo , entonces la media es igual a la mediana.


# **********************************************************************************
# *******************              VISUALIZACIONES               *******************
# **********************************************************************************
#   HISTOGRAMAS O DISTRIBUCIÓN CON DENSIDAD
f, axes = plt.subplots(4,5, figsize =(11.7,8.27))
sns.histplot(data["POR_CP"],                ax= axes [0,0],kde = True, bins = 20, color="Blue", fill=True)
sns.histplot(data["DISTANCIA"],             ax= axes [0,1],kde = True, bins = 20, color="Blue", fill=True)
sns.histplot(data["RITMO"],                 ax= axes [0,2],kde = True, bins = 20, color="Blue", fill=True)
sns.histplot(data["FREC_CARDIACA"],         ax= axes [0,3],kde = True, bins = 20, color="Blue", fill=True)
sns.histplot(data["CADENCIA"],              ax= axes [0,4],kde = True, bins = 20, color="Blue", fill=True)
sns.histplot(data["TSC"],                   ax= axes [1,0],kde = True, bins = 20, color="Red", fill=True)
sns.histplot(data["FP"],                    ax= axes [1,1],kde = True, bins = 20, color="Red", fill=True)
sns.histplot(data["LSS"],                   ax= axes [1,2],kde = True, bins = 20, color="Red", fill=True)
sns.histplot(data["OSC_VERTICAL"],          ax= axes [1,3],kde = True, bins = 20, color="Red", fill=True)
sns.histplot(data["L_ZANCADA"],             ax= axes [1,4],kde = True, bins = 20, color="Red", fill=True)
sns.histplot(data["RFP"],                   ax= axes [2,0],kde = True, bins = 20, color="Blue", fill=True)
sns.histplot(data["RLSS"],                  ax= axes [2,1],kde = True, bins = 20, color="Blue", fill=True)
sns.histplot(data["ROV"],                   ax= axes [2,2],kde = True, bins = 20, color="Blue", fill=True)
sns.histplot(data["RE"],                    ax= axes [2,3],kde = True, bins = 20, color="Blue", fill=True)
sns.histplot(data["AIRE"],                  ax= axes [2,4],kde = True, bins = 20, color="Blue", fill=True)
sns.histplot(data["PENDIENTE"],             ax= axes [3,0],kde = True, bins = 20, color="Red", fill=True)
sns.histplot(data["ALTITUD"],               ax= axes [3,1],kde = True, bins = 20, color="Red", fill=True)
sns.histplot(data["DESNIVEL"],              ax= axes [3,2],kde = True, bins = 20, color="Red", fill=True)
sns.histplot(data["RSS"],                   ax= axes [3,3],kde = True, bins = 20, color="Red", fill=True)
sns.histplot(data["DURACION"],              ax= axes [3,4],kde = True, bins = 20, color="Red", fill=True)
plt.tight_layout()
plt.show()

# GRAFICOS DE DENSIDAD
f, axes = plt.subplots(4,5, figsize =(11.7,8.27))
sns.kdeplot(data["POR_CP"],         ax = axes [0,0], shade = True, color = "Blue", fill = True,
                                    bw_adjust=.5, clip_on=False, alpha=1, linewidth=1.5)
sns.kdeplot(data["DISTANCIA"],      ax = axes [0,1], shade = True, color = "Blue", fill = True,
                                    bw_adjust=.5, clip_on=False, alpha=1, linewidth=1.5)
sns.kdeplot(data["RITMO"],          ax = axes [0,2], shade = True, color = "Blue", fill = True,
                                    bw_adjust=.5, clip_on=False, alpha=1, linewidth=1.5)
sns.kdeplot(data["FREC_CARDIACA"],  ax = axes [0,3], shade = True, color = "Blue", fill = True,
                                    bw_adjust=.5, clip_on=False, alpha=1, linewidth=1.5)
sns.kdeplot(data["CADENCIA"],       ax = axes [0,4], shade = True, color = "Blue", fill = True,
                                    bw_adjust=.5, clip_on=False, alpha=1, linewidth=1.5)
sns.kdeplot(data["TSC"],            ax = axes [1,0], shade = True, color = "Red", fill = True,
                                    bw_adjust=.5, clip_on=False, alpha=1, linewidth=1.5)
sns.kdeplot(data["FP"],             ax = axes [1,1], shade = True, color = "Red", fill = True,
                                    bw_adjust=.5, clip_on=False, alpha=1, linewidth=1.5)
sns.kdeplot(data["LSS"],            ax = axes [1,2], shade = True, color = "Red", fill = True,
                                    bw_adjust=.5, clip_on=False, alpha=1, linewidth=1.5)
sns.kdeplot(data["OSC_VERTICAL"],   ax = axes [1,3], shade = True, color = "Red", fill = True,
                                    bw_adjust=.5, clip_on=False, alpha=1, linewidth=1.5)
sns.kdeplot(data["L_ZANCADA"],      ax = axes [1,4], shade = True, color = "Red", fill = True,
                                    bw_adjust=.5, clip_on=False, alpha=1, linewidth=1.5)
sns.kdeplot(data["RFP"],            ax = axes [2,0], shade = True, color = "Red", fill = True,
                                    bw_adjust=.5, clip_on=False, alpha=1, linewidth=1.5)
sns.kdeplot(data["RLSS"],           ax = axes [2,1], shade = True, color = "Blue", fill = True,
                                    bw_adjust=.5, clip_on=False, alpha=1, linewidth=1.5)
sns.kdeplot(data["ROV"],            ax = axes [2,2], shade = True, color = "Blue", fill = True,
                                    bw_adjust=.5, clip_on=False, alpha=1, linewidth=1.5)
sns.kdeplot(data["RE"],             ax = axes [2,3], shade = True, color = "Blue", fill = True,
                                    bw_adjust=.5, clip_on=False, alpha=1, linewidth=1.5)
sns.kdeplot(data["AIRE"],           ax = axes [2,4], shade = True, color = "Blue", fill = True,
                                    bw_adjust=.5, clip_on=False, alpha=1, linewidth=1.5)
sns.kdeplot(data["PENDIENTE"],      ax = axes [3,0], shade = True, color = "Red", fill = True,
                                    bw_adjust=.5, clip_on=False, alpha=1, linewidth=1.5)
sns.kdeplot(data["ALTITUD"],        ax = axes [3,1], shade = True, color = "Red", fill = True,
                                    bw_adjust=.5, clip_on=False, alpha=1, linewidth=1.5)
sns.kdeplot(data["DESNIVEL"],       ax = axes [3,2], shade = True, color = "Red", fill = True,
                                    bw_adjust=.5, clip_on=False, alpha=1, linewidth=1.5)
sns.kdeplot(data["RSS"],            ax = axes [3,3], shade = True, color = "Red", fill = True,
                                    bw_adjust=.5, clip_on=False, alpha=1, linewidth=1.5)
sns.kdeplot(data["DURACION"],       ax = axes [3,4], shade = True, color = "Red", fill = True,
                                    bw_adjust=.5, clip_on=False, alpha=1, linewidth=1.5)
plt.tight_layout()
plt.show()
# GRAFICOS BOXPLOTS
f, axes = plt.subplots(4,5, figsize =(11.7,8.27))
sns.boxplot(x = data["POR_CP"],         ax = axes [0,0], orient = "h", color = "lightblue", saturation = 1,
                                        width = 0.7, dodge = True, fliersize = 3, linewidth = 2)
sns.boxplot(x = data["DISTANCIA"],      ax = axes [0,1], orient = "h", color = "lightblue", saturation = 1,
                                        width = 0.7, dodge = True, fliersize = 3, linewidth = 2)
sns.boxplot(x = data["RITMO"],          ax = axes [0,2], orient = "h", color = "lightblue", saturation = 1,
                                        width = 0.7, dodge = True, fliersize = 3, linewidth = 2)
sns.boxplot(x = data["FREC_CARDIACA"],  ax = axes [0,3], orient = "h", color = "lightblue", saturation = 1,
                                        width = 0.7, dodge = True, fliersize = 3, linewidth = 2)
sns.boxplot(x = data["CADENCIA"],       ax = axes [0,4], orient = "h", color = "lightblue", saturation = 1,
                                        width = 0.7, dodge = True, fliersize = 3, linewidth = 2)
sns.boxplot(x = data["TSC"],            ax = axes [1,0], orient = "h", color = "lightgreen", saturation = 1,
                                        width = 0.7, dodge = True, fliersize = 3, linewidth = 2)
sns.boxplot(x = data["FP"],             ax = axes [1,1], orient = "h", color = "lightgreen", saturation = 1,
                                        width = 0.7, dodge = True, fliersize = 3, linewidth = 2)
sns.boxplot(x = data["LSS"],            ax = axes [1,2], orient = "h", color = "lightgreen", saturation = 1,
                                        width = 0.7, dodge = True, fliersize = 3, linewidth = 2)
sns.boxplot(x = data["OSC_VERTICAL"],   ax = axes [1,3], orient = "h", color = "lightgreen", saturation = 1,
                                        width = 0.7, dodge = True, fliersize = 3, linewidth = 2)
sns.boxplot(x = data["L_ZANCADA"],      ax = axes [1,4], orient = "h", color = "lightgreen", saturation = 1,
                                        width = 0.7, dodge = True, fliersize = 3, linewidth = 2)
sns.boxplot(x = data["RFP"],            ax = axes [2,0], orient = "h", color = "lightblue", saturation = 1,
                                        width = 0.7, dodge = True, fliersize = 3, linewidth = 2)
sns.boxplot(x = data["RLSS"],           ax = axes [2,1], orient = "h", color = "lightblue", saturation = 1,
                                        width = 0.7, dodge = True, fliersize = 3, linewidth = 2)
sns.boxplot(x = data["ROV"],            ax = axes [2,2], orient = "h", color = "lightblue", saturation = 1,
                                        width = 0.7, dodge = True, fliersize = 3, linewidth = 2)
sns.boxplot(x = data["RE"],             ax = axes [2,3], orient = "h", color = "lightblue", saturation = 1,
                                        width = 0.7, dodge = True, fliersize = 3, linewidth = 2)
sns.boxplot(x = data["AIRE"],           ax = axes [2,4], orient = "h", color = "lightblue", saturation = 1,
                                        width = 0.7, dodge = True, fliersize = 3, linewidth = 2)
sns.boxplot(x = data["PENDIENTE"],      ax = axes [3,0], orient = "h", color = "lightgreen", saturation = 1,
                                        width = 0.7, dodge = True, fliersize = 3, linewidth = 2)
sns.boxplot(x = data["ALTITUD"],        ax = axes [3,1], orient = "h", color = "lightgreen", saturation = 1,
                                        width = 0.7, dodge = True, fliersize = 3, linewidth = 2)
sns.boxplot(x = data["DESNIVEL"],       ax = axes [3,2], orient = "h", color = "lightgreen", saturation = 1,
                                        width = 0.7, dodge = True, fliersize = 3, linewidth = 2)
sns.boxplot(x = data["RSS"],            ax = axes [3,3], orient = "h", color = "lightgreen", saturation = 1,
                                        width = 0.7, dodge = True, fliersize = 3, linewidth = 2)
sns.boxplot(x = data["DURACION"],       ax = axes [3,4], orient = "h", color = "lightgreen", saturation = 1,
                                        width = 0.7, dodge = True, fliersize = 3, linewidth = 2)
plt.tight_layout()
plt.show()

# Estudio Visualización "POR_CP"
# Métricas POR_CP
print("               ==============================================================================")
print(f"               ===============          MEDIA DE POR_CP:    {data['POR_CP'].mean():,.5f}          ===============")
print(f"               ===============          MEDIANA DE POR_CP:  {data['POR_CP'].median():,.5f}          ===============")
print(f"               ===============          SESGO DE POR_CP:     {data['POR_CP'].skew():,.5f}          ===============")
print(f"               ===============          VARIANZA DE POR_CP: {data['POR_CP'].std():,.5f}          ===============")
print("               ==============================================================================")
f, axes = plt.subplots(2,2, figsize =(11.7,8.27))

sns.histplot(data["POR_CP"],        ax = axes [0,0], kde = True, bins = 20, color="Blue", fill=True)

sns.kdeplot(data["POR_CP"],         ax = axes [0,1], shade = True, color = "Blue", fill = True,
                                    bw_adjust = .5, clip_on = False, alpha=1, linewidth=1.5)

sns.boxplot(x = data["POR_CP"],     ax = axes [1,0], orient = "h", color = "lightblue", saturation = 1,
                                    width = 0.7, dodge = True, fliersize = 3, linewidth = 2)
plt.tight_layout()
plt.show()

# Estudio Visualización "DISTANCIA"
# Métricas DISTANCIA
print("               =====================================================================================")
print(f"               ===============          MEDIA DE DISTANCIA:     {data['DISTANCIA'].mean():,.5f}          ===============")
print(f"               ===============          MEDIANA DE DISTANCIA:   {data['DISTANCIA'].median():,.5f}          ===============")
print(f"               ===============          SESGO DE DISTANCIA:         {data['DISTANCIA'].skew():,.5f}          ===============")
print(f"               ===============          VARIANZA DE DISTANCIA:  {data['DISTANCIA'].std():,.5f}          ===============")
print("               =====================================================================================")

# Visualización Histograma, Densidad y Boxplot de DISTANCIA
f, axes = plt.subplots(2,2, figsize =(11.7,8.27))

sns.histplot(data["DISTANCIA"],     ax = axes [0,0], kde = True, bins = 20, color="Blue", fill=True)

sns.kdeplot(data["DISTANCIA"],      ax = axes [0,1], shade = True, color = "Blue", fill = True,
                                        bw_adjust=.5, clip_on=False, alpha=1, linewidth=1.5)

sns.boxplot(x = data["DISTANCIA"],   ax = axes [1,0], orient = "h", color = "lightgreen", saturation = 1,
                                        width = 0.7, dodge = True, fliersize = 3, linewidth = 2)
plt.tight_layout()
plt.show()

# Estudio Visualización "RITMO"
# Métricas RITMO
print("               ===============================================================================")
print(f"               ===============          MEDIA DE RITMO:     {data['RITMO'].mean():,.5f}          ===============")
print(f"               ===============          MEDIANA DE RITMO:   {data['RITMO'].median():,.5f}          ===============")
print(f"               ===============          SESGO DE RITMO:      {data['RITMO'].skew():,.5f}          ===============")
print(f"               ===============          VARIANZA DE RITMO:   {data['RITMO'].std():,.5f}          ===============")
print("               ===============================================================================")

# Visualización Histograma, Densidad y Boxplot de RITMO
f, axes = plt.subplots(2,2, figsize =(11.7,8.27))

sns.histplot(data["RITMO"],     ax = axes [0,0], kde = True, bins = 20, color="Blue", fill=True)

sns.kdeplot(data["RITMO"],      ax = axes [0,1], shade = True, color = "Blue", fill = True,
                                        bw_adjust=.5, clip_on=False, alpha=1, linewidth=1.5)

sns.boxplot(x = data["RITMO"],   ax = axes [1,0], orient = "h", color = "lightgreen", saturation = 1,
                                        width = 0.7, dodge = True, fliersize = 3, linewidth = 2)
plt.tight_layout()
plt.show()

# Estudio Visualización "FREC_CARDIACA"
# Métricas FREC_CARDIACA
print("               ======================================================================================")
print(f"               ===============          MEDIA DE FREC_CARDIACA:    {data['FREC_CARDIACA'].mean():,.5f}          ===============")
print(f"               ===============          MEDIANA DE FREC_CARDIACA:  {data['FREC_CARDIACA'].median():,.5f}          ===============")
print(f"               ===============          SESGO DE FREC_CARDIACA:      {data['FREC_CARDIACA'].skew():,.5f}          ===============")
print(f"               ===============          VARIANZA DE FREC_CARDIACA:  {data['FREC_CARDIACA'].std():,.5f}          ===============")
print("               ======================================================================================")

# Visualización Histograma, Densidad y Boxplot de FREC_CARDIACA
f, axes = plt.subplots(2,2, figsize =(11.7,8.27))

sns.histplot(data["FREC_CARDIACA"],     ax = axes [0,0], kde = True, bins = 20, color="Blue", fill=True)

sns.kdeplot(data["FREC_CARDIACA"],      ax = axes [0,1], shade = True, color = "Blue", fill = True,
                                        bw_adjust=.5, clip_on=False, alpha=1, linewidth=1.5)

sns.boxplot(x = data["FREC_CARDIACA"],   ax = axes [1,0], orient = "h", color = "lightgreen", saturation = 1,
                                        width = 0.7, dodge = True, fliersize = 3, linewidth = 2)
plt.tight_layout()
plt.show()

# Estudio Visualización "CADENCIA"
# Métricas CADENCIA
print("               ==================================================================================")
print(f"               ===============          MEDIA DE CADENCIA:     {data['CADENCIA'].mean():,.5f}          ===============")
print(f"               ===============          MEDIANA DE CADENCIA:   {data['CADENCIA'].median():,.5f}          ===============")
print(f"               ===============          SESGO DE CADENCIA:      {data['CADENCIA'].skew():,.5f}          ===============")
print(f"               ===============          VARIANZA DE CADENCIA:    {data['CADENCIA'].std():,.5f}          ===============")
print("               ==================================================================================")

# Visualización Histograma, Densidad y Boxplot de CADENCIA
f, axes = plt.subplots(2,2, figsize =(11.7,8.27))

sns.histplot(data["CADENCIA"],     ax = axes [0,0], kde = True, bins = 20, color="Blue", fill=True)

sns.kdeplot(data["CADENCIA"],      ax = axes [0,1], shade = True, color = "Blue", fill = True,
                                        bw_adjust=.5, clip_on=False, alpha=1, linewidth=1.5)

sns.boxplot(x = data["CADENCIA"],   ax = axes [1,0], orient = "h", color = "lightgreen", saturation = 1,
                                        width = 0.7, dodge = True, fliersize = 3, linewidth = 2)
plt.tight_layout()
plt.show()

# Estudio Visualización "TSC"
# Métricas TSC
print("               =============================================================================")
print(f"               ===============          MEDIA DE TSC:     {data['TSC'].mean():,.5f}          ===============")
print(f"               ===============          MEDIANA DE TSC:   {data['TSC'].median():,.5f}          ===============")
print(f"               ===============          SESGO DE TSC:      {data['TSC'].skew():,.5f}          ===============")
print(f"               ===============          VARIANZA DE TSC:   {data['TSC'].std():,.5f}          ===============")
print("               =============================================================================")

# Visualización Histograma, Densidad y Boxplot de TSC
f, axes = plt.subplots(2,2, figsize =(11.7,8.27))

sns.histplot(data["TSC"],     ax = axes [0,0], kde = True, bins = 20, color="Blue", fill=True)

sns.kdeplot(data["TSC"],      ax = axes [0,1], shade = True, color = "Blue", fill = True,
                              bw_adjust=.5, clip_on=False, alpha=1, linewidth=1.5)

sns.boxplot(x = data["TSC"],  ax = axes [1,0], orient = "h", color = "lightgreen", saturation = 1,
                              width = 0.7, dodge = True, fliersize = 3, linewidth = 2)
plt.tight_layout()
plt.show()

# Estudio Visualización "FP"
# Métricas FP
print("               ============================================================================")
print(f"               ===============          MEDIA DE FP:      {data['FP'].mean():,.5f}          ===============")
print(f"               ===============          MEDIANA DE FP:    {data['FP'].median():,.5f}          ===============")
print(f"               ===============          SESGO DE FP:      {data['FP'].skew():,.5f}          ===============")
print(f"               ===============          VARIANZA DE FP:    {data['FP'].std():,.5f}          ===============")
print("               ============================================================================")

# Visualización Histograma, Densidad y Boxplot de FP
f, axes = plt.subplots(2,2, figsize =(11.7,8.27))

sns.histplot(data["FP"],     ax = axes [0,0], kde = True, bins = 20, color="Blue", fill=True)

sns.kdeplot(data["FP"],      ax = axes [0,1], shade = True, color = "Blue", fill = True,
                                        bw_adjust=.5, clip_on=False, alpha=1, linewidth=1.5)

sns.boxplot(x = data["FP"],   ax = axes [1,0], orient = "h", color = "lightgreen", saturation = 1,
                                        width = 0.7, dodge = True, fliersize = 3, linewidth = 2)
plt.tight_layout()
plt.show()

# Estudio Visualización "LSS"
# Métricas LSS
print("               =============================================================================")
print(f"               ===============          MEDIA DE LSS:      {data['LSS'].mean():,.5f}          ===============")
print(f"               ===============          MEDIANA DE LSS:    {data['LSS'].median():,.5f}          ===============")
print(f"               ===============          SESGO DE LSS:      {data['LSS'].skew():,.5f}          ===============")
print(f"               ===============          VARIANZA DE LSS:    {data['LSS'].std():,.5f}          ===============")
print("               =============================================================================")

# Visualización Histograma, Densidad y Boxplot de LSS
f, axes = plt.subplots(2,2, figsize =(11.7,8.27))

sns.histplot(data["LSS"],     ax = axes [0,0], kde = True, bins = 20, color="Blue", fill=True)

sns.kdeplot(data["LSS"],      ax = axes [0,1], shade = True, color = "Blue", fill = True,
                              bw_adjust=.5, clip_on=False, alpha=1, linewidth=1.5)

sns.boxplot(x = data["LSS"],  ax = axes [1,0], orient = "h", color = "lightgreen", saturation = 1,
                              width = 0.7, dodge = True, fliersize = 3, linewidth = 2)
plt.tight_layout()
plt.show()

# Estudio Visualización "OSC_VERTICAL"
# Métricas OSC_VERTICAL
print("               =======================================================================================")
print(f"               ===============          MEDIA DE OSC_VERTICAL:        {data['OSC_VERTICAL'].mean():,.5f}          ===============")
print(f"               ===============          MEDIANA DE OSC_VERTICAL:      {data['OSC_VERTICAL'].median():,.5f}          ===============")
print(f"               ===============          SESGO DE OSC_VERTICAL:       {data['OSC_VERTICAL'].skew():,.5f}          ===============")
print(f"               ===============          VARIANZA DE OSC_VERTICAL:     {data['OSC_VERTICAL'].std():,.5f}          ===============")
print("               =======================================================================================")

# Visualización Histograma, Densidad y Boxplot de OSC_VERTICAL
f, axes = plt.subplots(2,2, figsize =(11.7,8.27))

sns.histplot(data["OSC_VERTICAL"],     ax = axes [0,0], kde = True, bins = 20, color="Blue", fill=True)

sns.kdeplot(data["OSC_VERTICAL"],      ax = axes [0,1], shade = True, color = "Blue", fill = True,
                                        bw_adjust=.5, clip_on=False, alpha=1, linewidth=1.5)

sns.boxplot(x = data["OSC_VERTICAL"],   ax = axes [1,0], orient = "h", color = "lightgreen", saturation = 1,
                                        width = 0.7, dodge = True, fliersize = 3, linewidth = 2)
plt.tight_layout()
plt.show()

# Estudio Visualización "L_ZANCADA"
# Métricas L_ZANCADA
print("               ===================================================================================")
print(f"               ===============          MEDIA DE L_ZANCADA:       {data['L_ZANCADA'].mean():,.5f}          ===============")
print(f"               ===============          MEDIANA DE L_ZANCADA:     {data['L_ZANCADA'].median():,.5f}          ===============")
print(f"               ===============          SESGO DE L_ZANCADA:       {data['L_ZANCADA'].skew():,.5f}          ===============")
print(f"               ===============          VARIANZA DE L_ZANCADA:    {data['L_ZANCADA'].std():,.5f}          ===============")
print("               ===================================================================================")

# Visualización Histograma, Densidad y Boxplot de L_ZANCADA
f, axes = plt.subplots(2,2, figsize =(11.7,8.27))

sns.histplot(data["L_ZANCADA"],     ax = axes [0,0], kde = True, bins = 20, color="Blue", fill=True)

sns.kdeplot(data["L_ZANCADA"],      ax = axes [0,1], shade = True, color = "Blue", fill = True,
                                        bw_adjust=.5, clip_on=False, alpha=1, linewidth=1.5)

sns.boxplot(x = data["L_ZANCADA"],   ax = axes [1,0], orient = "h", color = "lightgreen", saturation = 1,
                                        width = 0.7, dodge = True, fliersize = 3, linewidth = 2)
plt.tight_layout()
plt.show()

# Estudio Visualización "RFP"
# Métricas RFP
print("               =============================================================================")
print(f"               ===============          MEDIA DE RFP:      {data['RFP'].mean():,.5f}          ===============")
print(f"               ===============          MEDIANA DE RFP:    {data['RFP'].median():,.5f}          ===============")
print(f"               ===============          SESGO DE RFP:      {data['RFP'].skew():,.5f}          ===============")
print(f"               ===============          VARIANZA DE RFP:    {data['RFP'].std():,.5f}          ===============")
print("               =============================================================================")

# Visualización Histograma, Densidad y Boxplot de RFP
f, axes = plt.subplots(2,2, figsize =(11.7,8.27))

sns.histplot(data["RFP"],     ax = axes [0,0], kde = True, bins = 20, color="Blue", fill=True)

sns.kdeplot(data["RFP"],      ax = axes [0,1], shade = True, color = "Blue", fill = True,
                                        bw_adjust=.5, clip_on=False, alpha=1, linewidth=1.5)

sns.boxplot(x = data["RFP"],   ax = axes [1,0], orient = "h", color = "lightgreen", saturation = 1,
                                        width = 0.7, dodge = True, fliersize = 3, linewidth = 2)
plt.tight_layout()
plt.show()

# Estudio Visualización "RLSS"
# Métricas RLSS
print("               ==============================================================================")
print(f"               ===============          MEDIA DE RLSS:     {data['RLSS'].mean():,.5f}          ===============")
print(f"               ===============          MEDIANA DE RLSS:   {data['RLSS'].median():,.5f}          ===============")
print(f"               ===============          SESGO DE RLSS:      {data['RLSS'].skew():,.5f}          ===============")
print(f"               ===============          VARIANZA DE RLSS:   {data['RLSS'].std():,.5f}          ===============")
print("               ==============================================================================")

# Visualización Histograma, Densidad y Boxplot de RLSS
f, axes = plt.subplots(2,2, figsize =(11.7,8.27))

sns.histplot(data["RLSS"],     ax = axes [0,0], kde = True, bins = 20, color="Blue", fill=True)

sns.kdeplot(data["RLSS"],      ax = axes [0,1], shade = True, color = "Blue", fill = True,
                                        bw_adjust=.5, clip_on=False, alpha=1, linewidth=1.5)

sns.boxplot(x = data["RLSS"],   ax = axes [1,0], orient = "h", color = "lightgreen", saturation = 1,
                                        width = 0.7, dodge = True, fliersize = 3, linewidth = 2)
plt.tight_layout()
plt.show()

# Estudio Visualización "ROV"
# Métricas ROV
print("               =============================================================================")
print(f"               ===============          MEDIA DE ROV:       {data['ROV'].mean():,.5f}          ===============")
print(f"               ===============          MEDIANA DE ROV:     {data['ROV'].median():,.5f}          ===============")
print(f"               ===============          SESGO DE ROV:      {data['ROV'].skew():,.5f}          ===============")
print(f"               ===============          VARIANZA DE ROV:    {data['ROV'].std():,.5f}          ===============")
print("               =============================================================================")

# Visualización Histograma, Densidad y Boxplot de ROV
f, axes = plt.subplots(2,2, figsize =(11.7,8.27))

sns.histplot(data["ROV"],     ax = axes [0,0], kde = True, bins = 20, color="Blue", fill=True)

sns.kdeplot(data["ROV"],      ax = axes [0,1], shade = True, color = "Blue", fill = True,
                              bw_adjust=.5, clip_on=False, alpha=1, linewidth=1.5)

sns.boxplot(x = data["ROV"],  ax = axes [1,0], orient = "h", color = "lightgreen", saturation = 1,
                              width = 0.7, dodge = True, fliersize = 3, linewidth = 2)
plt.tight_layout()
plt.show()

# Estudio Visualización "RE"
# Métricas RE
print("               ============================================================================")
print(f"               ===============          MEDIA DE RE:       {data['RE'].mean():,.5f}          ===============")
print(f"               ===============          MEDIANA DE RE:     {data['RE'].median():,.5f}          ===============")
print(f"               ===============          SESGO DE RE:      {data['RE'].skew():,.5f}          ===============")
print(f"               ===============          VARIANZA DE RE:    {data['RE'].std():,.5f}          ===============")
print("               ============================================================================")

# Visualización Histograma, Densidad y Boxplot de RE
f, axes = plt.subplots(2,2, figsize =(11.7,8.27))

sns.histplot(data["RE"],     ax = axes [0,0], kde = True, bins = 20, color="Blue", fill=True)

sns.kdeplot(data["RE"],      ax = axes [0,1], shade = True, color = "Blue", fill = True,
                             bw_adjust=.5, clip_on=False, alpha=1, linewidth=1.5)

sns.boxplot(x = data["RE"],  ax = axes [1,0], orient = "h", color = "lightgreen", saturation = 1,
                             width = 0.7, dodge = True, fliersize = 3, linewidth = 2)
plt.tight_layout()
plt.show()

# Estudio Visualización "AIRE"
# Métricas AIRE
print("               =============================================================================")
print(f"               ===============          MEDIA DE AIRE:      {data['AIRE'].mean():,.5f}          ===============")
print(f"               ===============          MEDIANA DE AIRE:    {data['AIRE'].median():,.5f}          ===============")
print(f"               ===============          SESGO DE AIRE:      {data['AIRE'].skew():,.5f}          ===============")
print(f"               ===============          VARIANZA DE AIRE:   {data['AIRE'].std():,.5f}          ===============")
print("               =============================================================================")

# Visualización Histograma, Densidad y Boxplot de AIRE
f, axes = plt.subplots(2,2, figsize =(11.7,8.27))

sns.histplot(data["AIRE"],     ax = axes [0,0], kde = True, bins = 20, color="Blue", fill=True)

sns.kdeplot(data["AIRE"],      ax = axes [0,1], shade = True, color = "Blue", fill = True,
                               bw_adjust=.5, clip_on=False, alpha=1, linewidth=1.5)

sns.boxplot(x = data["AIRE"],  ax = axes [1,0], orient = "h", color = "lightgreen", saturation = 1,
                               width = 0.7, dodge = True, fliersize = 3, linewidth = 2)
plt.tight_layout()
plt.show()

# Estudio Visualización "PENDIENTE"
# Métricas PENDIENTE
print("               ===================================================================================")
print(f"               ===============          MEDIA DE PENDIENTE:       {data['PENDIENTE'].mean():,.5f}          ===============")
print(f"               ===============          MEDIANA DE PENDIENTE:     {data['PENDIENTE'].median():,.5f}          ===============")
print(f"               ===============          SESGO DE PENDIENTE:       {data['PENDIENTE'].skew():,.5f}          ===============")
print(f"               ===============          VARIANZA DE PENDIENTE:    {data['PENDIENTE'].std():,.5f}          ===============")
print("               ===================================================================================")

# Visualización Histograma, Densidad y Boxplot de PENDIENTE
f, axes = plt.subplots(2,2, figsize =(11.7,8.27))

sns.histplot(data["PENDIENTE"],     ax = axes [0,0], kde = True, bins = 20, color="Blue", fill=True)

sns.kdeplot(data["PENDIENTE"],      ax = axes [0,1], shade = True, color = "Blue", fill = True,
                                        bw_adjust=.5, clip_on=False, alpha=1, linewidth=1.5)

sns.boxplot(x = data["PENDIENTE"],   ax = axes [1,0], orient = "h", color = "lightgreen", saturation = 1,
                                        width = 0.7, dodge = True, fliersize = 3, linewidth = 2)
plt.tight_layout()
plt.show()

# Estudio Visualización "ALTITUD"
# Métricas ALTITUD
print("               ================================================================================")
print(f"               ===============          MEDIA DE ALTITUD:     {data['ALTITUD'].mean():,.5f}          ===============")
print(f"               ===============          MEDIANA DE ALTITUD:   {data['ALTITUD'].median():,.5f}          ===============")
print(f"               ===============          SESGO DE ALTITUD:      {data['ALTITUD'].skew():,.5f}          ===============")
print(f"               ===============          VARIANZA DE ALTITUD:  {data['ALTITUD'].std():,.5f}          ===============")
print("               ================================================================================")

# Visualización Histograma, Densidad y Boxplot de ALTITUD
f, axes = plt.subplots(2,2, figsize =(11.7,8.27))

sns.histplot(data["ALTITUD"],     ax = axes [0,0], kde = True, bins = 20, color="Blue", fill=True)

sns.kdeplot(data["ALTITUD"],      ax = axes [0,1], shade = True, color = "Blue", fill = True,
                                        bw_adjust=.5, clip_on=False, alpha=1, linewidth=1.5)

sns.boxplot(x = data["ALTITUD"],   ax = axes [1,0], orient = "h", color = "lightgreen", saturation = 1,
                                        width = 0.7, dodge = True, fliersize = 3, linewidth = 2)
plt.tight_layout()
plt.show()

# Estudio Visualización "DESNIVEL"
# Métricas DESNIVEL
print("               =================================================================================")
print(f"               ===============          MEDIA DE DESNIVEL:      {data['DESNIVEL'].mean():,.5f}          ===============")
print(f"               ===============          MEDIANA DE DESNIVEL:    {data['DESNIVEL'].median():,.5f}          ===============")
print(f"               ===============          SESGO DE DESNIVEL:      {data['DESNIVEL'].skew():,.5f}          ===============")
print(f"               ===============          VARIANZA DE DESNIVEL:   {data['DESNIVEL'].std():,.5f}          ===============")
print("               =================================================================================")

# Visualización Histograma, Densidad y Boxplot de DESNIVEL
f, axes = plt.subplots(2,2, figsize =(11.7,8.27))

sns.histplot(data["DESNIVEL"],     ax = axes [0,0], kde = True, bins = 20, color="Blue", fill=True)

sns.kdeplot(data["DESNIVEL"],      ax = axes [0,1], shade = True, color = "Blue", fill = True,
                                        bw_adjust=.5, clip_on=False, alpha=1, linewidth=1.5)

sns.boxplot(x = data["DESNIVEL"],   ax = axes [1,0], orient = "h", color = "lightgreen", saturation = 1,
                                        width = 0.7, dodge = True, fliersize = 3, linewidth = 2)
plt.tight_layout()
plt.show()

# Estudio Visualización "RSS"
# Métricas RSS
print("               ============================================================================")
print(f"               ===============          MEDIA DE RSS:     {data['RSS'].mean():,.5f}          ===============")
print(f"               ===============          MEDIANA DE RSS:    {data['RSS'].median():,.5f}          ===============")
print(f"               ===============          SESGO DE RSS:      {data['RSS'].skew():,.5f}          ===============")
print(f"               ===============          VARIANZA DE RSS:  {data['RSS'].std():,.5f}          ===============")
print("               ============================================================================")

# Visualización Histograma, Densidad y Boxplot de RSS
f, axes = plt.subplots(2,2, figsize =(11.7,8.27))

sns.histplot(data["RSS"],     ax = axes [0,0], kde = True, bins = 20, color="Blue", fill=True)

sns.kdeplot(data["RSS"],      ax = axes [0,1], shade = True, color = "Blue", fill = True,
                                        bw_adjust=.5, clip_on=False, alpha=1, linewidth=1.5)

sns.boxplot(x = data["RSS"],   ax = axes [1,0], orient = "h", color = "lightgreen", saturation = 1,
                                        width = 0.7, dodge = True, fliersize = 3, linewidth = 2)
plt.tight_layout()
plt.show()

# Estudio Visualización "DURACION"
# Métricas DURACION
print("               ==================================================================================")
print(f"               ===============          MEDIA DE DURACION:     {data['DURACION'].mean():,.5f}          ===============")
print(f"               ===============          MEDIANA DE DURACION:   {data['DURACION'].median():,.5f}          ===============")
print(f"               ===============          SESGO DE DURACION:       {data['DURACION'].skew():,.5f}          ===============")
print(f"               ===============          VARIANZA DE DURACION:  {data['DURACION'].std():,.5f}          ===============")
print("               ==================================================================================")

# Visualización Histograma, Densidad y Boxplot de DURACION
f, axes = plt.subplots(2,2, figsize =(11.7,8.27))

sns.histplot(data["DURACION"],     ax = axes [0,0], kde = True, bins = 20, color="Blue", fill=True)

sns.kdeplot(data["DURACION"],      ax = axes [0,1], shade = True, color = "Blue", fill = True,
                                        bw_adjust=.5, clip_on=False, alpha=1, linewidth=1.5)

sns.boxplot(x = data["DURACION"],   ax = axes [1,0], orient = "h", color = "lightgreen", saturation = 1,
                                        width = 0.7, dodge = True, fliersize = 3, linewidth = 2)
plt.tight_layout()
plt.show()

# Visualización Multivariable
# **********************************************************************************
# *********        CORRELACIÓN ENTRE LAS DIFERENTES CARACTERÍSTICAS        *********
# **********************************************************************************
# COEFICIENTE DE PEARSON
print("=======================================================================================================================")
print("=======================================         COEFICIENTES DE PEARSON         =======================================")
print("=======================================================================================================================")
pearson     = data.corr(method="pearson")
#   Graficamos la matriz de correlación (Pearson)
plt.figure(figsize=(14,14))
sns.heatmap(pearson, vmax =1, annot=True, cmap='viridis')
plt.title("COEFICIENTES DE PEARSON")
plt.tight_layout()
plt.show()

# **********************************************************************************
# *********        CORRELACIÓN ENTRE LAS DIFERENTES CARACTERÍSTICAS        *********
# **********************************************************************************
# COEFICIENTE DE SPEARMAN
print("=======================================================================================================================")
print("=======================================         COEFICIENTES DE SPEARMAN        =======================================")
print("=======================================================================================================================")
pearson     = data.corr(method="spearman")
#   Graficamos la matriz de correlación (Spearman)
plt.figure(figsize=(14,14))
sns.heatmap(pearson, vmax =1, annot=True, cmap='viridis')
plt.title("COEFICIENTES DE SPEARMAN")
plt.tight_layout()
plt.show()



# **************************************************************************
# *********       GRÁFICOS DE MATRIZ DE CORRELACIÓN POR GRUPOS     *********
# **************************************************************************
# FUNCIÓN PARA OPTIMIZAR CÓDIGO
def matrizcorrelacion(data_grupo):

    g = sns.PairGrid(data_grupo,      palette = None, hue_kws = None,
                      vars = None,    corner = True,  diag_sharey = True,
                      height = 4,     aspect = 1,     layout_pad = 0.5,
                      despine = True, dropna = False, size = None)

    g.map_diag(sns.histplot, color="red")

    g.map_offdiag(sns.scatterplot, color="blue")

    g.add_legend()

    plt.tight_layout()
    plt.show()

# CREACIÓN DE DIFERENTES GRUPOS PARA EVITAR SATURACIÓN
df_grupo1 = data[["POR_CP","DISTANCIA","DURACION"]]
df_grupo2 = data[["RITMO","FREC_CARDIACA","DURACION"]]
df_grupo3 = data[["CADENCIA","TSC","DURACION"]]
df_grupo4 = data[["FP","LSS","DURACION"]]
df_grupo5 = data[["OSC_VERTICAL","L_ZANCADA","DURACION"]]
df_grupo6 = data[["RFP","RLSS","DURACION"]]
df_grupo7 = data[["ROV","RE","DURACION"]]
df_grupo8 = data[["AIRE","PENDIENTE","DURACION"]]
df_grupo9 = data[["ALTITUD","DESNIVEL","DURACION"]]
df_grupo10 = data[["RSS","DURACION"]]

# REPRESENTACIÓN GRÁFICA POR GRUPOS
# **************************************************************************
# *********        GRÁFICOS DE MATRIZ DE CORRELACIÓN GRUPO 1       *********
# **************************************************************************
matrizcorrelacion(df_grupo1)
# **************************************************************************
# *********        GRÁFICOS DE MATRIZ DE CORRELACIÓN GRUPO 2       *********
# **************************************************************************
matrizcorrelacion(df_grupo2)
# **************************************************************************
# *********        GRÁFICOS DE MATRIZ DE CORRELACIÓN GRUPO 3       *********
# **************************************************************************
matrizcorrelacion(df_grupo3)
# **************************************************************************
# *********        GRÁFICOS DE MATRIZ DE CORRELACIÓN GRUPO 4       *********
# **************************************************************************
matrizcorrelacion(df_grupo4)
# **************************************************************************
# *********        GRÁFICOS DE MATRIZ DE CORRELACIÓN GRUPO 5       *********
# **************************************************************************
matrizcorrelacion(df_grupo5)
# **************************************************************************
# *********        GRÁFICOS DE MATRIZ DE CORRELACIÓN GRUPO 6       *********
# **************************************************************************
matrizcorrelacion(df_grupo6)
# **************************************************************************
# *********        GRÁFICOS DE MATRIZ DE CORRELACIÓN GRUPO 7       *********
# **************************************************************************
matrizcorrelacion(df_grupo7)
# **************************************************************************
# *********        GRÁFICOS DE MATRIZ DE CORRELACIÓN GRUPO 8       *********
# **************************************************************************
matrizcorrelacion(df_grupo8)
# **************************************************************************
# *********        GRÁFICOS DE MATRIZ DE CORRELACIÓN GRUPO 9       *********
# **************************************************************************
matrizcorrelacion(df_grupo9)
# **************************************************************************
# *********        GRÁFICOS DE MATRIZ DE CORRELACIÓN GRUPO 10     *********
# **************************************************************************
matrizcorrelacion(df_grupo10)



