


# with open('data.json') as file:
#     data=file.read()


# data = eval(data)
# all_modules =["actuariat de l'assurance", 'administration systeme et reseaux', 'analyse et conception des bases de donnees', 
# 'analyse fonctionnelle et convexe', 'analyse technique et architecture ', 'architecture et qualite logicielle', 
# 'architecture jee et dotnet', 'automatique et systemes a evenements discrets', 'automatisation', 
# 'avant projet de fabrication', 'bases de donnees avancees client- serveur', 'calcul numerique des structures', 
# 'calcul stochastique pour la finance', 'calculs numeriques', 'commande des systemes industriels et supervision', 
# 'communication et gestion', 'communication et ouverture', 'communication professionnelle et culture internationale', 
# 'communication professionnelle et ouverture', "comptabilite et organisation d'entreprise", 
# 'comptabilite et organisation d\'entreprise', 'conception de produit 1', 'conception de produit 2', 
# 'conception des systemes logistiques', 'conception et amelioration des systemes industriels', 
# 'conception et calcul d\'ouvrages', 'conditionnement d\'air, acoustique et electricite en btp', 
# 'data science et big data', 'dynamique des structures et etudes parasismiques', 'decouverte entreprise btp', 
# 'economie de l\'energie et energies nouvelles', 'economie internationale et equilibre des marches', 
# 'economie, organisation et comptabilite d\'entreprise', 'econometrie et series temporelles', 
# 'electronique de puissance et electronique de commande', 'electronique et informatique industrielle', 
# 'electronique numerique et informatique industrielle', 'electrotechnique et automatisme', 'etude des mecanismes', 
# 'finance et marketing', 'finance participative et marketing', 'fluides complexes et transferts', 
# 'fondations, coffrages, beton precontraint', 'formation humaine et managerielle', 'gestion de la production et erp', 
# 'gestion de portefeuille et mesures de risques', 'gestion de production et erp', 'gestion de projet et analyse financiere', 
# 'gestion de projet et gestion de produit', 'gestion de projet et gestion financiere', 'gestion de projets et de produits', 
# 'gestion et droit', 'gestion et ordonnancement de projet btp', 'gestion et outils de la qualite', 'geologie pour l\'ingenieur', 
# 'geotechnique et geophysique', 'hydrogeologie et ouvrages hydrauliques', 'informatique decisionnelle et erp', 
# 'informatique et applications', 'informatique industrielle et systemes embarques', 'informatique repartie et cloud computing', 
# 'ingenierie des systemes d\'information', 'ingenierie des systemes electriques', 'installations electriques et protection', 
# 'intelligence artificielle et vission artficielle', "introduction a l'economie et pensee economique", 
# 'langages de programmation', 'langue, communication et ouverture culture',
# 'langues, communication  et ouverture', 'langues, communication et ouverture', 'langues, communication et ouverture culturelle', 
# 'logistique et maitrisestatistique des processus', 
# 'machine a commandenumerique et fao', 'machines electriques et commandes', 
# 'maintenance, fiabilite et surete de fonctionnement', 'management de projets et gestion industrielle', 
# 'management qualite et securite', 'management qualite et securite en btp', 'marcheset calculs financiers',
# 'mathematiques appliquees', 'mathematiques pour ingenieur', 'mathematiques pour l\'ingenieur', 'materiaux', 
# 'materiaux de construction et beton arme', 'microeconomie  et macroeconomie', 
# 'modelisation oriente objet et programmation java', 'mecanique appliquee ', 'mecanique de base', 
# 'mecanique des fluides et thermodynamique', 'mecanique des structures et des sols', 'methodes numeriques en finance', 
# 'optimisation et analyse des donnees', 'optimisation et recherche operationnelle', 'optimisation et theorie degraphes', 
# 'organisation et comptabilite de l\'entreprise', 'physique industrielle', 'pilotage de la performance et controle de gestion', 
# 'processus stochastiques et analyse de donnees', 'processus stochastiques et analyse des donnees', 
# 'productique et choix des materiaux', 'produits derives et courbes de taux', 
# 'programmation lineaire et non lineaire et recherche operationnelle', 'programmation web', 
# 'projet de fin d\'annee', 'projet industriel', 'qualite, environnement et securite', 'rdm et construction metallique', 
# 'robotique et ateliers flexibles', 'routes et ponts', 'rupture et endommagement', 'reseaux d\'acces et reseaux locaux',
# 'reseaux hydraulique et vrd', 'reseaux informatique et telecoms', 'reseaux locaux industriels et electronique de puissance', 
# 'reseaux electriques et telegestion', 'signal et automatique', 'signal, information et codage', 
# 'signaux electronique et electrotechnique', 'signaux, electronique et electrotechnique', 'statistique mathematique', 
# 'statistique non parametrique et add', 'statistiques mathematiques', 'structure de donnees et programmation oriente objet', 
# "systeme d'exploitation et reseaux informatiques", 'systeme d\'exploitation et reseaux informatiques', 
# 'securite des reseaux et des systemes d\'information', 'surete de fonctionnement, fiabilite et maintenance', 
# 'tec', 'techniques d\'expression et de communication 2', 'technologie xml et technologie mobile', 
# 'thermodynamique et mecanique des fluides', 'theorie de la decision', 'theorie de la mesure et processus aleatoires', 
# 'theorie de langage et compilation', 'transfert thermique et turbo machines', 'uml2 et genie logiciel', 
# 'urbanisme et topographie ', 'usinage, mesure et controle', 'valorisation des produits financiers classiques et fiscalite', 
# 'electrotechnique et automatisme']

