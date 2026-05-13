> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanPhantomSubjectToVideo/pt-BR.md)

O nó WanPhantomSubjectToVideo gera conteúdo de vídeo processando entradas de condicionamento e imagens de referência opcionais. Ele cria representações latentes para geração de vídeo e pode incorporar orientação visual a partir de imagens de entrada, quando fornecidas. O nó prepara dados de condicionamento com concatenação temporal para modelos de vídeo e gera condicionamento modificado junto com dados de vídeo latente gerados.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `positivo` | CONDITIONING | Sim | - | Entrada de condicionamento positivo para guiar a geração do vídeo |
| `negativo` | CONDITIONING | Sim | - | Entrada de condicionamento negativo para evitar certas características |
| `vae` | VAE | Sim | - | Modelo VAE para codificar imagens quando fornecido |
| `largura` | INT | Sim | 16 a MAX_RESOLUTION | Largura do vídeo de saída em pixels (padrão: 832, deve ser divisível por 16) |
| `altura` | INT | Sim | 16 a MAX_RESOLUTION | Altura do vídeo de saída em pixels (padrão: 480, deve ser divisível por 16) |
| `comprimento` | INT | Sim | 1 a MAX_RESOLUTION | Número de quadros no vídeo gerado (padrão: 81, deve ser divisível por 4) |
| `tamanho_do_lote` | INT | Sim | 1 a 4096 | Número de vídeos a serem gerados simultaneamente (padrão: 1) |
| `imagens` | IMAGE | Não | - | Imagens de referência opcionais para condicionamento temporal |

**Observação:** Quando `images` são fornecidas, elas são automaticamente redimensionadas para corresponder à `width` e `height` especificadas, e apenas os primeiros `length` quadros são usados para processamento.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `positivo` | CONDITIONING | Condicionamento positivo modificado com concatenação temporal quando imagens são fornecidas |
| `negative_text` | CONDITIONING | Condicionamento negativo modificado com concatenação temporal quando imagens são fornecidas |
| `negative_img_text` | CONDITIONING | Condicionamento negativo com concatenação temporal zerada quando imagens são fornecidas |
| `latent` | LATENT | Representação de vídeo latente gerada com dimensões e comprimento especificados |

---
**Source fingerprint (SHA-256):** `2e3e8277dca9e998220fc5939c2cc72fdc15e80cc4b95daa33f5b92e2270dd73`
