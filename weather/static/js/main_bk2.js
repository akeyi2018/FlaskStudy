let ctx = document.getElementById("myChart");
let barChartData = {
        labels : [ "1月", "2月", "3月", "4月", "5月", "6月", "7月" ],
        datasets : [ {
            label : "売上",
            data : [ 2000, 2850, 3900, 3210, 2500, 4000, 6500 ],
            backgroundColor : 'rgba(0, 0, 255, 0.3)',
            stack: 'stack-1',
        },{
            label : "売上2",
            data : [ 4000, 4850, 5900, 6210, 2500, 4000, 6500 ],
            backgroundColor : 'rgba(0, 255, 2, 0.3)',
            stack: 'stack-1',
        } ]
    
    };

let myChart = new Chart(ctx,
    {
        type : 'bar',
        data : barChartData,
        options : {
            tooltips : {
                callbacks : {
                    footer : function () {
                        let la = 10;
                        la = la + 10;
                        return la;
                    }
                }
            }
        }
    });