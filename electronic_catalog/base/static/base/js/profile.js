const xValues = [50,60,70,80,90,100,110,120,130,140,150];
const yValues = [7,8,8,9,9,9,10,11,14,14,15];

new Chart("myChart", {
  type: "line",
  data: {
    labels: xValues,
    datasets: [{
      fill: false,
      lineTension: 0,
      backgroundColor: "rgba(0,0,255,1.0)",
      borderColor: "rgba(0,0,255,0.1)",
      data: yValues
    }]
  },
  options: {
    title: {display:true,text:"Evolution of the GPA every month"},
    legend: {display:false},
    scales: {
      yAxes: [{ticks: {min: 6, max:16}}],
    }
  }
});


var xValues1 = ["1", "2", "3", "4", "5","6","7","8","9","10"];
var yValues1 = [55, 49, 44, 24, 15,23,54,12,6,9];
var barColors = ["red", "green","blue","orange","brown","pink","yellow","lightblue","gray","black"];

new Chart("secondChart", {
  type: "pie",
  data: {
    labels: xValues1,
    datasets: [{
      backgroundColor: barColors,
      data: yValues1
    }]
  },
  options: {
    title: {
      display: true,
      text: "Amount of marks"
    },
    legend:{
      display:false,
    }
  }
});