# WanCameraImageToVideo

O nó WanCameraImageToVideo prepara dados de condicionamento e latentes para geração de vídeo controlada por câmera a partir de imagens. Ele recebe prompts de condicionamento positivo e negativo, juntamente com entradas opcionais, como uma imagem inicial, saída de visão CLIP e condições de câmera, e retorna condicionamento atualizado mais um tensor latente vazio pronto para um modelo de vídeo preencher.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positivo` | Prompts de condicionamento positivo para geração de vídeo | CONDITIONING | Sim | - |
| `negativo` | Prompts de condicionamento negativo a evitar na geração de vídeo | CONDITIONING | Sim | - |
| `vae` | Modelo VAE para codificar imagens no espaço latente | VAE | Sim | - |
| `largura` | Largura do vídeo de saída em pixels (padrão: 832, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `altura` | Altura do vídeo de saída em pixels (padrão: 480, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `comprimento` | Número de quadros na sequência de vídeo (padrão: 81, passo: 4) | INT | Sim | 1 a MAX_RESOLUTION |
| `tamanho_do_lote` | Número de vídeos a gerar simultaneamente (padrão: 1) | INT | Sim | 1 a 4096 |
| `clip_vision_output` | Saída de visão CLIP opcional para condicionamento adicional | CLIP_VISION_OUTPUT | Não | - |
| `imagem_inicial` | Imagem inicial opcional para inicializar a sequência de vídeo. Quando fornecida, apenas os primeiros `length` quadros são usados, e a imagem é redimensionada para corresponder à `width` e à `height` especificadas. Os primeiros quadros da sequência são codificados no latente e uma máscara é aplicada para mesclar os quadros iniciais com o conteúdo gerado. | IMAGE | Não | - |
| `condições_da_câmera` | Condições opcionais de embedding de câmera para geração de vídeo. Quando fornecidas, essas condições são aplicadas tanto ao condicionamento positivo quanto ao negativo. | WAN_CAMERA_EMBEDDING | Não | - |

**Observação:** Quando `start_image` é fornecido, o nó define os valores de `concat_latent_image` e `concat_mask` tanto no condicionamento `positive` quanto no `negative`. Os parâmetros `camera_conditions` e `clip_vision_output` são opcionais, mas, quando fornecidos, modificam o condicionamento tanto para o prompt positivo quanto para o negativo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | Condicionamento positivo modificado com condições de câmera, saída de visão CLIP e/ou dados de imagem inicial aplicados | CONDITIONING |
| `negative` | Condicionamento negativo modificado com condições de câmera, saída de visão CLIP e/ou dados de imagem inicial aplicados | CONDITIONING |
| `latent` | Representação latente de vídeo vazia para uso com modelos de vídeo. O tensor latente tem dimensões [batch_size, 16, frames, height/8, width/8], onde frames é calculado como ((length - 1) // 4) + 1. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraImageToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `467a82be0dfd6ac1c3b2dd2a6cb02e0d0749de4536a7fbdb000456b817b20ebb`
