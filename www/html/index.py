#!/usr/bin/python3
# -*- coding: utf-8 -*-

import mod_python
from fonctions import baseHTML, connexionBD, lien

def index(req):
    req.content_type="text/html"
    content=str()

#sql part    
    conn=connexionBD()
    cur=conn.cursor()

    sql="SELECT * FROM paquet ORDER BY heure DESC LIMIT 20;"
    sql_count="SELECT COUNT(*) FROM paquet;"

    cur.execute(sql)
    conn.commit()
    data=cur.fetchall()

    cur.execute(sql_count)
    conn.commit()
    count=cur.fetchone()
    count=str(count[0])

    conn.close()
#sql part

#takes every lines from the select
    for i in data :
        content+=("""<tr>""" +
"""<td>""" + str(i[1]) + """</td>""" +
"""<td>""" + str(i[2]) + """</td>""" +
"""<td>""" + lien('ip_source.py?ip=' + str(i[3]), str(i[3])) + """</td>""" +
"""<td>""" + lien('ip_destination.py?ip=' + str(i[4]), str(i[4])) + """</td>""" +
"""<td>""" + lien('port_source.py?port=' + str(i[5]), str(i[5])) + """</td>""" +
"""<td>""" + lien('port_destination.py?port=' + str(i[6]), str(i[6])) + """</td>""" +
"""</tr>""")

#write the html page
    req.write(baseHTML("ATS - Accueil","""
<h1>ATS</h1>
<div id="tip" style="display:block;">
Afin de voir le reverse DNS d'une adresse IP, cliquez sur cette dernière dans le tableau <button id="ok" onclick="toggle_div(this,'tip');">OK</button></div>
<p>Nombre total de paquets : <b>"""+ count +"""</b></p>
<em>Pour afficher toute la table, cliquez</em>
<button id="afficheTas" onclick="affiche_tas()">ICI</button><br/>
<div id="tab">
<table class="data_tab">
<tr><th>Heure</th><th>Protocole</th><th>IP Source</th><th>IP Destination</th><th>Port Source</th><th>Port Destination</th></tr>
"""
+ content + 
"""
</table>
</div>
<script src="tip.js"></script>
<script src="tas.js"></script>
"""))
