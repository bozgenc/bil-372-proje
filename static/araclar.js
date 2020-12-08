function update(plaka, kapasite, id) {
    var input = document.getElementById("plaka");
    var input2 = document.getElementById("kapasite");

    input.setAttribute("readonly", true)
    var cancel_button = document.getElementById("cancel_button");
    var isInsert = document.getElementById("isInsert");
    isInsert.value = id;
    cancel_button.style.visibility = "visible"
    input.value = plaka;
    input2.value = kapasite;

}

function cancel() {
    var input = document.getElementById("plaka");
    var input2 = document.getElementById("kapasite");

    input.removeAttribute("readOnly");
    var cancel_button = document.getElementById("cancel_button");
    var isInsert = document.getElementById("isInsert");
    isInsert.value = '0';
    cancel_button.style.visibility = "hidden"
    input.value = '';
    input2.value = '';
}