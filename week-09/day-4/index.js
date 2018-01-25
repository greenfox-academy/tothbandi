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

app.listen(8080);

