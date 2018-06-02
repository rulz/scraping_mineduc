# encoding: utf-8
import urllib
from lxml import html
import re
from regiones import REGIONES, COMUNAS

from django.template.defaultfilters import slugify

#urllib3
#lxml
ARRAY_BASE = []
ARRAY = []
COUNT = 0

for r in REGIONES:
    #print REGIONES[r] #nombre
    for c in COMUNAS[r]:
        #print COMUNAS[r][c]
        path = 'dep=0&npar=0&nbas=0&nmed=1&sep=0&tens=0&esp=0&sec=0&espec=0&rbd1=&region={0}&comuna={1}&dependencia=0&idMedia=1&tipoEns=0&sectorEco=0&especialidad=0&nEspecial=0'.format(r,c)
        URL_BASE= 'http://www.mime.mineduc.cl/mime-web/mvc/mime/busqueda_avanzada?'+path

        print URL_BASE
        page = html.fromstring(urllib.urlopen(URL_BASE).read())
        for td in page.xpath('//table[@id="busqueda_avanzada"]//td/text()'):
            if td.strip():
                COUNT += 1
                ARRAY.append(td.strip())
                if COUNT >= 4:
                    for i, t in enumerate(ARRAY):
                        f = open(str(r)+'-region.txt', 'a')
                        f.write(slugify(t))
                        if i < 3:
                            f.write(';')
                        if i >= 3:
                            f.write(';')
                            f.write(REGIONES[r])
                            f.write(';')
                            f.write(COMUNAS[r][c])
                            f.write('\n')
                    COUNT = 0
                    ARRAY = []
                    i=0
