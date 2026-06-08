O nó WanFunInpaintToVideo cria sequências de vídeo por meio de inpaint entre imagens de início e fim. Ele recebe condicionamentos positivo e negativo, juntamente com imagens de quadro opcionais, para gerar latentes de vídeo. O nó gerencia a geração de vídeo com parâmetros configuráveis de dimensões e duração.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `positivo` | Prompts de condicionamento positivo para geração de vídeo | CONDITIONING | Sim | - |
| `negativo` | Prompts de condicionamento negativo a serem evitados na geração de vídeo | CONDITIONING | Sim | - |
| `vae` | Modelo VAE para operações de codificação/decodificação | VAE | Sim | - |
| `largura` | Largura do vídeo de saída em pixels (padrão: 832, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `altura` | Altura do vídeo de saída em pixels (padrão: 480, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `duração` | Número de quadros na sequência de vídeo (padrão: 81, passo: 4) | INT | Sim | 1 a MAX_RESOLUTION |
| `tamanho_do_lote` | Número de vídeos a serem gerados em um lote (padrão: 1) | INT | Sim | 1 a 4096 |
| `clip_vision_output` | Saída de visão CLIP opcional para condicionamento adicional | CLIP_VISION_OUTPUT | Não | - |
| `imagem_inicial` | Imagem de quadro inicial opcional para geração de vídeo | IMAGE | Não | - |
| `imagem_final` | Imagem de quadro final opcional para geração de vídeo | IMAGE | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `positivo` | Saída de condicionamento positivo processada | CONDITIONING |
| `negativo` | Saída de condicionamento negativo processada | CONDITIONING |
| `latent` | Representação latente do vídeo gerado | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFunInpaintToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `bbc5c2614f5fc21877345b3f01686ea57bee5108cdb253fb5dbf4b2cce9e59dd`
