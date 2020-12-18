function drawLineChart() {
  
    var jsonData = $.ajax({
      url: '/Data_Visualization/',
      dataType: 'json',
    }).done(function (results) {
  
      // Split timestamp and data into separate arrays
      var labels = [], data=[];
      results["packets"].forEach(function(packet) {
        labels.push(new Date(packet.timestamp).formatMMDDYYYY());
        data.push(parseFloat(packet.payloadString));
      });
  
      // Create the chart.js data structure using 'labels' and 'data'
      var tempData = {
        labels : labels,
        datasets : [{
            fillColor             : "rgba(151,187,205,0.2)",
            strokeColor           : "rgba(151,187,205,1)",
            pointColor            : "rgba(151,187,205,1)",
            pointStrokeColor      : "#fff",
            pointHighlightFill    : "#fff",
            pointHighlightStroke  : "rgba(151,187,205,1)",
            data                  : data
        }]
      };
  
      // Get the context of the canvas element we want to select
      var ctx = document.getElementById("myLineChart").getContext("2d");
  
      // Instantiate a new chart
      var myLineChart = new Chart(ctx).Line(tempData);
    });
  }
  
  drawLineChart();