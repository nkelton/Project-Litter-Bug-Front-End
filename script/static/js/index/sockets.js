$(document).ready(function(){
    var scriptWs = new WebSocket("ws://" + window.location.host + "/script/")
    scriptWs.onmessage = function(e){handlerScriptSocket(e)};
    scriptWs.onopen = function(){configureScriptSocket(scriptWs);}

    var contentWs = new WebSocket("ws://" + window.location.host + "/content/")
    contentWs.onmessage = function(e){handlerContentSocket(e)};
    contentWs.onopen = function(){configureContentSocket(contentWs)};
});

function configureScriptSocket(scriptWs) {
    var scriptMsg = {
        stream: "script",
        payload: {
            action: "subscribe",
            pk: "1",
            data: {
                action: "update"
            }
        }
    }
    scriptWs.send(JSON.stringify(scriptMsg))
}

function handlerScriptSocket(e) {
    var obj = JSON.parse(e.data)
    var status = obj.payload.data.status
    var litter_id = obj.payload.data.litter_id
    var download = obj.payload.data.download

    if(status != null) {
        updateStatus(status)
    }

    if(litter_id != null && litter_id != contentData["litterId"]) {
        clearContent()
        aggregateDataQuery()
        contentData["litterId"] = litter_id
    }

    if(download != null) {
        updateProgressBar(download)
    }
}

function configureContentSocket(contentWs) {
    var contentMsg = {
        stream: "content",
        payload: {
            action: "subscribe",
            data: {
                action: "create"
            }
        }
    }
    contentWs.send(JSON.stringify(contentMsg))
}

function handlerContentSocket(e) {
    var obj = JSON.parse(e.data)
    var url = obj.payload.data.url
    var type = obj.payload.data.type
    var litterId = obj.payload.data.litter_id
    var typeId = ""
    var name = ""

    if(type == "vid") {
        typeId = "vid-lst"
        name = "Vid "+(contentData["vidCount"] + 1)
        contentData["vidCount"] +=1
        contentData["vid"].push(obj)
    }

    else if(type == "gif") {
        typeId = "gif-lst"
        name = "Gif "+(contentData["gifCount"] + 1)
        contentData["gifCount"] +=1
        contentData["gif"].push(obj)
    }

    else if(type == "pic") {
        typeId = "pic-lst"
        name = "Pic "+(contentData["picCount"] + 1)
        contentData["picCount"] +=1
        contentData["pic"].push(obj)
    }

    else if(type == "sfx") {
        typeId = "sfx-lst"
        name = "Sfx "+(contentData["sfxCount"] + 1)
        contentData["sfxCount"] +=1
        contentData["sfx"].push(obj)
    }

    if(type != null && name != null && url != null && typeId != null && litterId == contentData["litterId"]) {
        addContent(name, url, typeId)
    }
}
