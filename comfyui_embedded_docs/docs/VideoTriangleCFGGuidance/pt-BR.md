# VideoTriangleCFGGuidance

O nó VideoTriangleCFGGuidance aplica um padrão de escala de orientação livre de classificador (CFG) triangular a um modelo de vídeo. Ele varia a escala de condicionamento ao longo do tempo usando uma onda triangular que oscila entre `min_cfg` e a escala de condicionamento original do modelo. Isso cria um padrão de orientação dinâmico que pode ajudar a melhorar a consistência e a qualidade da geração de vídeos.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo de vídeo ao qual aplicar a orientação CFG triangular | MODEL | Sim | - |
| `min_cfg` | O valor mínimo da escala CFG para o padrão triangular (padrão: 1.0). Este parâmetro é exibido na seção avançada da interface do nó. | FLOAT | Sim | 0.0 - 100.0 (step: 0.5, round: 0.01) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `model` | O modelo modificado com a orientação CFG triangular aplicada | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTriangleCFGGuidance/pt-BR.md)

---
**Source fingerprint (SHA-256):** `412d84d402f8c9a4852ee7b3f0ca0ab5650658fc26a37d10333a653e92e0294e`
