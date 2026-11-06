
from flask import Flask, render_template, request, jsonify, send_file
from io import BytesIO
import json

app = Flask(__name__)

# =====================================================
# BASE DE DADOS
# =====================================================

municipios_nordeste_dataset = {
    "metadados": {
        "regiao": "Nordeste",
        "pais": "Brasil",
        "total_municipios": 30,
        "fonte_dados_populacao": "IBGE"
    },

    "municipios": {

        # CEARÁ

        "Fortaleza": {
            "id_ibge": 2304400,
            "estado": "Ceará",
            "sigla_uf": "CE",
            "capital": True,
            "populacao_estimada": 2582360
        },

        "Caucaia": {
            "id_ibge": 2303709,
            "estado": "Ceará",
            "sigla_uf": "CE",
            "capital": False,
            "populacao_estimada": 375730
        },

        "Juazeiro do Norte": {
            "id_ibge": 2307304,
            "estado": "Ceará",
            "sigla_uf": "CE",
            "capital": False,
            "populacao_estimada": 303004
        },

        "Sobral": {
            "id_ibge": 2312908,
            "estado": "Ceará",
            "sigla_uf": "CE",
            "capital": False,
            "populacao_estimada": 215286
        },

        # BAHIA

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
            "populacao_estimada": 657948
        },

        "Vitória da Conquista": {
            "id_ibge": 2933307,
            "estado": "Bahia",
            "sigla_uf": "BA",
            "capital": False,
            "populacao_estimada": 394024
        },

        "Camaçari": {
            "id_ibge": 2905701,
            "estado": "Bahia",
            "sigla_uf": "BA",
            "capital": False,
            "populacao_estimada": 319394
        },

        # ALAGOAS

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
            "populacao_estimada": 243661
        },

        "Rio Largo": {
            "id_ibge": 2707701,
            "estado": "Alagoas",
            "sigla_uf": "AL",
            "capital": False,
            "populacao_estimada": 97435
        },

        # MARANHÃO

        "São Luís": {
            "id_ibge": 2111300,
            "estado": "Maranhão",
            "sigla_uf": "MA",
            "capital": True,
            "populacao_estimada": 1088057
        },

        "Timon": {
            "id_ibge": 2112209,
            "estado": "Maranhão",
            "sigla_uf": "MA",
            "capital": False,
            "populacao_estimada": 182241
        },

        "São José de Ribamar": {
            "id_ibge": 2111200,
            "estado": "Maranhão",
            "sigla_uf": "MA",
            "capital": False,
            "populacao_estimada": 257414
        },

        # PARAÍBA

        "João Pessoa": {
            "id_ibge": 2507507,
            "estado": "Paraíba",
            "sigla_uf": "PB",
            "capital": True,
            "populacao_estimada": 888679
        },

        "Campina Grande": {
            "id_ibge": 2504009,
            "estado": "Paraíba",
            "sigla_uf": "PB",
            "capital": False,
            "populacao_estimada": 440939
        },

        "Sousa": {
            "id_ibge": 2516201,
            "estado": "Paraíba",
            "sigla_uf": "PB",
            "capital": False,
            "populacao_estimada": 69876
        },

        # PERNAMBUCO

        "Recife": {
            "id_ibge": 2611606,
            "estado": "Pernambuco",
            "sigla_uf": "PE",
            "capital": True,
            "populacao_estimada": 1587707
        },

        "Caruaru": {
            "id_ibge": 2604106,
            "estado": "Pernambuco",
            "sigla_uf": "PE",
            "capital": False,
            "populacao_estimada": 402290
        },

        "Petrolina": {
            "id_ibge": 2611101,
            "estado": "Pernambuco",
            "sigla_uf": "PE",
            "capital": False,
            "populacao_estimada": 414083
        },

        # PIAUÍ

        "Teresina": {
            "id_ibge": 2211001,
            "estado": "Piauí",
            "sigla_uf": "PI",
            "capital": True,
            "populacao_estimada": 902644
        },

        "Parnaíba": {
            "id_ibge": 2207702,
            "estado": "Piauí",
            "sigla_uf": "PI",
            "capital": False,
            "populacao_estimada": 169552
        },

        "Picos": {
            "id_ibge": 2208007,
            "estado": "Piauí",
            "sigla_uf": "PI",
            "capital": False,
            "populacao_estimada": 86228
        },

        "Piripiri": {
            "id_ibge": 2208403,
            "estado": "Piauí",
            "sigla_uf": "PI",
            "capital": False,
            "populacao_estimada": 67676
        },

        # RIO GRANDE DO NORTE

        "Natal": {
            "id_ibge": 2408102,
            "estado": "Rio Grande do Norte",
            "sigla_uf": "RN",
            "capital": True,
            "populacao_estimada": 785368
        },

        "Mossoró": {
            "id_ibge": 2408003,
            "estado": "Rio Grande do Norte",
            "sigla_uf": "RN",
            "capital": False,
            "populacao_estimada": 278034
        },

        "Parnamirim": {
            "id_ibge": 2403251,
            "estado": "Rio Grande do Norte",
            "sigla_uf": "RN",
            "capital": False,
            "populacao_estimada": 269298
        },

        # SERGIPE

        "Aracaju": {
            "id_ibge": 2800308,
            "estado": "Sergipe",
            "sigla_uf": "SE",
            "capital": True,
            "populacao_estimada": 628849
        },

        "Itabaiana": {
            "id_ibge": 2802908,
            "estado": "Sergipe",
            "sigla_uf": "SE",
            "capital": False,
            "populacao_estimada": 103440
        },

        "Nossa Senhora do Socorro": {
            "id_ibge": 2804805,
            "estado": "Sergipe",
            "sigla_uf": "SE",
            "capital": False,
            "populacao_estimada": 192330
        }
    }
}