# modules_1 = {'statistiques mathematiques': ['GI', 'GE', 'GIND'], 'electronique et informatique industrielle': ['GI', 'GIND'], 
# 'analyse et conception des bases de donnees': ['GI', 'GE', 'GIND', 'FID'], 
# 'structure de donnees et programmation oriente objet': ['GI', 'GE', 'GIND', 'FID'], 'electrotechnique et automatisme': ['GI'],
# 'langues, communication et ouverture': ['GI', 'GE', 'GIND'], 
# 'mathematiques pour l\'ingenieur': ['GI', 'GE', 'GIND', 'FID', 'BTP'], 'signal et automatique': ['GI', 'GE', 'GIND'], 
# 'systeme d\'exploitation et reseaux informatiques': ['GI', 'GIND'], 'modelisation oriente objet et programmation java': ['GI'],
# 'programmation web': ['GI'], 'comptabilite et organisation d\'entreprise': ['GI', 'GIND', 'FID'],
# 'optimisation et theorie degraphes': ['GI'], 'architecture jee et dotnet': ['GI'],
# 'bases de donnees avancees client- serveur': ['GI'], 'processus stochastiques et analyse de donnees': ['GI'],
# 'gestion de projet et analyse financiere': ['GI'], 'tec': ['GI'], 'reseaux informatique et telecoms': ['GI'],
# 'uml2 et genie logiciel': ['GI'], 'technologie xml et technologie mobile': ['GI'], 'theorie de langage et compilation': ['GI'],
# 'administration systeme et reseaux': ['GI'], 'communication et gestion': ['GI'],
# 'intelligence artificielle et vission artficielle': ['GI'], 'informatique repartie et cloud computing': ['GI'], 
# 'architecture et qualite logicielle': ['GI'], 'informatique decisionnelle et erp': ['GI'], 
# 'securite des reseaux et des systemes d\'information': ['GI'], 'formation humaine et managerielle': ['GI', 'GE', 'GIND'], 
# 'electronique numerique et informatique industrielle': ['GE'], 'electrotechnique et automatisme': ['GE', 'GIND'], 
# 'physique industrielle': ['GE', 'GIND'], "systeme d'exploitation et reseaux informatiques": ['GE'], 
# 'langages de programmation': ['GE', 'GIND', 'FID'], "comptabilite et organisation d'entreprise": ['GE'], 
# 'optimisation et analyse des donnees': ['GE'], 'signal, information et codage': ['GE'], 'automatique et systemes a evenements discrets': ['GE'], 'electronique de puissance et electronique de commande': ['GE'], 'surete de fonctionnement, fiabilite et maintenance': ['GE'], 'communication et ouverture': ['GE', 'FID', 'GM'], 'reseaux d\'acces et reseaux locaux': ['GE'], 'informatique industrielle et systemes embarques': ['GE'], 'machines electriques et commandes': ['GE'], 'reseaux electriques et telegestion': ['GE'], 'projet de fin d\'annee': ['GE', 'GIND', 'FID'], 'management de projets et gestion industrielle': ['GE'], 'qualite, environnement et securite': ['GE', 'GIND'], 'installations electriques et protection': ['GE'], 'economie de l\'energie et energies nouvelles': ['GE'], 'ingenierie des systemes electriques': ['GE'], 'communication professionnelle et culture internationale': ['GE'], 'processus stochastiques et analyse des donnees': ['GIND'], 'optimisation et recherche operationnelle': ['GIND'], 'gestion de la production et erp': ['GIND'], 'maintenance, fiabilite et surete de fonctionnement': ['GIND', 'GM'], 'gestion et outils de la qualite': ['GIND'], 'reseaux locaux industriels et electronique de puissance': ['GIND'], 'commande des systemes industriels et supervision': ['GIND'], 'gestion de projets et de produits': ['GIND'], 'ingenierie des systemes d\'information': ['GIND'], 'finance et marketing': ['GIND'], 'conception et amelioration des systemes industriels': ['GIND'], 'conception des systemes logistiques': ['GIND'], 'pilotage de la performance et controle de gestion': ['GIND', 'FID'], 'communication professionnelle et ouverture': ['GIND', 'FID', 'GM'], 'statistique mathematique': ['FID'], 'analyse fonctionnelle et convexe': ['FID'], "introduction a l'economie et pensee economique": ['FID'], 'langues, communication  et ouverture': ['FID'], 'microeconomie  et macroeconomie': ['FID'], 'statistique non parametrique et add': ['FID'], 'marches et calculs financiers': ['FID'], 'theorie de la mesure et processus aleatoires': ['FID'], 'programmation lineaire et non lineaire et recherche operationnelle': ['FID'], 'data science et big data': ['FID'], 'economie internationale et equilibre des marches': ['FID'], 'valorisation des produits financiers classiques et fiscalite': ['FID'], 'gestion de projet et gestion financiere': ['FID'], 
# 'calcul stochastique pour la finance': ['FID'], 
# 'theorie de la decision': ['FID'], 'econometrie et series temporelles': ['FID'], 
# 'finance participative et marketing': ['FID'], 'methodes numeriques en finance': ['FID'], 
# 'gestion de portefeuille et mesures de risques': ['FID'], 'produits derives et courbes de taux': ['FID'], 
# "actuariat de l'assurance": ['FID'], 'mathematiques pour ingenieur': ['GM'], 'mecanique de base': ['GM', 'BTP'], 
# 'conception de produit 1': ['GM'], 'thermodynamique et mecanique des fluides': ['GM'],
# 'informatique et applications': ['GM', 'BTP'], 'langue, communication et ouverture culture': ['GM'], 
# 'mathematiques appliquees': ['GM', 'BTP'], 'mecanique appliquee ': ['GM'], 'conception de produit 2': ['GM'], 
# 'signaux, electronique et electrotechnique': ['GM'], 'transfert thermique et turbo machines': ['GM'], 
# 'economie, organisation et comptabilite d\'entreprise': ['GM'], 'usinage, mesure et controle': ['GM'], 
# 'materiaux': ['GM'], 'etude des mecanismes': ['GM'], 'gestion de production et erp': ['GM'], 'calculs numeriques': ['GM'], 
# 'avant projet de fabrication': ['GM'], 'automatisation': ['GM'], 'productique et choix des materiaux': ['GM'], 
# 'projet industriel': ['GM'], 'gestion de projet et gestion de produit': ['GM'], 'machine a commandenumerique et fao': ['GM'], 
# 'robotique et ateliers flexibles': ['GM'], 'rupture et endommagement': ['GM'], 'management qualite et securite': ['GM'], 
# 'logistique et maitrise statistique des processus': ['GM'], 'geologie pour l\'ingenieur': ['BTP'], 
# 'mecanique des fluides et thermodynamique': ['BTP'], 'langues, communication et ouverture culturelle': ['BTP'], 
# 'fluides complexes et transferts': ['BTP'], 'urbanisme et topographie ': ['BTP'], 'analyse technique et architecture ': ['BTP'], 
# 'signaux electronique et electrotechnique': ['BTP'], 'rdm et construction metallique': ['BTP'], 
# 'mecanique des structures et des sols': ['BTP'], 'hydrogeologie et ouvrages hydrauliques': ['BTP'], 
# 'materiaux de construction et beton arme': ['BTP'], 'calcul numerique des structures': ['BTP'], 
# 'decouverte entreprise btp': ['BTP'], 'techniques d\'expression et de communication 2': ['BTP'], 
# 'reseaux hydraulique et vrd': ['BTP'], 'fondations, coffrages, beton precontraint': ['BTP'], 
# 'geotechnique et geophysique': ['BTP'], 'gestion et ordonnancement de projet btp': ['BTP'], 
# 'organisation et comptabilite de l\'entreprise': ['BTP'], 'conception et calcul d\'ouvrages': ['BTP'], 
# 'conditionnement d\'air, acoustique et electricite en btp': ['BTP'], 'dynamique des structures et etudes parasismiques': ['BTP'], 
# 'routes et ponts': ['BTP'], 'management qualite et securite en btp': ['BTP'], 'gestion et droit': ['BTP']}

