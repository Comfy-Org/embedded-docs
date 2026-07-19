# UNetSelfAttentionMultiply

O nó UNetSelfAttentionMultiply aplica fatores de multiplicação aos componentes de consulta, chave, valor e saída do mecanismo de autoatenção em um modelo UNet. Ele permite escalar diferentes partes do cálculo de atenção para experimentar como os pesos de atenção afetam o comportamento do modelo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo UNet a ser modificado com fatores de escala de atenção | MODEL | Sim | - |
| `q` | Fator de multiplicação para o componente de consulta (padrão: 1.0) | FLOAT | Não | 0.0 - 10.0 |
| `k` | Fator de multiplicação para o componente de chave (padrão: 1.0) | FLOAT | Não | 0.0 - 10.0 |
| `v` | Fator de multiplicação para o componente de valor (padrão: 1.0) | FLOAT | Não | 0.0 - 10.0 |
| `saída` | Fator de multiplicação para o componente de saída (padrão: 1.0) | FLOAT | Não | 0.0 - 10.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `MODEL` | O modelo UNet modificado com componentes de atenção escalados | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNetSelfAttentionMultiply/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ee6328c6cba44d30d2e219a2af04bb3d3d9adeaabb959a46f87b3b299dfe2f43`
