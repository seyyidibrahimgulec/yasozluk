$(document).ready(function () {
  console.log("will call today api");
  loadTodayInHistory();
  setInterval(() => {
    console.log("polling new changes");
    pollNewMessages();
  }, 1000);
  scrollToLatest();
});

function pollNewMessages() {
  let lastPollTime = getCookie("last_poll_time");
  // lastPollTime = Date.now().toUTCString();
  if (!lastPollTime) {
    let s = new Date(Date.now()).toISOString()
    lastPollTime = s.substring(0, s.length - 1)
  }

  $.ajax({
      url: "/ajax/messages/count?lastPoll=" + lastPollTime,
      type: "get",
      beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
          xhr.setRequestHeader("X-CSRFToken", cookie);
        }
      }
    })
    .done(function (result) {
      console.log(result);
      if (result.count > 0) {
        if (window.messageFilter) {
          window.messageFilter(lastPollTime);
        } else {

        }
      }
      let s = new Date(Date.now()).toISOString()
      lastPollTime = s.substring(0, s.length - 1)
      setCookie("last_poll_time", lastPollTime, 7);
    }).fail(function (err) {
      console.log("error", err);
    });
}

function scrollToLatest() {
  if ($(".message").last()[0])
    $(".message").last()[0].
  scrollIntoView({
    behavior: "smooth",
    block: "end",
    inline: "nearest"
  });
  // .scrollIntoView({
  //   behavior: "smooth"
  // });
}

function loadTodayInHistory() {
  $.ajax("/ajax/today")
    .done(function (result) {
      //    console.log( "success",data ); 
      console.log(result);
      var size = 5;
      var items = result.events.slice(0, size).map(i => {
        return `<div class="todayRow">${i.no_year_html}</div>`
      });
      let rightFrame = $("#right_frame");
      rightFrame.empty();
      appendItemsToRight(rightFrame, items, "Olaylar");
      items = result.births.slice(0, size).map(i => {
        return `<div class="todayRow">${i.no_year_html}</div>`
      });
      appendItemsToRight(rightFrame, items, "Doğumlar");
      items = result.deaths.slice(0, size).map(i => {
        return `<div class="todayRow">${i.no_year_html}</div>`
      });
      appendItemsToRight(rightFrame, items, "Ölümler");

    }).fail(function (err) {
      $("#right_frame").empty();
      console.log("error", err);
    });
  $("#right_frame").append($("<h6>Yükleniyor..</h6><div class=\"loader\"></div>"))
}

function appendItemsToRight(rightFrame, items, title) {
  rightFrame.append($(`<h5 style="padding-top:10px">${title}</h5>`));
  for (row in items) {
    rightFrame.append($(items[row]));
  }
}

function sendMessage() {
  console.log("error");
  //get crsf token to pass backend via ajax header
  let cookie = getCookie("csrftoken");
  let txt = $("#txtMessage").val();
  let send_to_id = $("#send_to_id").val();
  console.log("txt:" + txt);
  $.ajax({
      url: "/ajax/messages/new/",
      type: "post",
      beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
          xhr.setRequestHeader("X-CSRFToken", cookie);
        }
      },
      data: {
        text: txt,
        send_to_id: send_to_id
      }
    })
    .done(function (result) {
      console.log(result);
      $("#txtMessage").val("");
      $("#message-container").append(result);
      scrollToLatest();
    }).fail(function (err) {
      console.log("error", err);

    });
}

function setCookie(name, value, days) {
  var expires = "";
  if (days) {
    var date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
    expires = "; expires=" + date.toUTCString();
  }
  document.cookie = name + "=" + (value || "") + expires + "; path=/";
}

function getCookie(name) {
  var nameEQ = name + "=";
  var ca = document.cookie.split(';');
  for (var i = 0; i < ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == ' ') c = c.substring(1, c.length);
    if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
  }
  return null;
}

function eraseCookie(name) {
  document.cookie = name + '=; Max-Age=-99999999;';
}

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

function csrfSafeMethod(method) {
  // these HTTP methods do not require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}