# 🏗️ Arquitetura — Gerador de Relatório Automático

Projeto do Dia 28. Lê uma base de investimentos em CSV, calcula indicadores e gera um relatório de texto pronto para arquivar.

## Fluxo do projeto

```
investimentos.csv        →   gerador_relatorio.py   →   relatorio_investimentos.txt
   (dado bruto)               (processamento)              (saída/entrega)
```

Todo relatório automático segue este mesmo pipeline de 4 etapas:

1. **Ler** os dados brutos (CSV).
2. **Calcular** os indicadores (totais, resultado, rentabilidade, melhor/pior).
3. **Formatar** em um texto legível (f-string de três aspas).
4. **Entregar** persistindo em arquivo (`.txt`).

## Entrada — `investimentos.csv`

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| `nome` | texto | Nome do ativo |
| `tipo` | texto | Classe (Cripto, Renda Fixa, FII...) |
| `valor_aquisicao` | número | Valor investido |
| `valor_atual` | número | Valor de mercado hoje |

> Todo valor numérico chega como texto e é convertido com `float()`.

## Processamento — `gerador_relatorio.py`

- **Acumuladores** (`total_investido`, `total_atual`) somam linha a linha, começando em zero.
- **Rentabilidade por ativo:** `(atual - aquisicao) / aquisicao * 100`, guardada de volta no dicionário.
- **Melhor/pior ativo:** rastreador que compara cada item ao campeão atual, protegido por `is None` (curto-circuito do `or`).
- **Rentabilidade total:** `resultado / total_investido * 100`.

## Saída — `relatorio_investimentos.txt`

Texto formatado com totais, resultado, rentabilidade geral e os destaques (melhor e pior ativo).

## Como rodar

```bash
python gerador_relatorio.py
```

## Decisões de projeto

- **CSV como entrada:** formato simples, editável em qualquer planilha, fácil de alimentar.
- **`.txt` como saída:** persistente, legível e consumível por outros sistemas — diferente de um `print` que some.
- **Cálculo separado da formatação:** primeiro os números, depois o texto — facilita evoluir cada parte sem quebrar a outra.

## Próximos passos (evolução)

- Separar em funções (`ler_dados`, `calcular`, `montar_relatorio`, `salvar`) — Dia 29.
- Aceitar o nome do arquivo por parâmetro.
- Exportar também em JSON ou PDF.

---

*Nota de arquitetura — Dia 28, Diário Técnico DevOS-Rodrigo.*
