'use strict';

const express = require('express');
const bodyParser = require('body-parser');
const app = express();

app.use(bodyParser.json());

app.post('/arrays', (req, res) => {
    let resObj = {};
    if (req.body.what === undefined || req.body.numbers === undefined) {
        resObj.error = 'Please provide what to do with the numbers!';
    } else {
        if (req.body.what === 'sum') {
            resObj.result = req.body.numbers.reduce((acc, val) => acc + val);
        } else if (req.body.what === 'multiply') {
            resObj.result = req.body.numbers.reduce((acc, val) => acc * val);
        } else if (req.body.what === 'double') {
            resObj.result = req.body.numbers.map((val) => 2 *val);
        }
    }
    res.send(res.json(resObj));
});

function randInt(max) {
    return Math.floor(Math.random() * Math.floor(max));
}

app.post('/sith', (req, res) => {
    let resObj = {};
    let text = req.body.text;    
    if(text === undefined || text === '' || typeof text !== 'string'){
        resObj.error = 'Feed me some text you have to, padawan young you are. Hmmm.';
    } else {
        let text = req.body.text.toLowerCase();
        text = text.split('.')
                .filter(sentence => sentence !== '')
                .map(sentence => sentence.trim())
                .map(sentence => sentence.split(' '));
        text = text.map(sentence => {
            for(let i = 0; i < sentence.length - 2; i += 2){
                [sentence[i], sentence[i+1]] = [sentence[i+1], sentence[i]];
            }
            let word = sentence[0].split('');
            word[0] = word[0].toUpperCase();
            sentence[0] = word.join('');
            sentence = sentence.join(' ').concat('.');
            let blah = [' Arrgh.', ' Uhm.', ' Err..Err.er.'];
            for(let i = 0; i <= randInt(2); i++){
                sentence = sentence.concat(blah[randInt(3)]);
            }
            return sentence;
        });
        resObj.sith_text = text.join(' ');
    }
    res.json(resObj);
    res.send();
});

app.listen(8080);