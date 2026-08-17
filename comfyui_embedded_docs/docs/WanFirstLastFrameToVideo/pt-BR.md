# WanFirstLastFrameToVideo

O nó WanFirstLastFrameToVideo cria condicionamento de vídeo combinando quadros inicial e final com prompts de texto. Ele gera uma representação latente para a geração de vídeo codificando o primeiro e o último quadro, aplicando máscaras para orientar o processo de geração e incorporando características de visão do CLIP quando disponíveis. Este nó prepara o condicionamento positivo e negativo para modelos de vídeo gerarem sequências coerentes entre os pontos inicial e final especificados.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positive` | Condicionamento de texto positivo para orientar a geração de vídeo | CONDITIONING | Sim | - |
| `negative` | Condicionamento de texto negativo para orientar a geração de vídeo | CONDITIONING | Sim | - |
| `vae` | Modelo VAE usado para codificar imagens para o espaço latente | VAE | Sim | - |
| `width` | Largura do vídeo de saída (padrão: 832, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `height` | Altura do vídeo de saída (padrão: 480, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `length` | Número de quadros na sequência de vídeo (padrão: 81, passo: 4) | INT | Sim | 1 a MAX_RESOLUTION |
| `batch_size` | Número de vídeos a serem gerados simultaneamente (padrão: 1) | INT | Sim | 1 a 4096 |
| `clip_vision_start_image` | Características de visão do CLIP extraídas da imagem inicial | CLIP_VISION_OUTPUT | Não | - |
| `clip_vision_end_image` | Características de visão do CLIP extraídas da imagem final | CLIP_VISION_OUTPUT | Não | - |
| `start_image` | Imagem do quadro inicial para a sequência de vídeo | IMAGE | Não | - |
| `end_image` | Imagem do quadro final para a sequência de vídeo | IMAGE | Não | - |

**Nota:** Quando tanto `start_image` quanto `end_image` são fornecidos, o nó cria uma sequência de vídeo que faz a transição entre esses dois quadros. O `start_image` é recortado para os primeiros `length` quadros, e o `end_image` é recortado para os últimos `length` quadros antes do processamento. Se apenas um deles for fornecido, o lado ausente é preenchido com quadros cinza neutros. A máscara é definida como 0 onde os quadros inicial e final estão presentes e 1 em outros lugares. Os parâmetros `clip_vision_start_image` e `clip_vision_end_image` são opcionais; quando ambos são fornecidos, suas características de visão do CLIP são concatenadas e aplicadas tanto ao condicionamento positivo quanto ao negativo. Quando apenas um é fornecido, suas características são usadas isoladamente.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | Condicionamento positivo com codificação de quadros de vídeo e características de visão do CLIP aplicadas | CONDITIONING |
| `negative` | Condicionamento negativo com codificação de quadros de vídeo e características de visão do CLIP aplicadas | CONDITIONING |
| `latent` | Tensor latente vazio com dimensões correspondentes aos parâmetros de vídeo especificados | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFirstLastFrameToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0072e441cb80334c3c961d1bbf2d081c78bc38ed1eacca840c577a2d01b36f05`
