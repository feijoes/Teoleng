# -*- coding: utf-8 -*-
import re
import sys
from pypdf import PdfReader

#Recibe la ruta relativa de un archivo PDF como parámetro y devuelve su
#contenido como texto (string).
def programa1(RutaPdf):
    reader = PdfReader(RutaPdf)
    text = ""

    for page in reader.pages:
        # Intenta extraer el texto de la página.
        page_text = page.extract_text()

        # Si page_text es None, se concatena string vacio para evitar errores de tipo.
        if page_text is not None:
            text += page_text

    return text


if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)
    
    ret = programa1(entrada) 
    
    f = open(salida, 'w', encoding='utf-8') # abrir archivo salida
    f.write(ret) # escribir archivo salida
    f.close() # cerrar archivo salida
