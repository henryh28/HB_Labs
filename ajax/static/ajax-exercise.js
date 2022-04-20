'use strict';

// PART 1: SHOW A FORTUNE
function showFortune(evt) {
  fetch('/fortune')
    .then(response => response.text())
    .then(fortune => document.querySelector("#fortune-text").innerHTML = fortune);
}
document.querySelector('#get-fortune-button').addEventListener('click', showFortune);

// PART 2: SHOW WEATHER
function showWeather(evt) {
  evt.preventDefault();
  const url = '/weather.json';
  const zipcode = document.querySelector('#zipcode-field').value;

  fetch(`${url}?zipcode=${zipcode}`)
    .then(response => response.json())
    .then(jsonData => {
      document.querySelector("#weather-info").innerText = jsonData.forecast;
    })
}
document.querySelector('#weather-form').addEventListener('submit', showWeather);

// PART 3: ORDER MELONS
function showResults(response) {
  if (response.code == 'OK') {
    document.querySelector('#order-status').classList.remove('order-error');
    document.querySelector('#order-status').innerHTML = `<p>${response.msg}</p>`;
  } else {
    document.querySelector('#order-status').classList.add('order-error');
    document.querySelector('#order-status').innerHTML = `<p><b>${response.msg}</b></p>`;    
  }
}


function orderMelons(evt) {
  evt.preventDefault();

  const formData = {
    melon_type: document.querySelector('[name=melon_type]').value,
    qty: document.querySelector('[name=qty]').value,
  };

  const requestOptions = {
    method: "POST",
    headers: { 'content-type': 'application/json' },
    body: JSON.stringify(formData)
  }
  
  fetch('/order-melons.json', requestOptions)
  .then(response => response.json())
  .then(showResults)
  

  // Reference: https://jasonwatmore.com/post/2021/09/05/fetch-http-post-request-examples
}
document.querySelector('#order-form').addEventListener('submit', orderMelons);


function displayPuppy(dogData) {
  if (dogData.status == "success") {
    document.querySelector("#dog-image").insertAdjacentHTML("beforebegin", `<img src=${dogData.message} alt="woof"></img>`)
  } else {
    console.log ("Implement error handling here")
  }
}

function getDog () {
  const url = "https://dog.ceo/api/breeds/image/random"
  fetch(url)
  .then(response => response.json())
  .then(displayPuppy)
}

document.querySelector('#get-dog-image').addEventListener('click', getDog);



