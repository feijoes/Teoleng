# -*- coding: utf-8 -*-
import re
import sys
from programa4 import programa4
from programa5 import programa5
from programa2 import programa2

#Dada una factura y el estado bancario xml, el programa elimina la línea coincidente. En caso de que no exista coincidencia, no se realiza ninguna modificación.


def programa6(RutaPdf,RutaXML):
    xml = programa4(RutaXML)

    if not programa5(RutaPdf, RutaXML):
        return xml

    fecha, monto = programa2(RutaPdf)

    patron_mov = (
    rf'\n?[ \t]*<[^>]*Movimiento[^>]*Importe\s*=\s*"{re.escape(monto)}"\s*'
    rf'Fecha\s*=\s*"{re.escape(fecha)}"[^>]*/>[ \t]*'
    )

    #\n? → puede haber un salto de línea antes del tag, [ \t]* → puede haber espacios o tabs antes del tag, [ \t]* → espacios o tabs después del tag
    # Se usa re.escape para que monto y fecha no alteren la regex.

    xml = re.sub(patron_mov, '', xml, count=1) 
    #re.sub: Retorna la string resultado de reemplazar las ocurrencias del patrón por repl– Si 
    #count es distinto de 0, reemplaza un máximo de count ocurrencias Busca una ocurrencia del patrón en la string
    #Retorna el match, o None si el patrón no ocurre en la string

    total_match = re.search(
        r'<BanTeng:TotalMovimientos>(\d+)</BanTeng:TotalMovimientos>',
        xml
    )
    total_actual = int(total_match.group(1))
    nuevo_total = total_actual - 1

    xml = re.sub(
        r'<BanTeng:TotalMovimientos>\d+</BanTeng:TotalMovimientos>',
        f'<BanTeng:TotalMovimientos>{nuevo_total}</BanTeng:TotalMovimientos>',
        xml,
        count=1
    )

    return xml

if __name__ == '__main__':
    entrada_pdf = sys.argv[1]  # archivo entrada (param)
    entrada_xml = sys.argv[2]  # archivo entrada (param)
    salida = sys.argv[3]   # archivo salida (param)    
 
    ret = programa6(entrada_pdf,entrada_xml)      # ejecutar 
    
    f = open(salida, 'w', encoding='utf-8') # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
