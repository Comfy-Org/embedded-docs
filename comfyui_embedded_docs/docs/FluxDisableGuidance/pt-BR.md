# FluxDisableGuidance

Este nó desativa completamente a funcionalidade de incorporação de orientação (guidance embed) para modelos Flux e semelhantes. Ele recebe dados de condicionamento como entrada, remove o componente de orientação definindo-o como None e retorna os dados de condicionamento modificados, desativando efetivamente o condicionamento baseado em orientação para o processo de geração.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `conditioning` | Os dados de condicionamento para processar e remover a orientação deles | CONDITIONING | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `conditioning` | Os dados de condicionamento modificados com a orientação desativada | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxDisableGuidance/pt-BR.md)

---
**Source fingerprint (SHA-256):** `da3286194f9f5e7e49dd7047d6b0a0c97bb2570eaa9281abbd3992a743302fbf`
