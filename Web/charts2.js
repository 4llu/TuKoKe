$(document).ready(function(){
    $.when(
        getResults(2),
        getResults(3),
        getResults(4),
        getResults(5),
        getResults(6),
        getResults(7),
        getResults(8),
        getResults(9),
        getResults(10),
        getResults(11),
        getResults(12),
        getResults(13),
        getResults(14),
        getResults(15)
    ).done(function(r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13) {
        main([r0[0], r1[0], r2[0], r3[0], r4[0], r5[0], r6[0], r7[0], r8[0], r9[0], r10[0], r11[0], r12[0], r13[0]]);
    });
});

function main(resultsJSON) {

    var results = [
        JSON.parse(resultsJSON[0]),
        JSON.parse(resultsJSON[1]),
        JSON.parse(resultsJSON[2]),
        JSON.parse(resultsJSON[3]),
        JSON.parse(resultsJSON[4]),
        JSON.parse(resultsJSON[5]),
        JSON.parse(resultsJSON[6]),
        JSON.parse(resultsJSON[7]),
        JSON.parse(resultsJSON[8]),
        JSON.parse(resultsJSON[9]),
        JSON.parse(resultsJSON[10]),
        JSON.parse(resultsJSON[11]),
        JSON.parse(resultsJSON[12]),
        JSON.parse(resultsJSON[13]),
    ];

    // DATA
    // =========================

    var s_same = [];
    var s_other = [];
    var s_difference = [];

    console.log(results[0])
    console.log(s_same_pref(results[0][0], 0.4));

    for (var result = 0; result < results.length; result++) {
        s_same.push(s_same_pref(results[result], 0.4));
        s_other.push(s_other_pref(results[result], 0.4));

        var dif = ((s_same[result] - s_other[result]) / s_other[result] * 100).toFixed(2);
        s_difference.push(dif);
    }
    // console.log(s_difference);



    // CHART 1
	// =========================

    // Chart creation
    var ctx1 = $("#chart1").get(0).getContext("2d");
    var data1 = {
        labels: [
            "0",
            "0.02",
            "0.04",
            "0.06",
            "0.08",
            "0.1",
            "0.12"

        ],
        datasets: [
            {
                label: "Without filter",
                fillColor: "rgba(0, 0, 0, 0)",
                strokeColor: "#3498db",
                pointColor: "#3498db",
                pointStrokeColor: "#fff",
                pointHighlightFill: "#fff",
                pointHighlightStroke: "#3498db",
                data: [
                    s_difference[0],
                    s_difference[1],
                    s_difference[2],
                    s_difference[3],
                    s_difference[4],
                    s_difference[5],
                    s_difference[6]
                ]
            },
            {
                label: "Without filter",
                fillColor: "rgba(0, 0, 0, 0)",
                strokeColor: "#2ecc71",
                pointColor: "#2ecc71",
                pointStrokeColor: "#fff",
                pointHighlightFill: "#fff",
                pointHighlightStroke: "#2ecc71",
                data: [
                    s_difference[7],
                    s_difference[8],
                    s_difference[9],
                    s_difference[10],
                    s_difference[11],
                    s_difference[12],
                    s_difference[13]
                ]
            }
        ]
    }
    var chart1 = new Chart(ctx1).Line(data1, lineOptions);
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
