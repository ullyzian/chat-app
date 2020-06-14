var socket = io.connect("https://" + document.domain + ":" + location.port);

socket.on("connect", () => {
  //get cookie username
  const username = document.cookie
    .split("; ")
    .find((row) => row.startsWith("username"))
    .split("=")[1];

  //send message about user connection
  socket.emit("send", { data: username + " connected", room: $("#room").val() });

  //send form message on submitting
  var form = $("form").on("submit", (e) => {
    e.preventDefault();
    let message = $("input.message").val();
    let room = $("#room").val();
    if (message !== "") {
      socket.emit("send", { message: message, username: username, room: room });
    }
    $("input.message").val("").focus();
  });
});


socket.on("response", (msg) => {
  if (typeof msg.history[0] !== "undefined") {
    // delete previos messages
    $("div.messages-list").empty();

    // add new messages
    msg.history.map((element) => {
      $("div.messages-list").append(
        "<div>" +
          "<b class='text-primary'>" +
          element.username +
          "</b>: " +
          element.message +
          " </div>",
      );
    });

    // scroll chat to bottom
    $(".messages-list").scrollTop($(".messages-list")[0].scrollHeight);

    // display connected user
    if (msg.data) {
      $(".alert-window").append(
        "<div class='alert alert-info mb-0' role='alert'>" + msg.data + "</div>",
      );

      $(".alert").alert();
      setTimeout(function () {
        $(".alert").remove();
      }, 3000);
    }
  }
});
