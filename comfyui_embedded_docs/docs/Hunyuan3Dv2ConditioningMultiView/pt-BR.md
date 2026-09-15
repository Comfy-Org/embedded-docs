# Hunyuan3Dv2ConditioningMultiView

O nó Hunyuan3Dv2ConditioningMultiView combina saídas de visão CLIP de até quatro vistas (frontal, esquerda, traseira e direita) em um único condicionamento multivista. Cada vista fornecida tem uma codificação posicional adicionada ao seu embedding de visão CLIP, e os embeddings resultantes são concatenados. O nó gera um condicionamento positivo com base nos embeddings combinados e um condicionamento negativo preenchido com zeros do mesmo formato.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `frente` | Saída de visão CLIP para a vista frontal. Entrada de vista opcional. | CLIP_VISION_OUTPUT | Não | - |
| `esquerda` | Saída de visão CLIP para a vista esquerda. Entrada de vista opcional. | CLIP_VISION_OUTPUT | Não | - |
| `trás` | Saída de visão CLIP para a vista traseira. Entrada de vista opcional. | CLIP_VISION_OUTPUT | Não | - |
| `direita` | Saída de visão CLIP para a vista direita. Entrada de vista opcional. | CLIP_VISION_OUTPUT | Não | - |

**Nota:** Pelo menos uma entrada de vista deve ser fornecida para que o nó funcione. O nó processa apenas vistas que contêm dados válidos de saída de visão CLIP e ignora vistas que não estão conectadas. Cada vista recebe uma codificação posicional fixa com base em seu slot (frontal, esquerda, traseira, direita), e os embeddings processados de todas as vistas fornecidas são unidos ao longo da dimensão de sequência.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | Condicionamento positivo contendo os embeddings multivista combinados com codificação posicional. | CONDITIONING |
| `negative` | Condicionamento negativo com valores zero correspondentes ao formato do condicionamento positivo. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2ConditioningMultiView/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1492b51661d0bb8f2c142c1b1e8ef104beed1b9dae532a970e2928e27ad71d69`
