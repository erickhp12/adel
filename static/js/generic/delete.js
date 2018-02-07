function deletePatient(){
    usuario = document.getElementById('idBorrar').innerHTML;
    $.ajax({
        type: "GET",
        url: "/deletePatient/"+usuario+"/",
        success: function(data) {
        $('#modal-borrar').modal('hide');
        location.reload();
        for(i = 0; i < data.length; i++){
            $('ul').append('<li>'+data[i]+'</li>');
        }
    }
    });
}

function deleteVisit(){
    item = document.getElementById('idBorrar').innerHTML;
    $.ajax({
        type: "GET",
        url: "/deleteVisit/"+item+"/",
        success: function(data) {
        $('#modal-borrar').modal('hide');
        location.reload();
        for(i = 0; i < data.length; i++){
            $('ul').append('<li>'+data[i]+'</li>');
        }
    }
    });
}

function deleteSpending(){
    item = document.getElementById('idBorrar').innerHTML;
    $.ajax({
        type: "GET",
        url: "/deleteSpending/"+item+"/",
        success: function(data) {
        $('#modal-borrar').modal('hide');
        location.reload();
        for(i = 0; i < data.length; i++){
            $('ul').append('<li>'+data[i]+'</li>');
        }
    }
    });
}

function deleteProvider(){
    item = document.getElementById('idBorrar').innerHTML;
    $.ajax({
        type: "GET",
        url: "/deleteProvider/"+item+"/",
        success: function(data) {
        $('#modal-borrar').modal('hide');
        location.reload();
        for(i = 0; i < data.length; i++){
            $('ul').append('<li>'+data[i]+'</li>');
        }
    }
    });
}

function deleteEmployee(){
    item = document.getElementById('idBorrar').innerHTML;
    $.ajax({
        type: "GET",
        url: "/deleteEmployee/"+item+"/",
        success: function(data) {
        $('#modal-borrar').modal('hide');
        location.reload();
        for(i = 0; i < data.length; i++){
            $('ul').append('<li>'+data[i]+'</li>');
        }
    }
    });
}

function deleteAgenda(){
    item = document.getElementById('idBorrar').innerHTML;
    $.ajax({
        type: "GET",
        url: "/deleteAgenda/"+item+"/",
        success: function(data) {
        $('#modal-borrar').modal('hide');
        location.reload();
        for(i = 0; i < data.length; i++){
            $('ul').append('<li>'+data[i]+'</li>');
        }
    }
    });
}

function deleteReceipt(){
    item = document.getElementById('idBorrar').innerHTML;
    $.ajax({
        type: "GET",
        url: "/deleteReceipt/"+item+"/",
        success: function(data) {
        $('#modal-borrar').modal('hide');
        location.reload();
        for(i = 0; i < data.length; i++){
            $('ul').append('<li>'+data[i]+'</li>');
        }
    }
    });
}