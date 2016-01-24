"use strict";
let async = require('async')
  , express = require('express')
  , fs = require('fs')
  , path = require('path')
  , process = require('process')
  ;

let list_files = function(source_dir, cb)
{
  console.log("Reading", source_dir);
  fs.readdir(source_dir, function(err, files) {
    if (err)
    {
      console.log(err, files);
    }
    let filtered = files
      .filter((file) => file.substr(-5) === '.json')
    cb(null, filtered);
  });
}


let get_data = function(source_dir, cb)
{
  list_files(source_dir, (err, files) =>
  {
    console.log("Got files", err, files);
    async.map(
      files,
      (file, cb) => fs.readFile(path.join(source_dir, file), 'utf-8', cb),
      (err, files) =>
      {
        cb(err, files); 
      }
    );
  });
}

const source = process.argv[process.argv.length-1];

var app = express();
app.get('/', express.static('site'));

app.get('/data', function (req, res) {

  console.log("Getting data");
  get_data(source, (err, data) => {
    res.send(JSON.stringify(data));
    console.log("Sent requested files");
  });
});

var server = app.listen(3000, function () {
  var host = server.address().address;
  var port = server.address().port;

  console.log('Running with ${source}');
  console.log('Temperature server listening at http://%s:%s', host, port);
});
