'use strict';

const express = require('express');
const bodyParser = require('body-parser');
const app = express();

app.use(bodyParser.json());
app.use('/assets', express.static('assets'));

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});

app.get('/doubling', (req, res) => {
    let resObj = {};
    if(req.query.input === undefined){
        resObj.error = 'Please provide an input!';
    } else {
        resObj.received = req.query.input;
        resObj.result = req.query.input * 2;
    }
    res.send(res.json(resObj));
});

app.get('/greeter', (req, res) => {
    let resObj = {};
    if(req.query.name === undefined){
        resObj.error = 'Please provide a name!';
    } else if (req.query.title === undefined) {
        resObj.error = 'Please provide a title!';
    } 
    else {
        resObj.welcome_message = `Oh, hi there ${req.query.name}, my dear ${req.query.title}!`;
    }
    res.send(res.json(resObj));
});

app.get('/appenda/:appendable', (req, res) => {
    let resObj = {};
    resObj.appended = req.params.appendable + 'a';
    res.send(res.json(resObj));
});

app.get('/appenda', (req, res) => {
    res.status(404);
    res.send();
});

app.post('/dountil/:action', (req, res) => {
    let resObj = {};

    let n = req.body.until;
    if (req.params.action === 'sum') {
        resObj.result = n * (n + 1) / 2;
    } else if (req.params.action === 'factor') {
        resObj.result = 1;
        for(let i = 1; i <= n; i++) {
            resObj.result *= i;
        }
    }
    res.send(res.json(resObj));
});

app.listen(8080);

