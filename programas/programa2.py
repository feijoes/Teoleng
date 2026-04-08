# -*- coding: utf-8 -*-
import re
import sys
from programa1 import programa1
from datetime import datetime
def programa2(RutaFactura):
    
    '''
    SU CÓDIGO
    
    NOTA: El formato de la fecha debe ser AAAA-MM-DD 
    '''
    texto = programa1(RutaFactura)
    
    fecha_string = re.search(r"FECHA:\s*\n*(\d{2}[-/]\d{2}[-/]\d{4})", texto).group(1)
    fecha = datetime.strptime(fecha_string.replace("/", "-"), "%d-%m-%Y").strftime("%Y-%m-%d")    
    monto = re.search(r"\n*\s*BANCARIO\s*(\d*,\d*)",texto).group(1)
    return fecha, monto
  

if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)
    
    fecha,monto = programa2(entrada)      # ejecutar 
    ret =f"Fecha: {fecha} | Monto: {monto}"
    f = open(salida, 'w')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida