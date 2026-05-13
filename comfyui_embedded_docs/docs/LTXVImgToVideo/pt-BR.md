> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideo/pt-BR.md)

O nó LTXVImgToVideo converte uma imagem de entrada em uma representação latente de vídeo para modelos de geração de vídeo. Ele recebe uma única imagem e a estende para uma sequência de quadros usando o codificador VAE, em seguida, aplica condicionamento com controle de intensidade para determinar quanto do conteúdo da imagem original é preservado versus modificado durante a geração do vídeo.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|--------------|-------------|-----------|-----------|
| `positive` | CONDITIONING | Sim | - | Prompts de condicionamento positivo para guiar a geração do vídeo |
| `negative` | CONDITIONING | Sim | - | Prompts de condicionamento negativo para evitar certos elementos no vídeo |
| `vae` | VAE | Sim | - | Modelo VAE usado para codificar a imagem de entrada no espaço latente |
| `image` | IMAGE | Sim | - | Imagem de entrada a ser convertida em quadros de vídeo |
| `width` | INT | Não | 64 a MAX_RESOLUTION | Largura do vídeo de saída em pixels (padrão: 768, passo: 32) |
| `height` | INT | Não | 64 a MAX_RESOLUTION | Altura do vídeo de saída em pixels (padrão: 512, passo: 32) |
| `length` | INT | Não | 9 a MAX_RESOLUTION | Número de quadros no vídeo gerado (padrão: 97, passo: 8) |
| `batch_size` | INT | Não | 1 a 4096 | Número de vídeos a serem gerados simultaneamente (padrão: 1) |
| `strength` | FLOAT | Não | 0.0 a 1.0 | Controle sobre quanto do conteúdo da imagem original é preservado no primeiro quadro do vídeo gerado. Um valor de 1.0 preserva a imagem original completamente, enquanto 0.0 permite a modificação máxima (padrão: 1.0) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `positive` | CONDITIONING | Condicionamento positivo processado com mascaramento de quadros de vídeo aplicado |
| `negative` | CONDITIONING | Condicionamento negativo processado com mascaramento de quadros de vídeo aplicado |
| `latent` | LATENT | Representação latente de vídeo contendo os quadros codificados e a máscara de ruído para geração de vídeo |

---
**Source fingerprint (SHA-256):** `fbd35623cd71bf917f39108d388986c9604138fbfb9380bdf936deff6d775cb9`
