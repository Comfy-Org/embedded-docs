> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGZeroStar/pt-BR.md)

Esta documentação foi gerada por IA. Se encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGZeroStar/en.md)

O nó CFGZeroStar aplica uma técnica especializada de escalonamento de orientação a modelos de difusão. Ele modifica o processo de orientação livre de classificador (classifier-free guidance) calculando um fator de escala otimizado com base na diferença entre as previsões condicionais e incondicionais. Essa abordagem ajusta a saída final para fornecer maior controle sobre o processo de geração, mantendo a estabilidade do modelo.

## Entradas

| Parâmetro | Tipo de Dado | Tipo de Entrada | Padrão | Intervalo | Descrição |
|-----------|--------------|-----------------|--------|-----------|-------------|
| `model` | MODEL | obrigatório | - | - | O modelo de difusão a ser modificado com a técnica de escalonamento de orientação CFGZeroStar |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `patched_model` | MODEL | O modelo modificado com o escalonamento de orientação CFGZeroStar aplicado |

---
**Source fingerprint (SHA-256):** `1f5fcd1377c64609e28d85e453aaaa0bcc8f3ac322b7b7240f34f71aa113562a`
