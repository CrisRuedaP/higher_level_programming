#!/usr/bin/node
const PathfileA = process.argv[1];
const PathfileB = process.argv[2];
const destination = process.argv[3];
const fs = require('fs');
const first = fs.readFileSync(PathfileA);
const second = fs.readFileSync(PathfileB);
fs.writeFileSync(destination, first + second);
