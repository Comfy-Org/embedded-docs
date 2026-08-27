# WanFunInpaintToVideo

O nó WanFunInpaintToVideo cria sequências de vídeo por meio de inpainting entre imagens inicial e final. Ele utiliza condicionamentos positivo e negativo, juntamente com imagens de quadro opcionais, para gerar latentes de vídeo. O nó gerencia a geração de vídeo com parâmetros configuráveis de dimensões e comprimento.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positivo` | Prompts de condicionamento positivo para geração de vídeo | CONDITIONING | Sim | - |
| `negativo` | Prompts de condicionamento negativo para evitar na geração de vídeo | CONDITIONING | Sim | - |
| `vae` | Modelo VAE para operações de codificação/decodificação | VAE | Sim | - |
| `largura` | Largura do vídeo de saída em pixels (padrão: 832, passo: 16) | INT | Sim | 16 to MAX_RESOLUTION |
| `altura` | Altura do vídeo de saída em pixels (padrão: 480, passo: 16) | INT | Sim | 16 to MAX_RESOLUTION |
| `duração` | Número de quadros na sequência de vídeo (padrão: 81, passo: 4) | INT | Sim | 1 to MAX_RESOLUTION |
| `tamanho_do_lote` | Número de vídeos a serem gerados em um lote (padrão: 1) | INT | Sim | 1 a 4096 |
| `clip_vision_output` | Saída de visão CLIP opcional usada como condicionamento para a imagem inicial | CLIP_VISION_OUTPUT | Não | - |
| `imagem_inicial` | Imagem inicial opcional para geração de vídeo | IMAGE | Não | - |
| `imagem_final` | Imagem final opcional para geração de vídeo | IMAGE | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positivo` | Saída de condicionamento positivo processado | CONDITIONING |
| `negativo` | Saída de condicionamento negativo processado | CONDITIONING |
| `latente` | Representação latente do vídeo gerado | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFunInpaintToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `70b58e961c5df12f94183245ce320197439b2505b47d0bb3ff643b25c9fe6175`
