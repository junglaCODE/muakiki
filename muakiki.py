import re
import wget
def __searchingAndDowloadOfUrls__(file):
    files = open(file)
    for linea in files.readlines():
        if(linea.find('src') > 0):
            patron__ = re.compile(r'\burl\(')
            __patron = re.compile(r'\b\)')
            __urls__ = patron__.split(linea)  
            __fonts__ = __patron.split(__urls__[1])
            wget.download(__fonts__[0])

__searchingAndDowloadOfUrls__('example.css')
