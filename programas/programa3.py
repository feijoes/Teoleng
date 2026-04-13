# -*- coding: utf-8 -*-
import re
import sys
from programa1 import programa1

def programa3(RutaFactura):
    
    '''
    SU CÓDIGO
    
    
    '''
    
    #res=f"Cant: 10 |Desc: PRUEBA | 10,10 c/u |Total: 101\n"
    texto = programa1(RutaFactura)
    res = ""
    #bloque = re.search(r'CANT\..+?SUBTOTAL', texto, re.DOTALL).group()

    info = re.findall(r'(?:^|\n)\s*(\d+)\s+(.+?)\s+(\d+,\d{2})\s+(\d+,\d{2})', texto)

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
