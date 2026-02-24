> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFirstLastFrameToVideo/pt-BR.md)

O nó WanFirstLastFrameToVideo cria condicionamento de vídeo combinando quadros inicial e final com prompts de texto. Ele gera uma representação latente para geração de vídeo codificando o primeiro e o último quadro, aplicando máscaras para orientar o processo de geração e incorporando recursos de visão CLIP quando disponíveis. Este nó prepara condicionamentos positivo e negativo para modelos de vídeo gerarem sequências coerentes entre pontos inicial e final especificados.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sim | - | Condicionamento de texto positivo para orientar a geração do vídeo |
| `negative` | CONDITIONING | Sim | - | Condicionamento de texto negativo para orientar a geração do vídeo |
| `vae` | VAE | Sim | - | Modelo VAE usado para codificar imagens no espaço latente |
| `width` | INT | Não | 16 a MAX_RESOLUTION | Largura do vídeo de saída (padrão: 832, incremento: 16) |
| `height` | INT | Não | 16 a MAX_RESOLUTION | Altura do vídeo de saída (padrão: 480, incremento: 16) |
| `length` | INT | Não | 1 a MAX_RESOLUTION | Número de quadros na sequência de vídeo (padrão: 81, incremento: 4) |
| `batch_size` | INT | Não | 1 a 4096 | Número de vídeos a serem gerados simultaneamente (padrão: 1) |
| `clip_vision_start_image` | CLIP_VISION_OUTPUT | Não | - | Recursos de visão CLIP extraídos da imagem inicial |
| `clip_vision_end_image` | CLIP_VISION_OUTPUT | Não | - | Recursos de visão CLIP extraídos da imagem final |
| `start_image` | IMAGE | Não | - | Imagem do quadro inicial para a sequência de vídeo |
| `end_image` | IMAGE | Não | - | Imagem do quadro final para a sequência de vídeo |

**Observação:** Quando tanto `start_image` quanto `end_image` são fornecidos, o nó cria uma sequência de vídeo que faz a transição entre esses dois quadros. Os parâmetros `clip_vision_start_image` e `clip_vision_end_image` são opcionais, mas quando fornecidos, seus recursos de visão CLIP são concatenados e aplicados tanto ao condicionamento positivo quanto ao negativo.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Condicionamento positivo com codificação de quadro de vídeo e recursos de visão CLIP aplicados |
| `negative` | CONDITIONING | Condicionamento negativo com codificação de quadro de vídeo e recursos de visão CLIP aplicados |
| `latent` | LATENT | Tensor latente vazio com dimensões correspondentes aos parâmetros de vídeo especificados |
