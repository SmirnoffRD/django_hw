window.onload = function () {
  
  
  $('.basket_list').on('change', 'input[type="number"]', function(event) {
    var target_href = event.target;

    if (target_href) {
      $.ajax({
        url: "/basket/edit/" + target_href.name + "/" + target_href.value + "/",

        success: function(data) {
          $('.basket_list').html(data.result);
          console.log('ajax done');
        },
      });
    }
    event.preventDefault();
  });

  var csrftoken = getCookie('csrftoken');

  $('.basket_list').on('click', 'button[type="submit"]', function(event) {
    var targetForm = event.target;
    console.log('nen')
    console.log(targetForm.name)
    if (targetForm) {
      $.ajax({
        url: "/basket/delete_all/",
        method: "POST",
        data: {"pk": targetForm.name, 'csrfmiddlewaretoken': csrftoken},
        success: function(data) {
          $('.basket_list').html(data.result);
          console.log('ajax done');
        },
      });
    }
    event.preventDefault();
  });

}

// using jQuery
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie != '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
          var cookie = jQuery.trim(cookies[i]);
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) == (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}
var csrftoken = getCookie('csrftoken');