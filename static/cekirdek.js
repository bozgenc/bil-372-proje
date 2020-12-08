function update(id,koken,miktar,tur,) {
    var input = document.getElementById("koken");
    var input2 = document.getElementById("miktar");
    var input3 = document.getElementById("tur");


    var cancel_button = document.getElementById("cancel_button");
    var isInsert = document.getElementById("isInsert");
    isInsert.value = id;
    cancel_button.style.visibility = "visible"
    input.value = koken;
    input2.value = miktar;
    input3.value = tur;


}

function cancel() {
    var input = document.getElementById("koken");
    var input2 = document.getElementById("miktar");
    var input3 = document.getElementById("tur");


    var cancel_button = document.getElementById("cancel_button");
    var isInsert = document.getElementById("isInsert");
    isInsert.value = '0';
    cancel_button.style.visibility = "hidden"
    input.value = '';
    input2.value = '';
    input3.value = '';

}