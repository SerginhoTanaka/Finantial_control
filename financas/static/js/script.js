function mostrarTabela() {
    var tabela = document.getElementsByClassName("minhaTabela");
    if (tabela.style.display === "none") {
        tabela.style.display = "table"; 
    } else {
        tabela.style.display = "none"; 
    }
}