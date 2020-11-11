
function createMatrix(rows, cols, id_mariz) {
    var content = ""
    for ( r = 0; r < rows; r++){
        content += "<tr>";
        for(c = 0; c < cols; c++){
            content += "<td><input type='number' style = 'width: 40px;-webkit-appearance: none;'></td> ";
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
    $('#matrizUno').empty();
    var rows = $('#rowsUno').val();
    var cols = $('#colsUno').val();
    if(rows == ""){
        alert("Digite el numero de filas y columnas correcto !!!");
    }else{
        createMatrix(rows, cols, "matrizUno");
    }
    
});
$( "#btnOkDos" ).on( "click", function() {
    $('#matrizDos').empty(); 
    var rows = $('#rowsUno').val();
    var cols = $('#colsUno').val();
    if(rows == ""){
        alert("Digite el numero de filas y columnas correcto !!!");
    }else{
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
        alert("NO se han creado las matrices ");
    }else{
        if(rowsCols[0][0] == rowsCols[1][0] && rowsCols[0][1] == rowsCols[1][1]){
            alert("alv : "+getMatrix('matrizUno'));
            
        }else{
            alert("las filas y columnas de las matrices deben ser iguales!!"); 
        }
    }
});

function getMatrix(nametable){
    var dats = [];
    $('#'+nametable+' tr').each(function (index){
        var row = [];

        $($(this).find('td')).each(function (){
            row.push($(this).find('input').val());
        });
        dats.push(row);

    });
    return dats;
}

//--------------------------------------------------------------------------------------------------------
$( "#btnRest" ).on( "click", function() {
    var rowsCols = getRowsCols();

    if(rowsCols[0].includes(NaN) || rowsCols[1].includes(NaN) ){
        alert("NO se han creado las matrices ");
    }else{
        if(rowsCols[0][0] == rowsCols[1][0] && rowsCols[0][1] == rowsCols[1][1]){
            alert("alv"+rowsCols);
        }else{
            alert("las filas y columnas de las matrices deben ser iguales!!");
        }
    }
});

