
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# =====================================================
# BASE DE DADOS EM MEMÓRIA
# =====================================================

municipios_nordeste_dataset = {
    "metadados": {
        "regiao": "Nordeste",
        "pais": "Brasil",
        "total_municipios": 30,
        "fonte_dados_populacao": "IBGE"
    },

    "municipios": {

        # ---------------- CEARÁ ----------------

        "Fortaleza": {
            "id_ibge": 2304400,
            "estado": "Ceará",
            "sigla_uf": "CE",
            "capital": True,
            "populacao_estimada": 2582360
        },

        "Juazeiro do Norte": {
            "id_ibge": 2307304,
            "estado": "Ceará",
            "sigla_uf": "CE",
            "capital": False,
            "populacao_estimada": 286120
        },

        "Sobral": {
            "id_ibge": 2312908,
            "estado": "Ceará",
            "sigla_uf": "CE",
            "capital": False,
            "populacao_estimada": 203023
        },

        "Crato": {
            "id_ibge": 2304202,
            "estado": "Ceará",
            "sigla_uf": "CE",
            "capital": False,
            "populacao_estimada": 131050
        },

        "Itapipoca": {
            "id_ibge": 2306405,
            "estado": "Ceará",
            "sigla_uf": "CE",
            "capital": False,
            "populacao_estimada": 131687
        },

        "Maracanaú": {
            "id_ibge": 2307650,
            "estado": "Ceará",
            "sigla_uf": "CE",
            "capital": False,
            "populacao_estimada": 234509
        },

        # ---------------- BAHIA ----------------

        "Salvador": {
            "id_ibge": 2927408,
            "estado": "Bahia",
            "sigla_uf": "BA",
            "capital": True,
            "populacao_estimada": 2559945
        },

        "Feira de Santana": {
            "id_ibge": 2910800,
            "estado": "Bahia",
            "sigla_uf": "BA",
            "capital": False,
            "populacao_estimada": 616272
        },

        "Vitória da Conquista": {
            "id_ibge": 2933307,
            "estado": "Bahia",
            "sigla_uf": "BA",
            "capital": False,
            "populacao_estimada": 370879
        },

        "Camaçari": {
            "id_ibge": 2905701,
            "estado": "Bahia",
            "sigla_uf": "BA",
            "capital": False,
            "populacao_estimada": 300372
        },

        "Ilhéus": {
            "id_ibge": 2913606,
            "estado": "Bahia",
            "sigla_uf": "BA",
            "capital": False,
            "populacao_estimada": 178703
        },

        "Itabuna": {
            "id_ibge": 2914802,
            "estado": "Bahia",
            "sigla_uf": "BA",
            "capital": False,
            "populacao_estimada": 186708
        },

        # ---------------- PERNAMBUCO ----------------

        "Recife": {
            "id_ibge": 2611606,
            "estado": "Pernambuco",
            "sigla_uf": "PE",
            "capital": True,
            "populacao_estimada": 1587707
        },

        "Jaboatão dos Guararapes": {
            "id_ibge": 2607901,
            "estado": "Pernambuco",
            "sigla_uf": "PE",
            "capital": False,
            "populacao_estimada": 644037
        },

        "Olinda": {
            "id_ibge": 2609600,
            "estado": "Pernambuco",
            "sigla_uf": "PE",
            "capital": False,
            "populacao_estimada": 349976
        },

        "Caruaru": {
            "id_ibge": 2604106,
            "estado": "Pernambuco",
            "sigla_uf": "PE",
            "capital": False,
            "populacao_estimada": 378048
        },

        "Petrolina": {
            "id_ibge": 2611101,
            "estado": "Pernambuco",
            "sigla_uf": "PE",
            "capital": False,
            "populacao_estimada": 386786
        },

        # ---------------- PIAUÍ ----------------

        "Teresina": {
            "id_ibge": 2211001,
            "estado": "Piauí",
            "sigla_uf": "PI",
            "capital": True,
            "populacao_estimada": 866300
        },

        "Parnaíba": {
            "id_ibge": 2207702,
            "estado": "Piauí",
            "sigla_uf": "PI",
            "capital": False,
            "populacao_estimada": 162159
        },

        "Picos": {
            "id_ibge": 2208007,
            "estado": "Piauí",
            "sigla_uf": "PI",
            "capital": False,
            "populacao_estimada": 83090
        },

        # ---------------- MARANHÃO ----------------

        "São Luís": {
            "id_ibge": 2111300,
            "estado": "Maranhão",
            "sigla_uf": "MA",
            "capital": True,
            "populacao_estimada": 1088055
        },

        "Imperatriz": {
            "id_ibge": 2105302,
            "estado": "Maranhão",
            "sigla_uf": "MA",
            "capital": False,
            "populacao_estimada": 273110
        },

        "Caxias": {
            "id_ibge": 2103000,
            "estado": "Maranhão",
            "sigla_uf": "MA",
            "capital": False,
            "populacao_estimada": 156973
        },

        # ---------------- PARAÍBA ----------------

        "João Pessoa": {
            "id_ibge": 2507507,
            "estado": "Paraíba",
            "sigla_uf": "PB",
            "capital": True,
            "populacao_estimada": 833932
        },

        "Campina Grande": {
            "id_ibge": 2504009,
            "estado": "Paraíba",
            "sigla_uf": "PB",
            "capital": False,
            "populacao_estimada": 419379
        },

        # ---------------- RIO GRANDE DO NORTE ----------------

        "Natal": {
            "id_ibge": 2408102,
            "estado": "Rio Grande do Norte",
            "sigla_uf": "RN",
            "capital": True,
            "populacao_estimada": 751300
        },

        "Mossoró": {
            "id_ibge": 2408003,
            "estado": "Rio Grande do Norte",
            "sigla_uf": "RN",
            "capital": False,
            "populacao_estimada": 278587
        },

        # ---------------- ALAGOAS ----------------

        "Maceió": {
            "id_ibge": 2704302,
            "estado": "Alagoas",
            "sigla_uf": "AL",
            "capital": True,
            "populacao_estimada": 994464
        },

        "Arapiraca": {
            "id_ibge": 2700300,
            "estado": "Alagoas",
            "sigla_uf": "AL",
            "capital": False,
            "populacao_estimada": 234696
        },

        # ---------------- SERGIPE ----------------

        "Aracaju": {
            "id_ibge": 2800308,
            "estado": "Sergipe",
            "sigla_uf": "SE",
            "capital": True,
            "populacao_estimada": 602757
        },

        "Itabaiana": {
            "id_ibge": 2802908,
            "estado": "Sergipe",
            "sigla_uf": "SE",
            "capital": False,
            "populacao_estimada": 103439
        }
    }
}


