function update(sorumlu_koordinator_tckn, tur_id, giren_miktar, cikan_miktar, islem_suresi, bitti_mi) {

    var input = document.getElementById("sorumlu_koordinator_tckn");
    var input2 = document.getElementById("tur_id");
    var input3 = document.getElementById("giren_miktar");
    var input4 = document.getElementById("cikan_miktar");
    var input5 = document.getElementById("islem_suresi");
    var input6 = document.getElementById("bitti_mi");

    var cancel_button = document.getElementById("cancel_button");
    var isInsert = document.getElementById("isInsert");
    isInsert.value = tur_id;
    cancel_button.style.visibility = "visible"
    input.value = sorumlu_koordinator_tckn;
    input2.value = tur_id;
    input3.value = giren_miktar;
    input4.value = cikan_miktar;
    input5.value = islem_suresi;
    input6.value = bitti_mi;
}

function cancel() {
    var input = document.getElementById("sorumlu_koordinator_tckn");
    var input2 = document.getElementById("tur_id");
    var input3 = document.getElementById("giren_miktar");
    var input4 = document.getElementById("cikan_miktar");
    var input5 = document.getElementById("islem_suresi");
    var input6 = document.getElementById("bitti_mi");

    var cancel_button = document.getElementById("cancel_button");
    var isInsert = document.getElementById("isInsert");
    isInsert.value = '0';
    cancel_button.style.visibility = "hidden"
    input.value = '';
    input2.value = '';
    input3.value = '';
    input4.value = '';
    input5.value = '';
    input6.value = '';
}