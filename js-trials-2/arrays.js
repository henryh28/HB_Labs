'use strict';

// 1. printIndices
function printIndices(items) {
  for (const i in items) {
    console.log(i);
  }
}

// 2. everyOtherItem
function everyOtherItem(items) {
  const answer = []
  for (const i in items) {
    if (i % 2 == 0) { answer.push(items[i])}  
  }
  
  console.log(answer)
}

// 3. smallestNItems
function smallestNItems(items, n) {
  items.sort((a,b) => a-b);
  const answer = items.slice(0, n);

  console.log(answer);
}