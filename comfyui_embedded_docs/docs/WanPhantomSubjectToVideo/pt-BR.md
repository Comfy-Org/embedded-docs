# WanPhantomSubjectToVideo

O nó WanPhantomSubjectToVideo gera conteúdo de vídeo processando entradas de condicionamento e imagens de referência opcionais. Ele cria representações latentes para a geração de vídeo e pode incorporar orientação visual das imagens de entrada quando fornecidas. O nó prepara dados de condicionamento com concatenação de dimensão temporal para os modelos de vídeo Wan e gera condicionamento modificado juntamente com os dados latentes de vídeo gerados.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positive` | Entrada de condicionamento positivo para orientar a geração de vídeo | CONDITIONING | Sim | - |
| `negative` | Entrada de condicionamento negativo para evitar determinadas características | CONDITIONING | Sim | - |
| `vae` | Modelo VAE para codificar imagens quando fornecido | VAE | Sim | - |
| `width` | Largura do vídeo de saída em pixels (padrão: 832, deve ser divisível por 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `height` | Altura do vídeo de saída em pixels (padrão: 480, deve ser divisível por 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `length` | Número de quadros no vídeo gerado (padrão: 81, deve ser divisível por 4) | INT | Sim | 1 a MAX_RESOLUTION |
| `batch_size` | Número de vídeos a serem gerados simultaneamente (padrão: 1) | INT | Sim | 1 a 4096 |
| `images` | Imagens de referência opcionais para condicionamento com dimensão temporal | IMAGE | Não | - |

**Nota:** Quando `images` são fornecidas, elas são automaticamente redimensionadas para corresponder aos valores de `width` e `height` especificados, e apenas os primeiros `length` quadros são usados no processamento. Cada imagem é reduzida aos seus 3 primeiros canais de cor antes de ser codificada pelo VAE. Quando `images` não são fornecidas, as entradas de condicionamento passam inalteradas.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | Condicionamento positivo modificado com concatenação de dimensão temporal quando `images` são fornecidas | CONDITIONING |
| `negative_text` | Condicionamento negativo modificado com concatenação de dimensão temporal quando `images` são fornecidas | CONDITIONING |
| `negative_img_text` | Condicionamento negativo com concatenação de dimensão temporal zerada quando `images` são fornecidas | CONDITIONING |
| `latent` | Representação latente de vídeo preenchida com zeros, com 16 canais, dimensão temporal de ((length - 1) // 4) + 1 e dimensões espaciais height // 8 e width // 8 | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanPhantomSubjectToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a1853382f6e564f66262b69dd7b06cc58e26b93386a460a98e6fcc2ff6acf12b`
