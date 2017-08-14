  $(function () {
    var global_url;//THIS IS VEEERY BAD

    var loadForm=function(){
    global_url=$(this).attr("data-url");
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: "get",
      dataType: "json",
      beforeSend: function () {
        $("#modal-add_list").modal("show");
      },
      success: function (data) {
        $("#modal-add_list .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    form.attr("action",global_url);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#Todo-List").html(data.queryset);
          $("#modal-add_list").modal("hide");
          window.location.reload();
        }
        else {
          $("#modal-add_list .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };

$(".js-create-list").click(loadForm);
$("#modal-add_list").on("submit", ".js-list-create-form", saveForm);

$(".js-create-item").on("click",loadForm);
});
