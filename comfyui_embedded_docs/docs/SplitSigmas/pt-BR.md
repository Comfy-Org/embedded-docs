> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitSigmas/pt-BR.md)

O nó SplitSigmas é projetado para dividir uma sequência de valores sigma em duas partes com base em uma etapa especificada. Essa funcionalidade é crucial para operações que exigem tratamento ou processamento diferenciado das partes inicial e subsequente da sequência de sigma, permitindo uma manipulação mais flexível e direcionada desses valores.

## Entradas

| Parâmetro | Tipo de Dado | Descrição |
|-----------|-------------|-------------|
| `sigmas`  | `SIGMAS`    | O parâmetro 'sigmas' representa a sequência de valores sigma a ser dividida. É essencial para determinar o ponto de divisão e as duas sequências resultantes de valores sigma, impactando a execução e os resultados do nó. |
| `step`    | `INT`       | O parâmetro 'step' especifica o índice no qual a sequência de sigma deve ser dividida. Ele desempenha um papel crítico na definição do limite entre as duas sequências de sigma resultantes, influenciando a funcionalidade do nó e as características da saída. |

## Saídas

| Parâmetro | Tipo de Dado | Descrição |
|-----------|-------------|-------------|
| `sigmas`  | `SIGMAS`    | O nó gera duas sequências de valores sigma, cada uma representando uma parte da sequência original dividida na etapa especificada. Essas saídas são cruciais para operações subsequentes que exigem tratamento diferenciado dos valores sigma. |
