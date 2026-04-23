# -*- coding: utf-8 -*-
import re
import sys
from programa1 import programa1
from datetime import datetime
#Dada una factura, despliega la fecha y el “débito bancario” con el siguiente formato: Fecha: 2026-03-16 | Monto: 954,25
def programa2(RutaFactura):
    
    '''
    SU CÓDIGO
    
    NOTA: El formato de la fecha debe ser AAAA-MM-DD 
    '''
    texto = programa1(RutaFactura)
    
    #r: Le dice a Python: “no interpretes las barras invertidas \ como escapes normales, sino como un caracter mas

    fecha_string = re.search(r"FECHA:\s*\n*(\d{2}[-/]\d{2}[-/]\d{4})", texto).group(1) # Busca la palabra FECHA y a continuacion dd-dd-dddd, \s*: es para los espacios,\n*: es para los saltos de linea, \d: solo digitos, .group(1): devuelve el primer elemento del patron, osea el primer parentesis.
    fecha = datetime.strptime(fecha_string.replace("/", "-"), "%d-%m-%Y").strftime("%Y-%m-%d")#strptime: string-> date, strftime: cambia el formato    
    monto = re.search(r"\n*\s*BANCARIO\s*(\d+,\d+)",texto).group(1) # Busca la palabra BANCARIO y se queda con el monto, *: 0 o mas ocurrencias, +: 1 o mas ocurrencias
    return fecha, monto

if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)
    
    fecha,monto = programa2(entrada)      # ejecutar 
    ret =f"Fecha: {fecha} | Monto: {monto}"
    f = open(salida, 'w', encoding='utf-8') # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
