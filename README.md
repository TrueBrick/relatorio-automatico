# 📊 Gerador de Relatório Automático

Automação em Python que lê uma base de investimentos em CSV, calcula os principais indicadores e gera um relatório de texto pronto para arquivar ou compartilhar.

## Objetivo

Transformar dados brutos (uma planilha de investimentos) em um resumo legível e automático: total investido, valor atual, resultado, rentabilidade geral e os destaques (melhor e pior ativo) — sem precisar fazer conta na mão.

## Como rodar

1. Tenha o Python 3 instalado.
2. Coloque seus dados no arquivo `investimentos.csv` (mesmo formato do exemplo).
3. No terminal, dentro da pasta do projeto:

```bash
python gerador_relatorio.py
```

O relatório aparece na tela **e** é salvo em `relatorio_investimentos.txt`.

## Estrutura

```
relatorio-automatico/
├── gerador_relatorio.py          # o programa (dividido em funções)
├── investimentos.csv             # dados de entrada
├── relatorio_investimentos.txt   # saída gerada automaticamente
├── ARQUITETURA.md                # decisões de projeto
└── README.md                     # este arquivo
```

### Funções principais

| Função | Responsabilidade |
|--------|------------------|
| `ler_dados(caminho)` | Lê o CSV e devolve a lista de registros |
| `calcular_indicadores(investimentos)` | Calcula totais, rentabilidade e melhor/pior |
| `montar_relatorio(dados)` | Formata o texto do relatório |
| `salvar_relatorio(texto, caminho)` | Grava o relatório em arquivo |
| `main()` | Orquestra as etapas na ordem |

## Formato do CSV de entrada

```
nome,tipo,valor_aquisicao,valor_atual
Bitcoin,Cripto,150000,316000
Tesouro Selic,Renda Fixa,10000,11200
```

## Exemplo de uso (saída)

```
========================================
RELATÓRIO DE INVESTIMENTOS
========================================
Registros analisados: 5
Total investido: R$ 193,000.00
Valor atual:     R$ 361,400.00
Resultado:       R$ 168,400.00
Rentabilidade:   87.25%

Melhor ativo: Bitcoin (110.67%)
Pior ativo:   Ações PETR4 (-14.00%)
========================================
```

## Tecnologias

- Python 3
- Módulo nativo `csv`

---

*Projeto do Diário Técnico DevOS-Rodrigo — refatorado e documentado no Dia 29.*
