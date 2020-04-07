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

function upVote(entryId) {
  console.log("sending  Upvote:", entryId);
  console.log("loadingElement:", createLoadingElement(entryId));
  //get upvote button
  let elmId = `btnUpVote-${entryId}`;
  let btn = $("#" + elmId);
  //hide it
  btn.css("display", "none");
  //create and prepend loading element to parent of button
  btn.parent().prepend(createLoadingElement(entryId));

  //find down button to disable
  let other = $(`#btnDownVote-${entryId}`);
  //set cursor & disable
  other.css("cursor", "not-allowed");
  other.attr("disabled", "disabled");

  //get crsf token to pass backend via ajax header
  let cookie = getCookie("csrftoken");
  var request = $.ajax({
    url: "/ajax/addVote",
    type: "POST",
    beforeSend: function (xhr, settings) {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", cookie);
      }
    },
    data: {
      entryId: entryId,
      value: 1
    }
  });

  request.done(function (msg) {
    console.log("done:", msg);
    if (msg.success) {
      notify("Kaydedildi");
    } else {
      notify("Başarısız");
    }
    let other = $(`#btnDownVote-${entryId}`);
    other.css("cursor", "pointer");
    other.removeAttr("disabled");

    let elmId = `btnUpVote-${entryId}`;
    let btn = $("#" + elmId);
    btn.css("display", "inline-block");
    $(`#loadingElement-${entryId}`).remove();
  });

  request.fail(function (jqXHR, textStatus) {
    console.log("Request failed: ", jqXHR, textStatus);
    notify("failed", jqXHR.responseText, "danger");
    let other = $(`#btnDownVote-${entryId}`);
    other.css("cursor", "pointer");
    other.removeAttr("disabled");

    let elmId = `btnUpVote-${entryId}`;
    let btn = $("#" + elmId);
    btn.css("display", "inline-block");
    $(`#loadingElement-${entryId}`).remove();
  });
}

function downVote(entryId) {
  console.log("sending  downVote:", entryId);
  console.log("loadingElement:", createLoadingElement(entryId));
  let elmId = `btnDownVote-${entryId}`;
  let btn = $("#" + elmId);
  btn.css("display", "none");
  btn.parent().prepend(createLoadingElement(entryId));

  let other = $(`#btnUpVote-${entryId}`);
  other.css("cursor", "not-allowed");
  other.attr("disabled", "disabled");
  let cookie = getCookie("csrftoken");
  var request = $.ajax({
    url: "/ajax/addVote",
    type: "POST",
    beforeSend: function (xhr, settings) {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", cookie);
      }
    },
    data: {
      entryId: entryId,
      value: -1
    }
  });

  request.done(function (msg) {
    console.log("done:", msg);
    if (msg.success) {
      notify("Kaydedildi");
    } else {
      notify("Başarısız");
    }
    let other = $(`#btnUpVote-${entryId}`);
    other.css("cursor", "pointer");
    other.removeAttr("disabled");

    let elmId = `btnDownVote-${entryId}`;
    let btn = $("#" + elmId);
    btn.css("display", "inline-block");
    $(`#loadingElement-${entryId}`).remove();
  });

  request.fail(function (jqXHR, textStatus) {
    console.log("Request failed: ", jqXHR, textStatus);
    notify("failed", jqXHR.responseText, "danger");
    let other = $(`#btnUpVote-${entryId}`);
    other.css("cursor", "pointer");
    other.removeAttr("disabled");

    let elmId = `btnDownVote-${entryId}`;
    let btn = $("#" + elmId);
    btn.css("display", "inline-block");
    $(`#loadingElement-${entryId}`).remove();
  });
}

function createLoadingElement(entryId) {
  return $(`<div class="spinner-grow spinner-grow-sm text-dark" id="loadingElement-${entryId}" role="status"><span class="sr-only">Loading...</span></div>`);
}

function notify(title = "", msg = "", type = "success") {
  $.notify({
    title: title,
    message: msg
  }, {
    type: type
  });
}