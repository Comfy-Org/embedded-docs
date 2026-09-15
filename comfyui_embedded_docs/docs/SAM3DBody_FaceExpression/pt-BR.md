# Expressão Facial para Corpo SAM3D

Este nó adiciona expressões faciais a um corpo SAM3D detectando rostos em uma imagem com o MediaPipe Face Landmarker, correspondendo cada rosto detectado a uma pessoa rastreada e mapeando os 52 blendshapes do ARKit para os parâmetros de expressão de 72 eixos do MHR. Em seguida, ele executa novamente o modelo de corpo para que os vértices da malha e os keypoints de saída reflitam a nova expressão.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `sam3d_body_model` | O modelo de corpo SAM3D que contém o detector de pontos faciais usado para detectar rostos e regenerar a malha do corpo. | SAM3D_BODY_MODEL | Sim | - |
| `mhr_pose_data` | Dados de pose contendo pessoas rastreadas por quadro, com caixas delimitadoras, keypoints e parâmetros de expressão. O nó corresponde cada rosto detectado a uma pessoa e grava os parâmetros de expressão atualizados nesses dados. | MHR_POSE_DATA | Sim | - |
| `image` | Quadros de imagem usados para detectar rostos. Se o lote de imagens tiver menos quadros do que os dados de pose, o último quadro será reutilizado para os quadros restantes. | IMAGE | Sim | - |
| `strength` | Multiplicador global em todos os blendshapes. >1 exagera. Padrão: 1.0. | FLOAT | Não | 0.0 a 4.0 (passo 0.05, padrão 1.0) |
| `mouth_strength` | Multiplicador nas formas de boca/mandíbula. O jawOpen do MediaPipe satura perto de 1.0. Padrão: 1.0. | FLOAT | Não | 0.0 a 4.0 (passo 0.05, padrão 1.0) |
| `eye_strength` | Multiplicador nas formas dos olhos. O MediaPipe raramente excede 0.5; 2-3x frequentemente é necessário. Padrão: 2.0. | FLOAT | Não | 0.0 a 4.0 (passo 0.05, padrão 2.0) |
| `brow_strength` | Multiplicador nas formas de sobrancelha/bochecha/desdém. O MediaPipe produz ~0.1-0.3; 2-3x. Padrão: 2.0. | FLOAT | Não | 0.0 a 4.0 (passo 0.05, padrão 2.0) |
| `input_threshold` | Zona morta na saída bruta do MediaPipe (abaixo = zero, acima = remapeamento linear). Padrão: 0.02. | FLOAT | Não | 0.0 a 0.5 (passo 0.01, padrão 0.02) |
| `blendshape_smooth_window` | Janela gaussiana no sinal por quadro do MediaPipe antes do mapeamento MHR. A saída bruta do MediaPipe oscila 30-70% de um quadro para outro em rostos estáticos. 1 = desativado. Use valores ímpares. Padrão: 7. | INT | Não | 1 a 31 (passo 2, padrão 7) |

Nota: Uma subtração de linha de base por clipe é aplicada somente quando pelo menos 30 quadros no clipe contêm pessoas detectadas. Lacunas de detecção de até 12 quadros por pessoa são preenchidas por interpolação.

## Saídas

| Nome de Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `mhr_pose_data` | Os dados de pose atualizados. Os parâmetros de expressão de cada pessoa rastreada são substituídos pela expressão facial mapeada, e os vértices da malha e os keypoints são regenerados para corresponder. | MHR_POSE_DATA |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3DBody_FaceExpression/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b2299e51be3556e639d5b04fcbee541ecf41e0d84c2c8a0fd4e211b2f6caba0b`
