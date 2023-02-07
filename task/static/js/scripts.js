$(document).ready(function(){
    var baseUrl = 'http://127.0.0.1:8000'
    var deleteBtn = $('#deleteBtn')
    var searchBtn = $('#search-btn')
    var searchForm = $('#search-form')
    var filter = $('#filter')

    $(deleteBtn).on('click', function(e){
        e.preventDefault()

        var delLink = $(this).attr('href')
        var resultado = confirm('Deseja deletar essa tarefa?')

        if(resultado){
            window.location.href = delLink;
        }
    })

    $(searchBtn).on('click', function(){
        searchForm.submit()
    })

    $(filter).change(function(){
        var filtro = $(this).val()
        window.location.href = baseUrl + '?filter=' + filtro
    })
})