var visible = false;




var fullname= document.getElementById("fullname");
fullname.addEventListener('keypress',function(event){
    if (event.key=='Enter'){
        getstarted(fullname.value,'spinner')
    }
})

function getstarted(name,id){
    if (name==""){
        window.alert("Please enter your full name")
    }else{
        showspinner(id)
        var req = new XMLHttpRequest();
        req.onload = function(){
            document.getElementById("ratingboard").innerHTML = this.responseText;
            showspinner(id)
        }
        req.open("POST","/modules",true)
        req.setRequestHeader('Content-Type','application/json')
        req.send(JSON.stringify({
            fullname:document.getElementById('fullname').value,
        }))
    }
}

function nextinp(event,id){
    if(event.key=='Enter'){
        if(parseInt(id)<=38){
            jd=parseInt(id)+1;
            document.getElementById(jd+"rating").focus()
        }
    }
}

function submitinfo(){
    var context = {}
    for(id=1;id<=39;id++){
        context[id] = document.getElementById(id+'rating').value;
    }
    var req = new XMLHttpRequest();
    req.onload = function(){
        // document.getElementById('sublist').remove();
        document.getElementById("ratingboard").innerHTML = this.responseText;
    }
    req.open("POST","/branchlist",true)
    req.setRequestHeader('Content-Type','application/json')
    req.send(JSON.stringify({
        fullname:document.getElementById("fullname").value,
        ratings:context
    }));
}


function contactme(){
    var req = new XMLHttpRequest();
    req.onload = function(){
        document.getElementById('body').innerHTML += this.responseText;
    }
    req.open('POST','/contactme')
    req.send()
}

function sendmessage(id){
    showspinner(id)
    var req = new XMLHttpRequest();
    req.onload = function(){
        showspinner(id)
        document.getElementById('bghider').remove();
    }
    req.open("POST","/sendtelemessage",true)
    req.setRequestHeader('Content-Type','application/json')
    req.send(JSON.stringify({
        name:document.getElementById("name").value,
        phonenumber:document.getElementById('phonenumber').value,
        message:document.getElementById('message').value,
    }));
}
function showspinner(id){
    if(visible){
        document.getElementById(id).style.visibility = 'hidden';
        visible=false;
    }else{
        document.getElementById(id).style.visibility = 'visible';
        visible = true;
    }
}