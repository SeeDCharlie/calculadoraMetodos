
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

