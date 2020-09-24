const $ = window.$;
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for (const movie in data.results) {
    $('ul#list_movies').append(`<li>${data.results[movie].title}</li>`);
  }
});
