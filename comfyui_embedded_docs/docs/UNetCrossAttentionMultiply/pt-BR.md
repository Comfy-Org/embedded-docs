# UNetCrossAttentionMultiply

O nó UNetCrossAttentionMultiply aplica fatores de multiplicação ao mecanismo de atenção cruzada em um modelo UNet. Ele permite escalar os componentes de consulta, chave, valor e saída das camadas de atenção cruzada para experimentar diferentes comportamentos e efeitos de atenção.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo UNet a ser modificado com fatores de escala de atenção | MODEL | Sim | - |
| `q` | Fator de escala para componentes de consulta na atenção cruzada (padrão: 1.0) | FLOAT | Não | 0.0 - 10.0 |
| `k` | Fator de escala para componentes de chave na atenção cruzada (padrão: 1.0) | FLOAT | Não | 0.0 - 10.0 |
| `v` | Fator de escala para componentes de valor na atenção cruzada (padrão: 1.0) | FLOAT | Não | 0.0 - 10.0 |
| `saída` | Fator de escala para componentes de saída na atenção cruzada (padrão: 1.0) | FLOAT | Não | 0.0 - 10.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `modelo` | O modelo UNet modificado com componentes de atenção cruzada escalados | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNetCrossAttentionMultiply/pt-BR.md)

---
**Source fingerprint (SHA-256):** `2623858c11e93ab5952194670c9e4ea74bba4e2ea32089540665eea361dc1491`
