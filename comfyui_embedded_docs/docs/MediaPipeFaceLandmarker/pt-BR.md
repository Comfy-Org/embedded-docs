> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MediaPipeFaceLandmarker/pt-BR.md)

# Visão Geral

Detecta rostos em uma imagem e identifica 468 pontos de referência faciais (pontos-chave) em cada rosto usando os modelos BlazeFace e FaceMesh do MediaPipe. Também calcula os coeficientes de blendshape ARKit-52 para análise de expressões faciais. O nó pode processar múltiplas imagens em lote e gera tanto os dados dos pontos de referência quanto as caixas delimitadoras para cada rosto detectado.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `face_detection_model` | FACE_DETECTION_MODEL | Sim | | O modelo de detecção facial do MediaPipe a ser usado para detecção de pontos de referência. |
| `image` | IMAGE | Sim | | A imagem de entrada ou lote de imagens para detectar rostos. |
| `detector_variant` | COMBO | Sim | `"short"`<br>`"full"`<br>`"both"` | Alcance do detector facial. `"short"` é ajustado para rostos próximos (até ~2 m da câmera); `"full"` cobre rostos mais distantes/menores (até ~5 m) mas é mais lento. `"both"` executa ambos os detectores e mantém aquele que encontrou mais rostos por quadro (~2x custo de detecção). Padrão: `"short"`. |
| `num_faces` | INT | Sim | 0 a 16 | Número máximo de rostos a retornar por quadro. 0 significa sem limite (retorna todos os detectados). Padrão: 1. |
| `min_confidence` | FLOAT | Não | 0,00 a 1,00 | Limiar de pontuação do BlazeFace. Valores mais baixos ajudam a capturar rostos pequenos ou ocluídos. Padrão: 0,5. |
| `missing_frame_fallback` | COMBO | Não | `"empty"`<br>`"previous"`<br>`"interpolate"` | Comportamento por quadro quando a detecção falha em um lote. `"empty"` deixa o quadro sem rosto. `"previous"` copia a detecção bem-sucedida mais recente. `"interpolate"` interpola pontos de referência/caixa delimitadora/blendshapes entre quadros bem-sucedidos adjacentes. Múltiplos rostos: pareia rostos entre quadros por NN guloso do centro da caixa delimitadora. Padrão: `"empty"`. |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `face_landmarks` | FACE_LANDMARKS | Uma saída estruturada contendo resultados de detecção facial por quadro, incluindo 468 pontos de referência faciais, coeficientes de blendshape ARKit-52, matrizes de transformação e conjuntos de conexões para visualização de malha. |
| `bboxes` | BOUNDING_BOX | Uma lista de caixas delimitadoras para cada rosto detectado, com coordenadas (x, y, largura, altura), rótulo "face" e pontuação de confiança. Uma lista por quadro de entrada. |

---
**Source fingerprint (SHA-256):** `f60ed6201288a59d65d62cc98c12f227a353870c36decea8da81a063cfdf2bba`
