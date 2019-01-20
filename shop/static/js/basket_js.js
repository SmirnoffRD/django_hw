window.onload = function () {
  
  
  $('.basket_list').on('click', 'input[type="number"]', function(event) {
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

  $('.basket_list').on('click', 'button[type="submit"]', function(event) {
    var targetForm = event.target;
    if (targetForm) {
      $.ajax({
        url: "/basket/delete_all/" + targetForm.name + "/",
        success: function(data) {
          $('.basket_list').html(data.result);
          console.log('ajax done');
        },
      });
    }
    event.preventDefault();
  });
}