import csv


def ler_dados(caminho):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        return list(csv.DictReader(arquivo))


def calcular_indicadores(investimentos):
    total_investido = 0
    total_atual = 0
    melhor = None
    pior = None

    for inv in investimentos:
        aquisicao = float(inv["valor_aquisicao"])
        atual = float(inv["valor_atual"])
        inv["rentabilidade"] = (atual - aquisicao) / aquisicao * 100

        total_investido += aquisicao
        total_atual += atual

        if melhor is None or inv["rentabilidade"] > melhor["rentabilidade"]:
            melhor = inv
        if pior is None or inv["rentabilidade"] < pior["rentabilidade"]:
            pior = inv

    resultado = total_atual - total_investido
    rentabilidade_total = resultado / total_investido * 100

    return {
        "quantidade": len(investimentos),
        "total_investido": total_investido,
        "total_atual": total_atual,
        "resultado": resultado,
        "rentabilidade_total": rentabilidade_total,
        "melhor": melhor,
        "pior": pior,
    }


def montar_relatorio(dados):
    return f"""========================================
RELATÓRIO DE INVESTIMENTOS
========================================
Registros analisados: {dados['quantidade']}
Total investido: R$ {dados['total_investido']:,.2f}
Valor atual:     R$ {dados['total_atual']:,.2f}
Resultado:       R$ {dados['resultado']:,.2f}
Rentabilidade:   {dados['rentabilidade_total']:,.2f}%

Melhor ativo: {dados['melhor']['nome']} ({dados['melhor']['rentabilidade']:,.2f}%)
Pior ativo:   {dados['pior']['nome']} ({dados['pior']['rentabilidade']:,.2f}%)
========================================"""


def salvar_relatorio(texto, caminho):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        arquivo.write(texto)


def main():
    investimentos = ler_dados("investimentos.csv")
    dados = calcular_indicadores(investimentos)
    relatorio = montar_relatorio(dados)
    print(relatorio)
    salvar_relatorio(relatorio, "relatorio_investimentos.txt")
    print("Relatório salvo em relatorio_investimentos.txt")


if __name__ == "__main__":
    main()