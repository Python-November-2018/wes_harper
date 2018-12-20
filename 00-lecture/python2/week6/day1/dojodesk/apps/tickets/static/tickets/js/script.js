$(document).ready(function() {
  $('#new-form').submit(function(e) {
    e.preventDefault();
    // console.log($('#new-form').serialize());
    $.ajax({
      url: "/ajax_create/",
      method: 'POST',
      data: $('#new-form').serialize(),
      success: function(data) {
        console.log('this was successful');
        console.log(data[0].fields);
        $('.errors').html('<h1>' + data[0].fields.title + '</h1>');
      },
      error: function(data) {
        var errors = data.responseJSON;
        var htmlString = '<ul>';
        for(var i = 0; i < errors.length; i++) {
          console.log(errors[i]);
          htmlString += "<li class='red'>"
          htmlString += errors[i];
          htmlString += '</li>';
        }
        htmlString += "</ul>"
        $('.errors').html(htmlString);
      }
    });
  });
});