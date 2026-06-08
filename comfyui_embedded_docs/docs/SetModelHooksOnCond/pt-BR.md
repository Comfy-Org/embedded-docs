Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetModelHooksOnCond/en.md)

Este nó anexa hooks personalizados a dados de condicionamento, permitindo que você intercepte e modifique o processo de condicionamento durante a execução do modelo. Ele recebe um conjunto de hooks e os aplica aos dados de condicionamento fornecidos, possibilitando a personalização avançada do fluxo de trabalho de geração de texto para imagem. O condicionamento modificado com os hooks anexados é então retornado para uso nas etapas de processamento subsequentes.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `conditioning` | Os dados de condicionamento aos quais os hooks serão anexados | CONDITIONING | Sim | - |
| `hooks` | As definições de hook que serão aplicadas aos dados de condicionamento | HOOKS | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `conditioning` | Os dados de condicionamento modificados com os hooks anexados | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetModelHooksOnCond/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a6e63a3a4d94d1b66a82d449af5ae001e1fc4a04f0f81d9fb5c4f8c13e5bdf8b`
