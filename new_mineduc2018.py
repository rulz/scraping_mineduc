# encoding: utf-8
from lxml import html
import requests

from RBD import CODE


for code in CODE:
    url = 'http://www.mime.mineduc.cl/mime-web/mvc/mime/ficha?rbd='+str(code)
    response = requests.get(url)
    page = html.fromstring(response.content)

    try:
        nombre_colegio = str(page.xpath('//table//td/text()')[2].encode('utf-8').decode('utf-8').strip())
    except Exception as e:
        nombre_colegio = ''


    descrip = page.find_class('letra_capital')

    try:
        direccion = str(descrip[0].text.encode('utf-8').decode('utf-8').strip())
    except Exception as e:
        direccion = ''

    try:
        telefono = str(descrip[3].text.encode('utf-8').decode('utf-8').strip())
    except Exception as e:
        telefono = ''

    try:
        director = str(descrip[4].text.encode('utf-8').decode('utf-8').strip())
    except Exception as e:
        director = ''






    link_2 = page.xpath("//a")

    try:
        email = str(link_2[2].text.encode('utf-8').decode('utf-8').strip())
    except Exception as e:
        email = ''

    try:
        web = str(link_2[3].text.encode('utf-8').decode('utf-8').strip())
    except Exception as e:
        web = ''




    info_inst = page.find_class('form_detalle')
    dep = ''
    array = []
    ba = True
    for i in range(0, len(info_inst)):
        if i == 0:
            rbd = str(info_inst[i].text.encode('utf-8').decode('utf-8').strip())
        if i == 1:
            r_ofic = str(info_inst[i].text.encode('utf-8').decode('utf-8').strip())
        if i >= 2:
            try:
                if int(info_inst[i].text.encode('utf-8').decode('utf-8').strip()):
                    array.append(info_inst[i].text.encode('utf-8').decode('utf-8').strip())
                    ba = False
            except Exception as e:
                if ba:
                    dep = dep+str(info_inst[i].text.encode('utf-8').decode('utf-8').strip())+' | '
                else:
                    array.append(info_inst[i].text.encode('utf-8').decode('utf-8').strip())


    nombre = ''
    c_email = ''
    t_movil = ''
    t_t = ''

    for i in range(0,len(page.xpath('//div//table//td/text()'))):
        try:
            if page.xpath('//div//table//td/text()')[i].strip():
                if len(page.xpath('//div//table//td/text()')[i].split('Nombre:')) == 2:
                    nombre = page.xpath('//div//table//td/text()')[i].split('Nombre:')[1]
                    array.append(page.xpath('//div//table//td/text()')[i].split('Nombre:')[1])

                if len(page.xpath('//div//table//td/text()')[i].split('Correo electrónico:')) == 2:
                    c_email = page.xpath('//div//table//td/text()')[i].split('Correo electrónico:')[1]
                    array.append(page.xpath('//div//table//td/text()')[i].split('Correo electrónico:')[1])

                if len(page.xpath('//div//table//td/text()')[i].split('Teléfono móvil:')) == 2:
                    t_movil = page.xpath('//div//table//td/text()')[i].split('Teléfono móvil:')[1]
                    array.append(page.xpath('//div//table//td/text()')[i].split('Teléfono móvil:')[1])

                if len(page.xpath('//div//table//td/text()')[i].split('Teléfono:')) == 2:
                    t_t = page.xpath('//div//table//td/text()')[i].split('Teléfono:')[1]
                    array.append(page.xpath('//div//table//td/text()')[i].split('Teléfono:')[1])
        except Exception as e:
            raise

    print (array)
    f = open('info_colegios.csv', 'a')
    f.write('"{0}"'.format(str(code)))
    f.write(',')
    f.write('"{0}"'.format(nombre_colegio))
    f.write(',')
    f.write('"{0}"'.format(direccion))
    f.write(',')
    f.write('"{0}"'.format(telefono))
    f.write(',')
    f.write('"{0}"'.format(director))
    f.write(',')
    f.write('"{0}"'.format(email))
    f.write(',')
    f.write('"{0}"'.format(web))
    f.write(',')
    f.write('"{0}"'.format(rbd))
    f.write(',')
    f.write('"{0}"'.format(r_ofic))
    f.write(',')
    f.write('"{0}"'.format(dep))
    f.write(',')
    if len(array):
        f.write('"{0}"'.format(str(array[0])))
        f.write(',')
        f.write('"{0}"'.format(str(array[1])))
        f.write(',')
        f.write('"{0}"'.format(str(array[2])))
        f.write(',')
        f.write('"{0}"'.format(str(array[3])))
        f.write(',')
        f.write('"{0}"'.format(str(array[4])))##sep

        for a in range(4, len(array)):
            if array[a].strip() != '':
                if array[a].strip() !='-':
                    f.write(',')
                    f.write('"{0}"'.format(str(array[a])))
    f.write('\n')
    f.close()

f = open('info_colegios.csv', 'a')
f.write('\n final \n')
f.close()
