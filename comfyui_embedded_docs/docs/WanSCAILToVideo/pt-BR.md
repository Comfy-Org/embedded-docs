# WanSCAILToVideo

O nó WanSCAILToVideo prepara o condicionamento e um espaço latente vazio para a geração de vídeo com os modelos de vídeo SCAIL e SCAIL-2. Ele processa entradas opcionais como imagens de referência, vídeos de pose, saídas do CLIP vision, máscaras de identidade coloridas e segmentos de quadros anteriores, incorporando-os ao condicionamento positivo e negativo. O nó gera o condicionamento modificado e um tensor latente vazio nas dimensões de vídeo especificadas, pronto para a amostragem.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `positivo` | A entrada de condicionamento positivo. | CONDITIONING | Sim | - |
| `negativo` | A entrada de condicionamento negativo. | CONDITIONING | Sim | - |
| `vae` | O modelo VAE usado para codificar imagens e quadros de vídeo. | VAE | Sim | - |
| `largura` | A largura do vídeo de saída em pixels (padrão: 512). Os valores aumentam de 32 em 32. | INT | Sim | 32 to MAX_RESOLUTION |
| `altura` | A altura do vídeo de saída em pixels (padrão: 896). Os valores aumentam de 32 em 32. | INT | Sim | 32 to MAX_RESOLUTION |
| `duração` | O número de quadros no vídeo (padrão: 81). Os valores aumentam de 4 em 4. | INT | Sim | 1 to MAX_RESOLUTION |
| `tamanho_do_lote` | O número de vídeos a serem gerados em um lote (padrão: 1). | INT | Sim | 1 a 4096 |
| `vídeo_de_pose` | Vídeo usado para condicionamento de pose. Será reduzido para metade da resolução do vídeo principal. | IMAGE | Não | - |
| `pose_video_mask` | Apenas SCAIL-2. Vídeo de máscara SAM3 colorida por identidade, na mesma resolução do `pose_video`. | IMAGE | Não | - |
| `replacement_mode` | Apenas SCAIL-2. False = Modo Animação (`pose_video_mask` deve ter fundo preto). True = Modo Substituição (`pose_video_mask` deve ter fundo branco). (padrão: False) | BOOLEAN | Não | - |
| `força_da_pose` | Força do latente de pose. (padrão: 1.0) | FLOAT | Sim | 0.0 a 10.0 |
| `início_da_pose` | Passo inicial do condicionamento de pose. (padrão: 0.0) | FLOAT | Sim | 0.0 a 1.0 |
| `fim_da_pose` | Passo final do condicionamento de pose. (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `imagem_de_referência` | Imagem de referência. A primeira imagem é a referência principal (componha todas as identidades sobre ela). SCAIL-2: imagens adicionais do lote são usadas como visualizações adicionais (vista traseira, close-up, fundo ocluído), cada uma exigindo um `reference_image_mask` correspondente na cor daquela identidade. | IMAGE | Não | - |
| `reference_image_mask` | Apenas SCAIL-2. Máscara de referência colorida, com o lote correspondendo ao `reference_image` (a primeira é a máscara da referência principal; as demais são máscaras de identidade para as imagens de referência adicionais). | IMAGE | Não | - |
| `clip_vision_output` | Recursos visuais do CLIP para condicionamento. O modelo foi treinado com redimensionamento por estiramento para a proporção de aspecto. | CLIP_VISION_OUTPUT | Não | - |
| `video_frame_offset` | Quadro de saída acumulado no qual este segmento começa. Conecte à saída `video_frame_offset` do segmento anterior. (padrão: 0) | INT | Sim | 0 to MAX_RESOLUTION |
| `previous_frame_count` | Quadros finais de `previous_frames` usados como âncora. SCAIL-2 treinado com 5 (segmentos de 81 quadros, passo de 76 quadros). (padrão: 5) | INT | Sim | 1 to MAX_RESOLUTION |
| `previous_frames` | Apenas SCAIL-2. Saída decodificada completa do segmento anterior. Apenas os últimos `previous_frame_count` são usados como âncora de extensão. | IMAGE | Não | - |

**Observação:** As entradas `pose_video` e `pose_video_mask` são truncadas juntas até a mais curta das duas e processadas apenas para os primeiros `length` quadros. Se qualquer uma das entradas for mais curta ou igual a `video_frame_offset`, ela será ignorada por completo. O `pose_video` é reduzido para metade da resolução do vídeo principal antes da codificação, e o latente de pose codificado é multiplicado por `pose_strength` e aplicado ao condicionamento apenas entre os passos de timestep `pose_start` e `pose_end`. Se `pose_video_mask` for fornecida, o vídeo de máscara colorida é reduzido para metade da resolução e convertido em uma máscara de condução de 28 canais, que é adicionada tanto ao condicionamento positivo quanto ao negativo.

**Observação:** Quando `reference_image` é fornecida, cada imagem do lote é codificada individualmente em um latente e incorporada tanto ao condicionamento positivo quanto ao negativo. A primeira imagem é a referência principal; as imagens adicionais são usadas como visualizações adicionais, cada uma exigindo um `reference_image_mask` correspondente. `reference_image_mask` só é usado quando `reference_image` também é fornecida; quando ambos são fornecidos, uma máscara de referência de 28 canais que vincula os quadros de referência às identidades também é criada a partir das máscaras e adicionada ao condicionamento. No Modo Substituição (`replacement_mode=True`), a imagem de referência é composta sobre um fundo preto usando a máscara de referência como matte alfa. Quando `clip_vision_output` é fornecido, ele é aplicado tanto ao condicionamento positivo quanto ao negativo.

**Observação:** Quando `previous_frames` é fornecida, apenas os últimos `previous_frame_count` quadros são usados como âncora de extensão, e `video_frame_offset` é ajustado de acordo (reduzido pelo número de quadros ancorados, limitado a 0). Os quadros ancorados são codificados e gravados no início do latente de saída, e uma máscara de ruído é incluída para que esses quadros permaneçam inalterados durante a geração.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `positivo` | O condicionamento positivo modificado, potencialmente contendo latentes de imagem de referência incorporados, saída do CLIP vision, latentes de vídeo de pose, máscaras de condução, máscaras de referência ou latentes de quadros anteriores. | CONDITIONING |
| `negativo` | O condicionamento negativo modificado, potencialmente contendo latentes de imagem de referência incorporados, saída do CLIP vision, latentes de vídeo de pose, máscaras de condução, máscaras de referência ou latentes de quadros anteriores. | CONDITIONING |
| `latente` | Um tensor latente vazio de formato `[batch_size, 16, ((length - 1) // 4) + 1, height // 8, width // 8]`. Quando `previous_frames` é fornecida, o latente é parcialmente preenchido com quadros anteriores codificados e uma máscara de ruído é incluída. | LATENT |
| `video_frame_offset` | Deslocamento ajustado + length. Conecte ao próximo segmento para geração sequencial de vídeo. | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSCAILToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4a1a2201dfa94bd2f1330db02ec18a5e0a6aae9e9ac5ae97d456b7af1aa84b7b`
