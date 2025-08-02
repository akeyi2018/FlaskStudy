let baseData_001 = [
  { label: 'OPT', value: 2964 }, 
  { label: 'KRS', value: 20 },
  { label: 'Core', value: 8 },
  { label: 'BTQ', value: 7 },
  { label: 'KRS', value: -894 },
  { label: 'Core', value: 22 },
  { label: 'BTQ', value: -39 },
  { label: 'KRS', value: 619 },
  { label: 'Core', value: -426 },
  { label: 'BTQ', value: -42 }
 ];

const labels = baseData_001.map(o => o.label).concat('Actual');
// const labels = baseData_001.map(o => o.label);
const data = [];
let total = 0;
for (let i = 0; i < baseData_001.length; i++) {
   const vStart = total;
   total += baseData_001[i].value;
   data.push([vStart, total]);  
 }
data.push(2239);
// const backgroundColors = data.map((o, i) => 'rgba(255, 99, 132, ' + (i + (11 - data.length)) * 0.1 + ')');
const backgroundColors = data.map((o, i) => 'rgba(120, 99, 132)'); 
new Chart('waterfall_01', {
   type: 'bar',
   data: {
     labels: labels,
     datasets: [{
       data: data,
       backgroundColor: backgroundColors,
       barPercentage: 1
     }]
   },
   options: {
     responsive: true,
     maintainAspectRatio: false,
     legend: {
       display: false
     },
     tooltips: {
       callbacks: {
         label: (tooltipItem, data) => {
           const v = data.datasets[0].data[tooltipItem.index];
           return Array.isArray(v) ? v[1] - v[0] : v;
         }
       }
     },
     scales: {
       yAxes: [{
         ticks: {
           beginAtZero: false
         }
       }]
     }
   }
 });