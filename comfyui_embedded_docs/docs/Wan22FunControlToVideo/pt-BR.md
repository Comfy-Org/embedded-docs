> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22FunControlToVideo/pt-BR.md)

O nó Wan22FunControlToVideo prepara representações de condicionamento e latentes para geração de vídeo usando a arquitetura do modelo de vídeo Wan. Ele processa entradas de condicionamento positivo e negativo, juntamente com imagens de referência opcionais e vídeos de controle, para criar as representações de espaço latente necessárias para a síntese de vídeo. O nó lida com o escalonamento espacial e as dimensões temporais para gerar dados de condicionamento apropriados para modelos de vídeo.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `positive` | CONDITIONING | Sim | - | Entrada de condicionamento positivo para guiar a geração do vídeo |
| `negative` | CONDITIONING | Sim | - | Entrada de condicionamento negativo para guiar a geração do vídeo |
| `vae` | VAE | Sim | - | Modelo VAE usado para codificar imagens para o espaço latente |
| `width` | INT | Sim | 16 a MAX_RESOLUTION | Largura do vídeo de saída em pixels (padrão: 832, passo: 16) |
| `height` | INT | Sim | 16 a MAX_RESOLUTION | Altura do vídeo de saída em pixels (padrão: 480, passo: 16) |
| `length` | INT | Sim | 1 a MAX_RESOLUTION | Número de quadros na sequência de vídeo (padrão: 81, passo: 4) |
| `batch_size` | INT | Sim | 1 a 4096 | Número de sequências de vídeo a serem geradas (padrão: 1) |
| `ref_image` | IMAGE | Não | - | Imagem de referência opcional para fornecer orientação visual |
| `control_video` | IMAGE | Não | - | Vídeo de controle opcional para guiar o processo de geração |

**Nota:** O parâmetro `length` é processado em blocos de 4 quadros, e o nó lida automaticamente com o escalonamento temporal para o espaço latente. Quando `ref_image` é fornecido, ele influencia o condicionamento por meio de latentes de referência. Quando `control_video` é fornecido, ele afeta diretamente a representação latente de concatenação usada no condicionamento. O parâmetro `start_image` não é exposto como uma entrada neste esquema de nó, mas é referenciado na lógica de execução.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `positive` | CONDITIONING | Condicionamento positivo modificado com dados latentes específicos de vídeo, incluindo latente de concatenação, máscara e latentes de referência opcionais |
| `negative` | CONDITIONING | Condicionamento negativo modificado com dados latentes específicos de vídeo, incluindo latente de concatenação, máscara e latentes de referência opcionais |
| `latent` | LATENT | Tensor latente vazio com dimensões apropriadas para geração de vídeo com base no tamanho do lote, canais latentes e escalonamento espacial/temporal |

---
**Source fingerprint (SHA-256):** `8b24058f06aa9f779371a402c41cffc95d13ad0131d23d1438067d77755c73e2`
