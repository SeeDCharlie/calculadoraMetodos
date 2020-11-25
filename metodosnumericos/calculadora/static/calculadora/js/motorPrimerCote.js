function graficarFuncion(funcion, a, b, nameImg){

    $("#"+nameImg).attr("src","/grafica/"+funcion+"/"+a+"/"+b);
    
}

function calcEcua(btnName,datos, ouUno, ouDos, ouTres){
    $.ajax({
        url: $('#'+btnName).attr('url'),
        data: {
            dats:datos,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            action: 'post'
        },
        type: 'POST',
        dataType: 'json',
        success: function (data) {
            if (data.success) {

                $("#"+ouUno).val(data.uno);
                $("#"+ouDos).val(data.dos);
                $("#"+ouTres).val(data.tres);
            }
            else {
                alert('error');
            }
        },
        error: function () {
            alert("Incongruencia en los datos!!");
        }
    });
}

//-------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------
//-------// metodos de biseccion


$("#btnGraficarBise").on("click", function(){
    var funcion = $("#ecuaBise").val();
    if(funcion != null && funcion != ""){
        graficarFuncion(funcion, -12, 12, "imgUnoBisec");
    }
    else{   
        alert("Ingrese Una funcion");
    }
});

$("#btnIntervalosBise").on("click", function(){

    var funcion = $("#ecuaBise").val();
    var a = $("#inaBise").val();
    var b = $("#inbBise").val();

    if(funcion != null && funcion != "" && a != "" && b != ""){
        graficarFuncion(funcion, a, b, "imgDosBisec");
    }
    else{
        
        alert("Ingrese Una funcion");
    }

});

$( "#btnCalcularBise" ).on( "click", function() {

    var ecuacion = $('#ecuaBise').val();
    var _a = $('#inaBise').val();
    var _b = $('#inbBise').val();
    var _n = $('#erToBise').val();
    var datos = JSON.stringify({
        funcion:ecuacion,
        a:_a,
        b:_b,
        error:_n
    });
    calcEcua("btnCalcularBise", datos,"reBise", "errBise", "" );

});

//-------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------
//-------// metodos de falsa pocicion


$("#btnGraficarFalP").on("click", function(){
    var funcion = $("#ecuaFalP").val();
    if(funcion != null && funcion != ""){
        graficarFuncion(funcion, -12, 12, "imgUnoFalP");
    }
    else{   
        alert("Ingrese Una funcion");
    }
});

$("#btnIntervalosFalP").on("click", function(){

    var funcion = $("#ecuaFalP").val();
    var a = $("#inaFalP").val();
    var b = $("#inbFalP").val();

    if(funcion != null && funcion != "" && a != "" && b != ""){
        graficarFuncion(funcion, a, b, "imgDosFalP");
    }
    else{
        
        alert("Ingrese Una funcion");
    }

});

$( "#btnCalcularFalP" ).on( "click", function() {

    var ecuacion = $('#ecuaFalP').val();
    var _a = $('#inaFalP').val();
    var _b = $('#inbFalP').val();
    var _n = $('#erToFalP').val();
    var datos = JSON.stringify({
        funcion:ecuacion,
        a:_a,
        b:_b,
        error:_n
    });
    calcEcua("btnCalcularFalP", datos,"reFalP", "errFalP", "" );

});

//-------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------
//-------// metodos de newton rhapson


$("#btnGraficarNew").on("click", function(){
    var funcion = $("#ecuaNew").val();
    if(funcion != null && funcion != ""){
        graficarFuncion(funcion, -12, 12, "imgUnoNew");
    }
    else{   
        alert("Ingrese Una funcion");
    }
});

$( "#btnCalcularNew" ).on( "click", function() {

    var ecuacion = $('#ecuaNew').val();
    var _a = $('#vaXNew').val();
    var _n = $('#erToNew').val();
    var datos = JSON.stringify({
        funcion:ecuacion,
        valor_x:_a,
        error:_n
    });
    calcEcua("btnCalcularNew", datos,"reNew", "errNew", "" );

});