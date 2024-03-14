try{
  let xValues = [1,2,3,4,5,6,7,8,9,10,11,12];
  let counts = [0,0,0,0,0,0,0,0,0,0,0,0];
  let yValues = [0,0,0,0,0,0,0,0,0,0,0,0];
  const months = {
    "january":1,
    "february":2,
    "march":3,
    "april":4,
    "may":5,
    "june":6,
    "july":7,
    "august":8,
    "september":9,
    "octomber":10,
    "november":11,
    "december":12,
  }

  for (mark of data_marks){
    yValues[months[mark[1]]-1] += mark[0]
    if (mark[0] != 0){
      counts[months[mark[1]]-1] += 1;
    }
  }

  for (let i = 0;i < yValues.length;i++){
      yValues[i] = yValues[i]/counts[i];
  }

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
        yAxes: [{ticks: {min: 0, max:10}}],
      }
    }
  });


  var xValues1 = ["1", "2", "3", "4", "5","6","7","8","9","10"];
  var yValues1 = [0,0,0,0,0,0,0,0,0,0];
  for (mark of data_marks){
    if (mark[0] != 0){
      yValues1[mark[0]-1] += 1;
    }
  }

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
}catch(error){
  
}