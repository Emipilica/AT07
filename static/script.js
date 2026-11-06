
// ==========================================
// CARREGAR E LISTAR MUNICÍPIOS
// ==========================================

async function carregarMunicipios() {

    const busca = document.getElementById("busca").value.toLowerCase();
    const uf = document.getElementById("filtroUF").value.trim();

    let url = "/municipios";

    if (uf) {
        url += "?uf=" + encodeURIComponent(uf);
    }

    const resposta = await fetch(url);
    const municipios = await resposta.json();

    const tabela = document.getElementById("listaMunicipios");

    tabela.innerHTML = "";

    let quantidade = 0;

    for (const [nome, dados] of Object.entries(municipios)) {

        if (!nome.toLowerCase().includes(busca)) {
            continue;
        }

        quantidade++;

        const linha = document.createElement("tr");

        const valores = [
            nome,
            dados.sigla_uf,
            dados.capital ? "Sim" : "Não",
            dados.populacao_estimada.toLocaleString("pt-BR"),
            dados.id_ibge
        ];

        valores.forEach((valor, indice) => {

            const celula = document.createElement("td");

            celula.textContent = valor;

            if (indice === 2) {
                celula.className = dados.capital
                    ? "capital-sim"
                    : "capital-nao";
            }

            linha.appendChild(celula);
        });

        const acoes = document.createElement("td");

        const botaoEditar = document.createElement("button");

        botaoEditar.className = "btn btn-sm btn-editar me-1";
        botaoEditar.textContent = "Editar";
        botaoEditar.onclick = () => editarMunicipio(nome);

        const botaoExcluir = document.createElement("button");

        botaoExcluir.className = "btn btn-sm btn-excluir";
        botaoExcluir.textContent = "Excluir";
        botaoExcluir.onclick = () => excluirMunicipio(nome);

        acoes.appendChild(botaoEditar);
        acoes.appendChild(botaoExcluir);

        linha.appendChild(acoes);
        tabela.appendChild(linha);
    }

    // TOTAL GERAL, INDEPENDENTE DOS FILTROS

    const respostaTotal = await fetch("/municipios");
    const todosMunicipios = await respostaTotal.json();

    document.getElementById("total").textContent =
        Object.keys(todosMunicipios).length;

    document.getElementById("mensagemLista").textContent =
        quantidade === 0 ? "Nenhum município encontrado." : "";
}


// ==========================================
// CADASTRAR OU ATUALIZAR MUNICÍPIO
// ==========================================

document.getElementById("formMunicipio").addEventListener(
    "submit",
    async function(event) {

        event.preventDefault();

        const nome = document.getElementById("nome").value.trim();

        const nomeOriginal =
            document.getElementById("nomeOriginal").value;

        const dados = {

            nome: nome,

            id_ibge: document.getElementById("id_ibge").value,

            estado: document.getElementById("estado").value,

            sigla_uf: document.getElementById("sigla_uf").value,

            capital: document.getElementById("capital").checked,

            populacao_estimada:
                document.getElementById("populacao").value
        };

        let url = "/municipios";
        let metodo = "POST";

        if (nomeOriginal) {

            url = "/municipios/" + encodeURIComponent(nomeOriginal);

            metodo = "PATCH";

            delete dados.nome;
        }

        const resposta = await fetch(url, {

            method: metodo,

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(dados)
        });

        const resultado = await resposta.json();

        alert(resultado.mensagem || resultado.erro);

        if (resposta.ok) {
            limparFormulario();
            carregarMunicipios();
        }
    }
);


// ==========================================
// BUSCAR MUNICÍPIO PELO NOME
// ==========================================

async function buscarPorNome() {

    const nome = document.getElementById("nome").value.trim();

    if (!nome) {
        alert("Digite o nome do município.");
        return;
    }

    const resposta = await fetch(
        "/municipios/" + encodeURIComponent(nome)
    );

    const dados = await resposta.json();

    if (!resposta.ok) {
        alert(dados.erro);
        return;
    }

    preencherFormulario(nome, dados);
}


// ==========================================
// EDITAR MUNICÍPIO
// ==========================================

async function editarMunicipio(nome) {

    const resposta = await fetch(
        "/municipios/" + encodeURIComponent(nome)
    );

    const dados = await resposta.json();

    if (!resposta.ok) {
        alert(dados.erro);
        return;
    }

    preencherFormulario(nome, dados);

    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
}


// ==========================================
// PREENCHER FORMULÁRIO
// ==========================================

function preencherFormulario(nome, dados) {

    document.getElementById("nome").value = nome;

    document.getElementById("nomeOriginal").value = nome;

    document.getElementById("nome").readOnly = true;

    document.getElementById("id_ibge").value = dados.id_ibge;

    document.getElementById("estado").value = dados.estado;

    document.getElementById("sigla_uf").value = dados.sigla_uf;

    document.getElementById("capital").checked = dados.capital;

    document.getElementById("populacao").value =
        dados.populacao_estimada;
}


// ==========================================
// EXCLUIR MUNICÍPIO
// ==========================================

async function excluirMunicipio(nome) {

    const confirmar = confirm(
        "Deseja realmente excluir " + nome + "?"
    );

    if (!confirmar) {
        return;
    }

    const resposta = await fetch(
        "/municipios/" + encodeURIComponent(nome),
        {
            method: "DELETE"
        }
    );

    const resultado = await resposta.json();

    alert(resultado.mensagem || resultado.erro);

    if (resposta.ok) {
        limparFormulario();
        carregarMunicipios();
    }
}


// ==========================================
// LIMPAR FORMULÁRIO
// ==========================================

function limparFormulario() {

    document.getElementById("formMunicipio").reset();

    document.getElementById("nomeOriginal").value = "";

    document.getElementById("nome").readOnly = false;
}


// ==========================================
// INICIALIZAÇÃO
// ==========================================

carregarMunicipios();