# =====================================================
# FUNÇÃO PARA ATUALIZAR O TOTAL DE MUNICÍPIOS
# =====================================================

def atualizar_total_municipios():
    total = len(municipios_nordeste_dataset["municipios"])

    municipios_nordeste_dataset["metadados"]["total_municipios"] = total


# =====================================================
# ROTA PRINCIPAL - PÁGINA INICIAL
# =====================================================

@app.route("/")
def inicio():
    return render_template("index.html")


# =====================================================
# GET - LISTAR TODOS OU FILTRAR POR ESTADO
# Rota: GET /municipios
# =====================================================

@app.route("/municipios", methods=["GET"])
def listar_municipios():

    # Recebe o parâmetro uf da URL
    uf = request.args.get("uf")

    municipios = municipios_nordeste_dataset["municipios"]

    # Se o usuário informar uma UF, realiza o filtro
    if uf:

        resultado = {}

        # Percorre o dicionário usando .items()
        for nome, dados in municipios.items():

            # Compara a sigla do estado
            if dados["sigla_uf"].upper() == uf.upper():
                resultado[nome] = dados

        return jsonify(resultado), 200

    # Caso não exista filtro, retorna todos
    return jsonify(municipios), 200


# =====================================================
# GET - CONSULTAR MUNICÍPIO POR NOME
# Rota: GET /municipios/<nome>
# =====================================================

