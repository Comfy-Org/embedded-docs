> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2ConditioningMultiView/pt-BR.md)

O nó Hunyuan3Dv2ConditioningMultiView processa embeddings de visão CLIP de múltiplas vistas para geração de vídeo 3D. Ele recebe embeddings opcionais das vistas frontal, esquerda, traseira e direita e os combina com codificação posicional para criar dados de condicionamento para modelos de vídeo. O nó gera tanto o condicionamento positivo a partir dos embeddings combinados quanto o condicionamento negativo com valores zero.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `front` | CLIP_VISION_OUTPUT | Não | - | Saída de visão CLIP para a vista frontal |
| `left` | CLIP_VISION_OUTPUT | Não | - | Saída de visão CLIP para a vista esquerda |
| `back` | CLIP_VISION_OUTPUT | Não | - | Saída de visão CLIP para a vista traseira |
| `right` | CLIP_VISION_OUTPUT | Não | - | Saída de visão CLIP para a vista direita |

**Observação:** Pelo menos uma entrada de vista deve ser fornecida para o nó funcionar. O nó processará apenas as vistas que contiverem dados válidos de saída de visão CLIP.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Condicionamento positivo contendo os embeddings de múltiplas vistas combinados com codificação posicional |
| `negative` | CONDITIONING | Condicionamento negativo com valores zero para aprendizado contrastivo |
