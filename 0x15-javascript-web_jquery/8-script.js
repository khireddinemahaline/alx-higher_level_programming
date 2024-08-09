$(function () {
  const $list = $('UL#list_movies');
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function (data) {
      const movies = data.results;
      movies.forEach(movie => {
        const $item = $('<li>' + movie.title + '</li>');
        $list.append($item);
      });
    }
  });
});
