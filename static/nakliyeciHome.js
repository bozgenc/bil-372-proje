function update(id,ad_soyad, odeme_miktari, urun_miktari, aciklama, plaka,) {
    var input = document.getElementById("miktar");
    var input2 = document.getElementById("odeme");
    var input3 = document.getElementById("aciklama");
    var input4 = document.getElementById("arac");
    var input5 = document.getElementById("uretici");

    var cancel_button = document.getElementById("cancel_button");
    var isInsert = document.getElementById("isInsert");
    isInsert.value = id;
    cancel_button.style.visibility = "visible"
    input.value = urun_miktari;
    input2.value = odeme_miktari;
    input3.value = aciklama;
    input4.value = plaka;
    input5.value = plaka;

}

function cancel() {
    var input = document.getElementById("miktar");
    var input2 = document.getElementById("odeme");
    var input3 = document.getElementById("aciklama");
    var input4 = document.getElementById("plaka");
    var input5 = document.getElementById("uretici");

    var cancel_button = document.getElementById("cancel_button");
    var isInsert = document.getElementById("isInsert");
    isInsert.value = '0';
    cancel_button.style.visibility = "hidden"
    input.value = '';
    input2.value = '';
    input3.value = '';
    input4.value = '';
    input5.value = '';
}