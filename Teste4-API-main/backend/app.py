from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

caminho_csv = os.path.join(os.path.dirname(__file__), "Relatorio_cadop.csv")
df = pd.read_csv(caminho_csv, sep=";", encoding="latin1", quotechar='"')

def buscar_empresa(termo, pagina=1, tamanho_pagina=10):
    """Busca textual nos campos relevantes e aplica paginação."""
    colunas_relevantes = ["Razao_Social", "Nome_Fantasia", "CNPJ", "Modalidade", "Cidade", "UF"]

    filtro = df[df[colunas_relevantes].apply(
        lambda col: col.astype(str).str.contains(termo, case=False, na=False)
    ).any(axis=1)]

    total_resultados = len(filtro)
    total_paginas = (total_resultados // tamanho_pagina) + (1 if total_resultados % tamanho_pagina > 0 else 0)

    inicio = (pagina - 1) * tamanho_pagina
    fim = inicio + tamanho_pagina
    resultados_paginados = filtro.iloc[inicio:fim][colunas_relevantes].to_dict(orient="records")

    return {
        "resultados": resultados_paginados,
        "total_paginas": total_paginas
    }

@app.route("/buscar", methods=["GET"])
def buscar():
    termo = request.args.get("termo", "").strip()
    pagina = int(request.args.get("pagina", 1))
    tamanho_pagina = int(request.args.get("tamanho_pagina", 10))

    if not termo:
        return jsonify({"erro": "Nenhum termo de busca fornecido."}), 400

    dados = buscar_empresa(termo, pagina, tamanho_pagina)
    return jsonify(dados)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
