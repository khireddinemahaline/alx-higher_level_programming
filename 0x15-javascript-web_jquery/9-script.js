$(function () {
  const $value = $('DIV#hello');
  $.ajax({
    type: 'GET',
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    success: function (data) {
      $value.text(data.hello);
    }
  });
});
