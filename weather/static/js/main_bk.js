// console.info(da);
const ctx = document.getElementById('myChart');

const chart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: da[1],
        datasets: [{
            label: 'data_01',
            data: da[2],
            borderColor: "rgba(255,255,0,1)",
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)'
            ],
        },{
            label:'data_02',
            data: da[3],
            borderColor: "rgba(0,0,255,1)",
            backgroundColor: [
                'rgba(25, 0, 132, 0.2)'
            ],
            borderWidth: 1
        }]
    }
})