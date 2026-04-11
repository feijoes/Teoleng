# -*- coding: utf-8 -*-
import re
import sys
from programa4 import programa4
from programa5 import programa5
from programa2 import programa2

def programa6(RutaPdf,RutaXML):
    xml = programa4(RutaXML)

    if not programa5(RutaPdf, RutaXML):
        return xml

    fecha, monto = programa2(RutaPdf)

    patron_mov = (
        r'\n?[ \t]*<[^>]*Movimiento[^>]*Importe\s*=\s*"'
        + re.escape(monto)
        + r'"\s*Fecha\s*=\s*"'
        + re.escape(fecha)
        + r'"[^>]*/>[ \t]*'
    )

    xml = re.sub(patron_mov, '', xml, count=1)

    total_match = re.search(
        r'<BanTeng:TotalMovimientos>(\d+)</BanTeng:TotalMovimientos>',
        xml
    )
    total_actual = int(total_match.group(1))
    nuevo_total = total_actual - 1   ###TODO: revisar esto si resta bien, porque puede pasar que entre, no borra pero si resta

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
    
    f = open(salida, 'w')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
