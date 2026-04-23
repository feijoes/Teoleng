# -*- coding: utf-8 -*-
import re
import sys
from programa1 import programa1

#Despliega todas las cantidades, la descripción, precio por unidad y precio total de los ítems facturados con el siguiente formato:
#Cant: 1 |Desc: Item1 | 200,11 c/u |Total: 200,11
#Cant: 1 |Desc: Item 2 | 0,70 c/u |Total: 0,70

def programa3(RutaFactura):
    
    '''
    SU CÓDIGO
    
    
    '''
    texto = programa1(RutaFactura)
    res = ""

    info = re.findall(r'(?:^|\n)\s*(\d+)\s+(.+?)\s+(\d+,\d{2})\s+(\d+,\d{2})', texto)
    # (?:^|\n)         -> inicio del texto o inicio de una nueva línea
    # (.+?)            -> descripción, en forma no codiciosa, se queda con lo minimo necesario

    # re.findall devuelve una lista de tuplas: [(cant, desc, precio, total), (...), ...]

    res += ''.join(
        f"Cant: {cant} |Desc: {desc} | {precio} c/u |Total:  {total}\n"
        for cant, desc, precio, total in info
    )
    return res

if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)    
 
    ret = programa3(entrada)      # ejecutar 
    
    f = open(salida, 'w', encoding='utf-8') # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
