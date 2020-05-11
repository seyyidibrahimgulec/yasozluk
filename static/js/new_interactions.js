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

// function create_new_favorite(){
//   $.ajax({
//     type: "POST",
//     url: "/api/new_favorite/",
//     data: {
//       csrfmiddlewaretoken: csrftoken,
//       user: $("#user-pk").val(),
//       entry: $('#entry-pk').val(),
//     }
//   }).done(function(){
//       let currentURL = window.location.pathname + window.location.search + window.location.hash;
//       window.location.replace(currentURL);
//   })
// }


// // function create_new_upvote(){
// //     console.log($(this).attr('class'))
// //   // $.ajax({
// //   //   type: "POST",
// //   //   url: "/api/new_vote/",
// //   //   data: {
// //   //     csrfmiddlewaretoken: csrftoken,
// //   //     vote: "upvote",
// //   //     user: $("#user-pk").val(),
// //   //     entry: $('#entry-pk').val(),
// //   //   }
// //   // }).done(function(){
// //   //     let currentURL = window.location.pathname + window.location.search + window.location.hash;
// //   //     window.location.replace(currentURL);
// //   // })

// // }


// function create_new_downvote(){
//   $.ajax({
//     type: "POST",
//     url: "/api/new_vote/",
//     data: {
//       csrfmiddlewaretoken: csrftoken,
//       vote: "downvote",
//       user: $("#user-pk").val(),
//       entry: $('#entry-pk').val(),
//     }
//   }).done(function(){
//       let currentURL = window.location.pathname + window.location.search + window.location.hash;
//       window.location.replace(currentURL);
//   })
// }


$(document).ready(function() {
    var csrftoken = getCookie('csrftoken');

    $(".fa-chevron-up").unbind().on("click", function() {
        if ($(this).attr("class").includes("text-success")) {
            // Zaten upvote verilmiş, UPVOTEYI SIL
            $.ajax({
                type: "DELETE",
                url: "/api/vote/" + $(this).parent().parent().find(".vote-pk").val() + "/",
                beforeSend: function(xhr) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                },
            }).done(function(){
                let currentURL = window.location.pathname + window.location.search + window.location.hash;
                window.location.replace(currentURL);
            })
        }
        else {
            // Upvote verilmemiş, downvote var mı diye kontrol et
            if ($(this).parent().next().children().attr("class").includes("text-danger")) {
                // Upvote verilmemiş ama downvote var, DOWNVOTE'YI SIL, UPVOTE OLUŞTUR
                $.ajax({
                    type: "DELETE",
                    url: "/api/vote/" + $(this).parent().parent().find(".vote-pk").val() + "/",
                    beforeSend: function(xhr) {
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    },
                }).done(function(){
                    let currentURL = window.location.pathname + window.location.search + window.location.hash;
                    window.location.replace(currentURL);
                })
                $.ajax({
                    type: "POST",
                    url: "/api/new_vote/",
                    data: {
                        csrfmiddlewaretoken: csrftoken,
                        vote: "upvote",
                        user: $(this).parent().parent().find(".user-pk").val(),
                        entry: $(this).parent().parent().find(".entry-pk").val(),
                    }
                }).done(function(){
                    let currentURL = window.location.pathname + window.location.search + window.location.hash;
                    window.location.replace(currentURL);
                })
            }
            else {
                // Herhangi bir vote verilmemiş, YENI UPVOTE OLUŞTUR.
                $.ajax({
                    type: "POST",
                    url: "/api/new_vote/",
                    data: {
                        csrfmiddlewaretoken: csrftoken,
                        vote: "upvote",
                        user: $(this).parent().parent().find(".user-pk").val(),
                        entry: $(this).parent().parent().find(".entry-pk").val(),
                    }
                }).done(function(){
                    let currentURL = window.location.pathname + window.location.search + window.location.hash;
                    window.location.replace(currentURL);
                })
            }
        }
    });

    $(".fa-chevron-down").unbind().on("click", function() {
        if ($(this).attr("class").includes("text-danger")) {
            // Zaten downvote verilmiş, DOWNVOTEYI SIL
            $.ajax({
                type: "DELETE",
                url: "/api/vote/" + $(this).parent().parent().find(".vote-pk").val() + "/",
                beforeSend: function(xhr) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                },
            }).done(function(){
                let currentURL = window.location.pathname + window.location.search + window.location.hash;
                window.location.replace(currentURL);
            })
        }
        else {
            // Downvote verilmemiş, upvote var mı diye kontrol et
            if ($(this).parent().prev().children().attr("class").includes("text-success")) {
                // Downvote verilmemiş ama upvote var, UPVOTE'YI SIL, DOWNVOTE OLUŞTUR
                $.ajax({
                    type: "DELETE",
                    url: "/api/vote/" + $(this).parent().parent().find(".vote-pk").val() + "/",
                    beforeSend: function(xhr) {
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    },
                }).done(function(){
                    let currentURL = window.location.pathname + window.location.search + window.location.hash;
                    window.location.replace(currentURL);
                })
                $.ajax({
                    type: "POST",
                    url: "/api/new_vote/",
                    data: {
                        csrfmiddlewaretoken: csrftoken,
                        vote: "downvote",
                        user: $(this).parent().parent().find(".user-pk").val(),
                        entry: $(this).parent().parent().find(".entry-pk").val(),
                    }
                }).done(function(){
                    let currentURL = window.location.pathname + window.location.search + window.location.hash;
                    window.location.replace(currentURL);
                })
            }
            else {
                // Herhangi bir vote verilmemiş, YENI DOWNVOTE OLUŞTUR.
                $.ajax({
                    type: "POST",
                    url: "/api/new_vote/",
                    data: {
                        csrfmiddlewaretoken: csrftoken,
                        vote: "downvote",
                        user: $(this).parent().parent().find(".user-pk").val(),
                        entry: $(this).parent().parent().find(".entry-pk").val(),
                    }
                }).done(function(){
                    let currentURL = window.location.pathname + window.location.search + window.location.hash;
                    window.location.replace(currentURL);
                })
            }
        }
    });

    $(".fa-tint").unbind().on("click", function() {
        if ($(this).attr("class").includes("text-success")) {
            // Zaten favlanmış verilmiş, FAVI SIL
            $.ajax({
                type: "DELETE",
                url: "/api/favorite/" + $(this).parent().parent().find(".favorite-pk").val() + "/",
                beforeSend: function(xhr) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                },
            }).done(function(){
                let currentURL = window.location.pathname + window.location.search + window.location.hash;
                window.location.replace(currentURL);
            })
        }
        else {
            // Favlanmamış, favla
            $.ajax({
                type: "POST",
                url: "/api/new_favorite/",
                data: {
                    csrfmiddlewaretoken: csrftoken,
                    user: $(this).parent().parent().find(".user-pk").val(),
                    entry: $(this).parent().parent().find(".entry-pk").val(),
                }
            }).done(function(){
                let currentURL = window.location.pathname + window.location.search + window.location.hash;
                window.location.replace(currentURL);
            })
        }
    });
});
