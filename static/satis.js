function update(alici_sirket_id,ucret,tarih,miktar) {
    var input = document.getElementById("alici_sirket_id");
    var input2 = document.getElementById("ucret");
    var input3 = document.getElementById("tarih");
    var input4 = document.getElementById("miktar");


    var cancel_button = document.getElementById("cancel_button");
    var isInsert = document.getElementById("isInsert");
    isInsert.value = id;
    cancel_button.style.visibility = "visible"
    input.value = alici_sirket_id;
    input2.value = ucret;
    input3.value = tarih;
    input4.value = miktar;


}

function cancel() {
    var input = document.getElementById("alici_sirket_id");
    var input2 = document.getElementById("ucret");
    var input3 = document.getElementById("tarih");
    var input4 = document.getElementById("miktar");


    var cancel_button = document.getElementById("cancel_button");
    var isInsert = document.getElementById("isInsert");
    isInsert.value = '0';
    cancel_button.style.visibility = "hidden"
    input.value = '';
    input2.value = '';
    input3.value = '';
    input4.value = '';
