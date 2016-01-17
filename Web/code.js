$(document).ready(function(){
    $.when(
        getParameters(1),
        getParameters(2),
        getParameters(3),
        getParameters(4),
        getResults(1),
        getResults(2),
        getResults(3),
        getResults(4)
    ).done(function(p1, p2, p3, p4, r1, r2, r3, r4) {
        main([p1[0], p2[0], p3[0], p4[0]], [r1[0], r2[0], r3[0], r4[0]]);
    });
});

function main(parameters, results) {
    // ---- CHART 1 ----
    // Data
    var s_own = seenOwn(results[0], 0.7);
    var s_own_nf = seenOwn(results[1], 0.7);
    var s_other = seenOther(results[0], 0.7);
    var s_other_nf = seenOther(results[1], 0.7);

    // Chart creation
    var ctx1 = $("#chart1").get(0).getContext("2d");
    var data1 = {
        labels: [
            "Seen own",
            "Seen other"
        ],
        datasets: [
            {
                label: "With filter",
                fillColor: "#3498db",
                highlightFill: "#85C4ED",
                data: [s_own_nf, s_own]
            },
            {
                label: "Without filter",
                fillColor: "#2ecc71",
                highlightFill: "#51D88C",
                data: [s_other_nf, s_other]
            }
        ]
    }
    var chart1 = new Chart(ctx1).Bar(data1, barOptions);

    // Info
    $("#info1").append("<p>Parameters 1: " + parameters[0].join(", ") + "</p>");
    $("#info1").append("<p>Parameters 2: " + parameters[1].join(", ") + "</p>");
    $("#info1").append("<p>Difference with filter: " + ((s_own - s_other) / s_other * 100).toFixed(2) + "%</p>");
    $("#info1").append("<p>Difference with no filter: " + ((s_own_nf - s_other_nf) / s_other_nf * 100).toFixed(2) + "%</p>");

    // ---- CHART 2 ----
    // Data
    var s_own_nb_nf = seenOwn(results[2], 0.7);
    var s_other_nb_nf = seenOther(results[2], 0.7);
    var s_own_nb = seenOwn(results[3], 0.7);
    var s_other_nb= seenOther(results[3], 0.7);

    // Chart creation
    var ctx2 = $("#chart2").get(0).getContext("2d");
    var data2 = {
        labels: [
            "Seen own",
            "Seen other"
        ],
        datasets: [
            {
                label: "With filter",
                fillColor: "#9b59b6",
                highlightFill: "#DDB9EB",
                data: [s_own_nb, s_own_nb_nf]
            },
            {
                label: "Without filter",
                fillColor: "#e67e22",
                highlightFill: "#FFB878",
                data: [s_other_nb, s_other_nb_nf]
            }
        ]
    }
    var chart2 = new Chart(ctx2).Bar(data2, barOptions);

    // Info
    var difference_nb = ((s_own_nb - s_other_nb) / s_other_nb * 100).toFixed(2);
    var difference_nb_nf = ((s_own_nb_nf - s_other_nb_nf) / s_other_nb_nf * 100).toFixed(2);
    $("#info2").append("<p>Parameters1: " + parameters[2].join(", ") + "</p>");
    $("#info2").append("<p>Parameters2: " + parameters[3].join(", ") + "</p>");
    $("#info2").append("<p>Difference with filter: " + difference_nb + "%</p>");
    $("#info2").append("<p>Difference without filter: " + difference_nb_nf + "%</p>");
}

// Helpers

function getParameters(num) {
    return $.get("../Results/params" + num + ".json");
}

function getResults(num) {
    return $.get("../Results/results" + num + ".json");
}

function mean(array) {
    var sum = 0;
    for (var ii = 0; ii < array.length; ii++) {
        sum += array[ii];
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

function seenOwn(results, limit) {
    var ret = [];
    var people = getAllPeople(results);
    for (var ii = 0; ii < people.length; ii++) {
        var person = people[ii];
        if (limit == "both") {
            if (person.interests.A != 0) {
                for (var type = 0; type < person.seen.A.length; type++) {
                    ret.push(person.seen.A[type][0]);
                }
            }
        }
        else {
            if (person.interests.A == limit) {
                for (var type = 0; type < person.seen.A.length; type++) {
                    ret.push(person.seen.A[type][0]);
                }
            }
        }
    }
    return mean(ret);
}

function seenOther(results, limit) {
    var ret = []
    var people = getAllPeople(results);
    for (var ii = 0; ii < people.length; ii++) {
        var person = people[ii];
        if (limit == "both") {
            if (person.interests.A != 0) {
                for (var type = 0; type < person.seen.A.length; type++) {
                    ret.push(person.seen.A[type][1]);
                }
            }
        }
        else {
            if (person.interests.A == limit) {
                for (var type = 0; type < person.seen.A.length; type++) {
                    ret.push(person.seen.A[type][1]);
                }
            }
        }
    }
    return mean(ret);
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
