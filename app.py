from flask import Flask, render_template, url_for, request, session, redirect
import json
import os
import requests










def telegram_bot_sendtext(bot_message="you have a new visiter."):
    bot_token = '5430901662:AAEHCVWdtlwdfI9DcIV7rCDfpbgM7Wkbo5w'
    bot_chatID = '1355875237'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

def dbconnector(method,**kwargs):
    if method == "r":
        with open(os.path.join(os.getcwd(),"static/database.json"),method) as db:
            data = json.load(db)
        return data
    elif method == "w":
        data = dbconnector("r")
        if kwargs['fullname'] in list(data.keys()):
            data[kwargs['fullname']][len(list(data[kwargs['fullname']].keys()))+1] = {
                "ratings":kwargs["ratings"],
                "order":kwargs["order"],
            }
        else:
            data[kwargs["fullname"]] = {1:{
                "ratings":kwargs["ratings"],
                "order":kwargs["order"],
            }}
        
        with open(os.path.join(os.getcwd(),"static/database.json"),method) as db:
            json.dump(data,db)
    else:
        return
    return 








# all_subjects=['bases de deonnees et reseau', 'mecanique des milieux continus', 'mecanique des fluides', 'transfert de chaleur', 'transfert de masse', 'electrochimie', 'chimie des eaux', 'statistique', 'biologie cellulaire', 'biologie moleculaire', 'thermodynamique de base', 'resistance des materiaux', 'science des materiaux', 'electrotechnique', "fondement de l'economie pour l'etreprise et le marche", 'Echangeurs', 'froid', 'air humide et climatisation', 'microbiologie', 'genie des reacteurs', 'operations unitaires (technique de separation)', 'methodes numiriques et simulation des phenomenes de transport', 'entreprenariat', 'analyse financiere', 'automatique', 'instrumentaion', 'hydrologie', 'hydraulique', 'ecoulements industriels', 'transfert thermique dans les fluides', "machines transformatrices d'energie", 'SME', 'hygiene et environnement', 'securite industrielle', "projet d'usine", 'evaluation economique des procedes', 'gestion de production ,formation humaine et managerielle', 'ressources energetique et optimisation des procedes', 'procedes de traitement des eaux', 'complement de probabilites', 'statistique inferentielle', 'electronique numerique ', 'informatique industrielle', 'analyse et conception de base de donnees', 'langage SQL', 'structure de donnees', 'programmation orientee objet', 'signal', "systemes d'exploitation", 'reseaux informatique', 'economie et organisation', 'UML', 'langage JAVA', 'processus stochastiques', 'analyse de donnees', 'theorie des graphes', 'gestion de production', 'ERP', 'gestion de maintenance', 'fiabilite et surete de fonctionnement', 'outils de qualite', 'systeme de managemet de la qualite', 'reseaux locaux industriels', 'electonique de puissance', 'commande numerique des systeme lineares', 'supervesion', 'marketing', 'gestion de produits', 'intelligence artificielle', "systemes d'information et de la decision", 'conception et reingenierie des systemes industriels', 'ingenierie systeme', 'securite industrielle', "systeme de management de l'envirennement", 'logistique', "conception d'un systeme logistique", 'pilotage de la performance', 'controle de gestion', "theorie des systemes d'exploitation", 'programmation shell et programation systeme', 'programmation web', 'JEE', 'DotNet', 'techniques de transmission numerique', 'reseaux mobiles', 'reseaux informatique', 'technologie XML', 'technologie Mobile', 'genie logiciel', 'theorie des langages', 'theorie de complitation', 'gestion systemes', 'gestion reseaux', 'administration base de donnees client-serveur', 'langage PL', 'securite logiciel', 'securite reseaux', 'vision artificielle', 'systeme repartis', 'cloud computing', 'qualite logicielle', 'architecture logicielle', 'informatique decisionnelle', 'statistique non parametrique', 'pensee economique', 'mecroeconomie', 'macroeconomie', 'marches et actifs financiers', 'mathematique financieres', 'analyse fonctionnelle et convexe', 'theorie de la mesure', 'processus aleatoires', 'programmation lineare et non lineaire', 'recherche operationnelle', 'data science', 'big data', 'economie monetiare internationale', 'equilibre des marches', 'theorie du risque', 'theorie des jeux', 'finance participative', 'econometrie', 'series temporelles', 'valorisation des produits financiers classiques', 'mesure de risques', 'gestion de portfeuilles', "actuariat de l'assurance", 'pilotage de la performance', 'produits derives et courbes de tauxx', 'methodes numeriques en finance', 'conception de produit', 'mecanique des fluides et thermodynamique', 'mecanique appliquee', 'cinematique et dynamique du solide', 'electronique', 'turbomachines', 'mesure et controle', 'usinage', 'caracterisation et designations des materiaux', 'etude des mecanisme', 'calculs numeriques des structures', 'industialisation', 'productique', 'choix des materiaux', 'machine a commande numerique', 'CFAO', 'robotique', 'areliers flexibles', 'securite', '6 sigma', 'fiabilite des structures', 'procedes generaux de construction', 'stabilite des structures', 'mecanique des milieux continus', 'Geologie', 'SIG', 'Construction metallique', 'RDM', 'topographie', 'urbanisme', 'architecture', 'analyse technique', ' reglement de construction', 'hydrogeologie', 'beton arme', 'mecanique du sol', 'mecanique des structures', 'Beton', 'coffrages et ferraillage', 'fondations', 'geotechnique', 'geophysique', 'organisation de chantier', 'ouvrages hydraulique', 'VRD', 'CAO', 'Conception', 'electricite de batiment', "conditionnement d'air", 'dynamique des structures', 'etudes parasismiques', 'routes et ponts', 'droit de construction', 'systemes embarques', 'machines electrique', 'telegestion/teleconduite', 'reseaux electrique', 'installations electrique', 'protections numeriques', "economie de l'energie", "nouvelles sources d'energie", 'ingenierie des systemes electriques', 'diagnostic des equipements electrique', 'analyse numerique']
# all_subjects = ['Mathematique','Algorithmique et resoulution des problemes', 'Chimique','Statistique ,Stochastiques et probabilites', 'Biologie',
# 'Thermodynamique','Mecanique Generale','Bases des donnees et langages de programmation','Electronique et Electrotechnique','Optimisation',
# 'Automatisme et science d\'automatisation','Economie ,entreprenatiat et comptabilite','finance et analyse financiere','Mecanique des fluides',
# 'Science des materiaux','Energie renouvlable','Droit et gestion des ressources Humaines','Conception 3D','Analyse des donnees','Gestion de production et de la maintenance',
# "Marketing","Intelegence Artificielle","Logistique","Ginie Logiciel","Reseau et Telecoms","Cloud Computing","Big data","Data science","Mecanique Appliquee","Robotique","Geologie","Hydraulogie et hydraulique","Topographie",
# "Architicture","Geophysique","Signal","systemes d'exploitation","systemes embarques","protection numerique"]

