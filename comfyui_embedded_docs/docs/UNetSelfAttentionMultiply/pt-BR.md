> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNetSelfAttentionMultiply/pt-BR.md)

O nó UNetSelfAttentionMultiply aplica fatores de multiplicação aos componentes de consulta, chave, valor e saída do mecanismo de autoatenção em um modelo UNet. Ele permite escalar diferentes partes do cálculo de atenção para experimentar como os pesos de atenção afetam o comportamento do modelo.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `modelo` | MODEL | Sim | - | O modelo UNet a ser modificado com fatores de escala de atenção |
| `q` | FLOAT | Não | 0.0 - 10.0 | Fator de multiplicação para o componente de consulta (padrão: 1.0) |
| `k` | FLOAT | Não | 0.0 - 10.0 | Fator de multiplicação para o componente de chave (padrão: 1.0) |
| `v` | FLOAT | Não | 0.0 - 10.0 | Fator de multiplicação para o componente de valor (padrão: 1.0) |
| `saída` | FLOAT | Não | 0.0 - 10.0 | Fator de multiplicação para o componente de saída (padrão: 1.0) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `MODEL` | MODEL | O modelo UNet modificado com componentes de atenção escalados |

---
**Source fingerprint (SHA-256):** `ee6328c6cba44d30d2e219a2af04bb3d3d9adeaabb959a46f87b3b299dfe2f43`
