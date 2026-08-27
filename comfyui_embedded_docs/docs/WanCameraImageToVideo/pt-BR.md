# WanCameraImageToVideo

O nó WanCameraImageToVideo prepara dados de condicionamento e latentes para geração de vídeo a partir de imagens. Ele recebe prompts de condicionamento positivo e negativo, juntamente com uma imagem inicial opcional e controles opcionais de câmera, e gera condicionamento modificado além de um tensor latente vazio pronto para ser preenchido por um modelo de vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `positivo` | Prompts de condicionamento positivos para geração de vídeo | CONDITIONING | Sim | - |
| `negativo` | Prompts de condicionamento negativos a evitar na geração de vídeo | CONDITIONING | Sim | - |
| `vae` | Modelo VAE para codificar imagens no espaço latente | VAE | Sim | - |
| `largura` | Largura do vídeo de saída em pixels (padrão: 832, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `altura` | Altura do vídeo de saída em pixels (padrão: 480, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `comprimento` | Número de quadros na sequência de vídeo (padrão: 81, passo: 4) | INT | Sim | 1 a MAX_RESOLUTION |
| `tamanho_do_lote` | Número de vídeos a serem gerados simultaneamente (padrão: 1) | INT | Sim | 1 a 4096 |
| `clip_vision_output` | Saída opcional de CLIP vision para condicionamento adicional | CLIP_VISION_OUTPUT | Não | - |
| `imagem_inicial` | Imagem inicial opcional para inicializar a sequência de vídeo. Quando fornecida, os primeiros quadros do vídeo serão baseados nesta imagem, com uma máscara aplicada para mesclar os quadros iniciais com o conteúdo gerado. A imagem é redimensionada para corresponder à largura e altura especificadas. | IMAGE | Não | - |
| `condições_da_câmera` | Condições opcionais de incorporação de câmera para geração de vídeo. Quando fornecidas, essas condições são aplicadas tanto ao condicionamento positivo quanto ao negativo. | WAN_CAMERA_EMBEDDING | Não | - |

**Nota:** Quando `start_image` é fornecida, apenas os primeiros `length` quadros da imagem de entrada são usados para inicializar a sequência de vídeo, e o nó aplica uma máscara para mesclar esses quadros iniciais com o conteúdo gerado. Os parâmetros `camera_conditions` e `clip_vision_output` são opcionais, mas, quando fornecidos, eles modificam o condicionamento tanto para os prompts positivos quanto para os negativos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positivo` | Condicionamento positivo modificado com condições de câmera aplicadas, saídas de CLIP vision e/ou dados da imagem inicial | CONDITIONING |
| `negativo` | Condicionamento negativo modificado com condições de câmera aplicadas, saídas de CLIP vision e/ou dados da imagem inicial | CONDITIONING |
| `latente` | Representação latente de vídeo vazia gerada para uso com modelos de vídeo. O tensor latente tem dimensões [batch_size, 16, frames, height/8, width/8], onde frames é calculado como ((length - 1) // 4) + 1. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraImageToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `467a82be0dfd6ac1c3b2dd2a6cb02e0d0749de4536a7fbdb000456b817b20ebb`
