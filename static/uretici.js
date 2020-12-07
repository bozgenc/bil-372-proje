function update(ad_soyad, tckn, koy, tel_no) {
    var input = document.getElementById("ad_soyad");
    var input2 = document.getElementById("tckn");
    var input3 = document.getElementById("koy");
    var input4 = document.getElementById("tel_no");

    var cancel_button = document.getElementById("cancel_button");
    var isInsert = document.getElementById("isInsert");
    isInsert.value = '5';
    cancel_button.style.visibility = "visible"
    input.value = ad_soyad;
    input2.value = tckn;
    input3.value = koy;
    input4.value = tel_no;

}

function cancel() {
    var input = document.getElementById("ad_soyad");
    var input2 = document.getElementById("tckn");
    var input3 = document.getElementById("koy");
    var input4 = document.getElementById("tel_no");

    var cancel_button = document.getElementById("cancel_button");
    var isInsert = document.getElementById("isInsert");
    isInsert.value = '0';
    cancel_button.style.visibility = "hidden"
    input.value = '';
    input2.value = '';
    input3.value = '';
    input4.value = '';
}