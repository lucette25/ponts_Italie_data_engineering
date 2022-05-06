from bs4 import BeautifulSoup
import requests
import pandas as pd

def getData():
    html_text = requests.get('https://fr.wikipedia.org/wiki/Liste_de_ponts_d%27Italie').text
    soup = BeautifulSoup(html_text, "html.parser")
    tableaux = soup.find_all('table', class_='wikitable sortable')

    nom = []
    distinction = []
    longueur = []
    type_final = []
    voie_p_voie_f = []
    date = []
    localisation = []
    region = []

    for t in range(len(tableaux)):
        lines = tableaux[t].find_all('tr')[1:]
        for line in lines:
            cols = line.find_all('td')[2:10]

            # recuperation des noms
            try:
                nom.append(cols[0].find('a').get_text())
            except:
                nom.append('')

            # recuperation des distinctions
            try:
                distinction.append(cols[1].get_text().replace(u'\xa0', u' '))
            except:
                distinction.append('')

            # recuperation des longueurs
            try:
                longueur.append(cols[2].get_text())
            except:
                longueur.append('')

            # recuperation des types
            try:
                type_final.append(cols[3].get_text())
            except:
                type_final.append('')

            # recuperation des voies
            try:
                voie_p_voie_f.append(cols[4].get_text().strip())
            except:
                voie_p_voie_f.append('')

            # recuperation des dates
            try:
                date.append(' '.join(cols[5].get_text().split()))
            except:
                date.append('')

            # recuperation des localisations
            try:
                localisation.append(' '.join(cols[6].get_text().split()))
            except:
                localisation.append('')

            # recuperation des regions
            try:
                region.append(cols[7].get_text())
            except:
                region.append('')

    ## on met tout dans un Dataframe
    ponts_df = pd.DataFrame({
        "nom": nom,
        "distinction": distinction,
        "longueur": longueur,
        "Type": type_final,
        "Voiep_voief": voie_p_voie_f,
        "Date": date,
        "localisation": localisation,
        "region": region
    })
    return ponts_df


  