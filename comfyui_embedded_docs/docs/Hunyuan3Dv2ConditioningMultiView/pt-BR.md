# Hunyuan3Dv2ConditioningMultiView

O nó Hunyuan3Dv2ConditioningMultiView processa embeddings de visão CLIP multiview para geração de vídeo 3D. Ele recebe embeddings opcionais das vistas frontal, esquerda, traseira e direita e adiciona codificação posicional a cada vista fornecida antes de combiná-las em uma única sequência de condicionamento. O nó gera tanto o condicionamento positivo a partir dos embeddings combinados quanto o condicionamento negativo com valores zero.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `front` | Saída de visão CLIP para a vista frontal | CLIP_VISION_OUTPUT | Não | - |
| `left` | Saída de visão CLIP para a vista esquerda | CLIP_VISION_OUTPUT | Não | - |
| `back` | Saída de visão CLIP para a vista traseira | CLIP_VISION_OUTPUT | Não | - |
| `right` | Saída de visão CLIP para a vista direita | CLIP_VISION_OUTPUT | Não | - |

**Nota:** Pelo menos uma entrada de vista deve ser fornecida para o nó funcionar. O nó processa apenas as vistas que contêm dados válidos de saída de visão CLIP. Cada vista fornecida recebe uma codificação posicional com base em sua posição (frontal, esquerda, traseira, direita), e as vistas codificadas são concatenadas nessa mesma ordem.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | Condicionamento positivo contendo os embeddings multiview combinados com codificação posicional | CONDITIONING |
| `negative` | Condicionamento negativo contendo valores zero com a mesma forma do condicionamento positivo | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2ConditioningMultiView/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1492b51661d0bb8f2c142c1b1e8ef104beed1b9dae532a970e2928e27ad71d69`
