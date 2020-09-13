"use strict";

document.addEventListener("DOMContentLoaded", function(event) {


    search()
    document.getElementById ("ceo_selector_click").addEventListener (
        "click", run);

    let objStock;
    let demoArr = [];
    let demoAr = [];
    let stockPrice = demoArr.reverse();
    let stockDate = demoAr.reverse();
    let chartHtml = document.getElementById("mixed-chart")
    let chart;

    function makeChart() {
        let chart = new Chart(chartHtml, {
            type: 'bar',
            data: {
                labels: stockDate,
                datasets: [{
                    label: "Stock",
                    type: "line",
                    borderColor: "#8e5ea2",
                    data: stockPrice,
                    fill: false
                }, {
                    label: "Tweets",
                    type: "scatter",
                    backgroundColor: "rgba(255, 255, 255 .4)",
                    backgroundColorHover: "#3e95cd",
                    data: [12, 24, 3, 45, 6]
                }]
            },
            options: {
                title: {
                    display: true,
                    text: 'Sample'
                },
                legend: {
                    display: false
                }
            }
        });
        return chart
    }



    function getStockPrice() {
        $.get(`http://localhost:5000/api/v1/get_financial_data?username=elonmusk`,
            function(response) {
                objStock = response;
                let len = objStock.length
                for (let i = len-1 ; i > 0; i--) {
                    demoArr.push(objStock[i].Close);
                }
                chart = makeChart();
                chart.update()
                return demoArr;
            });
    }

    function getStockDate() {
        $.get(`http://localhost:5000/api/v1/get_financial_data?username=elonmusk`,
            function(response) {
                let objStock = response;
                let len = objStock.length
                let counter = 0;
                for (let i = len-1 ; i > 0; i--) {
                    demoAr.push(objStock[i].DateTime);
                }
                chart = makeChart();
                chart.update()
                return demoAr;
            });

    }

    function run() {
        document.getElementById('ceo_selector').style.display = "none";
        getStockDate();
        getStockPrice();
        stockPrice = demoArr.reverse();
        stockDate = demoAr.reverse();
        console.log(stockPrice);
        let chart = new Chart(chartHtml, {
            type: 'bar',
            data: {
                labels: stockDate,
                datasets: [{
                    label: "Stock",
                    type: "line",
                    borderColor: "#8e5ea2",
                    data: stockPrice,
                    fill: false
                }, {
                    label: "Tweets",
                    type: "scatter",
                    backgroundColor: "rgba(255, 255, 255 .4)",
                    backgroundColorHover: "#3e95cd",
                    data: [12, 24, 3, 45, 6]
                }]
            },
            options: {
                title: {
                    display: true,
                    text: 'Sample'
                },
                legend: {
                    display: false
                }
            }
        });
        chart.update()
        chartHtml.style.display = "block"
    }

    function search() {
        $("input").on("change paste keyup", function() {
            let inputText = $("input").val()
            if (inputText.length >= 4) {
                document.getElementById('ceo_selector').style.display = "block";
            }
        });
    }
});