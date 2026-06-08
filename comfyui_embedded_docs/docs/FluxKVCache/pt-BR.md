O nó Flux KV Cache permite uma otimização de Cache de Chave-Valor (KV) para modelos da família Flux. Essa otimização melhora o desempenho ao usar imagens de referência, armazenando em cache determinados cálculos, o que pode acelerar o processo de geração.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo no qual aplicar a otimização de Cache KV. | MODEL | Sim |  |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `modelo` | O modelo modificado com a otimização de Cache KV ativada. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKVCache/pt-BR.md)

---
**Source fingerprint (SHA-256):** `530c660ae23607d4035815826ae73cdcbebe7693ba47a3b0fe98e69f329b9e86`
