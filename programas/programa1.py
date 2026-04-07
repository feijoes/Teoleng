# -*- coding: utf-8 -*-
import re
import sys
from pypdf import PdfReader

def programa1(RutaPdf):
    reader = PdfReader(RutaPdf)
    number_of_pages = len(reader.pages)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)
    
    ret = programa1(entrada)      # ejecutar 
    
    f = open(salida, 'w', encoding='cp1252', newline='')  # como salidas_esperadas (Windows-1252)
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
