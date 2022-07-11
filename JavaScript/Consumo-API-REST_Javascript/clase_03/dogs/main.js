console.log('Hello, world')

const URL = 'https://api.thedogapi.com/v1/images/search';

async function getDog() {
  const response = await fetch(URL);
  const data = await response.json();
  const img = document.querySelector('img');
  img.src = data[0].url;
}

const input = document.querySelector('input');
input.onclick = getDog;