@app.route("/municipios/<nome>", methods=["GET"])
def consultar_municipio(nome):

    municipios = municipios_nordeste_dataset["municipios"]

    # Busca o município diretamente pela chave
    if nome in municipios:
        return jsonify(municipios[nome]), 200

    # Retorna erro 404 caso não exista
    return jsonify({
        "erro": "Município não encontrado."
    }), 404


# =====================================================
# POST - CADASTRAR NOVO MUNICÍPIO
# Rota: POST /municipios
# =====================================================

@app.route("/municipios", methods=["POST"])
def cadastrar_municipio():

    # Recebe os dados enviados em JSON
    dados = request.get_json()

    # Verifica se os dados são um dicionário
    if not isinstance(dados, dict):
        return jsonify({
            "erro": "Envie os dados em formato JSON."
        }), 400

    # Recupera o nome do município
    nome = dados.get("nome")

    # Valida o nome
    if not isinstance(nome, str) or not nome.strip():
        return jsonify({
            "erro": "O nome do município é obrigatório."
        }), 400

    nome = nome.strip()

    municipios = municipios_nordeste_dataset["municipios"]

    # Verifica se o município já está cadastrado
    if nome in municipios:
        return jsonify({
            "erro": "Este município já está cadastrado."
        }), 409

    # Cria um novo dicionário sem o campo nome
    dados_municipio = {
        chave: valor
        for chave, valor in dados.items()
        if chave != "nome"
    }

    # Adiciona o município ao dicionário
    municipios[nome] = dados_municipio

    # Atualiza o total de municípios
    atualizar_total_municipios()

    return jsonify({
        "mensagem": "Município cadastrado com sucesso.",
        "municipio": {
            nome: dados_municipio
        }
    }), 201


# =====================================================
# PATCH - ATUALIZAR MUNICÍPIO
# Rota: PATCH /municipios/<nome>
# =====================================================

@app.route("/municipios/<nome>", methods=["PATCH"])
def atualizar_municipio(nome):

    municipios = municipios_nordeste_dataset["municipios"]

    # Verifica se o município existe
    if nome not in municipios:
        return jsonify({
            "erro": "Município não encontrado."
        }), 404

    # Recebe os dados para atualização
    dados = request.get_json()

    if not isinstance(dados, dict):
        return jsonify({
            "erro": "Envie os dados em formato JSON."
        }), 400

    # Atualiza somente os campos enviados
    municipios[nome].update(dados)

    return jsonify({
        "mensagem": "Município atualizado com sucesso.",
        "municipio": municipios[nome]
    }), 200


# =====================================================
# DELETE - EXCLUIR MUNICÍPIO
# Rota: DELETE /municipios/<nome>
# =====================================================

@app.route("/municipios/<nome>", methods=["DELETE"])
def excluir_municipio(nome):

    municipios = municipios_nordeste_dataset["municipios"]

    # Verifica se o município existe
    if nome not in municipios:
        return jsonify({
            "erro": "Município não encontrado."
        }), 404

    # Remove o município usando .pop()
    municipio_removido = municipios.pop(nome)

    # Atualiza o total de municípios
    atualizar_total_municipios()

    return jsonify({
        "mensagem": "Município removido com sucesso.",
        "municipio": municipio_removido
    }), 200


# =====================================================
# GET - CONSULTAR METADADOS
# Rota: GET /metadados
# =====================================================

@app.route("/metadados", methods=["GET"])
def consultar_metadados():

    return jsonify(
        municipios_nordeste_dataset["metadados"]
    ), 200


# =====================================================
# EXECUÇÃO DO SERVIDOR
# =====================================================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)