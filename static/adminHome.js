function update(tckn, ad, soyad, tel_no, email) {
    var input = document.getElementById("tckn");
    var input2 = document.getElementById("ad");
    var input3 = document.getElementById("soyad");
    var input4 = document.getElementById("tel_no");
    var input5 = document.getElementById("email");

    var cancel_button = document.getElementById("cancel_button");
    var isInsert = document.getElementById("isInsert");
    isInsert.value = tckn;
    cancel_button.style.visibility = "visible"
    input.value = tckn;
    input2.value = ad;
    input3.value = soyad;
    input4.value = tel_no;
    input5.value = email;
    document.getElementById("tckn").setAttribute("readonly", true)
}

function cancel() {
    var input = document.getElementById("tckn");
    var input2 = document.getElementById("ad");
    var input3 = document.getElementById("soyad");
    var input4 = document.getElementById("tel_no");
    var input5 = document.getElementById("email");

    var cancel_button = document.getElementById("cancel_button");
    var isInsert = document.getElementById("isInsert");
    isInsert.value = '0';
    cancel_button.style.visibility = "hidden"
    input.value = '';
    input2.value = '';
    input3.value = '';
    input4.value = '';
    input5.value = '';
    document.getElementById("tckn").removeAttribute("readonly");
}