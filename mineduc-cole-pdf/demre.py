# encoding: utf-8
import urllib
from lxml import html
import re
import unicodedata
from django.template.defaultfilters import slugify
#from regiones import REGIONES, COMUNAS

RBD=[78,72,67,12713,12502,12712,12720,50,60,12587,10915,25,10906,8,45,30003,12630,12716,12505,59,12539,56,12547,40230,28,5,69,7,12658,32,15,12750,52,12610,4,10911,1,12696,10892]
url_base = 'http://www.mime.mineduc.cl/mime-web/mvc/mime/ficha?rbd='
#page = html.fromstring(urllib.urlopen(url).read())

#print page.find_class('mineduc')[0]
#print page.xpath('//table[@id="busqueda_avanzada"]//td/text()')

for rr in RBD:
    url = url_base+str(rr)
    page = html.fromstring(urllib.urlopen(url).read())
    ARRAY_BASE = []
    ARRAY = []
    COUNT = 0
    print str(rr)
    nombre_colegio = page.xpath('//table//td/text()')[2].encode('utf-8').strip()
    
    link = page.find_class('letra_capital')

    direccion = link[0].text.encode('utf-8').strip()

    # comuna = link[2].text.strip()
    telefono = link[3].text.encode('utf-8').strip()
    director = link[4].text.encode('utf-8').strip()
    #director = u' '.join((link[4].text)).encode('utf-8').strip()

    link_2 = page.xpath("//a")

    email = link_2[2].text.encode('utf-8').strip()
    web = link_2[3].text.encode('utf-8').strip()

    f = open('15region_colegios.csv', 'a')
    f.write(str(rr))
    f.write(',')
    f.write(nombre_colegio)
    f.write(',')
    f.write(direccion)
    f.write(',')
    f.write(telefono)
    f.write(',')
    f.write(director)
    f.write(',')
    f.write(email)
    f.write(',')
    f.write(web)
    f.write('\n')
    f.close()

    
        
    
    
