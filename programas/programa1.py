# -*- coding: utf-8 -*-
import re
import sys
from pypdf import PdfReader

def programa1(RutaPdf):
    reader = PdfReader(RutaPdf)
    number_of_pages = len(reader.pages)  ###TODO: no se usa
    text = ""
    for page in reader.pages:
        text += page.extract_text()  ###TODO: que pasa si el texto es None, se rompe?
    return text


if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)
    
    ret = programa1(entrada)      # ejecutar 
    
    f = open(salida, 'w', encoding='utf-8') # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