# filliers=[
#     {
#         'id':'GPEE',
#         'name':'Genie Procedes de l\'Energie et de l\'Enverennement',
#         'modules':[],

#     }
# ]
modules = [{'id': 1, 'name': 'Mathematique', 'desc': ''}, 
{'id': 2, 'name': 'Algorithmique et resoulution des problemes', 'desc': ''}, 
{'id': 3, 'name': 'Chimie', 'desc': ''}, {'id': 4, 'name': 'Statistique ,Stochastiques et probabilites', 'desc': 'https://fr.wikipedia.org/wiki/Processus_stochastique'}, {'id': 5, 'name': 'Biologie', 'desc': ''}, {'id': 6, 'name': 'Thermo-dynamique', 'desc': ''}, {'id': 7, 'name': 'Mecanique Generale', 'desc': ''}, {'id': 8, 'name': 'Bases des donnees et langages de programmation', 'desc': ''}, {'id': 9, 'name': 'Electronique et Electrotechnique', 'desc': 'https://fr.wikipedia.org/wiki/%C3%89lectrotechnique'}, {'id': 10, 'name': 'Optimisation', 'desc': 'https://fr.wikipedia.org/wiki/Optimisation_(math%C3%A9matiques)'}, {'id': 11, 'name': "Automatisme et science d'automatisation", 'desc': 'https://fr.wikipedia.org/wiki/Automatisme'}, {'id': 12, 'name': 'Economie ,entreprenatiat et comptabilite', 'desc': ''}, {'id': 13, 'name': 'finance et analyse financiere', 'desc': 'https://fr.wikipedia.org/wiki/Finance'}, {'id': 14, 'name': 'Mecanique des fluides', 'desc': 'https://fr.wikipedia.org/wiki/M%C3%A9canique_des_fluides'}, {'id': 15, 'name': 'Science des materiaux', 'desc': 'https://fr.wikipedia.org/wiki/Science_des_mat%C3%A9riaux'}, {'id': 16, 'name': 'Energie renouvlable', 'desc': 'https://fr.wikipedia.org/wiki/%C3%89nergie_renouvelable'}, {'id': 17, 'name': 'Droit et gestion des ressources Humaines', 'desc': ''}, {'id': 18, 'name': 'Conception 3D', 'desc': ''}, {'id': 19, 'name': 'Analyse des donnees', 'desc': 'https://fr.wikipedia.org/wiki/Analyse_des_donn%C3%A9es'}, {'id': 20, 'name': 'Gestion de production et de la maintenance', 'desc': 'https://fr.wikipedia.org/wiki/Gestion_de_la_production'}, {'id': 21, 'name': 'Marketing', 'desc': 'https://fr.wikipedia.org/wiki/Marketing'}, {'id': 22, 'name': 'Intelegence Artificielle', 'desc': 'https://fr.wikipedia.org/wiki/Intelligence_artificielle'}, {'id': 23, 'name': 'Logistique', 'desc': 'https://fr.wikipedia.org/wiki/Logistique'}, {'id': 24, 'name': 'Ginie Logiciel', 'desc': 'https://fr.wikipedia.org/wiki/G%C3%A9nie_logiciel'}, {'id': 25, 'name': 'Reseau et Telecoms', 'desc': 'https://fr.wikipedia.org/wiki/R%C3%A9seau_de_t%C3%A9l%C3%A9communications'}, {'id': 26, 'name': 'Cloud Computing', 'desc': 'https://en.wikipedia.org/wiki/Cloud_computing'}, {'id': 27, 'name': 'Big data', 'desc': 'https://fr.wikipedia.org/wiki/Big_data'}, {'id': 28, 'name': 'Data science', 'desc': 'https://fr.wikipedia.org/wiki/Science_des_donn%C3%A9es'}, {'id': 29, 'name': 'Mecanique Appliquee', 'desc': ''}, {'id': 30, 'name': 'Robotique', 'desc': 'https://fr.wikipedia.org/wiki/Robotique'}, {'id': 31, 'name': 'Geologie', 'desc': ''}, {'id': 32, 'name': 'Hydraulogie et hydraulique', 'desc': 'https://fr.wikipedia.org/wiki/Hydrologie'}, {'id': 33, 'name': 'Topographie', 'desc': 'https://fr.wikipedia.org/wiki/Topographie'}, {'id': 34, 'name': 'Architicture', 'desc': 'https://fr.wikipedia.org/wiki/Architecture'}, {'id': 35, 'name': 'Geophysique', 'desc': 'https://fr.wikipedia.org/wiki/G%C3%A9ophysique'}, {'id': 36, 'name': 'Signal', 'desc': 'https://fr.wikipedia.org/wiki/Signal_%C3%A9lectrique'}, {'id': 37, 'name': "systemes d'exploitation", 'desc': 'https://fr.wikipedia.org/wiki/Syst%C3%A8me_d%27exploitation'}, {'id': 38, 'name': 'systemes embarques', 'desc': 'https://fr.wikipedia.org/wiki/Syst%C3%A8me_embarqu%C3%A9'}, {'id': 39, 'name': 'protection numerique', 'desc': ''}]

