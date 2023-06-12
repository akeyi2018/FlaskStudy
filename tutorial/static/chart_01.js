function view_myChart_1(){
  const ctx = document.getElementById('myChart_1');
  // const con = ctx.getContext('2d');
  // con.fillStyle = 'rgb( 0, 0, 0)';
  // con.fillRect(0, 0, ctx.width, ctx.height);
  const btx = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        backgroundColor: "rgba(0,0,0,0.2)",
        datasets: [{
          label: '# of Votes',
          data: [12, 19, 3, 5, 2, 3],
          borderWidth: 1,
          backgroundColor: "rgba(219,39,91,0.5)",
          borderColor: "rgba(25,255,128,0.5)"
        }]
      },
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
            text: "グラフ1",
            position: 'bottom'
          },
          subtitle:{
            display: true,
            text: 'sub text'
          },
          bgColor:{
              backgroundColor:'blue'
          }
        }
      }
    });

}

view_myChart_1()
