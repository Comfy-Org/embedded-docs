> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2ConditioningMultiView/pt-BR.md)

O nó **Hunyuan3Dv2ConditioningMultiView** processa embeddings de visão CLIP multivisão para geração de vídeo 3D. Ele aceita embeddings opcionais das vistas frontal, esquerda, traseira e direita e os combina com codificação posicional para criar dados de condicionamento para modelos de vídeo. O nó gera tanto o condicionamento positivo, a partir dos embeddings combinados, quanto o condicionamento negativo, com valores zero.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|--------------|-------------|-----------|-----------|
| `frente` | CLIP_VISION_OUTPUT | Não | - | Saída de visão CLIP para a vista frontal |
| `esquerda` | CLIP_VISION_OUTPUT | Não | - | Saída de visão CLIP para a vista esquerda |
| `trás` | CLIP_VISION_OUTPUT | Não | - | Saída de visão CLIP para a vista traseira |
| `direita` | CLIP_VISION_OUTPUT | Não | - | Saída de visão CLIP para a vista direita |

**Observação:** Pelo menos uma entrada de vista deve ser fornecida para que o nó funcione. O nó processará apenas as vistas que contiverem dados válidos de saída de visão CLIP.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `positive` | CONDITIONING | Condicionamento positivo contendo os embeddings multivisão combinados com codificação posicional |
| `negative` | CONDITIONING | Condicionamento negativo com valores zero para aprendizado contrastivo |

---
**Source fingerprint (SHA-256):** `01998ae9ba7d2ae9a2f6a0b5aee4c03168f935fb9769317cd80d93a7a4b96f13`
