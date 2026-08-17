# WanCameraImageToVideo

O nó WanCameraImageToVideo prepara dados de condicionamento e latentes para a geração de vídeos a partir de imagens. Ele recebe prompts de condicionamento positivos e negativos, juntamente com imagens iniciais e controles de câmera opcionais, e gera condicionamento modificado e um tensor latente vazio pronto para ser preenchido por um modelo de vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positive` | Prompts de condicionamento positivos para a geração de vídeo | CONDITIONING | Sim | - |
| `negative` | Prompts de condicionamento negativos para evitar na geração de vídeo | CONDITIONING | Sim | - |
| `vae` | Modelo VAE para codificar imagens para o espaço latente | VAE | Sim | - |
| `width` | Largura do vídeo de saída em pixels (padrão: 832, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `height` | Altura do vídeo de saída em pixels (padrão: 480, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `length` | Número de quadros na sequência de vídeo (padrão: 81, passo: 4) | INT | Sim | 1 a MAX_RESOLUTION |
| `batch_size` | Número de vídeos a serem gerados simultaneamente (padrão: 1) | INT | Sim | 1 a 4096 |
| `clip_vision_output` | Saída opcional do CLIP Vision para condicionamento adicional | CLIP_VISION_OUTPUT | Não | - |
| `start_image` | Imagem inicial opcional para inicializar a sequência de vídeo. Quando fornecida, os primeiros quadros do vídeo serão baseados nessa imagem, com uma máscara aplicada para mesclar os quadros iniciais com o conteúdo gerado. A imagem é redimensionada para corresponder à largura e à altura especificadas. | IMAGE | Não | - |
| `camera_conditions` | Condições opcionais de embedding de câmera para a geração de vídeo. Quando fornecidas, essas condições são aplicadas tanto ao condicionamento positivo quanto ao negativo. | WAN_CAMERA_EMBEDDING | Não | - |

**Observação:** Quando `start_image` é fornecido, o nó o utiliza para inicializar a sequência de vídeo e aplica uma máscara para mesclar os quadros iniciais com o conteúdo gerado. Os parâmetros `camera_conditions` e `clip_vision_output` são opcionais, mas, quando fornecidos, modificam o condicionamento tanto para os prompts positivos quanto para os negativos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | Condicionamento positivo modificado com condições de câmera, saídas do CLIP Vision e/ou dados da imagem inicial aplicados | CONDITIONING |
| `negative` | Condicionamento negativo modificado com condições de câmera, saídas do CLIP Vision e/ou dados da imagem inicial aplicados | CONDITIONING |
| `latent` | Representação latente de vídeo vazia gerada para uso com modelos de vídeo. O tensor latente tem dimensões [batch_size, 16, frames, height/8, width/8], onde frames é calculado como ((length - 1) // 4) + 1. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraImageToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `467a82be0dfd6ac1c3b2dd2a6cb02e0d0749de4536a7fbdb000456b817b20ebb`
