const ALPHABET = 'abcdefghijklmnopqrstuvwxyz';

const WORDS = [
  'strawberry',
  'orange',
  'apple',
  'banana',
  'pineapple',
  'kiwi',
  'peach',
  'pecan',
  'eggplant',
  'durian',
  'peanut',
  'chocolate',
];

let numWrong = 0;

// Loop over the chars in `word` and create divs.
// The divs should be appended to the section with id="word-container".
const createDivsForChars = (word) => {
  for (const char of word) {
    const container=document.querySelector('#word-container');
    container.insertAdjacentHTML("beforeend", `<div class="letter-box ${char}"></div>`);
  }

};

// Loop over each letter in the alphabet and generate a button for each letter
// The buttons should be appended to the section with id="letter-buttons"
const generateLetterButtons = () => {
  const buttons=document.querySelector("#letter-buttons")
  
  for (const char of ALPHABET) {
    buttons.insertAdjacentHTML("beforeend", `<button>${char}</button>`);
  }
};

// Set the `disabled` property of `buttonEl` to `true.
//
// `buttonEl` is an `HTMLElement` object.
//
const disableLetterButton = (buttonEl) => {
  buttonEl.disabled=true;
};


// This is a helper function we will use in the future
// It should return `true` if `letter` is in the word
// For now, you should test it out to make sure it works

const isLetterInWord = (letter) => {
  return document.querySelector(`div.${letter}`) != null;
};


const handleCorrectGuess = (letter) => {
  let correct_guesses = 0;

  const matches=document.querySelectorAll(`div.letter-box.${letter}`);  
  for (match of matches) {
    match.insertAdjacentHTML("beforeend", `${letter}`);
    match.setAttribute("guessed", true);
  }

  const all_letter_boxes=document.querySelectorAll(`div.letter-box`);  
  for (entry of all_letter_boxes) {
    if (entry.getAttribute("guessed") != null) {
      correct_guesses += 1;
    } 

    if (correct_guesses >= all_letter_boxes.length) {   
      disableAllLetterButtons();
      document.querySelector("#win").style.display="block";
   }
  }

};



//
// Called when `letter` is not in word.
//
// Increment `numWrong` and update the shark image.
// If the shark gets the person (5 wrong guesses), disable
// all buttons and show the "play again" message.

const handleWrongGuess = () => {
  numWrong += 1;

  if (numWrong >= 5) {
    disableAllLetterButtons();
    document.querySelector("#play-again").style.display="block";
  }

  document.querySelector("#shark-img img").setAttribute("src", `/static/images/guess${numWrong}.png`)
};

const disableAllLetterButtons = () => {
  const all_buttons=document.querySelectorAll("button");
  for (button of all_buttons) {
    button.disabled=true;
  }  
}


// This is like if __name__ == '__main__' in Python
// It will be called when the file is run (because
// we call the function on line 66)
(function startGame() {
  // For now, we'll hardcode the word that the user has to guess
  // You can change this to choose a random word from WORDS once you
  // finish this lab but we hard code it so we know what the word is
  // and can tell if things look correct for this word
  const word = WORDS[Math.floor(Math.random()*WORDS.length)];


  createDivsForChars(word);
  generateLetterButtons();

  for (const button of document.querySelectorAll('button')) {
    // add an event handler to handle clicking on a letter button
    button.addEventListener('click', () => {
      button.setAttribute("disabled", true);
      isLetterInWord(button.innerText) ? handleCorrectGuess(button.innerText) : handleWrongGuess();
    })

  const reset=document.querySelector('#play-again');
  reset.addEventListener('click', () => {
      window.location="/sharkwords";      
    })

  const win=document.querySelector('#win');
  win.addEventListener('click', () => {
      window.location="/sharkwords";      
    })
  

  }

  


})();

