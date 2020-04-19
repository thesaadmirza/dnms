// Empty JS for your own code to be here
		
$("label, a").each(function(index, tr) {
    var txt = tr.innerText.replace(":","");
    if (translator.hasOwnProperty(txt)) {
        tr.innerText = translator[tr.innerText.replace(":","")];
    }
});

$("option").each(function(index, tr) {
    var txt_array = tr.innerText.split("-");
    var output_array = [];
    for (var i = 0; i < txt_array.length; i++) {
        if (translator.hasOwnProperty(txt_array[i])) {
            output_array.push(translator[txt_array[i]]);
        } else {
            output_array.push(txt_array[i])
        }
    }
    tr.innerText = output_array.join("-");
});