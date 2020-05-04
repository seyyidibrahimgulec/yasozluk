$(document).ready(function () {
  console.log("will call today api");
  loadTodayInHistory();
});

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