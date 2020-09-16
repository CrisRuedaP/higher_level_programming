#!/usr/bin/node
const args = process.argv;
const splitted = args.splice(2);

function secondLargest (arr) {
  const sorted = arr.sort(function (a, b) {
    return a - b;
  });
  sorted.pop();
  const length = sorted.length;
  if (length > 1) {
    const result = Number(sorted.pop());
    return result;
  } else {
    return 0;
  }
}

console.log(secondLargest(splitted));
