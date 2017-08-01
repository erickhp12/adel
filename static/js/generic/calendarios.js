$(function () {
  $.datepicker.setDefaults($.datepicker.regional["es"]);
  $("#datepicker").datepicker({
    firstDay: 1,
    monthNames: ['Enero', 'Febrero', 'Marzo','Abril', 'Mayo','Junio',
    'Julio','Agosto','Septiempbre','Octubre','Noviembre','Diciembre'],
    dayNamesMin: ['Dom','Lun','Mar','Mier','Jue','Vier','Sab'],
    dateFormat: 'yy-mm-dd',
    timeFormat:  "hh:mm:ss"
    });
  });

$(function () {
  $.datepicker.setDefaults($.datepicker.regional["es"]);
  $("#datepickerf").datepicker({
    firstDay: 1,
    monthNames: ['Enero', 'Febrero', 'Marzo','Abril', 'Mayo','Junio',
    'Julio','Agosto','Septiempbre','Octubre','Noviembre','Diciembre'],
    dayNamesMin: ['Dom','Lun','Mar','Mier','Jue','Vier','Sab'],
    dateFormat: 'yy-mm-dd',
    timeFormat:  "hh:mm:ss"
    });
  });

function clear_text() { 
    document.getElementById('datepicker').placeholder = "";
}
function clear_textf() { 
    document.getElementById('datepickerf').placeholder = "";
}
