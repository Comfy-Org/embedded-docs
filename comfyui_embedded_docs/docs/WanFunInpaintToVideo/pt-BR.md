# WanFunInpaintToVideo

O nó WanFunInpaintToVideo prepara dados de condicionamento e latentes para geração de vídeo no estilo de inpainting, usando uma imagem inicial e uma imagem final opcionais para guiar o resultado. Ele funciona passando o condicionamento, o VAE e os quadros de imagem fornecidos pela mesma lógica usada para geração de vídeo com primeiro e último quadro, e retorna condicionamento atualizado, além de um latente vazio para amostragem.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positivo` | Prompts de condicionamento positivo para geração de vídeo | CONDITIONING | Sim | - |
| `negativo` | Prompts de condicionamento negativo a evitar na geração de vídeo | CONDITIONING | Sim | - |
| `vae` | Modelo VAE usado para codificar e decodificar os quadros do vídeo | VAE | Sim | - |
| `largura` | Largura do vídeo de saída em pixels (padrão: 832, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `altura` | Altura do vídeo de saída em pixels (padrão: 480, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `duração` | Número de quadros na sequência de vídeo (padrão: 81, passo: 4) | INT | Sim | 1 a MAX_RESOLUTION |
| `tamanho_do_lote` | Número de vídeos a serem gerados em um lote (padrão: 1) | INT | Sim | 1 a 4096 |
| `clip_vision_output` | Saída opcional de visão CLIP usada como condicionamento para a imagem inicial | CLIP_VISION_OUTPUT | Não | - |
| `imagem_inicial` | Imagem de quadro inicial opcional para geração de vídeo | IMAGE | Não | - |
| `imagem_final` | Imagem de quadro final opcional para geração de vídeo | IMAGE | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | Saída de condicionamento positivo processado | CONDITIONING |
| `negative` | Saída de condicionamento negativo processado | CONDITIONING |
| `latent` | Representação latente do vídeo gerado | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFunInpaintToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `70b58e961c5df12f94183245ce320197439b2505b47d0bb3ff643b25c9fe6175`
