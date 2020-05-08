window.messageFilter = function (lastPollTime) {
    let cookie = getCookie("csrftoken");
    $.ajax({
        url: "/ajax/messages/get?lastPoll=" + lastPollTime,
        type: "get",
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", cookie);
            }
        }
    }).done(function (result) {
        $("#message-container").append(result);
        scrollToLatest();
    });
}

window.historyFilter = function (conversation_list) {
    $('#conversation_list').children().fadeOut(250, function () {
        $("#conversation_list").empty();
        $("#conversation_list").append($(conversation_list));
    });
}