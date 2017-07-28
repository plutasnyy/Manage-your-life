$(function () {
  var loadForm =  function () {
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
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#Todo-List").html(data.queryset);  // <-- Replace the table body
          $("#modal-add_list").modal("hide");  // <-- Close the modal
        }
        else {
          $("#modal-add_list .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };

function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}
var csrf=function(){
  var old_token=getCookie("csrftoken");
  console.log(old_token);
  console.log($("input"));
};

$(".js-create-list").click(loadForm);
$("#modal-add_list").on("submit", ".js-list-create-form", saveForm);
$(".js-log").click(csrf);
});
