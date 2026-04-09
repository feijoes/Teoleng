# -*- coding: utf-8 -*-
import re
import sys
from programa4 import programa4
from programa5 import programa5
from programa2 import programa2

def programa6(RutaPdf,RutaXML):
    text = ""
    '''
    SU CÓDIGO
    '''
    xml = programa4(RutaXML)

    if not programa5(RutaPdf,RutaXML):
        return xml
    fecha, monto = programa2(RutaPdf)

    #Nos interesa encontrar algo del tipo: Movimiento ... Importe ... Fecha ...
    movimientos = re.findall(r'<[^>]*Movimiento[^>]*/>', xml)

    #mov es el movimiento que buscamos
    mov = re.search(r'<[^>]*Movimiento[^>]*Importe\s*=\s*"' + monto + r'"\s*Fecha\s*=\s*"' + fecha + r'"[^>]*/>', xml)


    xml = xml.replace(mov.group(0), '')
    


    return xml
if __name__ == '__main__':
    entrada_pdf = sys.argv[1]  # archivo entrada (param)
    entrada_xml = sys.argv[2]  # archivo entrada (param)
    salida = sys.argv[3]   # archivo salida (param)    
 
    ret = programa6(entrada_pdf,entrada_xml)      # ejecutar 
    
    f = open(salida, 'w')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
