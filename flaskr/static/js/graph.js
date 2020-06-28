const CHART = document.getElementById("graphRating").getContext("2d");

let barChart = new Chart(chart, {
    type: 'bar',
    data: {
        labels: ["Ontario", "Alberta","PEI","BC"],
        datasets: [
            {
                data: [10, 20, 55, 30]
            }
        ]
    }
});