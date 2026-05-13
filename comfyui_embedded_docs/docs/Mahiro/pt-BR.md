> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Mahiro/pt-BR.md)

O nó Mahiro modifica a função de orientação para focar mais na direção do prompt positivo, em vez da diferença entre prompts positivos e negativos. Ele cria um modelo corrigido que aplica uma abordagem personalizada de escala de orientação usando similaridade de cosseno entre as saídas de eliminação de ruído condicionais e incondicionais normalizadas. Este nó experimental ajuda a direcionar a geração mais fortemente para a direção pretendida do prompt positivo.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `model` | MODEL | Sim | | O modelo a ser corrigido com a função de orientação modificada |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `patched_model` | MODEL | O modelo modificado com a função de orientação Mahiro aplicada |

---
**Source fingerprint (SHA-256):** `8b4a73cfa488f97d87e5a18d5ab30765055b5d5a66c6c2f1a5f016eed2af0300`
