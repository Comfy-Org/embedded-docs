> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetFirstSigma/pt-BR.md)

O nó SetFirstSigma modifica uma sequência de valores sigma substituindo o primeiro valor sigma na sequência por um valor personalizado. Ele recebe uma sequência de sigma existente e um novo valor sigma como entradas e retorna uma nova sequência de sigma onde apenas o primeiro elemento foi alterado, mantendo todos os outros valores sigma inalterados.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `sigmas` | SIGMAS | Sim | - | A sequência de entrada de valores sigma a ser modificada |
| `sigma` | FLOAT | Sim | 0.0 a 20000.0 | O novo valor sigma a ser definido como o primeiro elemento na sequência (padrão: 136.0) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `sigmas` | SIGMAS | A sequência de sigma modificada com o primeiro elemento substituído pelo valor sigma personalizado |