# modules = {}

# # for fillier in data['formations'].keys():
# #     fill = data['formations'][fillier]
# #     fill = [i.lower() for i in fill]
# #     for module in fill:
# #         if module not in modules.keys():
# #             modules[module]=[fillier]
# #         else:
# #             modules[module].append(fillier)

# # print(modules)
# all_modules = list(modules_1.keys())
# matches = {}
# import nltk
# from nltk.translate import bleu
# from nltk.translate.bleu_score import SmoothingFunction
# smoothie = SmoothingFunction().method4


# for i in all_modules:
#     matches[i]=[]
#     all_modules.remove(i)
#     for j in all_modules:
#         if bleu([i], j, smoothing_function=smoothie)>=0.5:
#             matches[i].append(j)



# print(matches)


branches = {'GPEE': {'Mathematique': '1', 'Algorithmique et resoulution des problemes': '1', 'Chimique': '7', 'Statistique ,Stochastiques et probabilites': '1', 'Biologie': '7', 'Thermodynamique': '7', 'Mecanique Generale': '3', 'Bases des donnees et langages de programmation': '1', 'Electronique et Electrotechnique': '6', 'Optimisation': '2', "Automatisme et science d'automatisation": '3', 'Economie ,entreprenatiat et comptabilite': '3', 'finance et analyse financiere': '2', 'Mecanique des fluides': '6', 'Science des materiaux': '5', 'Energie renouvlable': '7', 'Droit et gestion des ressources Humaines': '2', 'Conception 3D': '2', 'Analyse des donnees': '1', 'Gestion de production et de la maintenance': '4', 'Marketing': '1', 'Intelegence Artificielle': 0, 'Logistique': '6', 'Ginie Logiciel': 0, 'Reseau et Telecoms': 0, 'Cloud Computing': 0, 'Big data': 0, 'Data science': 0, 'Mecanique Appliquee': '6', 'Robotique': 0, 'Geologie': 0, 'Hydraulogie et hydraulique': 0, 'Topographie': 0, 'Architicture': 0, 'Geophysique': 0, 'Signal': 0, "systemes d'exploitation": 0, 'systemes embarques': 0, 'protection numerique': 0}, 'GI': {'Mathematique': '6', 'Algorithmique et resoulution des problemes': '7', 'Chimique': 0, 'Statistique ,Stochastiques et probabilites': '6', 'Biologie': 0, 'Thermodynamique': 0, 'Mecanique Generale': 0, 'Bases des donnees et langages de programmation': '7', 'Electronique et Electrotechnique': '5', 'Optimisation': '6', "Automatisme et science d'automatisation": '6', 'Economie ,entreprenatiat et comptabilite': '4', 'finance et analyse financiere': '4', 'Mecanique des fluides': 0, 'Science des materiaux': 0, 'Energie renouvlable': 0, 'Droit et gestion des ressources Humaines': '4', 'Conception 3D': '1', 'Analyse des donnees': '6', 'Gestion de production et de la maintenance': '4', 'Marketing': '4', 'Intelegence Artificielle': '7', 'Logistique': '4', 'Ginie Logiciel': '7', 'Reseau et Telecoms': '7', 'Cloud Computing': '7', 'Big data': '4', 'Data science': '4', 'Mecanique Appliquee': 0, 'Robotique': '4', 'Geologie': 0, 'Hydraulogie et hydraulique': 0, 'Topographie': 0, 'Architicture': 0, 'Geophysique': 0, 'Signal': '4', "systemes d'exploitation": '7', 'systemes embarques': '6', 'protection numerique': '6'}, 'GE': {'Mathematique': '4', 'Algorithmique et resoulution des problemes': '4', 'Chimique': 0, 'Statistique ,Stochastiques et probabilites': '4', 'Biologie': 0, 'Thermodynamique': '4', 'Mecanique Generale': '2', 'Bases des donnees et langages de programmation': '4', 'Electronique et Electrotechnique': '7', 'Optimisation': '5', "Automatisme et science d'automatisation": '7', 'Economie ,entreprenatiat et comptabilite': '3', 'finance et analyse financiere': '3', 'Mecanique des fluides': '3', 'Science des materiaux': '3', 'Energie renouvlable': '6', 'Droit et gestion des ressources Humaines': '4', 'Conception 3D': '5', 'Analyse des donnees': '3', 'Gestion de production et de la maintenance': '7', 'Marketing': '3', 'Intelegence Artificielle': '2', 'Logistique': '2', 'Ginie Logiciel': '5', 'Reseau et Telecoms': '6', 'Cloud Computing': 0, 'Big data': 0, 'Data science': 0, 'Mecanique Appliquee': '3', 'Robotique': '6', 'Geologie': 0, 'Hydraulogie et hydraulique': 0, 'Topographie': 0, 'Architicture': 0, 'Geophysique': 0, 'Signal': '7', "systemes d'exploitation": '6', 'systemes embarques': '7', 'protection numerique': '7'}, 'GM': {'Mathematique': '3', 'Algorithmique et resoulution des problemes': '3', 'Chimique': 0, 'Statistique ,Stochastiques et probabilites': '3', 'Biologie': 0, 'Thermodynamique': '5', 'Mecanique Generale': '7', 'Bases des donnees et langages de programmation': '3', 'Electronique et Electrotechnique': '3', 'Optimisation': '4', "Automatisme et science d'automatisation": '4', 'Economie ,entreprenatiat et comptabilite': '3', 'finance et analyse financiere': '3', 'Mecanique des fluides': '7', 'Science des materiaux': '7', 'Energie renouvlable': 0, 'Droit et gestion des ressources Humaines': '4', 'Conception 3D': '7', 'Analyse des donnees': '2', 'Gestion de production et de la maintenance': '6', 'Marketing': '3', 'Intelegence Artificielle': 0, 'Logistique': '1', 'Ginie Logiciel': 0, 'Reseau et Telecoms': 0, 'Cloud Computing': 0, 'Big data': 0, 'Data science': 0, 'Mecanique Appliquee': '7', 'Robotique': '5', 'Geologie': 0, 'Hydraulogie et hydraulique': '2', 'Topographie': 0, 'Architicture': 0, 'Geophysique': 0, 'Signal': 0, "systemes d'exploitation": 0, 'systemes embarques': 0, 'protection numerique': 0}, 'BTP': {'Mathematique': '2', 'Algorithmique et resoulution des problemes': '2', 'Chimique': '6', 'Statistique ,Stochastiques et probabilites': '2', 'Biologie': 0, 'Thermodynamique': '6', 'Mecanique Generale': '3', 'Bases des donnees et langages de programmation': '2', 'Electronique et Electrotechnique': '2', 'Optimisation': '2', "Automatisme et science d'automatisation": '1', 'Economie ,entreprenatiat et comptabilite': '3', 'finance et analyse financiere': '2', 'Mecanique des fluides': '5', 'Science des materiaux': '6', 'Energie renouvlable': 0, 'Droit et gestion des ressources Humaines': '5', 'Conception 3D': '6', 'Analyse des donnees': '2', 'Gestion de production et de la maintenance': '2', 'Marketing': '2', 'Intelegence Artificielle': 0, 'Logistique': '3', 'Ginie Logiciel': 0, 'Reseau et Telecoms': 0, 'Cloud Computing': 0, 'Big data': 0, 'Data science': 0, 'Mecanique Appliquee': '4', 'Robotique': 0, 'Geologie': '7', 'Hydraulogie et hydraulique': '7', 'Topographie': '7', 'Architicture': '7', 'Geophysique': '7', 'Signal': 0, "systemes d'exploitation": 0, 'systemes embarques': 0, 'protection numerique': 0}, 'FID': {'Mathematique': '7', 'Algorithmique et resoulution des problemes': '6', 'Chimique': 0, 'Statistique ,Stochastiques et probabilites': '7', 'Biologie': 0, 'Thermodynamique': 0, 'Mecanique Generale': 0, 'Bases des donnees et langages de programmation': '6', 'Electronique et Electrotechnique': 0, 'Optimisation': '3', "Automatisme et science d'automatisation": '2', 'Economie ,entreprenatiat et comptabilite': '6', 'finance et analyse financiere': '7', 'Mecanique des fluides': 0, 'Science des materiaux': 0, 'Energie renouvlable': 0, 'Droit et gestion des ressources Humaines': '6', 'Conception 3D': 0, 'Analyse des donnees': '7', 'Gestion de production et de la maintenance': '1', 'Marketing': '6', 'Intelegence Artificielle': '5', 'Logistique': '3', 'Ginie Logiciel': '5', 'Reseau et Telecoms': 0, 'Cloud Computing': '2', 'Big data': '7', 'Data science': '7', 'Mecanique Appliquee': 0, 'Robotique': 0, 'Geologie': 0, 'Hydraulogie et hydraulique': 0, 'Topographie': 0, 'Architicture': 0, 'Geophysique': 0, 'Signal': 0, "systemes d'exploitation": 0, 'systemes embarques': 0, 'protection numerique': '3'}, 'GIND': {'Mathematique': '5', 'Algorithmique et resoulution des problemes': '5', 'Chimique': 0, 'Statistique ,Stochastiques et probabilites': '5', 'Biologie': 0, 'Thermodynamique': '3', 'Mecanique Generale': '3', 'Bases des donnees et langages de programmation': '5', 'Electronique et Electrotechnique': '4', 'Optimisation': '7', "Automatisme et science d'automatisation": '5', 'Economie ,entreprenatiat et comptabilite': '5', 'finance et analyse financiere': '6', 'Mecanique des fluides': '4', 'Science des materiaux': '4', 'Energie renouvlable': '2', 'Droit et gestion des ressources Humaines': '7', 'Conception 3D': '4', 'Analyse des donnees': '5', 'Gestion de production et de la maintenance': '5', 'Marketing': '6', 'Intelegence Artificielle': '6', 'Logistique': '7', 'Ginie Logiciel': '6', 'Reseau et Telecoms': '4', 'Cloud Computing': '3', 'Big data': '4', 'Data science': '3', 'Mecanique Appliquee': '5', 'Robotique': '3', 'Geologie': 0, 'Hydraulogie et hydraulique': 0, 'Topographie': 0, 'Architicture': 0, 'Geophysique': 0, 'Signal': '3', "systemes d'exploitation": '5', 'systemes embarques': '5', 'protection numerique': '4'}}


