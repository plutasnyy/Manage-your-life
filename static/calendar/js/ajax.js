$(function(){
  var loadForm = function(){
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: "GET",
      dataType: "json",
      beforeSend: function(){
        $("#modal-event").modal("show");
      },
      success: function(data){
        $("#modal-event .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function(){
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      succes: function(data){
        if(data.form_is_valid){
          $("#modal-event").modal("hide");
        }
        else{
          $("#modal-event .modal-content").html(data.html_form);
        }
      },
      error: function(data) {
          console.log(data);
        }
    });
  };

  $(".js-create-event").click(loadForm);
  $("#modal-event").on("submit",".js-event-save-form",saveForm);
});
