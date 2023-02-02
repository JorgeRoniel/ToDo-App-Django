deleteBtn = document.getElementById('deleteBtn')
searchBtn = document.getElementById('search-btn')
searchForm = document.getElementById('search-form')

deleteBtn.onclick = function(e){
    e.preventDefault();

    var delLink = this.getAttribute('href');
    var confirmacao = confirm('Voce deseja mesmo apagar essa tarefa?');

    if(confirmacao){
        window.location.href = delLink;
    }
}

searchBtn.onclick = function(){
    searchForm.submit();
}