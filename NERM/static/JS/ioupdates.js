var gauge = [];
var plateColors = [];
var meterNames = [];
var numberGauges = 0;
var textColor = [];
var min = [];
var max = [];
var unit = [];
var ticks = [];
var minor_ticks = [];
var high_lights = [];
$("#monitorMenu").css("background-color", "rgba(48, 150, 150, .95)");

$.get("/static/json/analogs.json", function(data, status){
  plateColors = data['face_color'];
  meterNames = data['lables'];
  textColor = data['legend_color'];
  numberGauges = data['qty_gauges'];
  min = data['min_value'];
  max = data['max_value'];
  unit = data['unit'];
  ticks = data['ticks'];
  minor_ticks = data['minor_tick']
  high_lights = data['high_lights']
  for (var i = 0; i < 4; i++) {
    if (i+1 > numberGauges) {
      $("#Volt_"+i).toggleClass("getlost");
    }
  }
  makeGauges(numberGauges);
})

function makeGauges(qty){
  for (i=0; i<qty;i+=1){
  var voltmeter = 'Volt_'+ i;
  gauge[i] = new RadialGauge({
        renderTo: voltmeter,
        width: 250,
        height: 250,
        title: meterNames[i],
        units: unit[i],
        minValue: min[i],
        maxValue: max[i],
        majorTicks: ticks[i],
        minorTicks: minor_ticks[i],
        strokeTicks: true,
        highlights: high_lights[i],
        colorPlate: plateColors[i],
        borderShadowWidth: 0,
        borderOuterWidth: 5,
        borders: true,
        colorMajorTicks: textColor[i],
        colorMinorTicks: textColor[i],
        colorTitle: textColor[i],
        colorUnits: textColor[i],
        colorNumbers: textColor[i],
        colorBorderOuter: "#333",
        colorBorderOuter: "#333",
        colorBorderOuterEnd: "#111",
        colorBorderMiddle: "#222",
        colorBorderMiddleEnd: "#111",
        colorBorderInner: "#111",
        colorBorderInnerEnd: "#333",
        needleType: "arrow",
        needleWidth: 2,
        needleCircleSize: 7,
        needleCircleOuter: true,
        needleCircleInner: false,
        animationDuration: 10,
        animationRule: "linear",
        animateOnInit: true,
  }).draw();
}}

function LoadLables() {
  $.get("static/json/digitals.json", function(data, status){
    for (var i=0; i < 16; i+=1){
      $("#i_lbl_"+i).text(data['input_lbl'][i]);
      $("#i_lbl_"+i).css('backgroundColor', 'gray');
      $("#input_"+i).prop('src', 'static/images/not_used.png')
    }
  })
}

var ioUpdate = setInterval(function() {
  var used_labels = [];
  $.get("static/json/digitals.json", function(data, status){
    used_labels = data['used'];
    alarm_status = data['alarm_on']
  });
  $.get("static/json/reg.json", function(data, status){
    if (data['error'] !== 'none') {
      $("#registers").text(data['error']);
    }else{
      $("#registers").text(data['registers']);
    }
    for (var i=0; i < 16; i+=1){
      if (i<8) {
        if (data['digitals'][i]){
          if (used_labels[i] && !alarm_status[i]) {
            $("#input_"+i).prop('src', 'static/images/red_on.png');
            $("#i_lbl_"+i).css('backgroundColor', 'blue');
          }
          if (used_labels[i] && alarm_status[i]) {
            $("#input_"+i).prop('src', 'static/images/red_on.png');
            $("#i_lbl_"+i).css('backgroundColor', 'red');
          }
        }else{
          if (used_labels[i] && !alarm_status[i]) {
            $("#input_"+i).prop('src', 'static/images/red_off.png');
            $("#i_lbl_"+i).css('backgroundColor', 'red');
          }
          if (used_labels[i] && alarm_status[i]) {
            $("#input_"+i).prop('src', 'static/images/red_off.png');
            $("#i_lbl_"+i).css('backgroundColor', 'blue');
          }
        }
      }else {
        if (data['digitals'][i]){
          if (used_labels[i] && !alarm_status[i]) {
            $("#input_"+i).prop('src', 'static/images/red_on.png');
            $("#i_lbl_"+i).css('backgroundColor', 'green');
            $("#i_lbl_"+i).css('color', 'white');
          }
          if (used_labels[i] && alarm_status[i]) {
            $("#input_"+i).prop('src', 'static/images/red_on.png');
            $("#i_lbl_"+i).css('backgroundColor', 'orange');
            $("#i_lbl_"+i).css('color', 'black');
          }
        }else{
          if (used_labels[i] && !alarm_status[i]) {
            $("#input_"+i).prop('src', 'static/images/red_off.png');
            $("#i_lbl_"+i).css('backgroundColor', 'orange');
            $("#i_lbl_"+i).css('color', 'black');
          }
          if (used_labels[i] && alarm_status[i]) {
            $("#input_"+i).prop('src', 'static/images/red_off.png');
            $("#i_lbl_"+i).css('backgroundColor', 'green');
            $("#i_lbl_"+i).css('color', 'white');
          }
        }
      }
    }
    for (var i = 0; i < numberGauges; i++) {
      gauge[i].value = data['analogs'][i];
    }
  });
}, 100)
