$(document).ready(function(){
  calendar();


  $(".day-box").mouseover(function(){
    $(this).css( "background-color", "#eaf2ff" );
  });
  $(".day-box").mouseleave(function(){
    $(this).css( "background-color", "white" );
  });

  $(".day-box").click(function(){
    let date=$(this).attr("date");
    $(".event-box").addClass('date="'+date+'"');
    $(".event-box").html(date);
  });

});
function calendar(date) {
  if (date==null){
    date = new Date();
  }

  day = date.getDate();
  month = date.getMonth();
  year = date.getFullYear();

  months = new Array('January','February','March','April','May','June','July','August','September','October','November','December');

  this_month = new Date(year, month, 1);
  next_month = new Date(year, month + 1, 1);

  first_week_day = this_month.getDay();
  days_in_this_month = Math.round((next_month.getTime() - this_month.getTime()) / (1000 * 60 * 60 * 24));

  calendar_html = '<table class="col-md-7" style="background-color:666699; color:ffffff;">';
  calendar_html += '<tr><td colspan="7" style="background-color:9999cc; color:000000; text-align: center;">' + months[month] + ' ' + year + '</td></tr>';
  calendar_html += '<tr>';

  var this_date;
  for(week_day = 0; week_day < first_week_day; week_day++) {
    calendar_html += '<td style="background-color:9999cc; color:000000;"> </td>';
  }

  week_day = first_week_day;
  for(day_counter = 1; day_counter <= days_in_this_month; day_counter++) {
    week_day %= 7;
    if(week_day == 0)
      calendar_html += '</tr><tr>';

    this_date=new Date(year,month,day_counter);

    if(day == day_counter)
      calendar_html += '<td class="col-md-1 day-box" date="'+this_date+'>" <b> ' + day_counter + '</b></td>';
    else
      calendar_html += '<td class="col-md-1 day-box" date="'+this_date+'">' + day_counter + ' </td>';
    week_day++;
  }

  calendar_html += '</tr>';
  calendar_html += '</table>';
  calendar_html+= '<div class="col-md-5 event-box">A tu moze jakies zdarzenia jak sie uda zrobic xD</div>';
  document.getElementById("calendar").innerHTML = calendar_html;
}
