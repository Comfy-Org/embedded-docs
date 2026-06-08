# Visão Geral

Este nó carrega um modelo MediaPipe Face Landmarker v2, que pode detectar rostos e pontos faciais de referência (como olhos, nariz e boca) em imagens. Ele contém duas variantes de detecção (curto alcance e alcance total) juntamente com dados de malha compartilhados, blendshapes e geometria canônica para análise facial.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model_name` | Modelo de detecção facial do diretório models/detection/. | STRING | Sim | Lista de modelos disponíveis no diretório `models/detection/` |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `FACE_DETECTION_MODEL` | Um objeto de modelo FaceLandmarker carregado contendo ambas as variantes de detecção (curto/alcance total), conjuntos de conexão para topologia facial, dados canônicos e patchers de modelo para gerenciamento de GPU. | FACE_DETECTION_MODEL |

**Observação:** A saída é um objeto complexo que pode ser utilizado por outros nós para tarefas de detecção facial e extração de pontos de referência. Ele contém duas variantes de detecção: "curto" para detecção de curto alcance e "total" para detecção de alcance total.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadMediaPipeFaceLandmarker/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b30bf4d04aa06a227f3661c0e1346d3dab3ea1e25d6627fce5b6480198203c26`
