#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
const sToWrite = process.argv[3];
fs.writeFile(filePath, sToWrite, { encoding: 'utf-8' }, function (err, data) {
  if (err) {
    console.log(err);
  }
});
