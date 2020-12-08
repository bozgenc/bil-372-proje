function update(tckn, giren, cikan, islem_suresi, id) {
    var input = document.getElementById("sorumlu_koordinator_tckn");
    var input2 = document.getElementById("giren_miktar");
    var input3 = document.getElementById("cikan_miktar");
    var input4 = document.getElementById("islem_suresi");

    var cancel_button = document.getElementById("cancel_button");
    var isInsert = document.getElementById("isInsert");
    isInsert.value = id;
    cancel_button.style.visibility = "visible"
    input.value = tckn;
    input2.value = giren;
    input3.value = cikan;
    input4.value = islem_suresi;

    document.getElementById("islem_suresi").setAttribute("readonly", true)
    document.getElementById("cikan_miktar").setAttribute("readonly", true)
    document.getElementById("bitti").setAttribute("readonly", true)

}

function update2(tckn, giren, cikan, islem_suresi, id) {
    var input = document.getElementById("sorumlu_koordinator_tckn");
    var input2 = document.getElementById("giren_miktar");
    var input3 = document.getElementById("cikan_miktar");
    var input4 = document.getElementById("islem_suresi");

    var label1 = document.getElementById("label1");
    var label2 = document.getElementById("label2");

    input3.style.visibility = "visible"
    input4.style.visibility = "visible"
    label1.style.visibility = "visible"
    label2.style.visibility = "visible"


    var cancel_button = document.getElementById("cancel_button");
    var isInsert = document.getElementById("isInsert");
    isInsert.value = id;
    cancel_button.style.visibility = "visible"
    input.value = tckn;
    input2.value = giren;
    input3.value = cikan;
    input4.value = islem_suresi;
    document.getElementById("sorumlu_koordinator_tckn").setAttribute("readonly", true)
    document.getElementById("giren_miktar").setAttribute("readonly", true)
}

function cancel() {
    var input = document.getElementById("sorumlu_koordinator_tckn");
    var input2 = document.getElementById("giren_miktar");
    var input3 = document.getElementById("cikan_miktar");
    var input4 = document.getElementById("islem_suresi");
    var label1 = document.getElementById("label1");
    var label2 = document.getElementById("label2");
    var cancel_button = document.getElementById("cancel_button");
    var isInsert = document.getElementById("isInsert");

    isInsert.value = '0';
    cancel_button.style.visibility = "hidden"
    input3.style.visibility = "hidden"
    input4.style.visibility = "hidden"
    label1.style.visibility = "hidden"
    label2.style.visibility = "hidden"

    input.value = '';
    input2.value = '';
    input3.value = '';
    input4.value = '';
    document.getElementById("sorumlu_koordinator_tckn").removeAttribute("readOnly");
    document.getElementById("giren_miktar").removeAttribute("readOnly");
    document.getElementById("islem_suresi").removeAttribute("readOnly");
    document.getElementById("cikan_miktar").removeAttribute("readOnly");
    document.getElementById("bitti").removeAttribute("readOnly");






}