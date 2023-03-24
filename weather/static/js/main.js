var canvas = document.getElementById('myChart');
        new Chart(canvas, {
            type: 'bar',
            data: {
                datasets: [
                    {
                        label: '売上',
                        data: [1000, 7000, 3000]
                    }
                ],
                labels: ['前々月', '前月', '今月']
            },
            options: {
                scales: {
                    xAxes: [
                        {
                            ticks: {}
                        }
                    ],
                    yAxes: [
                        {
                            ticks: {
                                min: 0,
                                max: 1000,
                                stepSize: 50,
                                callback: function(label, index, labels) {

                                    return label.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',') +' 円';

                                }
                            }
                        }
                    ]
                },
                tooltips: {
                    callbacks: {
                        label: function(tooltipItem, data){
                            let l1 = tooltipItem.yLabel.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
                            let l2 = da[1][tooltipItem.index] + '%';
                            return l2;
                        }
                    }
                }
            }
        });