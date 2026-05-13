> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetFirstSigma/pt-BR.md)

O nó SetFirstSigma modifica uma sequência de valores sigma substituindo o primeiro valor sigma da sequência por um valor personalizado. Ele recebe uma sequência sigma existente e um novo valor sigma como entradas e retorna uma nova sequência sigma onde apenas o primeiro elemento foi alterado, mantendo todos os outros valores sigma inalterados.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `sigmas` | SIGMAS | Sim | - | A sequência de entrada de valores sigma a ser modificada |
| `sigma` | FLOAT | Sim | 0.0 a 20000.0 | O novo valor sigma a ser definido como primeiro elemento na sequência (padrão: 136.0) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `sigmas` | SIGMAS | A sequência sigma modificada com o primeiro elemento substituído pelo valor sigma personalizado |

---
**Source fingerprint (SHA-256):** `2414acd7f3f42032c12bae2c581de4721f4c1daa912255fa0956caaa567291d5`
