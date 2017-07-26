$(function () {
  $(".js-create-list").click(function () {
    $.ajax({
      url: '/todo_list/list/create/',
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-add_list").modal("show");
      },
      success: function (data) {
        $("#modal-add_list .modal-content").html(data.html_form);
      }
    });
  });
});
