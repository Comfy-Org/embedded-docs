> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNetSelfAttentionMultiply/pt-BR.md)

O nó UNetSelfAttentionMultiply aplica fatores de multiplicação aos componentes de consulta (query), chave (key), valor (value) e saída (output) do mecanismo de auto-atenção em um modelo UNet. Ele permite que você escale diferentes partes do cálculo de atenção para experimentar como os pesos de atenção afetam o comportamento do modelo.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo UNet a ser modificado com os fatores de escala de atenção |
| `q` | FLOAT | Não | 0.0 - 10.0 | Fator de multiplicação para o componente de consulta (query) (padrão: 1.0) |
| `k` | FLOAT | Não | 0.0 - 10.0 | Fator de multiplicação para o componente de chave (key) (padrão: 1.0) |
| `v` | FLOAT | Não | 0.0 - 10.0 | Fator de multiplicação para o componente de valor (value) (padrão: 1.0) |
| `out` | FLOAT | Não | 0.0 - 10.0 | Fator de multiplicação para o componente de saída (output) (padrão: 1.0) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `MODEL` | MODEL | O modelo UNet modificado com os componentes de atenção escalados |
