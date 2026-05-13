> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPAttentionMultiply/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPAttentionMultiply/en.md)

O nó CLIPAttentionMultiply permite ajustar o mecanismo de atenção em modelos CLIP aplicando fatores de multiplicação a diferentes componentes das camadas de autoatenção. Ele funciona modificando os pesos e vieses das projeções de consulta, chave, valor e saída no mecanismo de atenção do modelo CLIP. Este nó experimental cria uma cópia modificada do modelo CLIP de entrada com os fatores de escala especificados aplicados.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `clip` | CLIP | Sim | - | O modelo CLIP a ser modificado |
| `q` | FLOAT | Sim | 0.0 - 10.0 | Fator de multiplicação para pesos e vieses da projeção de consulta (padrão: 1.0) |
| `k` | FLOAT | Sim | 0.0 - 10.0 | Fator de multiplicação para pesos e vieses da projeção de chave (padrão: 1.0) |
| `v` | FLOAT | Sim | 0.0 - 10.0 | Fator de multiplicação para pesos e vieses da projeção de valor (padrão: 1.0) |
| `out` | FLOAT | Sim | 0.0 - 10.0 | Fator de multiplicação para pesos e vieses da projeção de saída (padrão: 1.0) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `CLIP` | CLIP | Retorna um modelo CLIP modificado com os fatores de escala de atenção especificados aplicados |

---
**Source fingerprint (SHA-256):** `43dab83ecfc928f3359eb7560658f43235bf3faa62c81084a2b4f482e3a4638f`
