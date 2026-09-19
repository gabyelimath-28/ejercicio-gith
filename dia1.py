import sys
import pandas as pd
import numpy as np

nombre = "Gaby Moscoso"  # Escribe aquí tu nombre
profesion = "Ing. Estadistica" # Escribe aquí tu profesión u ocupación
print(f"Hola, soy {nombre}, {profesion}.")
print("Python", sys.version.split()[0])
print("pandas", pd.__version__, "| numpy", np.__version__)