import pandas as pd
import unidecode as un

#Ordenar datos alfabeticamente
def ordenar(x,word):

    x = x.sort_values(word)
    x.reset_index(drop=True, inplace=True)
    return x

#Quitar tilde de datos
def quitar_tilde(x,columna):

    for i in range(len(x)):
        x[columna][i] = un.unidecode(x[columna][i])
    return x
