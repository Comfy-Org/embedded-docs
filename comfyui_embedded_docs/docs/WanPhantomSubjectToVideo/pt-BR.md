# WanPhantomSubjectToVideo

O nó **WanPhantomSubjectToVideo** prepara dados de condicionamento e um latente para a geração de vídeos Wan. Ele cria um vídeo latente vazio a partir da largura, altura, comprimento e tamanho do lote solicitados e, quando imagens de referência são fornecidas, codifica-as com a VAE e as adiciona aos condicionamentos como orientação visual com dimensão temporal.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positivo` | Entrada de condicionamento positivo para orientar a geração de vídeo | CONDITIONING | Sim | - |
| `negativo` | Entrada de condicionamento negativo para evitar determinadas características | CONDITIONING | Sim | - |
| `vae` | Modelo VAE usado para codificar as imagens de referência quando elas são fornecidas | VAE | Sim | - |
| `largura` | Largura do vídeo de saída em pixels (padrão: 832, deve ser múltiplo de 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `altura` | Altura do vídeo de saída em pixels (padrão: 480, deve ser múltiplo de 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `comprimento` | Número de quadros no vídeo gerado (padrão: 81, deve ser múltiplo de 4) | INT | Sim | 1 a MAX_RESOLUTION |
| `tamanho_do_lote` | Número de vídeos a serem gerados simultaneamente (padrão: 1) | INT | Sim | 1 a 4096 |
| `imagens` | Imagens de referência opcionais usadas como orientação visual com dimensão temporal | IMAGE | Não | - |

**Nota:** Quando `images` são fornecidas, elas são automaticamente redimensionadas para corresponder à `width` e `height` especificadas, e apenas as primeiras `length` imagens são usadas no processamento. Cada imagem é codificada com a `vae` e concatenada ao longo da dimensão temporal, sendo utilizados apenas os canais RGB de cada imagem.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `positivo` | Condicionamento positivo com concatenação temporal das imagens de referência codificadas quando imagens são fornecidas; caso contrário, o `positive` de entrada é retornado inalterado | CONDITIONING |
| `texto_negativo` | Condicionamento negativo com concatenação temporal das imagens de referência codificadas quando imagens são fornecidas; caso contrário, o `negative` de entrada é retornado inalterado | CONDITIONING |
| `texto_img_negativo` | Condicionamento negativo com concatenação temporal zerada quando imagens são fornecidas; caso contrário, o `negative` de entrada é retornado inalterado | CONDITIONING |
| `latent` | Tensor de vídeo latente preenchido com zeros e 16 canais; sua contagem de quadros é derivada de `length` e suas dimensões espaciais de `height` e `width` | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanPhantomSubjectToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a1853382f6e564f66262b69dd7b06cc58e26b93386a460a98e6fcc2ff6acf12b`
