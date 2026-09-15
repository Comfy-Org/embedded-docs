# FluxDisableGuidance

Este nó desativa completamente o embed de guidance em modelos Flux e similares ao Flux. Ele recebe dados de condicionamento como entrada e define seu valor de guidance como None, efetivamente desativando o condicionamento baseado em guidance para o processo de geração.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `condicionamento` | Os dados de condicionamento a serem processados e dos quais o guidance será removido | CONDITIONING | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `conditioning` | Os dados de condicionamento modificados com o guidance desativado | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxDisableGuidance/pt-BR.md)

---
**Source fingerprint (SHA-256):** `da3286194f9f5e7e49dd7047d6b0a0c97bb2570eaa9281abbd3992a743302fbf`
