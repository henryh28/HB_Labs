'use strict';

// PART 1: SHOW A FORTUNE
async function showFortune(evt) {
  const response = await fetch('/fortune');
  const fortune = await response.text();
  document.querySelector("#fortune-text").innerHTML = fortune;
}
document.querySelector('#get-fortune-button').addEventListener('click', showFortune);

// PART 2: SHOW WEATHER
async function showWeather(evt) {
  evt.preventDefault();
  const url = '/weather.json';
  const zipcode = document.querySelector('#zipcode-field').value;

  const response = await fetch(`${url}?zipcode=${zipcode}`)
  const weatherInfo = await response.json()
  document.querySelector("#weather-info").innerText = weatherInfo.forecast;
}
document.querySelector('#weather-form').addEventListener('submit', showWeather);

// PART 3: ORDER MELONS
async function orderMelons(evt) {
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

//  const melonData = await (await fetch('/order-melons.json', requestOptions)).json()
  const response = await fetch('/order-melons.json', requestOptions)
  const melonData = await response.json()

  if (melonData.code == 'OK') {
    document.querySelector('#order-status').classList.remove('order-error');
    document.querySelector('#order-status').innerHTML = `<p>${melonData.msg}</p>`;
  } else {
    document.querySelector('#order-status').classList.add('order-error');
    document.querySelector('#order-status').innerHTML = `<p><b>${melonData.msg}</b></p>`;    
  }
}

document.querySelector('#order-form').addEventListener('submit', orderMelons);
// Reference: https://jasonwatmore.com/post/2021/09/05/fetch-http-post-request-examples
// https://stackoverflow.com/a/64165114


function displayPuppy(dogData) {
  if (dogData.status == "success") {
    document.querySelector("#dog-image").insertAdjacentHTML("beforebegin", `<img src=${dogData.message} alt="woof"></img>`)
  } else {
    console.log ("Implement error handling here")
  }
}

async function getDog () {
  const url = "https://dog.ceo/api/breeds/image/random"
  const response = await fetch(url)
  const puppyData = await response.json()

  if (puppyData.status == "success") {
    document.querySelector("#dog-image").insertAdjacentHTML("beforebegin", `<img src=${puppyData.message} alt="woof"></img>`)
  } else {
    console.log ("Implement error handling here")
  }
}

document.querySelector('#get-dog-image').addEventListener('click', getDog);



