> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPAttentionMultiply/pt-BR.md)

O nó CLIPAttentionMultiply permite ajustar o mecanismo de atenção em modelos CLIP aplicando fatores de multiplicação a diferentes componentes das camadas de self-attention. Ele funciona modificando os pesos e vieses das projeções de consulta (query), chave (key), valor (value) e saída (output) no mecanismo de atenção do modelo CLIP. Este nó experimental cria uma cópia modificada do modelo CLIP de entrada com os fatores de escala especificados aplicados.

## Entradas

| Parâmetro | Tipo de Dados | Tipo de Entrada | Padrão | Intervalo | Descrição |
|-----------|-----------|------------|---------|-------|-------------|
| `clip` | CLIP | obrigatório | - | - | O modelo CLIP a ser modificado |
| `q` | FLOAT | obrigatório | 1.0 | 0.0 - 10.0 | Fator de multiplicação para os pesos e vieses da projeção de consulta (query) |
| `k` | FLOAT | obrigatório | 1.0 | 0.0 - 10.0 | Fator de multiplicação para os pesos e vieses da projeção de chave (key) |
| `v` | FLOAT | obrigatório | 1.0 | 0.0 - 10.0 | Fator de multiplicação para os pesos e vieses da projeção de valor (value) |
| `out` | FLOAT | obrigatório | 1.0 | 0.0 - 10.0 | Fator de multiplicação para os pesos e vieses da projeção de saída (output) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `CLIP` | CLIP | Retorna um modelo CLIP modificado com os fatores de escala de atenção especificados aplicados |
