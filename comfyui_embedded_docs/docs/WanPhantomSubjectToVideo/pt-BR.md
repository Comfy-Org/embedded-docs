> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanPhantomSubjectToVideo/pt-BR.md)

O nó WanPhantomSubjectToVideo gera conteúdo de vídeo processando entradas de condicionamento e imagens de referência opcionais. Ele cria representações latentes para geração de vídeo e pode incorporar orientação visual de imagens de entrada quando fornecidas. O nó prepara dados de condicionamento com concatenação temporal para modelos de vídeo e retorna o condicionamento modificado junto com os dados latentes de vídeo gerados.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sim | - | Entrada de condicionamento positivo para orientar a geração do vídeo |
| `negative` | CONDITIONING | Sim | - | Entrada de condicionamento negativo para evitar certas características |
| `vae` | VAE | Sim | - | Modelo VAE para codificar imagens quando fornecidas |
| `width` | INT | Não | 16 a MAX_RESOLUTION | Largura do vídeo de saída em pixels (padrão: 832, deve ser divisível por 16) |
| `height` | INT | Não | 16 a MAX_RESOLUTION | Altura do vídeo de saída em pixels (padrão: 480, deve ser divisível por 16) |
| `length` | INT | Não | 1 a MAX_RESOLUTION | Número de quadros no vídeo gerado (padrão: 81, deve ser divisível por 4) |
| `batch_size` | INT | Não | 1 a 4096 | Número de vídeos a serem gerados simultaneamente (padrão: 1) |
| `images` | IMAGE | Não | - | Imagens de referência opcionais para condicionamento temporal |

**Observação:** Quando `images` são fornecidas, elas são automaticamente redimensionadas para cima para corresponder à `width` e `height` especificadas, e apenas os primeiros `length` quadros são usados para o processamento.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Condicionamento positivo modificado com concatenação temporal quando imagens são fornecidas |
| `negative_text` | CONDITIONING | Condicionamento negativo modificado com concatenação temporal quando imagens são fornecidas |
| `negative_img_text` | CONDITIONING | Condicionamento negativo com concatenação temporal zerada quando imagens são fornecidas |
| `latent` | LATENT | Representação latente de vídeo gerada com as dimensões e duração especificadas |
