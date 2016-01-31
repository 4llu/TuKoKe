$(document).ready(function(){
    $.when(
        getParameters(0),
        getResults(0),
        getParameters(1),
        getResults(1)
    ).done(function(p0, r0, p1, r1) {
        main([p0[0], p1[0]], [r0[0], r1[0]]);
    });
});

function main(parametersJSON, resultsJSON) {

    var results = [
        JSON.parse(resultsJSON[0]),
        JSON.parse(resultsJSON[1])
    ];

    var parameters = [
        JSON.parse(parametersJSON[0]),
        JSON.parse(parametersJSON[1])
    ];

    // DATA
    // =========================

    var s_same = s_same_pref(results[0], 0.4);
    var s_same_nf = s_same_pref(results[1], 0.4);
    var s_other = s_other_pref(results[0], 0.4);
    var s_other_nf = s_other_pref(results[1], 0.4);

    // CHART 1
	// =========================


    // Chart creation
    var ctx1 = $("#chart1").get(0).getContext("2d");
    var data1 = {
        labels: [
            "Seen same",
            "Seen other"
        ],
        datasets: [
            {
                label: "With filter",
                fillColor: "#3498db",
                highlightFill: "#85C4ED",
                data: [s_same_nf, s_same]
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

	// CHART 2
	// =========================

    // numbers
    // var difference_nf = ((s_same_nf - s_other_nf) / s_other_nf).toFixed(2);
    // var difference_f = ((s_same - s_other) / s_other).toFixed(2);
    var difference_nf = ((s_same_nf - s_other_nf) / s_other_nf * 100).toFixed(2);
    var difference_f = ((s_same - s_other) / s_other * 100).toFixed(2);

    // Chart creation
    var ctx1 = $("#chart2").get(0).getContext("2d");
    var data1 = {
        labels: [
            "Difference between preferences"
        ],
        datasets: [
            {
                label: "With filter",
                fillColor: "#3498db",
                highlightFill: "#85C4ED",
                data: [difference_nf]
            },
            {
                label: "With filter",
                fillColor: "#2ecc71",
                highlightFill: "#51D88C",
                data: [difference_f]
            }
        ]
    }
    var chart1 = new Chart(ctx1).Bar(data1, barOptions);
}

// FUNCTIONS
// =======================

function s_same_pref(results, limit) {
    var ret = [];
    var people = getAllPeople(results);
    for (var ii = 0; ii < people.length; ii++) {
        var person = people[ii];
        if (person.interests.A >= limit) {
            for (var type = 0; type < person.seen.A.length; type++) {
                ret.push(person.seen.A[type][0]);
            }
        }
    }
    return mean(ret);
}

function s_other_pref(results, limit) {
    var ret = [];
    var people = getAllPeople(results);
    for (var ii = 0; ii < people.length; ii++) {
        var person = people[ii];
        if (person.interests.A >= limit) {
            for (var type = 0; type < person.seen.A.length; type++) {
                ret.push(person.seen.A[type][1]);
            }
        }
    }
    return mean(ret);
}