all_subjects = ['Mathematique','Algorithmique et resoulution des problemes', 'Chimique','Statistique ,Stochastiques et probabilites', 'Biologie',
'Thermodynamique','Mecanique Generale','Bases des donnees et langages de programmation','Electronique et Electrotechnique','Optimisation',
'Automatisme et science d\'automatisation','Economie ,entreprenatiat et comptabilite','finance et analyse financiere','Mecanique des fluides',
'Science des materiaux','Energie renouvlable','Droit et gestion des ressources Humaines','Conception 3D','Analyse des donnees','Gestion de production et de la maintenance',
"Marketing","Intelegence Artificielle","Logistique","Ginie Logiciel","Reseau et Telecoms","Cloud Computing","Big data","Data science","Mecanique Appliquee","Robotique","Geologie","Hydraulogie et hydraulique","Topographie",
"Architicture","Geophysique","Signal","systemes d'exploitation","systemes embarques","protection numerique"]


modules = [{'id': 1, 'name': 'Mathematique', 'desc': ''}, {'id': 2, 'name': 'Algorithmique et resoulution des problemes', 'desc': ''}, {'id': 3, 'name': 'Chimique', 'desc': ''}, {'id': 4, 'name': 'Statistique ,Stochastiques et probabilites', 'desc': 'https://fr.wikipedia.org/wiki/Processus_stochastique'}, {'id': 5, 'name': 'Biologie', 'desc': ''}, {'id': 6, 'name': 'Thermodynamique', 'desc': ''}, {'id': 7, 'name': 'Mecanique Generale', 'desc': ''}, {'id': 8, 'name': 'Bases des donnees et langages de programmation', 'desc': ''}, {'id': 9, 'name': 'Electronique et Electrotechnique', 'desc': 'https://fr.wikipedia.org/wiki/%C3%89lectrotechnique'}, {'id': 10, 'name': 'Optimisation', 'desc': 'https://fr.wikipedia.org/wiki/Optimisation_(math%C3%A9matiques)'}, {'id': 11, 'name': "Automatisme et science d'automatisation", 'desc': 'https://fr.wikipedia.org/wiki/Automatisme'}, {'id': 12, 'name': 'Economie ,entreprenatiat et comptabilite', 'desc': ''}, {'id': 13, 'name': 'finance et analyse financiere', 'desc': 'https://fr.wikipedia.org/wiki/Finance'}, {'id': 14, 'name': 'Mecanique des fluides', 'desc': 'https://fr.wikipedia.org/wiki/M%C3%A9canique_des_fluides'}, {'id': 15, 'name': 'Science des materiaux', 'desc': 'https://fr.wikipedia.org/wiki/Science_des_mat%C3%A9riaux'}, {'id': 16, 'name': 'Energie renouvlable', 'desc': 'https://fr.wikipedia.org/wiki/%C3%89nergie_renouvelable'}, {'id': 17, 'name': 'Droit et gestion des ressources Humaines', 'desc': ''}, {'id': 18, 'name': 'Conception 3D', 'desc': ''}, {'id': 19, 'name': 'Analyse des donnees', 'desc': 'https://fr.wikipedia.org/wiki/Analyse_des_donn%C3%A9es'}, {'id': 20, 'name': 'Gestion de production et de la maintenance', 'desc': 'https://fr.wikipedia.org/wiki/Gestion_de_la_production'}, {'id': 21, 'name': 'Marketing', 'desc': 'https://fr.wikipedia.org/wiki/Marketing'}, {'id': 22, 'name': 'Intelegence Artificielle', 'desc': 'https://fr.wikipedia.org/wiki/Intelligence_artificielle'}, {'id': 23, 'name': 'Logistique', 'desc': 'https://fr.wikipedia.org/wiki/Logistique'}, {'id': 24, 'name': 'Ginie Logiciel', 'desc': 'https://fr.wikipedia.org/wiki/G%C3%A9nie_logiciel'}, {'id': 25, 'name': 'Reseau et Telecoms', 'desc': 'https://fr.wikipedia.org/wiki/R%C3%A9seau_de_t%C3%A9l%C3%A9communications'}, {'id': 26, 'name': 'Cloud Computing', 'desc': 'https://en.wikipedia.org/wiki/Cloud_computing'}, {'id': 27, 'name': 'Big data', 'desc': 'https://fr.wikipedia.org/wiki/Big_data'}, {'id': 28, 'name': 'Data science', 'desc': 'https://fr.wikipedia.org/wiki/Science_des_donn%C3%A9es'}, {'id': 29, 'name': 'Mecanique Appliquee', 'desc': ''}, {'id': 30, 'name': 'Robotique', 'desc': 'https://fr.wikipedia.org/wiki/Robotique'}, {'id': 31, 'name': 'Geologie', 'desc': ''}, {'id': 32, 'name': 'Hydraulogie et hydraulique', 'desc': 'https://fr.wikipedia.org/wiki/Hydrologie'}, {'id': 33, 'name': 'Topographie', 'desc': 'https://fr.wikipedia.org/wiki/Topographie'}, {'id': 34, 'name': 'Architicture', 'desc': 'https://fr.wikipedia.org/wiki/Architecture'}, {'id': 35, 'name': 'Geophysique', 'desc': 'https://fr.wikipedia.org/wiki/G%C3%A9ophysique'}, {'id': 36, 'name': 'Signal', 'desc': 'https://fr.wikipedia.org/wiki/Signal_%C3%A9lectrique'}, {'id': 37, 'name': "systemes d'exploitation", 'desc': 'https://fr.wikipedia.org/wiki/Syst%C3%A8me_d%27exploitation'}, {'id': 38, 'name': 'systemes embarques', 'desc': 'https://fr.wikipedia.org/wiki/Syst%C3%A8me_embarqu%C3%A9'}, {'id': 39, 'name': 'protection numerique', 'desc': ''}]


# id = 1
# for module in all_subjects:
#     modules[id-1]["id"]=id
#     id+=1

# print(modules)
# fill = list(branches.keys())

# for module in all_subjects:
#     print(module)
#     for f in fill:
#         coef = input(f+' :')
#         if coef=='s':
#             print(branches)
#         if coef == '':
#             coef =0
#         branches[f][module]=coef

# print(branches)


# branches_2 = {}

# for f in list(branches.keys()):
#     branches_2[f]={}
#     for m in list(branches[f].keys()):
#         for mo in modules:
#             if mo["name"]== m:
#                 branches_2[f][mo["id"]]=branches[f][m]

# print(branches_2)
