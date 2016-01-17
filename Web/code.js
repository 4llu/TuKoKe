$(document).ready(function(){
    $.when(
        getParameters(1),
        getParameters(2),
        getResults(1),
        getResults(2)
    ).done(function(p1, p2, r1, r2) {
        main([p1[0], p2[0]], [r1[0], r2[0]]);
    });
});

function main(parameters, results) {
    console.log(results[0]);
    console.log(results[1]);
    var seen_own_filter = seenOwn(results[0], 0.7);
    var seen_own_filter_no = seenOwn(results[1], 0.7);
    var seen_other_filter = seenOther(results[0], 0.7);
    var seen_other_filter_no = seenOther(results[1], 0.7);
    // Population set

    console.log(average(seen_own_filter));
    console.log(average(seen_own_filter_no));
    console.log(average(seen_other_filter));
    console.log(average(seen_other_filter_no));
}

// Helpers

function getParameters(num) {
    return $.get("../Results/params" + num + ".json");
}

function getResults(num) {
    return $.get("../Results/results" + num + ".json");
}

function average(array) {
    var sum = 0;
    for (var ii = 0; ii < array.length; ii++) {
        sum += array[ii];
    }
    return sum / array.length;
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
    return ret;
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
    return ret;
}
