'use strict';

function wordsInCommon(words1, words2) {
  const answer = new Set;
  
  words1.forEach(word => {
    if (words2.includes(word)) { answer.add(word) };
  })

  return Array.from(answer)
}


function kids_game(words) {

  if (words.length == 0) {
    return 0;
  }
  
  const answer = [words.shift()];
  const words_starting_with_letter = {}

  words.forEach(word => {
    word[0] in words_starting_with_letter ? words_starting_with_letter[word[0]].push(word) : words_starting_with_letter[word[0]] = [word]
  })

  while (true) {
    let starting_letter = answer[answer.length-1].slice(-1)
    
    if (starting_letter in words_starting_with_letter) {
      if (words_starting_with_letter[starting_letter].length == 0) {
        return answer
      }
      answer.push(words_starting_with_letter[starting_letter].shift());
    } else {
      return (answer);
    }
  }  
}
