function update(tur_id, islem_ismi) {
    var input = document.getElementById("tur_id");
    var input2 = document.getElementById("islem_ismi");

    var cancel_button = document.getElementById("cancel_button");
    var isInsert = document.getElementById("isInsert");
    isInsert.value = tur_id;
    cancel_button.style.visibility = "visible"
    input.value = tur_id;
    input2.value = islem_ismi;
    document.getElementById("tur_id").setAttribute("readonly", true)
}

function cancel() {
    var input = document.getElementById("tur_id");
    var input2 = document.getElementById("islem_ismi");

    var cancel_button = document.getElementById("cancel_button");
    var isInsert = document.getElementById("isInsert");
    isInsert.value = '0';
    cancel_button.style.visibility = "hidden"
    input.value = '';
    input2.value = '';
}