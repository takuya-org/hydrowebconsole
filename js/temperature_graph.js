var hwc = hwc || {};

hwc.temperatureGraph = function (label, data, domCanvas) {
  var lineChartData = {
    labels: label,
    datasets: [
      {
        fillColor: "rgba(151,187,205,0.5)",
        strokeColor: "rgba(151,187,205,1)",
        pointColor: "rgba(151,187,205,1)",
        pointStrokeColor: "#fff",
        data: data
      }
    ]
  };
  return new Chart(domCanvas.getContext('2d')).Line(lineChartData);
};
