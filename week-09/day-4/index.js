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
    console.log('====', req.query.input);
    let resObj = {};
    if(req.query.input === undefined){
        resObj.error = "Please provide an input!";
    } else {
        resObj.received = req.query.input;
        resObj.result = req.query.input * 2;
    }
    res.send(res.json(resObj));
});

app.listen(8080);

