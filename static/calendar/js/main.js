$(document).ready(function(){
  calendar();
});


$(document).on('click','.day-box',function(){
  var date=$(this).attr("date");
  $(".event-box").addClass('date="'+date+'"');
  $.ajax({
    url: "/calendar/event_list",
    type: 'get',
    data: date,
    dataType: 'json',
    success: function(data){
      $(".event-box").append(data['html_form']);
    },
    error: function(data){
      console.log(data);
    }
  });
});

$(document).on('mouseleave','.day-box',function(){
  $(this).css( "background-color", "white" );
});
$(document).on('mouseover','.day-box',function(){
  $(this).css( "background-color", "#eaf2ff" );
});

$(document).on('click','.pager .next',function(){
  months_counter++;
  calendar();
});
$(document).on('click','.pager .previous',function(){
  months_counter--;
  calendar();
});

var months_counter=0;

function calendar() {
  date = new Date();
  day = date.getDate();
  month = date.getMonth();
  year = date.getFullYear();

  month += months_counter;
  year += Math.floor(month/12);

  if(month<0)
    month = 12 + month%12;

  month = Math.abs(month%12);

  months = new Array('January','February','March','April','May','June','July','August','September','October','November','December');

  this_month = new Date(year, month, 1);
  next_month = new Date(year, month + 1, 1);

  first_week_day = this_month.getDay();
  days_in_this_month = Math.round((next_month.getTime() - this_month.getTime()) / (1000 * 60 * 60 * 24));

  calendar_html = '<table style="background-color:666699; color:ffffff;">';
  calendar_html += '<tr><td colspan="7" style="background-color:9999cc; color:000000; text-align: center;">' + months[month] + ' ' + year + '</td></tr>';
  calendar_html += '<ul class="pager">';
  calendar_html += '  <li class="previous"><a role="button">Previous</a></li>';
  calendar_html += '  <li class="next"><a role="button">Next</a></li>';
  calendar_html += '</ul>';
  calendar_html += '<tr>';

  for(week_day = 0; week_day < first_week_day; week_day++)
  {
    calendar_html += '<td style="background-color:9999cc; color:000000;"> </td>';
  }

  week_day = first_week_day;
  for(day_counter = 1; day_counter <= days_in_this_month; day_counter++)
  {
    week_day %= 7;
    if(week_day == 0)
      calendar_html += '</tr><tr>';

    this_date = new Date(year,month,day_counter);

    if(date.getDate() == this_date.getDate() && date.getMonth() == this_date.getMonth() && date.getFullYear() == this_date.getFullYear())
      calendar_html += '<td class="col-md-1 day-box" date="'+this_date+'"> <b> ' + day_counter + '</b></td>';
    else
      calendar_html += '<td class="col-md-1 day-box" date="'+this_date+'">' + day_counter + ' </td>';
    week_day++;
  }

  calendar_html += '</tr>';

  calendar_html += '</table>';
  document.getElementById("calendar").innerHTML = calendar_html;
}