# branches = {'GPEE': {'Mathematique': '1', 'Algorithmique et resoulution des problemes': '1', 'Chimique': '7', 'Statistique ,Stochastiques et probabilites': '1', 'Biologie': '7', 'Thermodynamique': '7', 'Mecanique Generale': '3', 'Bases des donnees et langages de programmation': '1', 'Electronique et Electrotechnique': '6', 'Optimisation': '2', "Automatisme et science d'automatisation": '3', 'Economie ,entreprenatiat et comptabilite': '3', 'finance et analyse financiere': '2', 'Mecanique des fluides': '6', 'Science des materiaux': '5', 'Energie renouvlable': '7', 'Droit et gestion des ressources Humaines': '2', 'Conception 3D': '2', 'Analyse des donnees': '1', 'Gestion de production et de la maintenance': '4', 'Marketing': '1', 'Intelegence Artificielle': 0, 'Logistique': '6', 'Ginie Logiciel': 0, 'Reseau et Telecoms': 0, 'Cloud Computing': 0, 'Big data': 0, 'Data science': 0, 'Mecanique Appliquee': '6', 'Robotique': 0, 'Geologie': 0, 'Hydraulogie et hydraulique': 0, 'Topographie': 0, 'Architicture': 0, 'Geophysique': 0, 'Signal': 0, "systemes d'exploitation": 0, 'systemes embarques': 0, 'protection numerique': 0}, 'GI': {'Mathematique': '6', 'Algorithmique et resoulution des problemes': '7', 'Chimique': 0, 'Statistique ,Stochastiques et probabilites': '6', 'Biologie': 0, 'Thermodynamique': 0, 'Mecanique Generale': 0, 'Bases des donnees et langages de programmation': '7', 'Electronique et Electrotechnique': '5', 'Optimisation': '6', "Automatisme et science d'automatisation": '6', 'Economie ,entreprenatiat et comptabilite': '4', 'finance et analyse financiere': '4', 'Mecanique des fluides': 0, 'Science des materiaux': 0, 'Energie renouvlable': 0, 'Droit et gestion des ressources Humaines': '4', 'Conception 3D': '1', 'Analyse des donnees': '6', 'Gestion de production et de la maintenance': '4', 'Marketing': '4', 'Intelegence Artificielle': '7', 'Logistique': '4', 'Ginie Logiciel': '7', 'Reseau et Telecoms': '7', 'Cloud Computing': '7', 'Big data': '4', 'Data science': '4', 'Mecanique Appliquee': 0, 'Robotique': '4', 'Geologie': 0, 'Hydraulogie et hydraulique': 0, 'Topographie': 0, 'Architicture': 0, 'Geophysique': 0, 'Signal': '4', "systemes d'exploitation": '7', 'systemes embarques': '6', 'protection numerique': '6'}, 'GE': {'Mathematique': '4', 'Algorithmique et resoulution des problemes': '4', 'Chimique': 0, 'Statistique ,Stochastiques et probabilites': '4', 'Biologie': 0, 'Thermodynamique': '4', 'Mecanique Generale': '2', 'Bases des donnees et langages de programmation': '4', 'Electronique et Electrotechnique': '7', 'Optimisation': '5', "Automatisme et science d'automatisation": '7', 'Economie ,entreprenatiat et comptabilite': '3', 'finance et analyse financiere': '3', 'Mecanique des fluides': '3', 'Science des materiaux': '3', 'Energie renouvlable': '6', 'Droit et gestion des ressources Humaines': '4', 'Conception 3D': '5', 'Analyse des donnees': '3', 'Gestion de production et de la maintenance': '7', 'Marketing': '3', 'Intelegence Artificielle': '2', 'Logistique': '2', 'Ginie Logiciel': '5', 'Reseau et Telecoms': '6', 'Cloud Computing': 0, 'Big data': 0, 'Data science': 0, 'Mecanique Appliquee': '3', 'Robotique': '6', 'Geologie': 0, 'Hydraulogie et hydraulique': 0, 'Topographie': 0, 'Architicture': 0, 'Geophysique': 0, 'Signal': '7', "systemes d'exploitation": '6', 'systemes embarques': '7', 'protection numerique': '7'}, 'GM': {'Mathematique': '3', 'Algorithmique et resoulution des problemes': '3', 'Chimique': 0, 'Statistique ,Stochastiques et probabilites': '3', 'Biologie': 0, 'Thermodynamique': '5', 'Mecanique Generale': '7', 'Bases des donnees et langages de programmation': '3', 'Electronique et Electrotechnique': '3', 'Optimisation': '4', "Automatisme et science d'automatisation": '4', 'Economie ,entreprenatiat et comptabilite': '3', 'finance et analyse financiere': '3', 'Mecanique des fluides': '7', 'Science des materiaux': '7', 'Energie renouvlable': 0, 'Droit et gestion des ressources Humaines': '4', 'Conception 3D': '7', 'Analyse des donnees': '2', 'Gestion de production et de la maintenance': '6', 'Marketing': '3', 'Intelegence Artificielle': 0, 'Logistique': '1', 'Ginie Logiciel': 0, 'Reseau et Telecoms': 0, 'Cloud Computing': 0, 'Big data': 0, 'Data science': 0, 'Mecanique Appliquee': '7', 'Robotique': '5', 'Geologie': 0, 'Hydraulogie et hydraulique': '2', 'Topographie': 0, 'Architicture': 0, 'Geophysique': 0, 'Signal': 0, "systemes d'exploitation": 0, 'systemes embarques': 0, 'protection numerique': 0}, 'BTP': {'Mathematique': '2', 'Algorithmique et resoulution des problemes': '2', 'Chimique': '6', 'Statistique ,Stochastiques et probabilites': '2', 'Biologie': 0, 'Thermodynamique': '6', 'Mecanique Generale': '3', 'Bases des donnees et langages de programmation': '2', 'Electronique et Electrotechnique': '2', 'Optimisation': '2', "Automatisme et science d'automatisation": '1', 'Economie ,entreprenatiat et comptabilite': '3', 'finance et analyse financiere': '2', 'Mecanique des fluides': '5', 'Science des materiaux': '6', 'Energie renouvlable': 0, 'Droit et gestion des ressources Humaines': '5', 'Conception 3D': '6', 'Analyse des donnees': '2', 'Gestion de production et de la maintenance': '2', 'Marketing': '2', 'Intelegence Artificielle': 0, 'Logistique': '3', 'Ginie Logiciel': 0, 'Reseau et Telecoms': 0, 'Cloud Computing': 0, 'Big data': 0, 'Data science': 0, 'Mecanique Appliquee': '4', 'Robotique': 0, 'Geologie': '7', 'Hydraulogie et hydraulique': '7', 'Topographie': '7', 'Architicture': '7', 'Geophysique': '7', 'Signal': 0, "systemes d'exploitation": 0, 'systemes embarques': 0, 'protection numerique': 0}, 'FID': {'Mathematique': '7', 'Algorithmique et resoulution des problemes': '6', 'Chimique': 0, 'Statistique ,Stochastiques et probabilites': '7', 'Biologie': 0, 'Thermodynamique': 0, 'Mecanique Generale': 0, 'Bases des donnees et langages de programmation': '6', 'Electronique et Electrotechnique': 0, 'Optimisation': '3', "Automatisme et science d'automatisation": '2', 'Economie ,entreprenatiat et comptabilite': '6', 'finance et analyse financiere': '7', 'Mecanique des fluides': 0, 'Science des materiaux': 0, 'Energie renouvlable': 0, 'Droit et gestion des ressources Humaines': '6', 'Conception 3D': 0, 'Analyse des donnees': '7', 'Gestion de production et de la maintenance': '1', 'Marketing': '6', 'Intelegence Artificielle': '5', 'Logistique': '3', 'Ginie Logiciel': '5', 'Reseau et Telecoms': 0, 'Cloud Computing': '2', 'Big data': '7', 'Data science': '7', 'Mecanique Appliquee': 0, 'Robotique': 0, 'Geologie': 0, 'Hydraulogie et hydraulique': 0, 'Topographie': 0, 'Architicture': 0, 'Geophysique': 0, 'Signal': 0, "systemes d'exploitation": 0, 'systemes embarques': 0, 'protection numerique': '3'}, 'GIND': {'Mathematique': '5', 'Algorithmique et resoulution des problemes': '5', 'Chimique': 0, 'Statistique ,Stochastiques et probabilites': '5', 'Biologie': 0, 'Thermodynamique': '3', 'Mecanique Generale': '3', 'Bases des donnees et langages de programmation': '5', 'Electronique et Electrotechnique': '4', 'Optimisation': '7', "Automatisme et science d'automatisation": '5', 'Economie ,entreprenatiat et comptabilite': '5', 'finance et analyse financiere': '6', 'Mecanique des fluides': '4', 'Science des materiaux': '4', 'Energie renouvlable': '2', 'Droit et gestion des ressources Humaines': '7', 'Conception 3D': '4', 'Analyse des donnees': '5', 'Gestion de production et de la maintenance': '5', 'Marketing': '6', 'Intelegence Artificielle': '6', 'Logistique': '7', 'Ginie Logiciel': '6', 'Reseau et Telecoms': '4', 'Cloud Computing': '3', 'Big data': '4', 'Data science': '3', 'Mecanique Appliquee': '5', 'Robotique': '3', 'Geologie': 0, 'Hydraulogie et hydraulique': 0, 'Topographie': 0, 'Architicture': 0, 'Geophysique': 0, 'Signal': '3', "systemes d'exploitation": '5', 'systemes embarques': '5', 'protection numerique': '4'}}
branches = {
    'GPEE': {1: '2', 2: '2', 3: '7', 4: '2', 5: '8', 6: '7', 7: '3', 8: '2', 9: '6', 10: '2', 11: '3', 12: '3', 13: '2', 14: '6', 15: '5', 16: '7', 17: '2', 18: '2', 19: '2', 20: '4', 21: '2', 22: 0, 23: '6', 24: 0, 25: 0, 26: 0, 27: 0, 28: 0, 29: '6', 30: 0, 31: 0, 32: 0, 33: 0, 34: 0, 35: 0, 36: 0, 37: 0, 38: 0, 39: 0}, 
    'GI': {1: '6', 2: '7', 3: 0, 4: '6', 5: 0, 6: 0, 7: 0, 8: '7', 9: '5', 10: '6', 11: '6', 12: '4', 13: '4', 14: 0, 15: 0, 16: 0, 17: '4', 18: '1', 19: '6', 20: '4', 21: '4', 22: '7', 23: '4', 24: '7', 25: '7', 26: '7', 27: '4', 28: '4', 29: 0, 30: '4', 31: 0, 32: 0, 33: 0, 34: 0, 35: 0, 36: '4', 37: '7', 38: '6', 39: '6'}, 
    'GE': {1: '4', 2: '4', 3: 0, 4: '4', 5: 0, 6: '4', 7: '2', 8: '4', 9: '7', 10: '5', 11: '7', 12: '3', 13: '3', 14: '3', 15: '3', 16: '6', 17: '4', 18: '5', 19: '3', 20: '7', 21: '3', 22: '2', 23: '2', 24: '5', 25: '6', 26: 0, 27: 0, 28: 0, 29: '3', 30: '6', 31: 0, 32: 0, 33: 0, 34: 0, 35: 0, 36: '7', 37: '6', 38: '7', 39: '7'}, 
    'GM': {1: '3', 2: '3', 3: 0, 4: '3', 5: 0, 6: '5', 7: '7', 8: '3', 9: '3', 10: '4', 11: '4', 12: '3', 13: '3', 14: '7', 15: '7', 16: 0, 17: '4', 18: '7', 19: '2', 20: '6', 21: '3', 22: 0, 23: '1', 24: 0, 25: 0, 26: 0, 27: 0, 28: 0, 29: '7', 30: '5', 31: 0, 32: '2', 33: 0, 34: 0, 35: 0, 36: 0, 37: 0, 38: 0, 39: 0}, 
    'BTP': {1: '2', 2: '2', 3: '6', 4: '2', 5: 0, 6: '6', 7: '3', 8: '2', 9: '2', 10: '2', 11: '1', 12: '3', 13: '2', 14: '5', 15: '6', 16: 0, 17: '5', 18: '6', 19: '2', 20: '2', 21: '2', 22: 0, 23: '3', 24: 0, 25: 0, 26: 0, 27: 0, 28: 0, 29: '4', 30: 0, 31: '7', 32: '7', 33: '7', 34: '7', 35: '7', 36: 0, 37: 0, 38: 0, 39: 0}, 
    'FID': {1: '7', 2: '6', 3: 0, 4: '7', 5: 0, 6: 0, 7: 0, 8: '6', 9: 0, 10: '3', 11: '2', 12: '6', 13: '7', 14: 0, 15: 0, 16: 0, 17: '6', 18: 0, 19: '7', 20: '1', 21: '6', 22: '5', 23: '3', 24: '5', 25: 0, 26: '2', 27: '7', 28: '7', 29: 0, 30: 0, 31: 0, 32: 0, 33: 0, 34: 0, 35: 0, 36: 0, 37: 0, 38: 0, 39: '3'}, 
    'GIND': {1: '5', 2: '5', 3: 0, 4: '5', 5: 0, 6: '3', 7: '3', 8: '5', 9: '4', 10: '7', 11: '5', 12: '5', 13: '6', 14: '4', 15: '4', 16: '2', 17: '7', 18: '4', 19: '5', 20: '5', 21: '6', 22: '6', 23: '7', 24: '6', 25: '4', 26: '3', 27: '4', 28: '3', 29: '5', 30: '3', 31: 0, 32: 0, 33: 0, 34: 0, 35: 0, 36: '3', 37: '5', 38: '5', 39: '4'}
    }
