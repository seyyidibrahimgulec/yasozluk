function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function create_new_entry(){
  $.ajax({
    type: "POST",
    url: "/api/new_entry/",
    data: {
      csrfmiddlewaretoken: csrftoken,
      text: $("#entry-box").val(),
      created_by: $("#user-pk").val(),
      topic: $('#topic-pk').val(), 	
    }
  }).done(function(){
    window.location.replace("/");
  });
}

$("#entry-post").click(function(){
    create_new_entry()
})

