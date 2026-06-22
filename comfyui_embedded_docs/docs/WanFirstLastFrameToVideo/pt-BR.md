# WanFirstLastFrameToVideo

O nó WanFirstLastFrameToVideo cria condicionamento de vídeo combinando quadros inicial e final com prompts de texto. Ele gera uma representação latente para geração de vídeo codificando o primeiro e o último quadro, aplicando máscaras para guiar o processo de geração e incorporando recursos de visão CLIP quando disponíveis. Este nó prepara condicionamentos positivo e negativo para modelos de vídeo gerarem sequências coerentes entre os pontos inicial e final especificados.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `positivo` | Condicionamento de texto positivo para guiar a geração do vídeo | CONDITIONING | Sim | - |
| `negativo` | Condicionamento de texto negativo para guiar a geração do vídeo | CONDITIONING | Sim | - |
| `vae` | Modelo VAE usado para codificar imagens para o espaço latente | VAE | Sim | - |
| `largura` | Largura do vídeo de saída (padrão: 832, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `altura` | Altura do vídeo de saída (padrão: 480, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `comprimento` | Número de quadros na sequência de vídeo (padrão: 81, passo: 4) | INT | Sim | 1 a MAX_RESOLUTION |
| `tamanho_do_lote` | Número de vídeos a serem gerados simultaneamente (padrão: 1) | INT | Sim | 1 a 4096 |
| `clip_vision_start_image` | Recursos de visão CLIP extraídos da imagem inicial | CLIP_VISION_OUTPUT | Não | - |
| `clip_vision_end_image` | Recursos de visão CLIP extraídos da imagem final | CLIP_VISION_OUTPUT | Não | - |
| `imagem_inicial` | Imagem do quadro inicial para a sequência de vídeo | IMAGE | Não | - |
| `imagem_final` | Imagem do quadro final para a sequência de vídeo | IMAGE | Não | - |

**Observação:** Quando tanto `start_image` quanto `end_image` são fornecidos, o nó cria uma sequência de vídeo que faz a transição entre esses dois quadros. Os parâmetros `clip_vision_start_image` e `clip_vision_end_image` são opcionais, mas quando fornecidos, seus recursos de visão CLIP são concatenados e aplicados tanto ao condicionamento positivo quanto ao negativo. A `start_image` é recortada para os primeiros `length` quadros, e a `end_image` é recortada para os últimos `length` quadros antes do processamento.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `positivo` | Condicionamento positivo com codificação de quadro de vídeo aplicada e recursos de visão CLIP | CONDITIONING |
| `negativo` | Condicionamento negativo com codificação de quadro de vídeo aplicada e recursos de visão CLIP | CONDITIONING |
| `latent` | Tensor latente vazio com dimensões correspondentes aos parâmetros de vídeo especificados | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFirstLastFrameToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8cfca692fc4975bb5238ce749d2102fad4b6cd84e96ef74c3eff2b297ee60c3c`
