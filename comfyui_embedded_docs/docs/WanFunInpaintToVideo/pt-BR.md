# WanFunInpaintToVideo

O nó WanFunInpaintToVideo cria sequências de vídeo por meio de inpaint entre as imagens inicial e final. Ele recebe condicionamentos positivo e negativo, juntamente com imagens de quadro opcionais, para gerar latentes de vídeo. O nó lida com a geração de vídeos com parâmetros configuráveis de dimensões e comprimento.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positive` | Condicionamento positivo para prompts de geração de vídeo | CONDITIONING | Sim | - |
| `negative` | Condicionamento negativo para prompts a serem evitados na geração de vídeo | CONDITIONING | Sim | - |
| `vae` | Modelo VAE para operações de codificação/decodificação | VAE | Sim | - |
| `width` | Largura do vídeo de saída em pixels (padrão: 832, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `height` | Altura do vídeo de saída em pixels (padrão: 480, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `length` | Número de quadros na sequência de vídeo (padrão: 81, passo: 4) | INT | Sim | 1 a MAX_RESOLUTION |
| `batch_size` | Número de vídeos a serem gerados em um lote (padrão: 1) | INT | Sim | 1 a 4096 |
| `clip_vision_output` | Saída opcional do CLIP vision para condicionamento adicional | CLIP_VISION_OUTPUT | Não | - |
| `start_image` | Imagem opcional do quadro inicial para geração de vídeo | IMAGE | Não | - |
| `end_image` | Imagem opcional do quadro final para geração de vídeo | IMAGE | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `positive` | Saída de condicionamento positivo processado | CONDITIONING |
| `negative` | Saída de condicionamento negativo processado | CONDITIONING |
| `latent` | Representação latente do vídeo gerado | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFunInpaintToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `70b58e961c5df12f94183245ce320197439b2505b47d0bb3ff643b25c9fe6175`
