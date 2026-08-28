# LTXVImgToVideo

O LTXVImgToVideo converte uma imagem de entrada em uma representação latente de vídeo para modelos de geração de vídeo. Ele redimensiona a imagem para a largura e altura solicitadas, codifica-a com o VAE e coloca os quadros codificados no início de um latente de vídeo preenchido com zeros. O controle de intensidade determina quanto do conteúdo da imagem original é preservado em vez de modificado durante a geração do vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positive` | Condicionamento positivo (prompts) para orientar a geração de vídeo | CONDITIONING | Sim | - |
| `negative` | Condicionamento negativo (prompts) para evitar certos elementos no vídeo | CONDITIONING | Sim | - |
| `vae` | Modelo VAE usado para codificar a imagem de entrada no espaço latente | VAE | Sim | - |
| `image` | Imagem de entrada a ser convertida em quadros de vídeo | IMAGE | Sim | - |
| `width` | Largura do vídeo de saída em pixels (padrão: 768, passo: 32) | INT | Não | 64 a MAX_RESOLUTION |
| `height` | Altura do vídeo de saída em pixels (padrão: 512, passo: 32) | INT | Não | 64 a MAX_RESOLUTION |
| `length` | Número de quadros no vídeo gerado (padrão: 97, passo: 8) | INT | Não | 9 a MAX_RESOLUTION |
| `batch_size` | Número de vídeos a serem gerados simultaneamente (padrão: 1) | INT | Não | 1 a 4096 |
| `strength` | Controle sobre o quanto do conteúdo da imagem original é preservado nos primeiros quadros do vídeo gerado. Um valor de 1.0 preserva a imagem original completamente, enquanto 0.0 permite modificação máxima (padrão: 1.0) | FLOAT | Não | 0.0 a 1.0 |

Nota: `width` e `height` mudam em passos de 32 pixels, e `length` muda em passos de 8 quadros, correspondendo à compressão latente do vídeo (32x nas dimensões espaciais e 8x na dimensão temporal). O latente de vídeo contém ((length - 1) // 8) + 1 quadros.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | O condicionamento positivo transmitido inalterado para uso com o latente gerado | CONDITIONING |
| `negative` | O condicionamento negativo transmitido inalterado para uso com o latente gerado | CONDITIONING |
| `latent` | Representação latente de vídeo contendo os quadros de imagem codificados e uma máscara de ruído que controla a intensidade com que o condicionamento é aplicado durante a geração de vídeo | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4ebc7f80b4d9ac3329e3349c7048885de22b827b5bdd102976687afd7e07a16b`
