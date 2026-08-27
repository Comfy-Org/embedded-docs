# DefinirPrimeiroSigma

O nó SetFirstSigma altera uma sequência de sigma substituindo apenas seu primeiro valor por um valor sigma personalizado. Ele recebe uma sequência de sigma existente e um novo valor sigma, e retorna uma nova sequência de sigma onde todos os valores, exceto o primeiro, permanecem inalterados.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `sigmas` | A sequência de entrada de valores sigma a ser modificada | SIGMAS | Sim | - |
| `sigma` | O novo valor sigma para definir como o primeiro elemento da sequência (padrão: 136.0) | FLOAT | Sim | 0.0 a 20000.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `sigmas` | A sequência de sigma modificada com o primeiro elemento substituído pelo valor sigma personalizado | SIGMAS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetFirstSigma/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5302bc61a7ca094fee9ee2ad8c9dc32997ef0bbf27c9945acd7287e7df6b6db3`
