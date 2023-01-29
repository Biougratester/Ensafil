from flask import Flask, render_template, url_for, request, session, redirect
import json
import os
import requests










#when the user clicks on contact me and sends to the server, this function reseavs the message and sends it to me on telegram.
def telegram_bot_sendtext(bot_message="you have a new visiter."):
    bot_token = 'TELEGRAM_BOT_TOKEN'
    bot_chatID = 'YOUR_CHAT_ID'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    requests.get(send_text)

    
#this function connects me with database.json where the data is at.
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




#these data structurs can be found in data.json file.
modules = [{'id': 1, 'name': 'Mathematique', 'desc': ''}, 
{'id': 2, 'name': 'Algorithmique et resoulution des problemes', 'desc': ''}, 
{'id': 3, 'name': 'Chimie', 'desc': ''}, {'id': 4, 'name': 'Statistique ,Stochastiques et probabilites', 'desc': 'https://fr.wikipedia.org/wiki/Processus_stochastique'}, {'id': 5, 'name': 'Biologie', 'desc': ''}, {'id': 6, 'name': 'Thermo-dynamique', 'desc': ''}, {'id': 7, 'name': 'Mecanique Generale', 'desc': ''}, {'id': 8, 'name': 'Bases des donnees et langages de programmation', 'desc': ''}, {'id': 9, 'name': 'Electronique et Electrotechnique', 'desc': 'https://fr.wikipedia.org/wiki/%C3%89lectrotechnique'}, {'id': 10, 'name': 'Optimisation', 'desc': 'https://fr.wikipedia.org/wiki/Optimisation_(math%C3%A9matiques)'}, {'id': 11, 'name': "Automatisme et science d'automatisation", 'desc': 'https://fr.wikipedia.org/wiki/Automatisme'}, {'id': 12, 'name': 'Economie ,entreprenatiat et comptabilite', 'desc': ''}, {'id': 13, 'name': 'finance et analyse financiere', 'desc': 'https://fr.wikipedia.org/wiki/Finance'}, {'id': 14, 'name': 'Mecanique des fluides', 'desc': 'https://fr.wikipedia.org/wiki/M%C3%A9canique_des_fluides'}, {'id': 15, 'name': 'Science des materiaux', 'desc': 'https://fr.wikipedia.org/wiki/Science_des_mat%C3%A9riaux'}, {'id': 16, 'name': 'Energie renouvlable', 'desc': 'https://fr.wikipedia.org/wiki/%C3%89nergie_renouvelable'}, {'id': 17, 'name': 'Droit et gestion des ressources Humaines', 'desc': ''}, {'id': 18, 'name': 'Conception 3D', 'desc': ''}, {'id': 19, 'name': 'Analyse des donnees', 'desc': 'https://fr.wikipedia.org/wiki/Analyse_des_donn%C3%A9es'}, {'id': 20, 'name': 'Gestion de production et de la maintenance', 'desc': 'https://fr.wikipedia.org/wiki/Gestion_de_la_production'}, {'id': 21, 'name': 'Marketing', 'desc': 'https://fr.wikipedia.org/wiki/Marketing'}, {'id': 22, 'name': 'Intelegence Artificielle', 'desc': 'https://fr.wikipedia.org/wiki/Intelligence_artificielle'}, {'id': 23, 'name': 'Logistique', 'desc': 'https://fr.wikipedia.org/wiki/Logistique'}, {'id': 24, 'name': 'Ginie Logiciel', 'desc': 'https://fr.wikipedia.org/wiki/G%C3%A9nie_logiciel'}, {'id': 25, 'name': 'Reseau et Telecoms', 'desc': 'https://fr.wikipedia.org/wiki/R%C3%A9seau_de_t%C3%A9l%C3%A9communications'}, {'id': 26, 'name': 'Cloud Computing', 'desc': 'https://en.wikipedia.org/wiki/Cloud_computing'}, {'id': 27, 'name': 'Big data', 'desc': 'https://fr.wikipedia.org/wiki/Big_data'}, {'id': 28, 'name': 'Data science', 'desc': 'https://fr.wikipedia.org/wiki/Science_des_donn%C3%A9es'}, {'id': 29, 'name': 'Mecanique Appliquee', 'desc': ''}, {'id': 30, 'name': 'Robotique', 'desc': 'https://fr.wikipedia.org/wiki/Robotique'}, {'id': 31, 'name': 'Geologie', 'desc': ''}, {'id': 32, 'name': 'Hydraulogie et hydraulique', 'desc': 'https://fr.wikipedia.org/wiki/Hydrologie'}, {'id': 33, 'name': 'Topographie', 'desc': 'https://fr.wikipedia.org/wiki/Topographie'}, {'id': 34, 'name': 'Architicture', 'desc': 'https://fr.wikipedia.org/wiki/Architecture'}, {'id': 35, 'name': 'Geophysique', 'desc': 'https://fr.wikipedia.org/wiki/G%C3%A9ophysique'}, {'id': 36, 'name': 'Signal', 'desc': 'https://fr.wikipedia.org/wiki/Signal_%C3%A9lectrique'}, {'id': 37, 'name': "systemes d'exploitation", 'desc': 'https://fr.wikipedia.org/wiki/Syst%C3%A8me_d%27exploitation'}, {'id': 38, 'name': 'systemes embarques', 'desc': 'https://fr.wikipedia.org/wiki/Syst%C3%A8me_embarqu%C3%A9'}, {'id': 39, 'name': 'protection numerique', 'desc': ''}]

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
app.config["SECRET_KEY"] = "session encryption key"



@app.route('/')
def home():
    return render_template('home.html',session=session)

@app.route('/modules',methods=['GET','POST'])
def subjects():
    session["fullname"] = request.json["fullname"] 
    if request.method == "POST":
        if request.json['fullname']:
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
        #the hex code bellow represents list item colors, unfortunatly it did not look good on the website
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
    #put debuging to False on the production phase.
    app.run(debug=True)
