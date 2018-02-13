'use strict';

const mysql = require('mysql');
const express = require('express');
// const bodyParser = require('body-parser');

const connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '12345',
    database: 'redditdb'
});

// connection.connect(function(err){ //?
//     if(err){
//       console.log("Error connecting to Db!");
//       return;
//     }
//     console.log("Connection established !");
// });

const app = express();

app.use(express.json());
app.use(express.static('webpage'));

// app.use('/', express.static('webpage'));

// app.get('/', function (req, res) {
//     res.sendFile(__dirname + '/webpage/index.html');
// });

// sample posts - created

// let post1 = `INSERT INTO posts (title, url, timestamp, score)
//              VALUES ("Green Fox Academy webpage",
//              "https://www.greenfoxacademy.com",
//              ${Date.now()},
//              0);`

// let post2 = `INSERT INTO posts (title, url, timestamp, score)
// VALUES ("How the original looks like",
// "https://www.reddit.com/r/space/",
// ${Date.now()},
// 0);`


// function doQuery(query){
//     let dataFromDB;
//     connection.connect(function(err){
//         if(err) {
//             console.log("Error connecting to Db");
//             return;
//         }
//         console.log('ROWS   ???????????????     \n' + connection.query(query, logger));
//         console.log("Connection established");
        
//     });

//     function logger(err, rows) {
//         if (err) {
//             console.log('valami rossz');
//             return;
//         }
//         console.log("Data received from Db:\n");
//         console.log(rows);
//         dataFromDB = rows;
//     }
//     console.log(dataFromDB);
//     return dataFromDB;
// }


app.get('/posts', (req, res) => {
    // let resObj = {};
    // let posts = [];
    connection.query('SELECT * FROM posts;', (err, rows) => {
        if (err) {
            console.log('GET query valami rossz');
            return;
        }
        res.status(200);
        res.json(rows);
        // console.log('GET rows\n', rows);
        // rows.forEach(row => {
        //     let post = {};
        //     post.id = row.id;
        //     post.title = row.title;
        //     post.url = row.url;
        //     post.timestamp = row.timestamp;
        //     post.score = row.score;
        //     post.owner = row.owner;
        //     posts.push(post);
        // });
        // resObj.posts = posts;
        // console.log(resObj);
        // res.json(resObj);
        // res.send();
        // res.end();
    });
    // connection.end();
});

app.put('/posts/:id/:vote', (req, res) => {
    console.log('vote beckend ')
    let id = req.params.id;
    let vote = req.params.vote;
    let query = `UPDATE posts SET score = score ${vote === 'upvote' ? '+ 1' : '- 1'} WHERE id = ${connection.escape(id)};`; 

    let resObj = {};
    let posts = [];

    connection.query(query, (err, rows) => {
        if (err) {
            console.log('PUT query valami rossz');
            return;
        }
    });
    connection.query(`SELECT * FROM posts WHERE id = ${connection.escape(id)};`, (err, row) => { // query a querybe !!!!!!
        console.log('vote select', row);
        // rows.forEach(row => {
        //     let post = {};
        //     post.id = row.id;
        //     post.title = row.title;
        //     post.url = row.url;
        //     post.timestamp = row.timestamp;
        //     post.score = row.score;
        //     post.owner = row.owner;
        //     posts.push(post);
        // });
        // resObj.posts = posts;
        // console.log(resObj);
        res.status(200);
        res.json(row);
        // res.send();
    });
});

app.post('/posts', (req, res) => {
    // console.log('new post - req:\n', req);
    // console.log('new post - res:\n', res);
    console.log( (req.body));
});

app.listen(3000);
//website.com/articles?id=1
//website.com/articles?id=1; drop table articles; 
// leads to drop the table values

// let id = '1';

//                                             // ...= ?' + id -> auto escape          
// connection.query('select * from articles where id = ' + connection.escape(id), function(err, result){
//     console.log(result);
// });

// connection.end();