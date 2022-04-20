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

  // TODO: show the result message after your form
  // TODO: if the result code is ERROR, make it show up in red (see our CSS!)
}
document.querySelector('#order-form').addEventListener('submit', orderMelons);
