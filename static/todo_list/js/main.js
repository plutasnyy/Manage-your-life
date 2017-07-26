$(function () {
  $(".js-create-list").click(function () {
    $.ajax({
      url: '/todo_list/list/create/',
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-add_list").modal("show");
        alert("lol");
      },
      success: function (data) {
        $("#modal-book .modal-content").html(data.html_form);
      }
    });
  });
});
