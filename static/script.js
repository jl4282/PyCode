function runPython(){
    var url = 'http://localhost:5000/api/run';
    var req = new XMLHttpRequest();
    req.open('POST', url, true);
    req.onload = function(){
        if (req.status >= 200 && req.status < 400){
            var terminal = JSON.parse(req.responseText);
            console.log(terminal);
            document.getElementById('terminal').innerHTML= terminal.text;
        }
        document.getElementById('submit').classList.toggle('invisible');
        document.getElementById('spinner').classList.toggle('invisible');
    }
    req.onerror = function(){
        console.log('there was an error');
        document.getElementById('submit').classList.toggle('invisible');
        document.getElementById('spinner').classList.toggle('invisible');
    }
//    content type can also just be json
//  req.send("text=" + text + "&modules=" + modules)
    req.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');
    var text = document.getElementById('textarea1').value;
    var modules = document.getElementById('modulesText').value;
    console.log(text, encodeURIComponent(text));
      req.send("text=" + encodeURIComponent(text) + "&modules=" + modules + "&path=" + window.location.pathname);
//    JSON.stringify({text:text, modules: modules});
//    req.send(JSON.stringify({text:encodeURIComponent(text), modules:encodeURIComponent(modules)}));
    document.getElementById('submit').classList.toggle('invisible');
    document.getElementById('spinner').classList.toggle('invisible');
};

document.getElementById('submit').addEventListener('click', runPython);

function getStats(){
    var url = 'http://localhost:5000/api/stats';
    var req = new XMLHttpRequest();
    req.open('GET', url, true);
    req.onload = function(){
        console.log('loaded');
        var text = '';
        if (req.status >= 200 && req.status < 400){
            var userStats = JSON.parse(req.responseText);
            console.log(userStats);
            for (var i in userStats.programs){
                var p = userStats.programs[i];
                text += '\nCode:\n' +  p.code;
                text += '\nModules:\n' +  p.modules;
                text += '\nResult:\n' +  p.result;
            }
            if (userStats.modules){
                text += '\nModules Count (only if there are modules): \n';
            }

            for (var k in userStats.modules){
                text += k + ': ' + userStats.modules[k] + '\n';
            }
            document.getElementById('userStats').innerHTML= text;
        }
    }
    req.onerror = function(){
        console.log('there was an error');
    }
    req.send();
}

document.getElementById('goStats').addEventListener('click', getStats);