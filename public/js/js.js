

function addComponent(id_e,id_p){
    $.ajax({
        url: '/pages/component/get',
        type: 'GET',
        data: {
            id_e: id_e,
            id_p: id_p
        },

        success: function(data){
            $('#editorBody').html(data);
            $('#openModalEditor').attr("onclick","");
            $('#openModalEditor').click();
        }
    })
}
