'use strict';

// 1. countWords
function countWords(phrase) {
  const word_count = new Object;

  phrase.split(' ').forEach( word => word_count[word] = word_count[word] + 1 || 1)

  return word_count;
}

// 2. getMelonsAtPrice
function getMelonsAtPrice(price) {

  melon_prices = {
    2.50: ['Cantaloupe', 'Honeydew'],
    2.95: ['Watermelon'],
    3.25: ['Musk', 'Crenshaw'],
    14.25: ['Christmas']
  }

  return price in melon_prices ? melon_prices[price] : "None"
}

