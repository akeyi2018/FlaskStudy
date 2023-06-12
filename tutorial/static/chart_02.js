function myChart_2(){

  const ctx_2 = document.getElementById('myChart_2');

  const labels = [1,2,3,4,5,6,7];
  const data = {
    labels: labels,
    datasets: [{
      label: 'My First Dataset',
      data: [65, 59, 80, 81, 56, 55, 40],
      fill: false,
      borderColor: 'rgb(75, 192, 192)',
      tension: 0.1
    }]
  };

  new Chart(ctx_2, {
    type: 'line',
    data: data,
    options: {
      responsive: false,
      scales: {
        y: {
          beginAtZero: true
        }
      },
      plugins:{
        title:{
          display: true,
          text: 'グラフ2',
          position: 'bottom'
        },
        bgColor:{
            backgroundColor:'blue'
        }
      }
    }
  });
}

myChart_2()