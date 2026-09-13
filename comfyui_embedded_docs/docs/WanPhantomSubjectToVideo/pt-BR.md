# WanPhantomSubjectToVideo

O nó WanPhantomSubjectToVideo prepara dados de condicionamento e um latent para a geração de vídeo do Wan. Ele cria um vídeo latente vazio a partir da largura, altura, comprimento e tamanho do lote solicitados e, quando imagens de referência são fornecidas, codifica-as com o VAE e as adiciona aos condicionamentos como orientação visual na dimensão temporal.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positive` | Entrada de condicionamento positiva para orientar a geração de vídeo | CONDITIONING | Sim | - |
| `negative` | Entrada de condicionamento negativa para evitar determinadas características | CONDITIONING | Sim | - |
| `vae` | Modelo VAE usado para codificar as imagens de referência quando fornecidas | VAE | Sim | - |
| `width` | Largura do vídeo de saída em pixels (padrão: 832) | INT | Sim | 16 to MAX_RESOLUTION (passo: 16) |
| `height` | Altura do vídeo de saída em pixels (padrão: 480) | INT | Sim | 16 to MAX_RESOLUTION (passo: 16) |
| `length` | Número de quadros no vídeo gerado (padrão: 81) | INT | Sim | 1 to MAX_RESOLUTION (passo: 4) |
| `batch_size` | Número de vídeos a serem gerados simultaneamente (padrão: 1) | INT | Sim | 1 a 4096 |
| `images` | Imagens de referência opcionais usadas como orientação visual na dimensão temporal | IMAGE | Não | - |

**Nota:** Quando `images` são fornecidas, elas são automaticamente redimensionadas para corresponder à `width` e `height` especificadas, e apenas as primeiras `length` imagens são usadas para processamento. Cada imagem é codificada com o `vae` e concatenada ao longo da dimensão temporal, e apenas os canais RGB de cada imagem são usados. Quando `images` não são fornecidas, todas as três saídas de condicionamento são retornadas inalteradas a partir dos condicionamentos de entrada.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `positive` | Condicionamento positivo com concatenação na dimensão temporal das imagens de referência codificadas quando imagens são fornecidas; caso contrário, a entrada `positive` é retornada inalterada | CONDITIONING |
| `negative_text` | Condicionamento negativo com concatenação na dimensão temporal das imagens de referência codificadas quando imagens são fornecidas; caso contrário, a entrada `negative` é retornada inalterada | CONDITIONING |
| `negative_img_text` | Condicionamento negativo com uma concatenação na dimensão temporal zerada quando imagens são fornecidas; caso contrário, a entrada `negative` é retornada inalterada | CONDITIONING |
| `latent` | Tensor de vídeo latente preenchido com zeros com 16 canais; sua contagem de quadros é derivada de `length` e suas dimensões espaciais de `height` e `width` | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanPhantomSubjectToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a1853382f6e564f66262b69dd7b06cc58e26b93386a460a98e6fcc2ff6acf12b`
