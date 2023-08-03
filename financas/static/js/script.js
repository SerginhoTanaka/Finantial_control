function mostrarTabela() {
    var tabela = document.getElementById("minhaTabela");
    if (tabela.style.display === "none") {
        tabela.style.display = "table";
    } else {
        tabela.style.display = "none";
    }
}