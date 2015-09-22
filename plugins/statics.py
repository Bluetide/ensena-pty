#!/usr/bin/env python
# -*- coding: utf-8 -*-

PAGE_LINKS = [
    {'url':'index.html', 'title':'Inicio'},
    {'url':'about.html', 'title':'Nosotros'},
    {'url':'challenge.html', 'title':'El Desafío'},
    {'url':'leadership.html', 'title':'Programa de Liderazgo'},
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
        'title':'¡APLICACIONES ABIERTAS para la primera cohorte de Profesionales de Enseña por Panamá!. ¡APLICA YA!'
    },{
        'image':'assets/images/slider/Drobis_01.JPG',
        'title':'Puedes hacerlo realidad',
        'subtitle':'<p>¡Aplica al <b>programa de liderazgo!</b> Tú eres parte del cambio y puedes ayudar a lograr una educación de calidad a todos los niños y jovenes en Panamá</p>'
    },{
        'image':'assets/images/slider/Drobis_02.JPG',
        'title':'¡Sé parte de un movimiento internacional!',
        'subtitle':'<a href="http://teachforall.org/en/our-network-and-impact/network-partners" target="_blank"><p>Red TEACH FOR ALL</p></a>'
    },{
        'image':'assets/images/slider/Drobis_03.JPG',
        'title':'Un día todos los niños, las niñas y jóvenes de Panamá tendrán la oportunidad de recibir una educación de excelencia'
    },{
        'image':'assets/images/slider/Drobis_04.JPG',
        'title':'Puedes hacerlo realidad',
        'subtitle':'<p>¡Aplica al <b>programa de liderazgo!</b> Tú eres parte del cambio y puedes ayudar a lograr una educación de calidad a todos los niños y jovenes en Panamá</p>'
    },{
        'image':'assets/images/slider/Drobis_05.JPG',
        'title':'¿Sabías que el 80% de los estudiantes de tercer grado no saben leer? Unete y se parte del cambio!'
    }
]

HEADER_BACKGROUND = "assets/images/header-bg.jpg"

CONTACT_EMAIL = "info@ensenaporpanama.com"
CONTACT_PHONE = "+507 322 0437"
CONTACT_ADDRESS = "Edif. 909, Calle 74 con Calle 50, San Francisco"

def preBuildPage(site, page, context, data):
    context['header_background'] = HEADER_BACKGROUND
    context['header_links'] = PAGE_LINKS
    context['footer_links'] = [
        PAGE_LINKS[:len(PAGE_LINKS)/2],
        PAGE_LINKS[len(PAGE_LINKS)/2:],
    ]
    context['slider_image_list'] = SLIDER_IMAGE_LIST
    context['social_links'] = SOCIAL_LINKS
    context['contact_email'] = CONTACT_EMAIL
    context['contact_phone'] = CONTACT_PHONE
    context['contact_address'] = CONTACT_ADDRESS
    context['contact_email_link'] = "mailto:" + CONTACT_EMAIL
    context['contact_phone_link'] = "tel:" + CONTACT_PHONE.replace(" ", "")
    return context, data
