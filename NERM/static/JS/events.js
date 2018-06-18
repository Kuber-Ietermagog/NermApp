$("#eventsMenu").css("background-color", "rgba(48, 150, 150, .95)");

$.get("/static/json/jobinfo.json", function(data, status){
  var arlen = data['desc'].length
  for (var i = 0; i < arlen; i++) {
    var jobtab = document.getElementById("jobTable");
    var row = jobtab.insertRow(i+1);
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    cell1.innerHTML = data['desc'][i],
    cell2.innerHTML = data['info'][i]
    cell1.style.width = "30%"
  }
});

$.get("/static/json/events.json", function(data, status){
  var arlen = data['eventNo'].length
  var triplog = {'tripNo':[], 'dtStamp':[], 'descTrip':[], 'status':[], 'type':[], 'alarm_on':[]};
  var i = 0;
  for (var j = arlen - 1 ; j > -1 ; j--) {
    triplog['tripNo'].push(data['eventNo'][j]);
    triplog['dtStamp'].push(data['eventTime'][j]);
    triplog['descTrip'].push(data['eventDesc'][j]);
    triplog['status'].push(data['eventState'][j]);
    triplog['type'].push(data['eventType'][j]);
    triplog['alarm_on'].push(data['alarm_on'][j])
  }
  for (var j=0; j < triplog['tripNo'].length; j++){
    if (triplog['type'][j] === "Trip") {
        if (triplog['status'][j] === triplog['alarm_on'][j]) {
          var tripType = "Trip";
        }else {
          var tripType = "Healthy";
        }
    }else if (triplog['type'][j] === "Alarm") {
        if (triplog['status'][j] === triplog['alarm_on'][j]) {
          var tripType = "Alarm";
        }else {
          var tripType = "Healthy";
        }
      }
    var table = document.getElementById("myTable");
    var row = table.insertRow(j+1);
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    var cell3 = row.insertCell(2);
    var cell4 = row.insertCell(3);
    cell1.innerHTML = triplog['tripNo'][j],
    cell2.innerHTML = triplog['dtStamp'][j],
    cell3.innerHTML = triplog['descTrip'][j],
    cell4.innerHTML = tripType
    if (triplog['type'][j] === "Trip" && triplog['status'][j] === triplog['alarm_on'][j]) {
      cell1.style.backgroundColor = 'red';
      cell2.style.backgroundColor = 'red';
      cell3.style.backgroundColor = 'red';
      cell4.style.backgroundColor = 'red';
    }else if (triplog['type'][j] === "Alarm" && triplog['status'][j] === triplog['alarm_on'][j]) {
      cell1.style.backgroundColor = 'yellow';
      cell2.style.backgroundColor = 'yellow';
      cell3.style.backgroundColor = 'yellow';
      cell4.style.backgroundColor = 'yellow';
    }else if (triplog['descTrip'][j] === "System Boot Complete!") {
      cell1.style.backgroundColor = 'pink';
      cell2.style.backgroundColor = 'pink';
      cell3.style.backgroundColor = 'pink';
      cell4.style.backgroundColor = 'pink';
    }else {
      cell1.style.backgroundColor = 'lightgreen';
      cell2.style.backgroundColor = 'lightgreen';
      cell3.style.backgroundColor = 'lightgreen';
      cell4.style.backgroundColor = 'lightgreen';
    }
  }
});

var eventUpdate = setInterval(function() {
  $.get("/static/json/events.json", function(data, status){
    var arlen = data['eventNo'].length;
    var tableLength = $("#myTable thead tr").length-1;
    if (arlen !== tableLength) {
      if (arlen-tableLength === 1) {
        if (data['eventType'][arlen-1] === "Trip") {
            if (data['eventState'][arlen-1] === data['alarm_on'][arlen-1]) {
              var tripType = "Trip";
            }else {
              var tripType = "Healthy";
            }
        }else if (data['eventType'][arlen-1] === "Alarm") {
            if (data['eventState'][arlen-1] === data['alarm_on'][arlen-1]) {
              var tripType = "Alarm";
            }else {
              var tripType = "Healthy";
            }
          }
        var table = document.getElementById("myTable");
        var row = table.insertRow(1);
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        var cell3 = row.insertCell(2);
        var cell4 = row.insertCell(3);
        cell1.innerHTML = data['eventNo'][arlen-1],
        cell2.innerHTML = data['eventTime'][arlen-1],
        cell3.innerHTML = data['eventDesc'][arlen-1],
        cell4.innerHTML = tripType
        if (data['eventType'][arlen-1] === "Trip" && data['eventState'][arlen-1] === data['alarm_on'][arlen-1]) {
          cell1.style.backgroundColor = 'red';
          cell2.style.backgroundColor = 'red';
          cell3.style.backgroundColor = 'red';
          cell4.style.backgroundColor = 'red';
        }else if (data['eventType'][arlen-1] === "Alarm" && data['eventState'][arlen-1] === data['alarm_on'][arlen-1]) {
          cell1.style.backgroundColor = 'yellow';
          cell2.style.backgroundColor = 'yellow';
          cell3.style.backgroundColor = 'yellow';
          cell4.style.backgroundColor = 'yellow';
        }else if (data['eventDesc'][arlen-1] === "System Boot Complete!") {
          cell1.style.backgroundColor = 'pink';
          cell2.style.backgroundColor = 'pink';
          cell3.style.backgroundColor = 'pink';
          cell4.style.backgroundColor = 'pink';
        }else {
          cell1.style.backgroundColor = 'lightgreen';
          cell2.style.backgroundColor = 'lightgreen';
          cell3.style.backgroundColor = 'lightgreen';
          cell4.style.backgroundColor = 'lightgreen';
        }
      }else {
        location.reload(true);
      }

    }
  });
}, 3000)
