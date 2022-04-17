'use strict';

function wordsInCommon(words1, words2) {
  const answer = new Set;
  
  words1.forEach(word => {
    if (words2.includes(word)) { answer.add(word) };
  })

  return Array.from(answer)
}


function kidsGame(names) {
  // Replace this with your code
}
