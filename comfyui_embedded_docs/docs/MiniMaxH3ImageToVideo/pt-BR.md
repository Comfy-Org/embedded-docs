# MiniMax H3 Imagem para Vídeo

Este nó prepara o condicionamento e o latent vazio necessários para gerar um vídeo com o modelo MiniMax H3. Ele recebe um prompt de texto e, opcionalmente, imagens para o primeiro e/ou o último quadro do vídeo, e as converte em entradas do modelo. As imagens de keyframe são redimensionadas, codificadas e anexadas ao condicionamento no início e no final do vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `clip` | Modelo CLIP usado para tokenizar o prompt e codificar as imagens de keyframe em condicionamento. | CLIP | Sim |  |
| `vae` | Modelo VAE usado para codificar as imagens de keyframe no espaço latente quando imagens de keyframe são fornecidas. | VAE | Sim |  |
| `prompt` | Prompt de texto descrevendo o vídeo a gerar. Compatível com múltiplas linhas e prompts dinâmicos. | STRING | Sim |  |
| `largura` | Largura do vídeo em pixels (padrão: 1344). | INT | Sim | 32 a MAX_RESOLUTION (passo 32) |
| `altura` | Altura do vídeo em pixels (padrão: 768). | INT | Sim | 32 a MAX_RESOLUTION (passo 32) |
| `duração` | Contagem de quadros a 24 fps, ajustada para cima para a grade 17k+5 do modelo (124 = ~5s; o intervalo treinado é ~124-362; valores maiores não foram testados) (padrão: 124). | INT | Sim | 5 a 3600 (passo 17) |
| `primeiro_quadro` | Imagem opcional usada como o primeiro quadro do vídeo. Ela é esticada para o tamanho total da tela, então sua proporção não é preservada. Apenas a primeira imagem do lote de entrada é usada. | IMAGE | Não |  |
| `último_quadro` | Imagem opcional usada como o último quadro do vídeo. Ela é cortada para cobrir a tela enquanto preserva sua proporção. Apenas a primeira imagem do lote de entrada é usada. | IMAGE | Não |  |

Quando `first_frame` e/ou `last_frame` são fornecidos, as imagens de keyframe são codificadas com o VAE e anexadas ao condicionamento no quadro 0 e no quadro final, respectivamente. Quando nenhum deles é fornecido, o nó trabalha apenas com o prompt. O `length` solicitado é ajustado para cima para a contagem de quadros válida mais próxima (17k + 5), então a contagem efetiva de quadros pode ser ligeiramente maior que a solicitada.

O latent de áudio e vídeo é criado como um par vazio correspondente aos valores solicitados de `width`, `height` e à contagem de quadros ajustada. A porção de áudio é dimensionada a partir da mesma contagem de quadros a 40 quadros de áudio por segundo.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `positive` | Condicionamento contendo o prompt codificado e, quando imagens de keyframe são fornecidas, os keyframes codificados e a contagem de quadros para o modelo MiniMax H3. | CONDITIONING |
| `latent` | Latent vazio de áudio e vídeo representando o conteúdo a ser gerado, com a largura, a altura e a contagem de quadros solicitadas. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ImageToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d1bdf3f8c66ef20ff11c35203d2c266a88dcf8cc00c65dbb0aea2b1dd16befd6`
