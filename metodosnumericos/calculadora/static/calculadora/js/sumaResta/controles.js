
function createMatrix(rows, cols, id_mariz) {
    var content = ""
    for ( r = 0; r < rows; r++){
        content += "<tr>";
        for(c = 0; c < cols; c++){
            content += "<td><input type='number' style = 'width: 40px;-webkit-appearance: none;'> ";
        }
        content += "</tr>";
    }
    

    $('#'+id_mariz).append(content);
}

function getRowsCols(){
    var dat = [[parseInt($('#rowsUno').val(), 10),parseInt($('#colsUno').val(),10)],
                [parseInt($('#rowsDos').val(),10),parseInt($('#colsDos').val(),10)]];
    return dat;
}


$( "#btnOkUno" ).on( "click", function() {
    var rows = $('#rowsUno').val();
    var cols = $('#colsUno').val();
    if(rows == ""){
        alert("Digite el numero de filas y columnas correcto !!!");
    }else{
        console.log( "create matriz uno" );
        createMatrix(rows, cols, "matrizUno");
    }
    
});
$( "#btnOkDos" ).on( "click", function() {
    var rows = $('#rowsUno').val();
    var cols = $('#colsUno').val();
    if(rows == ""){
        alert("Digite el numero de filas y columnas correcto !!!");
    }else{
        console.log( "create matriz uno" );
        createMatrix(rows, cols, "matrizDos");
    }
    
});
$( "#btnDeleteOne" ).on( "click", function() {
    $('#matrizUno').empty();
    
});
$( "#btnDeleteTwo" ).on( "click", function() {
    $('#matrizDos').empty();    
});


$( "#btnSum" ).on( "click", function() {
    var rowsCols = getRowsCols();

    if(rowsCols[0].includes(NaN) || rowsCols[1].includes(NaN) ){
        alert("NO se han creado las matrices correctamente");
    }else{
        if(rowsCols[0][0] == rowsCols[1][0] && rowsCols[0][1] == rowsCols[1][1]){
            alert("alv"+rowsCols);
            
        }else{
            alert("las filas y columnas de las matrices deben ser iguales!!"); 
        }
    }

    

});
$( "#btnRest" ).on( "click", function() {
       
});

