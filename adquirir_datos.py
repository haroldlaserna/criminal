import pandas as pd
from organizar import *

class Obtener_Datos:

    def __init__(self,name_data):

        """
        self.name_data = "direccion de la carpeta de los datos"
        self.data = "DataFrame del contenido de los datos"
        self.count = numero de hurtos a personas por Departamentos
        self.count_sintilde = numero de hurtos a personas por Departamentos sin tildes
        self.ordenados = numero de hurtos a personas por Departamentos ordenados alfabeticamente
        """
        columna = 'Departamento'
        self.name_data = name_data
        self.data = pd.read_excel(self.name_data,header=9)
        self.count = pd.value_counts(self.data[columna]).rename_axis(columna).reset_index(name="Conteo")
        self.count_sintilde = quitar_tilde(self.count, columna)


        #contar hurtos en bogota e indexarlos
        for i in range(len(self.count_sintilde)):

            if self.count_sintilde.Departamento[i] == "CUNDINAMARCA":

                change = self.data.Municipio.value_counts()["BOGOTÁ D.C. (CT)"]
                self.count_sintilde.Conteo[i] = self.count_sintilde.Conteo[i] - change
                self.count_sintilde.loc[len(self.count_sintilde)] = ["BOGOTA", change]
                break

        self.ordenado = ordenar(self.count_sintilde, columna)
