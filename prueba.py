import matplotlib.pyplot as plt
from adquirir_datos import *
from mapear import *

def graficar(map, data_conteo):

    #Unir mapa y datos
    map = pd.concat([map, data_conteo], axis=1,sort=False)
    fig, ax = plt.subplots(1, 1)
    map.plot(column="Conteo",ax=ax, cmap='OrRd', legend=True, edgecolor='black',linewidth=0.3)
    plt.xticks([])
    plt.yticks([])
    plt.show()

mapa = Mapeo("map/depto.shp").ordenado
d_2018 = Obtener_Datos("data/hurto-personas-2018_0.xlsx").ordenado
graficar(mapa,d_2018)
