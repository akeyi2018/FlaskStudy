function get_data(ctx){
  // let data = document.querySelectorAll('textarea')[0].Value;
  // console.log(data);
  ctx.options.plugins.title.text="グラフ1";
  ctx.update();
}

const ctx = document.getElementById('myChart');
const btx = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
      datasets: [{
        label: '# of Votes',
        data: [12, 19, 3, 5, 2, 3],
        borderWidth: 1,
        backgroundColor: "rgba(219,39,91,0.5)",
        borderColor: "rgba(25,255,128,0.5)"
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      },
      plugins:{
        title:{
          display: true,
          text: "",
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

get_data(btx);