# =====================================================
# PÁGINA INICIAL
# =====================================================

@app.route("/")
def inicio():
    return render_template("index.html")


# =====================================================
# LISTAR / FILTRAR MUNICÍPIOS
# GET /municipios
# =====================================================

@app.route("/municipios", methods=["GET"])
def listar_municipios():

    municipios = municipios_nordeste_dataset["municipios"]
    uf = request.args.get("uf")

    if uf:
        filtrados = {}

        for nome, dados in municipios.items():
            if dados["sigla_uf"].upper() == uf.upper():
                filtrados[nome] = dados

        return jsonify(filtrados)

    return jsonify(municipios)


# =====================================================
# CONSULTAR MUNICÍPIO
# GET /municipios/<nome>
# =====================================================

@app.route("/municipios/<nome>", methods=["GET"])
def consultar_municipio(nome):

    municipios = municipios_nordeste_dataset["municipios"]

    if nome in municipios:
        return jsonify(municipios[nome])

    return jsonify({"erro": "Município não encontrado."}), 404


# =====================================================
# CADASTRAR MUNICÍPIO
# POST /municipios
# =====================================================

@app.route("/municipios", methods=["POST"])
def cadastrar_municipio():

    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "Nenhum dado foi enviado."}), 400

    nome = dados.get("nome")

    if not isinstance(nome, str) or not nome.strip():
        return jsonify({"erro": "Nome obrigatório."}), 400

    nome = nome.strip()
    municipios = municipios_nordeste_dataset["municipios"]

    if nome in municipios:
        return jsonify({"erro": "Município já cadastrado."}), 409

    try:
        novo_municipio = {
            "id_ibge": int(dados["id_ibge"]),
            "estado": dados["estado"].strip(),
            "sigla_uf": dados["sigla_uf"].strip().upper(),
            "capital": dados["capital"],
            "populacao_estimada": int(dados["populacao_estimada"])
        }

        if not novo_municipio["estado"] or len(novo_municipio["sigla_uf"]) != 2:
            raise ValueError()

        if not isinstance(novo_municipio["capital"], bool):
            raise ValueError()

    except (KeyError, ValueError, TypeError, AttributeError):
        return jsonify({"erro": "Verifique os dados informados."}), 400

    municipios[nome] = novo_municipio

    return jsonify({
        "mensagem": "Município cadastrado com sucesso!",
        "municipio": novo_municipio
    }), 201


# =====================================================
# ATUALIZAR MUNICÍPIO
# PATCH /municipios/<nome>
# =====================================================

@app.route("/municipios/<nome>", methods=["PATCH"])
def atualizar_municipio(nome):

    municipios = municipios_nordeste_dataset["municipios"]

    if nome not in municipios:
        return jsonify({"erro": "Município não encontrado."}), 404

    dados = request.get_json()

    if not isinstance(dados, dict) or not dados:
        return jsonify({"erro": "Nenhum dado foi enviado."}), 400

    try:
        municipio = municipios[nome]

        if "id_ibge" in dados:
            municipio["id_ibge"] = int(dados["id_ibge"])

        if "estado" in dados:
            municipio["estado"] = dados["estado"].strip()

        if "sigla_uf" in dados:
            uf = dados["sigla_uf"].strip().upper()

            if len(uf) != 2:
                raise ValueError()

            municipio["sigla_uf"] = uf

        if "capital" in dados:
            if not isinstance(dados["capital"], bool):
                raise ValueError()

            municipio["capital"] = dados["capital"]

        if "populacao_estimada" in dados:
            municipio["populacao_estimada"] = int(
                dados["populacao_estimada"]
            )

    except (ValueError, TypeError, AttributeError):
        return jsonify({"erro": "Verifique os dados informados."}), 400

    return jsonify({
        "mensagem": "Município atualizado com sucesso!",
        "municipio": municipio
    })


# =====================================================
# EXCLUIR MUNICÍPIO
# DELETE /municipios/<nome>
# =====================================================

@app.route("/municipios/<nome>", methods=["DELETE"])
def excluir_municipio(nome):

    municipios = municipios_nordeste_dataset["municipios"]

    if nome not in municipios:
        return jsonify({"erro": "Município não encontrado."}), 404

    municipios.pop(nome)

    return jsonify({"mensagem": "Município excluído com sucesso!"})


# =====================================================
# EXPORTAR ARQUIVO JSON
# GET /municipios/exportar
# =====================================================

@app.route("/municipios/exportar", methods=["GET"])
def exportar_json():

    arquivo = BytesIO()

    arquivo.write(
        json.dumps(
            municipios_nordeste_dataset,
            ensure_ascii=False,
            indent=4
        ).encode("utf-8")
    )

    arquivo.seek(0)

    return send_file(
        arquivo,
        mimetype="application/json",
        as_attachment=True,
        download_name="municipios_nordeste.json"
    )


# =====================================================
# EXECUTAR A APLICAÇÃO
# =====================================================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
