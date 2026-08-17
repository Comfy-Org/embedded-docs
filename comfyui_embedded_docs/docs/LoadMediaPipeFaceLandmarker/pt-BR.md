# Carregar MediaPipe Face Landmarker

Este nó carrega um modelo MediaPipe Face Landmarker v2, capaz de detectar faces e pontos de referência faciais (como olhos, nariz e boca) em imagens. O modelo carregado contém duas variantes de detecção (short e full), além de dados de malha compartilhados, blendshapes e geometria canônica para análise facial.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model_name` | Modelo de detecção facial de models/detection/. | COMBO | Sim | Lista de modelos disponíveis no diretório `models/detection/` |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `FACE_DETECTION_MODEL` | Um objeto de modelo MediaPipe Face Landmarker carregado, contendo ambas as variantes de detecção (short/full), dados compartilhados de malha e blendshapes, geometria canônica, conjuntos de conexões de topologia facial e patchers de modelo para gerenciamento de GPU. | FACE_DETECTION_MODEL |

**Observação:** A saída é um objeto complexo que pode ser usado por outros nós para tarefas de detecção de faces e extração de pontos de referência. Ela contém duas variantes de detecção: "short" para detecção de curto alcance e "full" para detecção de alcance completo.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadMediaPipeFaceLandmarker/pt-BR.md)

---
**Source fingerprint (SHA-256):** `33dda845b572ccffc1bd4b64fb9c338ce4313783b092fe311d89741a211f18c9`
