#!/usr/bin/python3
# -*- coding: utf-8 -*-
import psycopg2

def baseHTML(title,body):
    content=("""<!DOCTYPE html>
<html>
        <head>
                <title>"""+ title +"""</title>
                <meta charset="UTF-8">
                <link rel="stylesheet" type="text/css" href="style.css">
        </head>
        <body>"""+ body +"""</body>
</html>

            """)
    return content


def connexionBD():
    connexion=psycopg2.connect ("host='localhost' dbname='atsdb' user='atsuser' password='123456'")
    return connexion

def lien(url,text):
    content=("""<a href=" """ + url + """ ">""" + texte + """</a>""")
    return content