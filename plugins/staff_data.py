#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.utils.text import slugify

STAFF_DATA = [
    {
        'name': 'Lorena Valencia',
        'photo': 'assets/images/staff/lorena_valencia.jpg' ,
        'tagline': 'Directora Ejecutiva y Co-Fundadora',
    },
    {
        'name': 'David Alexander Bernal Díaz',
        'photo': 'assets/images/staff/david_bernal.jpg',
        'tagline': 'Director de Reclutamiento, Selección y Colocación',
    },
    {
        'name': 'Marisa Arias',
        'photo': 'assets/images/staff/marisa_arias.jpg',
        'tagline': 'Directora',
    },
    {
        'name': 'Jorge Arosemena',
        'photo': 'assets/images/staff/jorge_arosemena.jpg',
        'tagline': 'Director',
    },
    {
        'name': 'Jorge Vallarino',
        'photo': 'assets/images/staff/jorge_vallarino.jpg',
        'tagline': 'Director',
    },
    {
        'name': 'Ana María Vallarino',
        'photo': 'assets/images/staff/ana_maria_vallarino.jpg',
        'tagline': 'Directora',
    },
    {
        'name': 'Marilú Salvador',
        'photo': 'assets/images/staff/marilu_salvador.jpg',
        'tagline': 'Asesora',
    },
    {
        'name': 'Julio Escobar Villarué',
        'photo': 'assets/images/staff/julio_escobar.jpg',
        'tagline': 'Asesor',
    },
    {
        'name': 'Marta Amorós',
        'photo': 'assets/images/staff/marta_amoros.jpg',
        'tagline': 'Directora de Formación y Apoyo',
    },
    {
        'name': 'Estefanía Sánchez',
        'photo': 'assets/images/staff/estefania_sanchez.jpg',
        'tagline': 'Tutora Académica',
    },
    {
        'name': 'Yuri Pittí',
        'photo': 'assets/images/staff/yuri_pitti.jpg',
        'tagline': 'Asistente Técnica',
    },{
        'name': 'Dalys Rodríguez',
        'photo': 'assets/images/staff/dalys_rodriguez.jpg',
        'tagline': 'Directora de Desarrollo'
    }
]

# Adds extra attributes programatically to the staff items.
def parse_staff_data(item):

    #Adds a link-able ID to the object, used for anchors
    item['link'] = slugify(item['name'])

    # Return the item
    return item

# Executed before the page is built
def preBuildPage(site, page, context, data):

    # Iterates through the entire STAFF_DATA list, and executes the 'parse_staff_data' function
    parsed_data = [ parse_staff_data(data_item)
        for data_item in STAFF_DATA ]

    # Pass the data to the template
    context['staff_data'] = parsed_data

    return context, data
