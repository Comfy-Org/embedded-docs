# Carregar MediaPipe Face Landmarker

## Visão Geral

Este nó carrega um modelo MediaPipe Face Landmarker v2, que pode detectar rostos e marcos faciais (como olhos, nariz e boca) em imagens. Ele contém duas variantes de detecção (curto alcance e alcance total), juntamente com dados de malha compartilhados, blendshapes e geometria canônica para análise facial.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model_name` | Modelo de detecção facial do diretório models/detection/. | COMBO | Sim | Lista de modelos disponíveis no diretório `models/detection/` |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `FACE_DETECTION_MODEL` | Um objeto de modelo FaceLandmarker carregado contendo ambas as variantes de detecção (curto/completo), conjuntos de conexões para topologia facial, dados canônicos e patchers de modelo para gerenciamento de GPU. | FACE_DETECTION_MODEL |

**Nota:** A saída é um objeto complexo que pode ser usado por outros nós para tarefas de detecção facial e extração de marcos faciais. Ele contém duas variantes de detecção: "short" para detecção de curto alcance e "full" para detecção de alcance total.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadMediaPipeFaceLandmarker/pt-BR.md)

---
**Source fingerprint (SHA-256):** `33dda845b572ccffc1bd4b64fb9c338ce4313783b092fe311d89741a211f18c9`
