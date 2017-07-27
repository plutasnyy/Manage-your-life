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
        $("#modal-add_list .modal-content").html(data.html_form).hide();
      }
    });
  });
});

$("#modal-book").on("submit", ".js-list-create-form", function () {
  var form = $(this);
  $.ajax({
    url: form.attr("action"),
    data: form.serialize(),
    type: form.attr("method"),
    dataType: 'json',
    success: function (data) {
      if (data.form_is_valid) {
        //$("#book-table tbody").html(data.html_book_list);  // <-- Replace the table body
        $("#modal-book").modal("hide");  // <-- Close the modal
      }
      else {
        $("#modal-add_list .modal-content").html(data.html_form);
      }
    }
  });
  return false;
});
