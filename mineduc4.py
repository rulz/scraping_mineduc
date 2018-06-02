# encoding: utf-8
import urllib
from lxml import html
import re
import unicodedata
from django.template.defaultfilters import slugify
#from regiones import REGIONES, COMUNAS

RBD=[22517,22388,6787,22188,22496,6835,22398,6836,6828,22014,6770,22231,22459,22629,6779,6832,6830,22177,6826,6766,6843,12185,22627,22415,6844,31012,6751,22516,22351,22540,22634,6829,22374,6754,31010,6755,6757,6756,6753,22633,6752,22160,22759,22462,6925,6916,6899,6922,6897,7015,7031,7044,22097,6929,22313,22317,22024,7200,22218,22476,6895,6886,31002,6853,6846,6896,22549,7049,22514,7085,40102,22483,7102,16843,16844,7004,6983,11591,7006,22758,7299,22445,31005,22503,7180,22559,7128,7181,7135,22354,22158,22062,22140,22752,7129,31011,22446,22495,7276,11554,7240,22755,7236]
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

    f = open('14region_colegios.csv', 'a')
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
