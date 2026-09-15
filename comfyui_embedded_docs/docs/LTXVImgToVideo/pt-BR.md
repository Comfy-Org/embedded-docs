# LTXVImgToVideo

LTXVImgToVideo converte uma imagem de entrada em uma representação latente de vídeo para modelos de geração de vídeo. Ele redimensiona a imagem para a largura e a altura solicitadas, codifica-a com o VAE e posiciona os quadros codificados no início de um latente de zeros do tamanho do vídeo. O controle `strength` determina quanto do conteúdo da imagem original é preservado versus modificado durante a geração do vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positive` | Prompts de condicionamento positivo para orientar a geração do vídeo | CONDITIONING | Sim | - |
| `negative` | Prompts de condicionamento negativo para evitar certos elementos no vídeo | CONDITIONING | Sim | - |
| `vae` | Modelo VAE usado para codificar a imagem de entrada no espaço latente | VAE | Sim | - |
| `image` | Imagem de entrada a ser convertida em quadros de vídeo | IMAGE | Sim | - |
| `width` | Largura do vídeo de saída em pixels (padrão: 768, passo: 32) | INT | Sim | 64 a MAX_RESOLUTION |
| `height` | Altura do vídeo de saída em pixels (padrão: 512, passo: 32) | INT | Sim | 64 a MAX_RESOLUTION |
| `length` | Número de quadros no vídeo gerado (padrão: 97, passo: 8) | INT | Sim | 9 a MAX_RESOLUTION |
| `batch_size` | Número de vídeos a serem gerados simultaneamente (padrão: 1) | INT | Sim | 1 a 4096 |
| `strength` | Controle sobre quanto do conteúdo da imagem original é preservado nos primeiros quadros do vídeo gerado. Um valor de 1.0 preserva a imagem original completamente, enquanto 0.0 permite a modificação máxima (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |

Nota: `width` e `height` mudam em passos de 32 pixels, e `length` muda em passos de 8 quadros, correspondendo à compressão latente do vídeo (32x nas dimensões espaciais e 8x na dimensão temporal). O latente de vídeo contém ((length - 1) // 8) + 1 quadros. A imagem de entrada é redimensionada para `width` x `height` usando escala bilinear com corte centralizado, e apenas os três primeiros canais são usados para codificação.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | O condicionamento positivo repassado sem alterações para uso com o latente gerado | CONDITIONING |
| `negative` | O condicionamento negativo repassado sem alterações para uso com o latente gerado | CONDITIONING |
| `latent` | Representação latente de vídeo contendo os quadros de imagem codificados e uma máscara de ruído que controla com que intensidade o condicionamento é aplicado durante a geração do vídeo | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4ebc7f80b4d9ac3329e3349c7048885de22b827b5bdd102976687afd7e07a16b`
