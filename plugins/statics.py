#!/usr/bin/env python
# -*- coding: utf-8 -*-

PAGE_LINKS = [
    {'url':'index.html', 'title':'Inicio'},
    {'url':'team.html', 'title':'Nuestro Equipo'},
    {'url':'about.html', 'title':'Nosotros'},
    {'url':'teach.html', 'title':'Teach for All'},
    {'url':'challenge.html', 'title':'El Desafío'},
    {'url':'leadership.html', 'title':'Programa de Liderazgo - ¿A quién buscamos?'},
    {'url':'leadership2.html', 'title':'Programa de Liderazgo - ¿Cómo lo hacemos?'},
    {'url':'leadership3.html', 'title':'Programa de Liderazgo - ¿Quiénes y cómo pueden aplicarse?'},
    {'url':'leadership4.html', 'title':'Programa de Liderazgo - Preparación'},
    {'url':'leadership5.html', 'title':'Programa de Liderazgo - ¿Cómo te beneficias?'},
    {'url':'leadership6.html', 'title':'Programa de Liderazgo - ¿Dónde estamos?'},
    {'url':'alumni.html', 'title':'Alumni'},
    {'url':'allies.html', 'title':'Aliados'},
]

SOCIAL_LINKS = [
    {'icon':'fa-facebook', 'url':'https://www.facebook.com/ensenaxpanama'},
    {'icon':'fa-twitter', 'url':'https://twitter.com/ensenaxpanama'},
    {'icon':'fa-instagram', 'url':'https://instagram.com/ensenaxpanama/'},
]

# Each slider imgae has a url and a title. Subtitle is optional.
SLIDER_IMAGE_LIST = [
    {
        'image':'assets/images/slider/slider_0.jpg',
        'title':'¡APLICACIONES ABIERTAS!',
        'subtitle':'<p>Incríbete para la primera cohorte de Profesionales de Enseña por Panamá.<div style="margin-top: -13px;" class="callout-actions"><a href="/aplica/" class="button red callbox" style="width: 50%;">¡Aplica Ya!</a></div>',
        'type':'2'
    },{
        'image':'assets/images/slider/Drobis_01.JPG',
        'title':'Puedes hacerlo realidad',
        'subtitle':'<p>¡Aplica al <b>programa de liderazgo!</b> Tú eres parte del cambio y puedes ayudar a lograr una educación de calidad a todos los niños y jovenes en Panamá</p>',
        'type':'1'
    },{
        'image':'assets/images/slider/Drobis_02.JPG',
        'title':'Red TEACH FOR ALL',
        'subtitle':'<p>En países de todo el mundo, el lugar donde nacen los niños determina el tipo de educación que recibirán y, finalmente en el largo plazo, sus opciones en la vida.</p>',
        'type':'1'
    },{
        'image':'assets/images/slider/Drobis_03.JPG',
        'title':'El objetivo de Enseña por Panamá',
        'subtitle':'<p>Un día todos los niños, las niñas y jóvenes de Panamá tendrán la oportunidad de recibir una educación de excelencia</p>',
        'type':'1'
    },{
        'image':'assets/images/slider/Drobis_05.JPG',
        'title':'Tú puedes ayudar a cambiarlo',
        'subtitle':'<p>¿Sabías que el 80% de los estudiantes de tercer grado no saben leer? Unete y se parte del cambio!</p>',
        'type':'1'
    }
]

HEADER_BACKGROUND = "assets/images/header-bg.jpg"

CONTACT_EMAIL = "info@ensenaporpanama.com"
CONTACT_PHONE = "+507 6301 1448"
CONTACT_ADDRESS = "Edif. 909, Calle 74 con Calle 50, San Francisco"

def preBuildPage(site, page, context, data):
    context['header_background'] = HEADER_BACKGROUND
    context['header_links'] = PAGE_LINKS
    context['footer_links'] = [
        PAGE_LINKS[:PAGE_LINKS.__len__()],
        PAGE_LINKS[PAGE_LINKS.__len__()/:],
    ]
    context['slider_image_list'] = SLIDER_IMAGE_LIST
    context['social_links'] = SOCIAL_LINKS
    context['contact_email'] = CONTACT_EMAIL
    context['contact_phone'] = CONTACT_PHONE
    context['contact_address'] = CONTACT_ADDRESS
    context['contact_email_link'] = "mailto:" + CONTACT_EMAIL
    context['contact_phone_link'] = "tel:" + CONTACT_PHONE.replace(" ", "")
    return context, data