filliers = {
    "GPEE":"Genie Des Procedes, De L'Energie Et De l'Enverenement",
    "GI":"Ginie Informatique",
    "GE":"Ginie Electrique",
    "GM":"Genie Mecanique",
    "BTP":"Batiment Et Travaux Publique",
    "FID":"Finance Et Ingenierie Decisionnelle",
    "GIND":"Genie Industrielle",
}


app= Flask(__name__)
app.config["SECRET_KEY"] = "hlkdmmq5646à)à-)è#~|`"

@app.route('/')
def home():
    # with open(os.path.join(os.getcwd(),"static\\data.json"),'r') as file:
    #     data = file.read()
    
    # print(data)
    return render_template('home.html',session=session)

@app.route('/modules',methods=['GET','POST'])
def subjects():
    session["fullname"] = request.json["fullname"] 
    if request.method == "POST":
        if request.json['fullname']:
            # dbconnector("w",fullname = request.json["fullname"])
            return render_template("sublist.html",modules=modules,session=session)

@app.route('/nodef')
def nodef():
    return "<h1>No description available</h1>"

@app.route('/branchlist',methods=['POST'])
def treatdata():
    if request.method =='POST':
        order_list = {}
        for fillier in list(branches.keys()):
            order = 0
            for i in range(1,40):
                if request.json["ratings"][str(i)] !=None:
                    try:
                        order += (float(request.json["ratings"][str(i)])-5)*float(branches[fillier][i])
                    except:
                        order+=0
                else:
                    order += 0
            order_list[order]=fillier
        context = []
        listkeys=list(order_list.keys())
        listkeys.sort(reverse = True)
        for f,c,o in zip(listkeys,["33FF00","#66CC99","#33FFCC","#3399FF","#0000FF","#9933CC","#FF0033"],[1,2,3,4,5,6,7]):
            context.append({"fill":filliers[order_list[f]],"clr":c,"order":o})
        dbconnector("w",fullname = request.json["fullname"],ratings = request.json["ratings"],order = order_list)
        return render_template("orderlist.html",context = context)
    else:
        return redirect(url_for("home"))

@app.route("/contactme",methods=['POST'])
def contactme():
    print(session)
    return render_template("contactme.html")

@app.route('/sendtelemessage',methods=['POST'])
def sendtelemessage():
    if request.json['name'] or request.json["phonenumber"]:
        telegram_bot_sendtext(request.json['name']+'\n'+request.json['phonenumber']+':\n\n'+request.json['message'])
    return ''


if __name__ == '__main__':
    app.run(debug=True)