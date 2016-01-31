function mean(array) {
    var sum = 0;
    for (var ii = 0; ii < array.length; ii++) {
        sum += array[0]
    }
    return (sum / array.length).toFixed(2);
}

function getAllPeople(results) {
    var ret = []
    for (var pop_set = 0; pop_set < results.length; pop_set++) {
        // Repetition
        for (var rep_set = 0; rep_set < results[pop_set].length; rep_set++) {
            // Person
            for (var per_num = 0; per_num < results[pop_set][rep_set].length; per_num++) {
                ret.push(results[pop_set][rep_set][per_num]);
            }
        }
    }
    return ret;
}

var barOptions = {
    //Boolean - Whether the scale should start at zero, or an order of magnitude down from the lowest value
    scaleBeginAtZero : true,

    //Boolean - Whether grid lines are shown across the chart
    scaleShowGridLines : true,

    //String - Colour of the grid lines
    scaleGridLineColor : "rgba(0,0,0,.05)",

    //Number - Width of the grid lines
    scaleGridLineWidth : 1,

    //Boolean - Whether to show horizontal lines (except X axis)
    scaleShowHorizontalLines: true,

    //Boolean - Whether to show vertical lines (except Y axis)
    scaleShowVerticalLines: true,

    //Boolean - If there is a stroke on each bar
    barShowStroke : false,

    //Number - Pixel width of the bar stroke
    barStrokeWidth : 2,

    //Number - Spacing between each of the X value sets
    barValueSpacing : 5,

    //Number - Spacing between data sets within X values
    barDatasetSpacing : 1,

    //String - A legend template
    legendTemplate : "<ul class=\"<%=name.toLowerCase()%>-legend\"><% for (var i=0; i<datasets.length; i++){%><li><span style=\"background-color:<%=datasets[i].fillColor%>\"></span><%if(datasets[i].label){%><%=datasets[i].label%><%}%></li><%}%></ul>"
}

function getParameters(num) {
    return $.get("../Results/params" + num + ".json");
}

function getResults(num) {
    return $.get("../Results/results" + num + ".json");
}
