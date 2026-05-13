> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraImageToVideo/pt-BR.md)

O nó WanCameraImageToVideo converte imagens em sequências de vídeo gerando representações latentes para geração de vídeos. Ele processa entradas de condicionamento e imagens iniciais opcionais para criar latentes de vídeo que podem ser usados com modelos de vídeo. O nó suporta condições de câmera e saídas de visão CLIP para maior controle na geração de vídeos.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|-----------|----------|-------|-------------|
| `positivo` | CONDITIONING | Sim | - | Prompts de condicionamento positivo para geração de vídeo |
| `negativo` | CONDITIONING | Sim | - | Prompts de condicionamento negativo a serem evitados na geração de vídeo |
| `vae` | VAE | Sim | - | Modelo VAE para codificar imagens para o espaço latente |
| `largura` | INT | Sim | 16 a MAX_RESOLUTION | Largura do vídeo de saída em pixels (padrão: 832, passo: 16) |
| `altura` | INT | Sim | 16 a MAX_RESOLUTION | Altura do vídeo de saída em pixels (padrão: 480, passo: 16) |
| `comprimento` | INT | Sim | 1 a MAX_RESOLUTION | Número de quadros na sequência de vídeo (padrão: 81, passo: 4) |
| `tamanho_do_lote` | INT | Sim | 1 a 4096 | Número de vídeos a serem gerados simultaneamente (padrão: 1) |
| `clip_vision_output` | CLIP_VISION_OUTPUT | Não | - | Saída opcional de visão CLIP para condicionamento adicional |
| `imagem_inicial` | IMAGE | Não | - | Imagem inicial opcional para iniciar a sequência de vídeo. Quando fornecida, os primeiros quadros do vídeo serão baseados nesta imagem, com uma máscara aplicada para mesclar os quadros iniciais com o conteúdo gerado. A imagem é redimensionada para corresponder à largura e altura especificadas. |
| `condições_da_câmera` | WAN_CAMERA_EMBEDDING | Não | - | Condições opcionais de incorporação de câmera para geração de vídeo. Quando fornecidas, essas condições são aplicadas tanto ao condicionamento positivo quanto ao negativo. |

**Observação:** Quando `start_image` é fornecido, o nó o utiliza para inicializar a sequência de vídeo e aplica mascaramento para mesclar os quadros iniciais com o conteúdo gerado. Os parâmetros `camera_conditions` e `clip_vision_output` são opcionais, mas quando fornecidos, modificam o condicionamento tanto para prompts positivos quanto negativos.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `positivo` | CONDITIONING | Condicionamento positivo modificado com condições de câmera e saídas de visão CLIP aplicadas |
| `negativo` | CONDITIONING | Condicionamento negativo modificado com condições de câmera e saídas de visão CLIP aplicadas |
| `latent` | LATENT | Representação latente de vídeo gerada para uso com modelos de vídeo. O tensor latente tem dimensões [batch_size, 16, quadros, altura/8, largura/8] onde quadros é calculado como ((comprimento - 1) // 4) + 1. |

---
**Source fingerprint (SHA-256):** `19d76097d580b14663afd0aab58810f9dc1685cd32e8f67aa43c820be65239e7`
