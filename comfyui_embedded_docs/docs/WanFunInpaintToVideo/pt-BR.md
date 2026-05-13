> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFunInpaintToVideo/pt-BR.md)

O nó WanFunInpaintToVideo cria sequências de vídeo por meio de inpaint entre imagens de início e fim. Ele recebe condicionamentos positivo e negativo, juntamente com imagens de quadro opcionais, para gerar latentes de vídeo. O nó gerencia a geração de vídeo com parâmetros configuráveis de dimensões e duração.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sim | - | Prompts de condicionamento positivo para geração de vídeo |
| `negative` | CONDITIONING | Sim | - | Prompts de condicionamento negativo a serem evitados na geração de vídeo |
| `vae` | VAE | Sim | - | Modelo VAE para operações de codificação/decodificação |
| `width` | INT | Sim | 16 a MAX_RESOLUTION | Largura do vídeo de saída em pixels (padrão: 832, passo: 16) |
| `height` | INT | Sim | 16 a MAX_RESOLUTION | Altura do vídeo de saída em pixels (padrão: 480, passo: 16) |
| `length` | INT | Sim | 1 a MAX_RESOLUTION | Número de quadros na sequência de vídeo (padrão: 81, passo: 4) |
| `batch_size` | INT | Sim | 1 a 4096 | Número de vídeos a serem gerados em um lote (padrão: 1) |
| `clip_vision_output` | CLIP_VISION_OUTPUT | Não | - | Saída de visão CLIP opcional para condicionamento adicional |
| `start_image` | IMAGE | Não | - | Imagem de quadro inicial opcional para geração de vídeo |
| `end_image` | IMAGE | Não | - | Imagem de quadro final opcional para geração de vídeo |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Saída de condicionamento positivo processada |
| `negative` | CONDITIONING | Saída de condicionamento negativo processada |
| `latent` | LATENT | Representação latente do vídeo gerado |

---
**Source fingerprint (SHA-256):** `bbc5c2614f5fc21877345b3f01686ea57bee5108cdb253fb5dbf4b2cce9e59dd`
