# VideoTriangleCFGGuidance

O nó VideoTriangleCFGGuidance aplica um padrão de escala de orientação sem classificador em formato triangular a modelos de vídeo. Ele modifica a escala de orientação ao longo do tempo usando uma função de onda triangular que oscila entre o valor mínimo de CFG e a escala de orientação original. Isso cria um padrão de orientação dinâmico que pode ajudar a melhorar a consistência e a qualidade da geração de vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo de vídeo ao qual aplicar a orientação CFG triangular | MODEL | Sim | - |
| `min_cfg` | O valor mínimo da escala de CFG para o padrão triangular (por padrão: 1.0) | FLOAT | Sim | 0.0 - 100.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo modificado com a orientação CFG triangular aplicada | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTriangleCFGGuidance/pt-BR.md)

---
**Source fingerprint (SHA-256):** `412d84d402f8c9a4852ee7b3f0ca0ab5650658fc26a37d10333a653e92e0294e`
