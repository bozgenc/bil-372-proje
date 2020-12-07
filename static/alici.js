function update(sirket_adi) {
    var input = document.getElementById("sirket_adi");
    var input2 = document.getElementById("sirket_id");

    var cancel_button = document.getElementById("cancel_button");
    var isInsert = document.getElementById("isInsert");
    isInsert.value = id;
    cancel_button.style.visibility = "visible"
    input.value = sirket_adi;
    input2.value=sirket_id;


}

function cancel() {
    var input = document.getElementById("sirket_adi");
    var input2 = document.getElementById("sirket_id");

    var cancel_button = document.getElementById("cancel_button");
    var isInsert = document.getElementById("isInsert");
    isInsert.value = '0';
    cancel_button.style.visibility = "hidden"
    input.value = '';
    input2.value= '';

}