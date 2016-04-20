function runPython(){
    var url = 'http://localhost:5000/api/run';
    var req = new XMLHttpRequest();
    req.open('POST', url, true)
    req.onload = function(){
        if (req.status >= 200 && req.status < 400){
            var terminal = JSON.parse(req.responseText);
            console.log(terminal);
            document.getElementById('terminal').innerHTML= terminal.text;
        }
    }
    req.onerror = function(){
        console.log('there was an error');
    }
    req.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');
    var text = document.getElementById('textarea1').value;
    req.send(text);
};

document.getElementById('submit').addEventListener('click', runPython);