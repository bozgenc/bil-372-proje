function update(id,tur,gramaj,skt,) {
    var input = document.getElementById("tur");
    var input2 = document.getElementById("gramaj");
    var input3 = document.getElementById("skt");


    var cancel_button = document.getElementById("cancel_button");
    var isInsert = document.getElementById("isInsert");
    isInsert.value = id;
    cancel_button.style.visibility = "visible"
    input.value = tur;
    input2.value = gramaj;
    input3.value = skt;


}

function cancel() {
    var input = document.getElementById("tur");
    var input2 = document.getElementById("gramaj");
    var input3 = document.getElementById("skt");


    var cancel_button = document.getElementById("cancel_button");
    var isInsert = document.getElementById("isInsert");
    isInsert.value = '0';
    cancel_button.style.visibility = "hidden"
    input.value = '';
    input2.value = '';
    input3.value = '';

}