# FluxDisableGuidance

Este nó desativa completamente o embedding de orientação em modelos Flux e semelhantes ao Flux. Ele recebe dados de condicionamento como entrada e remove o componente de orientação definindo-o como None, desativando efetivamente o condicionamento baseado em orientação para o processo de geração.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `condicionamento` | Os dados de condicionamento a processar e dos quais remover a orientação | CONDITIONING | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `conditioning` | Os dados de condicionamento modificados com a orientação desativada | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxDisableGuidance/pt-BR.md)

---
**Source fingerprint (SHA-256):** `da3286194f9f5e7e49dd7047d6b0a0c97bb2570eaa9281abbd3992a743302fbf`
