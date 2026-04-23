# -*- coding: utf-8 -*-
import re
import sys

from programa4 import programa4
from programa2 import programa2
from programa1 import programa1

#Dada una factura y el estado bancario, este programa devuelve True si hay un movimiento coincidente (misma fecha e importe que la factura), o False en otro caso.
#Sugerencia: Usar el programa2 para obtener la fecha y el “débito bancario” que se deberá buscar en el XML.
def programa5(RutaPdf,RutaXML):
    
    texto_xml = programa4(RutaXML)
    fecha, monto = programa2(RutaPdf)
    
    #rf: Sirve para interpolar variables dentro del texto

    regex = rf"<BanTeng:Movimiento .*?Importe=\"{monto}\" Fecha=\"{fecha}" #.*?: ignora todo lo que hay entre medio de "Movimiento" e "Importe"
    resultado = re.search(regex, texto_xml)
    if resultado:
        return(True)
    else:
        return(False)

if __name__ == '__main__':
    entrada_pdf = sys.argv[1]  # archivo entrada (param)
    entrada_xml = sys.argv[2]  # archivo entrada (param)
    salida = sys.argv[3]   # archivo salida (param)    
 
    ret = programa5(entrada_pdf,entrada_xml)      # ejecutar 
    if (ret):
        ret = "Encontrado"
    else:
        ret = "No encontrado"
    
    f = open(salida, 'w', encoding='utf-8') # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
