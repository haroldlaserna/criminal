import geopandas as gpd
from organizar import *

class Mapeo:

    def __init__(self, name_map):

        """
        self.name_map = "nombre del mapa"
        self.read = "mapa leido"
        self.ordenado = "mapa organizado por Departamento alfabeticamente"
        """
        self.name_map = name_map
        self.read = gpd.read_file(self.name_map)
        self.read = self.read.replace({self.read["NOMBRE_DPT"][32]:'SAN ANDRES',
                                   self.read["NOMBRE_DPT"][2]:'BOGOTA'})
        self.ordenado = ordenar(self.read,"NOMBRE_DPT")
