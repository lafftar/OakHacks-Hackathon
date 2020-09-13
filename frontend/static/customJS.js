
            var objStock;
            var demoArr = [];
            var demoAr = [];
            
            function getStockPrice(){
                $.get(`http://localhost:5000/api/v1/get_financial_data?username=elonmusk`,
                function (response) {
                 let objStock = response;

                 var len = objStock.length

               for(var i =0; i < len; i++){
                   demoArr.push(objStock[i].Close);
                   
               }
              
               
               return demoArr;
               console.log(demoArr);

                });
                
            }
            function getStockDate(){
                $.get(`http://localhost:5000/api/v1/get_financial_data?username=elonmusk`,
                function (response) {
                 let objStock = response;

                 var len = objStock.length
                 var counter = 0;
                 for(var i =0; i < len; i++){
                    demoAr.push(objStock[i].DateTime);
                    
                }
                 
                 return demoAr;
                 console.log(demoArr);
                 console.log(demoAr);
                  });
                  
            }
            getStockDate();
            getStockPrice();
                console.log(demoArr);

                
            
            
            var stockPrice = demoArr.reverse();
            var stockDate = demoAr.reverse();
            console.log(stockPrice);
            new Chart(document.getElementById("mixed-chart"), {
                type: 'bar',
                data: {
                labels: stockDate,
                datasets: [{
                    label: "Stock",
                    type: "line",
                    borderColor: "#8e5ea2",
                    data: stockPrice,
                    fill: false
                    },{
                    label: "Tweets",
                    type: "scatter",
                    backgroundColor: "rgba(255, 255, 255 .4)",
                    backgroundColorHover: "#3e95cd",
                    data: [12, 24, 3, 45, 6]
                    }
                ]
                },
                options: {
                title: {
                    display: true,
                    text: 'Sample'
                },
                legend: { display: false }
                }
        });
        function search(){
            $("input").on("change paste keyup", function () {
                let inputText = $("input").val()
                if(inputText.length >= 2){
                    resetSearchResults();
                    $.get(
                        `http://localhost:5000/api/v1/search?query=${inputText}`,
                        function (response) {
                        //    build results view here
                        }
                    )
                }
            });
        }
 