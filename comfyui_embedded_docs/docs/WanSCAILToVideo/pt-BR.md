# WanSCAILToVideo

O nó WanSCAILToVideo prepara o condicionamento e um espaço latente vazio para a geração de vídeos. Ele processa entradas opcionais, como imagens de referência, vídeos de pose, saídas de CLIP vision e segmentos de quadros anteriores, incorporando-os ao condicionamento positivo e negativo para um modelo de vídeo. O nó produz o condicionamento modificado e um tensor latente em branco com as dimensões de vídeo especificadas.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `positive` | A entrada de condicionamento positivo. | CONDITIONING | Sim | - |
| `negative` | A entrada de condicionamento negativo. | CONDITIONING | Sim | - |
| `vae` | O modelo VAE usado para codificar imagens e quadros de vídeo. | VAE | Sim | - |
| `width` | A largura do vídeo de saída em pixels (padrão: 512). Ajustável em incrementos de 32. | INT | Sim | 32 to MAX_RESOLUTION |
| `height` | A altura do vídeo de saída em pixels (padrão: 896). Ajustável em incrementos de 32. | INT | Sim | 32 to MAX_RESOLUTION |
| `length` | O número de quadros no vídeo (padrão: 81). Ajustável em incrementos de 4 a partir de 1. | INT | Sim | 1 to MAX_RESOLUTION |
| `batch_size` | O número de vídeos a serem gerados em um lote (padrão: 1). | INT | Sim | 1 to 4096 |
| `pose_strength` | Força do latente de pose (padrão: 1.0). | FLOAT | Sim | 0.0 to 10.0 |
| `pose_start` | Etapa inicial do condicionamento de pose (padrão: 0.0). | FLOAT | Sim | 0.0 to 1.0 |
| `pose_end` | Etapa final do condicionamento de pose (padrão: 1.0). | FLOAT | Sim | 0.0 to 1.0 |
| `video_frame_offset` | Quadro de saída acumulado em que este segmento começa. Conecte a partir da saída video_frame_offset do segmento anterior (padrão: 0). | INT | Sim | 0 to MAX_RESOLUTION |
| `previous_frame_count` | Quadros finais de previous_frames para ancoragem. SCAIL-2 treinado com 5 (segmentos de 81 quadros, passo de 76 quadros) (padrão: 5). | INT | Sim | 1 to MAX_RESOLUTION |
| `pose_video` | Vídeo usado para condicionamento de pose. Será reduzido para metade da resolução do vídeo principal. | IMAGE | Não | - |
| `pose_video_mask` | Apenas SCAIL-2. Vídeo de máscara SAM3 colorido por identidade, na mesma resolução do pose_video. | IMAGE | Não | - |
| `replacement_mode` | Apenas SCAIL-2. False = Modo Animação (pose_video_mask deve ter fundo preto). True = Modo Substituição (pose_video_mask deve ter fundo branco). Padrão: False. | BOOLEAN | Não | - |
| `reference_image` | Imagem de referência. A primeira imagem é a referência principal (componha todas as identidades sobre ela). SCAIL-2: imagens extras do lote são usadas como vistas adicionais (vista traseira, close-up, fundo ocluído), cada uma exigindo uma reference_image_mask correspondente na cor dessa identidade. | IMAGE | Não | - |
| `reference_image_mask` | Apenas SCAIL-2. Máscara de referência colorida, com lote correspondente ao reference_image (primeira = máscara de referência principal, demais = máscaras de identidade para as imagens de referência adicionais). | IMAGE | Não | - |
| `clip_vision_output` | Características do CLIP vision para condicionamento. O modelo é treinado com redimensionamento por estiramento para a proporção de aspecto. | CLIP_VISION_OUTPUT | Não | - |
| `previous_frames` | Apenas SCAIL-2. Saída decodificada completa do segmento anterior. Apenas os últimos previous_frame_count quadros são usados como âncora de extensão. | IMAGE | Não | - |

**Nota:**

- As entradas `pose_video` e `pose_video_mask` são recortadas a partir de `video_frame_offset`; se o vídeo não tiver quadros além desse deslocamento, ele é ignorado. Em seguida, elas são truncadas juntas para o mais curto das duas e limitadas a `length` quadros. O `pose_video` é reduzido para metade da resolução do vídeo principal antes da codificação.
- A entrada `reference_image_mask` só se aplica quando `reference_image` também é fornecida. Cada imagem no lote de `reference_image` é codificada individualmente como uma referência latente de quadro único. No Modo Substituição (`replacement_mode=True`), as imagens de referência são compostas sobre um fundo preto usando a máscara de referência como matte alfa.
- Quando `clip_vision_output` é fornecido, ele é aplicado tanto ao condicionamento positivo quanto ao negativo.
- Quando `previous_frames` é fornecido, apenas os últimos `previous_frame_count` quadros são usados como âncora de extensão. O latente de saída é parcialmente preenchido com a codificação desses quadros, uma máscara de ruído é incluída na saída latente, e `video_frame_offset` é ajustado subtraindo-se o número de quadros mantidos (nunca abaixo de 0).

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `positive` | O condicionamento positivo modificado, potencialmente contendo latentes de imagem de referência incorporados, saída de CLIP vision, latentes de vídeo de pose, máscaras de condução, máscaras de referência ou latentes de quadros anteriores. | CONDITIONING |
| `negative` | O condicionamento negativo modificado, potencialmente contendo latentes de imagem de referência incorporados, saída de CLIP vision, latentes de vídeo de pose, máscaras de condução, máscaras de referência ou latentes de quadros anteriores. | CONDITIONING |
| `latent` | Um tensor latente vazio com o formato `[batch_size, 16, ((length - 1) // 4) + 1, height // 8, width // 8]`. Quando `previous_frames` é fornecido, o latente é parcialmente preenchido com quadros anteriores codificados e uma máscara de ruído é incluída. | LATENT |
| `video_frame_offset` | Deslocamento ajustado + length. Conecte ao próximo segmento para geração sequencial de vídeos. | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSCAILToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4a1a2201dfa94bd2f1330db02ec18a5e0a6aae9e9ac5ae97d456b7af1aa84b7b`
