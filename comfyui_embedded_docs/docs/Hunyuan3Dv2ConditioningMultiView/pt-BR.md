# Hunyuan3Dv2ConditioningMultiView

O nó Hunyuan3Dv2ConditioningMultiView combina as saídas de CLIP vision de até quatro vistas (frontal, esquerda, traseira e direita) em um único condicionamento de múltiplas vistas. Cada vista fornecida recebe uma codificação posicional adicionada ao seu embedding de CLIP vision, e os embeddings resultantes são concatenados. O nó gera um condicionamento positivo baseado nos embeddings combinados e um condicionamento negativo preenchido com zeros da mesma forma.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `frente` | Saída de CLIP vision da vista frontal. Entrada de vista opcional. | CLIP_VISION_OUTPUT | Não | - |
| `esquerda` | Saída de CLIP vision da vista esquerda. Entrada de vista opcional. | CLIP_VISION_OUTPUT | Não | - |
| `trás` | Saída de CLIP vision da vista traseira. Entrada de vista opcional. | CLIP_VISION_OUTPUT | Não | - |
| `direita` | Saída de CLIP vision da vista direita. Entrada de vista opcional. | CLIP_VISION_OUTPUT | Não | - |

**Nota:** Pelo menos uma entrada de vista deve ser fornecida para o nó funcionar. O nó processa apenas vistas que contenham dados de saída CLIP vision válidos e ignora as vistas que não estão conectadas.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `positivo` | Condicionamento positivo contendo os embeddings de múltiplas vistas combinados com codificação posicional. | CONDITIONING |
| `negativo` | Condicionamento negativo com valores zero correspondendo à forma do condicionamento positivo. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2ConditioningMultiView/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1492b51661d0bb8f2c142c1b1e8ef104beed1b9dae532a970e2928e27ad71d69`
