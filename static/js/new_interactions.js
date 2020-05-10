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

function create_new_favorite(){
  $.ajax({
    type: "POST",
    url: "/api/new_favorite/",
    data: {
      csrfmiddlewaretoken: csrftoken,
      user: $("#user-pk").val(),
      entry: $('#entry-pk').val(), 	
    }
  }).done(function(){
      let currentURL = window.location.pathname + window.location.search + window.location.hash;
      window.location.replace(currentURL);
  })   
}


function create_new_upvote(){
  $.ajax({
    type: "POST",
    url: "/api/new_vote/",
    data: {
      csrfmiddlewaretoken: csrftoken,
      vote: "upvote",
      user: $("#user-pk").val(),
      entry: $('#entry-pk').val(), 	
    }
  }).done(function(){
      let currentURL = window.location.pathname + window.location.search + window.location.hash;
      window.location.replace(currentURL);
  })   
}


function create_new_downvote(){
  $.ajax({
    type: "POST",
    url: "/api/new_vote/",
    data: {
      csrfmiddlewaretoken: csrftoken,
      vote: "downvote",
      user: $("#user-pk").val(),
      entry: $('#entry-pk').val(), 	
    }
  }).done(function(){
      let currentURL = window.location.pathname + window.location.search + window.location.hash;
      window.location.replace(currentURL);
  })   
}

