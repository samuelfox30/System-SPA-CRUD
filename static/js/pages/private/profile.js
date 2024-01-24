function selecionarTodos() {
    var checkboxes = document.querySelectorAll('tbody input[type="checkbox"]');
    var checkSelecionarTodos = document.getElementById('checkSelecionarTodos');

    checkboxes.forEach(function (checkbox) {
        checkbox.checked = checkSelecionarTodos.checked;
    });
}