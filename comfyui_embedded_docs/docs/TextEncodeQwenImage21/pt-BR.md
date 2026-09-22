# TextEncodeQwenImage21

O nó TextEncodeQwenImage21 codifica um prompt e um prompt negativo para o modelo Qwen-Image 2.1, opcionalmente anexando imagens de referência. As imagens de referência são vistas pelo codificador de texto e, quando um VAE está conectado, também são codificadas como latents que são inseridos na sequência, de modo que o condicionamento carrega tanto a instrução de texto quanto a referência visual. O nó retorna condicionamento positivo e negativo junto com um latent vazio dimensionado para a primeira imagem de referência, pronto para ser amostrado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `clip` | O codificador de texto do Qwen-Image 2.1 usado para tokenizar e codificar os prompts. | CLIP | Sim | - |
| `prompt` | Prompt de texto descrevendo a imagem a ser gerada ou a edição a ser aplicada. Suporta entrada multilinha e prompts dinâmicos. | STRING | Sim | Qualquer texto |
| `negative_prompt` | Prompt de texto descrevendo o que o resultado deve evitar. Suporta entrada multilinha e prompts dinâmicos. | STRING | Sim | Qualquer texto |
| `vae` | VAE usado para codificar as imagens de referência em latents de referência. Quando omitido, as imagens de referência condicionam o resultado apenas por meio do codificador de texto. | VAE | Não | - |
| `resolution` | As imagens de referência são redimensionadas para aproximadamente `resolution` x `resolution` pixels, em múltiplos de 32, preservando a proporção. 0 mantém cada referência em seu próprio tamanho, arredondado para um múltiplo de 32 (padrão: 1024). | INT | Sim | 0 a 4096 (passo 32) |
| `images` | Imagens de referência, vistas pelo codificador de texto e inseridas na sequência como latents de VAE. Slot expansível: conecte até 16 imagens (`image_1` ... `image_16`). | IMAGE | Não | 0 a 16 imagens |

A saída de latent vazio é dimensionada para a primeira imagem de referência conectada, ou para `resolution` quando nenhuma imagem de referência está conectada. Faça a amostragem no latent que este nó retorna: qualquer outro tamanho altera a edição. Quando um VAE está conectado, os mesmos latents de referência são anexados tanto ao condicionamento positivo quanto ao negativo, então uma única etapa do amostrador pode remover o ruído de ambos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | Condicionamento codificado para o prompt, carregando os latents de referência quando um VAE está conectado. | CONDITIONING |
| `negative` | Condicionamento codificado para o prompt negativo, com os mesmos latents de referência. | CONDITIONING |
| `latent` | Latent vazio no tamanho da primeira imagem de referência, ou 1024 x 1024 quando nenhuma imagem de referência está conectada. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImage21/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3870f04597d12b593498c12ca139428af2d717b65aa40c889de9373ae9eb475e`
