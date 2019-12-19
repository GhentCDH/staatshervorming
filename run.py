#!/usr/bin/env python
import data
import markdown2
import re

from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader('run', 'templates'),
    autoescape=select_autoescape(['html', 'xml']),
    line_statement_prefix='#'
)

def generate_personen():

    # init template
    template = env.get_template('page-persoon.html')

    for (id,persoon) in data.personen.items():

        # convert text to markdown
        keys = ['sociaal','carrière','bezit','cultureel']

        for key in keys:

            if persoon[key] is None:
                continue

            ## lists
            persoon[key] = re.sub("\n- ","\n* ", persoon[key])

            ## titles
            titels = 'Antecedenten en origine|Familie|Huwelijk|Nageslacht|Statuut|Overlijden|Giften|Netwerken|Contemporaine vermeldingen|Taken en dienstreizen|Hoofdcarrière|Leen- en grondbezit|Leenbezit verwanten|Ambtsbezit|Gilden|Hofcultuur / literaire interesse|Begraafplaats'

            persoon[key] = re.sub("\n(" + titels + ")\s*\:?\n",r"\n### \1\n\n", persoon[key])

            ## references
            persoon[key] = re.sub("\(([0-9]{1,4})\)",r"<sup>([\1](#\1))</sup>", persoon[key])

            ## convert markdown to html
            persoon[key] = markdown2.markdown(persoon[key])

        if 'titels' in persoon:
            for titel in persoon['titels']:
                titel['label'] = markdown2.markdown(re.sub("\(([0-9]{1,4})\)",r"<sup>([\1](#\1))</sup>", titel['label']))

        template_options = {
            'persoon': persoon,
            'template_base_url': 'https://cdn.jsdelivr.net/gh/ugent-lw/huisstijl2016@2',
            'show_nav_left': 1,
            'show_page_navigation': 1,
            'css': [
                '../css/style.css'
            ]
        }
        html = template.render(template_options)

        # to save the results
        with open("output/persoon/" + id + ".html", "w") as fh:
            fh.write(html)

def generate_index():
    template = env.get_template('page-index.html')

    template_options = {
        'personen': data.personen,
        'template_base_url': 'https://cdn.jsdelivr.net/gh/ugent-lw/huisstijl2016@2',
        'css': [
            'css/style.css'
        ],
        'js_footer': [
            'js/default.js'
        ]
    }
    html = template.render(template_options)

    # to save the results
    with open("output/personen.html", "w") as fh:
        fh.write(html)

generate_index()
generate_personen()
