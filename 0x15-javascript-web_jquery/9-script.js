const $ = window.$;
$.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
  var hi = `${data.hello}`;
  $('#hello').text(hi);
});
