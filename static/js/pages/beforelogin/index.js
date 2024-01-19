// Fechar aba anterior ao abrir uma nova
$('#turmasTabs a').on('click', function (e) {
    e.preventDefault();
    $(this).tab('show');
});