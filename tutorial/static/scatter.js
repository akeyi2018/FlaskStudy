function ScatterChart(){
  var ctx = document.getElementById("ScatterChart");
  var myScatterChart = new Chart(ctx, {
  type: 'scatter', 
  data: { 
    datasets: [
      {
        label: '1組',
        data: [
          {% for x,y in dd %}
          {x: {{ x }}, y: {{ y }}},
          {% endfor %}
        ],
        backgroundColor: 'RGBA(225,95,150, 1)',
      }]
  },
  options:{
    title: {
      display: true,
        text: 'test date'
    },
    scales: {
      xAxes: [{        
        scaleLabel: {             
          display: true,          
          labelString: 'axis_x' 
        },
        ticks: {
          suggestedMin: 0,
          suggestedMax: 100,
          stepSize: 10,
          callback: function(value, index, values){
            return  value +  '点'
          }
        }
      }],
      yAxes: [{        
        scaleLabel: {             
          display: true,          
          labelString: 'axis_y' 
        },
        ticks: {
          suggestedMax: 100,
          suggestedMin: 0,
          stepSize: 10,
          callback: function(value, index, values){
            return  value +  '点'
          }
        }
      }]
    }
  }
  });
}
ScatterChart()