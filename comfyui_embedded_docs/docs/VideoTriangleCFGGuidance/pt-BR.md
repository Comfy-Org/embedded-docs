# VideoTriangleCFGGuidance

O nó VideoTriangleCFGGuidance aplica um padrão de orientação triangular de escala livre de classificador a modelos de vídeo. Ele modifica a escala de condicionamento ao longo do tempo usando uma função de onda triangular que oscila entre o valor mínimo de CFG e a escala de condicionamento original. Isso cria um padrão de orientação dinâmico que pode ajudar a melhorar a consistência e a qualidade da geração de vídeos.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model` | O modelo de vídeo ao qual aplicar a orientação CFG triangular | MODEL | Sim | - |
| `min_cfg` | O valor mínimo da escala CFG para o padrão triangular (padrão: 1.0) | FLOAT | Sim | 0.0 - 100.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `model` | O modelo modificado com a orientação CFG triangular aplicada | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTriangleCFGGuidance/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0b854d78f32e265b1a4322cb11b231df33e6072611142537e0c8cff4e93db49a`
