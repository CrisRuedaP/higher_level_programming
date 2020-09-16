#!/usr/bin/node
const args = process.argv;

args.shift();
args.shift();
const splitted = args;

function secondLargest (arr) {
  const sorted = arr.sort(function (a, b) {
    return a - b;
  });
  sorted.pop();
  const length = sorted.length;
  if (length > 1) {
    const result = Number(sorted.pop());
    console.log(result);
  } else {
    console.log(0);
  }
}

secondLargest(splitted);
