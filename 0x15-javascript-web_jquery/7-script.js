const $ = window.$;
$.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  var nme = `${data.name}`;
  $('#character').text(nme);
});
