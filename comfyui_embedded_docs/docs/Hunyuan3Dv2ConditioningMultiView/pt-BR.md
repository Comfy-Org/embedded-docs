O nó **Hunyuan3Dv2ConditioningMultiView** processa embeddings de visão CLIP multivisão para geração de vídeo 3D. Ele aceita embeddings opcionais das vistas frontal, esquerda, traseira e direita e os combina com codificação posicional para criar dados de condicionamento para modelos de vídeo. O nó gera tanto o condicionamento positivo, a partir dos embeddings combinados, quanto o condicionamento negativo, com valores zero.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `frente` | Saída de visão CLIP para a vista frontal | CLIP_VISION_OUTPUT | Não | - |
| `esquerda` | Saída de visão CLIP para a vista esquerda | CLIP_VISION_OUTPUT | Não | - |
| `trás` | Saída de visão CLIP para a vista traseira | CLIP_VISION_OUTPUT | Não | - |
| `direita` | Saída de visão CLIP para a vista direita | CLIP_VISION_OUTPUT | Não | - |

**Observação:** Pelo menos uma entrada de vista deve ser fornecida para que o nó funcione. O nó processará apenas as vistas que contiverem dados válidos de saída de visão CLIP.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `positive` | Condicionamento positivo contendo os embeddings multivisão combinados com codificação posicional | CONDITIONING |
| `negative` | Condicionamento negativo com valores zero para aprendizado contrastivo | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2ConditioningMultiView/pt-BR.md)

---
**Source fingerprint (SHA-256):** `01998ae9ba7d2ae9a2f6a0b5aee4c03168f935fb9769317cd80d93a7a4b96f13`
