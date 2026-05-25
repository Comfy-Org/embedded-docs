> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringFormat/pt-BR.md)

## Visão Geral

Este nó formata texto utilizando o método de formatação de strings do Python. Funciona como um modelo onde você define um padrão de texto com espaços reservados e, em seguida, fornece valores para preenchê-los. Suporta todas as opções e recursos de formatação do Python.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `f_string` | STRING | Sim | N/A | O modelo de string de formato com espaços reservados (padrão: `{a}`). Suporta entrada multilinha. |
| `values` | STRING | Sim | N/A | Entrada dinâmica para fornecer valores que preenchem os espaços reservados na string de formato. Múltiplas entradas de valores podem ser adicionadas conforme necessário. |

**Observação sobre a entrada `values`:** Esta entrada é dinâmica e pode ser expandida para incluir múltiplos valores nomeados. Cada entrada de valor é identificada por uma letra (a, b, c, etc.) e corresponde a um espaço reservado na string de formato (ex.: `{a}`, `{b}`, `{c}`). Você pode adicionar ou remover entradas de valor conforme necessário.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `STRING` | STRING | A string de texto formatada com todos os espaços reservados substituídos por seus valores correspondentes. |

---
**Source fingerprint (SHA-256):** `72625287533829a8087687bb47f39bc265aced3d5f43066f615326d729725122`
