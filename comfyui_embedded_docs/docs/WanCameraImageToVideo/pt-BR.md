> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraImageToVideo/pt-BR.md)

O nó WanCameraImageToVideo converte imagens em sequências de vídeo gerando representações latentes para geração de vídeo. Ele processa entradas de condicionamento e imagens iniciais opcionais para criar latentes de vídeo que podem ser usados com modelos de vídeo. O nó suporta condições de câmera e saídas de visão CLIP para um controle aprimorado na geração de vídeo.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sim | - | Prompts de condicionamento positivo para geração de vídeo |
| `negative` | CONDITIONING | Sim | - | Prompts de condicionamento negativo para evitar na geração de vídeo |
| `vae` | VAE | Sim | - | Modelo VAE para codificar imagens no espaço latente |
| `width` | INT | Sim | 16 a MAX_RESOLUTION | Largura do vídeo de saída em pixels (padrão: 832, passo: 16) |
| `height` | INT | Sim | 16 a MAX_RESOLUTION | Altura do vídeo de saída em pixels (padrão: 480, passo: 16) |
| `length` | INT | Sim | 1 a MAX_RESOLUTION | Número de quadros na sequência de vídeo (padrão: 81, passo: 4) |
| `batch_size` | INT | Sim | 1 a 4096 | Número de vídeos a serem gerados simultaneamente (padrão: 1) |
| `clip_vision_output` | CLIP_VISION_OUTPUT | Não | - | Saída de visão CLIP opcional para condicionamento adicional |
| `start_image` | IMAGE | Não | - | Imagem inicial opcional para inicializar a sequência de vídeo |
| `camera_conditions` | WAN_CAMERA_EMBEDDING | Não | - | Condições de incorporação de câmera opcionais para geração de vídeo |

**Observação:** Quando `start_image` é fornecida, o nó a usa para inicializar a sequência de vídeo e aplica mascaramento para mesclar os quadros iniciais com o conteúdo gerado. Os parâmetros `camera_conditions` e `clip_vision_output` são opcionais, mas quando fornecidos, eles modificam o condicionamento tanto para os prompts positivos quanto para os negativos.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Condicionamento positivo modificado com as condições de câmera e saídas de visão CLIP aplicadas |
| `negative` | CONDITIONING | Condicionamento negativo modificado com as condições de câmera e saídas de visão CLIP aplicadas |
| `latent` | LATENT | Representação latente de vídeo gerada para uso com modelos de vídeo |
