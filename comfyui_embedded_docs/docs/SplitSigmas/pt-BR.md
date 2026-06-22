# SplitSigmas

O nó SplitSigmas foi projetado para dividir uma sequência de valores sigma em duas partes com base em uma etapa especificada. Essa funcionalidade é crucial para operações que exigem tratamento ou processamento diferenciado das partes inicial e subsequente da sequência sigma, permitindo uma manipulação mais flexível e direcionada desses valores.

## Entradas

| Parâmetro | Descrição | Tipo de Dados |
| --- | --- | --- |
| `sigmas` | O parâmetro 'sigmas' representa a sequência de valores sigma a ser dividida. Ele é essencial para determinar o ponto de divisão e as duas sequências resultantes de valores sigma, impactando a execução do nó e seus resultados. | `SIGMAS` |
| `passo` | O parâmetro 'step' especifica o índice no qual a sequência sigma deve ser dividida. Ele desempenha um papel crítico na definição do limite entre as duas sequências sigma resultantes, influenciando a funcionalidade do nó e as características da saída. | `INT` |

## Saídas

| Parâmetro | Descrição | Tipo de Dados |
| --- | --- | --- |
| `sigmas` | O nó gera duas sequências de valores sigma, cada uma representando uma parte da sequência original dividida na etapa especificada. Essas saídas são cruciais para operações subsequentes que exigem tratamento diferenciado dos valores sigma. | `SIGMAS` |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitSigmas/pt-BR.md)
