$(document).ready(function(){
    $.when(
        getResults(16),
        getResults(17),
        getResults(18),
        getResults(19),
        getResults(20),
        getResults(21)
    ).done(function(r1, r2, r3, r4, r5, r6) {
        main([r1[0], r2[0], r3[0], r4[0], r5[0], r6[0]]);
    });
});

function main(resultsJSON) {

    var results = [
        JSON.parse(resultsJSON[0]),
        JSON.parse(resultsJSON[1]),
        JSON.parse(resultsJSON[2]),
        JSON.parse(resultsJSON[3]),
        JSON.parse(resultsJSON[4]),
        JSON.parse(resultsJSON[5])
    ];

    // DATA
    // =========================

    var s_same = [];
    var s_other = [];
    var s_difference = [];

    for (var result = 0; result < results.length; result++) {
        s_same.push(s_same_pref(results[result], 0.4));
        s_other.push(s_other_pref(results[result], 0.4));

        var dif = ((s_same[result] - s_other[result]) / s_other[result] * 100).toFixed(2);
        s_difference.push(dif);
    }

    // CHART 1
	// =========================


    // Chart creation
    var ctx1 = $("#chart1").get(0).getContext("2d");
    var data1 = {
        labels: [
            "Don't prefer",
            "Prefer",
            "Prefer strongly"
        ],
        datasets: [
            {
                label: "Don't prefer",
                fillColor: "#3498db",
                highlightFill: "#85C4ED",
                data: [s_difference[0], s_difference[2], s_difference[4]]
            },
            {
                label: "Prefer",
                fillColor: "#2ecc71",
                highlightFill: "#51D88C",
                data: [s_difference[1], s_difference[3], s_difference[5]]
            }
        ]
    }
    var chart1 = new Chart(ctx1).Bar(data1, barOptions);
}
