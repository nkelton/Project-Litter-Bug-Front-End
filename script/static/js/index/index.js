$(document).ready(function(){
    contentData["vidCount"] = contentData["vid"].length;
    contentData["gifCount"] = contentData["gif"].length;
    contentData["picCount"] = contentData["pic"].length;
    contentData["sfxCount"] = contentData["sfx"].length;
    onLoad(contentData);
});

function onLoad(contentData) {
    var name ="";
    var i;

    updateIFrame(contentData["life_stats"].embedded_url);
    updateProgressBar(contentData["download"]);
    updateLifeStats(contentData["life_stats"]);
    updateStatus(contentData["status"]);

    for(i = 0; i < contentData["vid"].length; i++) {
        name = "Vid "+(i+1);
        addContent(name, contentData["vid"][i], "vid-lst");
    }

    for(i = 0; i < contentData["gif"].length; i++) {
        name = "Gif "+(i+1);
        addContent(name, contentData["gif"][i], "gif-lst");
    }

    for(i = 0; i < contentData["pic"].length; i++) {
        name = "Pic "+(i+1);
        addContent(name, contentData["pic"][i], "pic-lst");
    }

    for(i = 0; i < contentData["sfx"].length; i++) {
        name = "Sfx "+(i+1);
        addContent(name, contentData["sfx"][i], "sfx-lst");
    }
}

function updateProgressBar(download) {
    var bar = document.getElementById("progress-bar");
    var num = document.getElementById("progress-num");
    bar.style.width = download + "%";
    num.innerHTML = download;
}

function updateStatus(newStatus) {
    var h = document.getElementById("status-head");
    h.innerHTML = newStatus;
}

function addContent(name, url, typeId) {
    var ul = document.getElementById(typeId);
    var li = document.createElement('li');
    a = document.createElement('a');
    a.href = url;
    a.innerHTML = name;
    li.appendChild(a);
    ul.appendChild(li);
}

function updateIFrame(url) {
    var frame = document.getElementById("video-frame");
    frame.src = url;
}

function updateLifeStats(lifeStats) {
    document.getElementById("bytes-generated-num").innerHTML = lifeStats.total_weight;
    document.getElementById("energy-used-num").innerHTML = lifeStats.total_energy;
    document.getElementById("litter-emissions").innerHTML = lifeStats.total_emissions;
    document.getElementById("cost-used-num").innerHTML = lifeStats.total_cost;
    document.getElementById("litter-generated-num").innerHTML = lifeStats.total_litter;
}

function removeElements(root) {
    while( root.firstChild ){
        root.removeChild(root.firstChild);
    }
}

function clearContent() {
    var vidRoot = document.getElementById("vid-lst");
    var gifRoot = document.getElementById("gif-lst");
    var picRoot = document.getElementById("pic-lst");
    var sfxRoot = document.getElementById("sfx-lst");

    removeElements(vidRoot);
    removeElements(gifRoot);
    removeElements(picRoot);
    removeElements(sfxRoot);

    contentData["vid"] = [];
    contentData["gif"] = [];
    contentData["pic"] = [];
    contentData["sfx"] = [];

    contentData["vidCount"] = 0;
    contentData["gifCount"] = 0;
    contentData["picCount"] = 0;
    contentData["sfxCount"] = 0;
}
