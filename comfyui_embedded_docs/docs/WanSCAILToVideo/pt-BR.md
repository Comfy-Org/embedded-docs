# WanSCAILToVideo

O nó WanSCAILToVideo prepara o condicionamento e um espaço latente vazio para a geração de vídeo com os modelos de vídeo SCAIL e SCAIL-2. Ele processa entradas opcionais, como imagens de referência, vídeos de pose, saídas de visão CLIP, máscaras de identidade coloridas e blocos de quadros anteriores, incorporando-as ao condicionamento positivo e negativo. O nó gera como saída o condicionamento modificado e um tensor latente em branco com as dimensões de vídeo especificadas, pronto para amostragem.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `positivo` | A entrada de condicionamento positivo. | CONDITIONING | Sim | - |
| `negativo` | A entrada de condicionamento negativo. | CONDITIONING | Sim | - |
| `vae` | O modelo VAE usado para codificar imagens e quadros de vídeo. | VAE | Sim | - |
| `largura` | A largura do vídeo de saída em pixels (padrão: 512). Os valores variam em incrementos de 32. | INT | Sim | 32 a MAX_RESOLUTION |
| `altura` | A altura do vídeo de saída em pixels (padrão: 896). Os valores variam em incrementos de 32. | INT | Sim | 32 a MAX_RESOLUTION |
| `duração` | O número de quadros no vídeo (padrão: 81). Os valores variam em incrementos de 4. | INT | Sim | 1 a MAX_RESOLUTION |
| `tamanho_do_lote` | O número de vídeos a gerar em um lote (padrão: 1). | INT | Sim | 1 a 4096 |
| `vídeo_de_pose` | Vídeo usado para condicionamento de pose. Será reduzido à metade da resolução do vídeo principal. | IMAGE | Não | - |
| `pose_video_mask` | Apenas SCAIL-2. Vídeo de máscara SAM3 colorida por identidade na mesma resolução que `pose_video`. | IMAGE | Não | - |
| `replacement_mode` | Apenas SCAIL-2. False = Modo Animação (`pose_video_mask` deve ter fundo preto). True = Modo Substituição (`pose_video_mask` deve ter fundo branco). (padrão: False) | BOOLEAN | Não | - |
| `força_da_pose` | Força do latente de pose. (padrão: 1.0) | FLOAT | Sim | 0.0 a 10.0 |
| `início_da_pose` | Etapa inicial do condicionamento de pose. (padrão: 0.0) | FLOAT | Sim | 0.0 a 1.0 |
| `fim_da_pose` | Etapa final do condicionamento de pose. (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `imagem_de_referência` | Imagem de referência. A primeira imagem é a referência primária (compõe todas as identidades sobre ela). SCAIL-2: imagens extras no lote são usadas como vistas adicionais (vista traseira, close-up, fundo ocluído), cada uma precisando de uma `reference_image_mask` correspondente na cor daquela identidade. | IMAGE | Não | - |
| `reference_image_mask` | Apenas SCAIL-2. Máscara de referência colorida, com lote correspondente a `reference_image` (primeira = máscara de referência primária, restantes = máscaras de identidade para as `reference_image` adicionais). | IMAGE | Não | - |
| `clip_vision_output` | Recursos de visão CLIP para condicionamento. O modelo é treinado com redimensionamento por alongamento para a proporção de aspecto. | CLIP_VISION_OUTPUT | Não | - |
| `video_frame_offset` | Quadro de saída cumulativo no qual este bloco começa. Conecte a partir da saída `video_frame_offset` do bloco anterior. (padrão: 0) | INT | Sim | 0 a MAX_RESOLUTION |
| `previous_frame_count` | Quadros finais de `previous_frames` a ancorar. SCAIL-2 treinado em 5 (blocos de 81 quadros, passo de 76 quadros). (padrão: 5). Os valores variam em incrementos de 4. | INT | Sim | 1 a MAX_RESOLUTION |
| `previous_frames` | Apenas SCAIL-2. Saída decodificada completa do bloco anterior. Apenas os últimos `previous_frame_count` são usados como âncora de extensão. | IMAGE | Não | - |

**Observação:** As entradas `pose_video` e `pose_video_mask` são truncadas juntas para o menor dos dois, e são processadas apenas para os primeiros `length` quadros. Se qualquer entrada for menor ou igual a `video_frame_offset`, ela será ignorada completamente. O `pose_video` é reduzido à metade da resolução do vídeo principal antes da codificação, e o latente de pose codificado é multiplicado por `pose_strength` e aplicado ao condicionamento apenas entre as etapas de timestep `pose_start` e `pose_end`. Se `pose_video_mask` for fornecido, o vídeo de máscara colorida é reduzido para metade da resolução e convertido em uma máscara de condução de 28 canais, que é adicionada tanto ao condicionamento positivo quanto ao negativo.

**Observação:** Quando `reference_image` é fornecida, cada imagem no lote é codificada individualmente em um latente e incorporada tanto ao condicionamento positivo quanto ao negativo. A primeira imagem é a referência primária; imagens adicionais são usadas como vistas adicionais, cada uma precisando de uma `reference_image_mask` correspondente. `reference_image_mask` só é usada quando `reference_image` também é fornecida; quando ambas são fornecidas, uma máscara de referência de 28 canais que vincula os quadros de referência às identidades também é construída a partir das máscaras e adicionada ao condicionamento. No Modo Substituição (`replacement_mode=True`), a imagem de referência é composta em um fundo preto usando a máscara de imagem de referência como um matte alfa. Quando `clip_vision_output` é fornecido, ele é aplicado tanto ao condicionamento positivo quanto ao negativo.

**Observação:** Quando `previous_frames` é fornecido, apenas os últimos `previous_frame_count` quadros são usados como âncora de extensão, e `video_frame_offset` é ajustado de acordo (reduzido pelo número de quadros ancorados, limitado a 0). Os quadros ancorados são codificados e gravados no início do latente de saída, e uma máscara de ruído é incluída para que esses quadros sejam mantidos inalterados durante a geração.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `positive` | O condicionamento positivo modificado, potencialmente contendo latentes de imagem de referência incorporados, saída de visão CLIP, latentes de vídeo de pose, máscaras de condução, máscaras de referência ou latentes de quadros anteriores. | CONDITIONING |
| `negative` | O condicionamento negativo modificado, potencialmente contendo latentes de imagem de referência incorporados, saída de visão CLIP, latentes de vídeo de pose, máscaras de condução, máscaras de referência ou latentes de quadros anteriores. | CONDITIONING |
| `latent` | Um tensor latente vazio com formato `[batch_size, 16, ((length - 1) // 4) + 1, height // 8, width // 8]`. Quando `previous_frames` é fornecido, o latente é parcialmente preenchido com quadros anteriores codificados e uma máscara de ruído é incluída. | LATENT |
| `video_frame_offset` | Deslocamento ajustado + comprimento. Conecte ao próximo bloco para geração sequencial de vídeo. | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSCAILToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4a1a2201dfa94bd2f1330db02ec18a5e0a6aae9e9ac5ae97d456b7af1aa84b7b`
