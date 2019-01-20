window.onload = function () {
  
  
  $('.basket_record').on('click', 'input[type="number"]', function(event) {
    var target_href = event.target;

    if (target_href) {
      $.ajax({
        url: "/basket/edit/" + target_href.name + "/" + target_href.value + "/",

        success: function(data) {
          $('.basket_record').html(data.result);
          console.log('ajax done');
        },
      });
    }
    event.preventDefault();
  });
}