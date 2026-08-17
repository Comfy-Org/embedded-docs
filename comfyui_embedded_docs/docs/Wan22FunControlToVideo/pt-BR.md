# Wan22FunControlToVideo

O nó Wan22FunControlToVideo prepara representações de condicionamento e latentes para geração de vídeo usando a arquitetura do modelo de vídeo Wan. Ele processa entradas de condicionamento positivas e negativas juntamente com imagens de referência opcionais e vídeos de controle para criar as representações de espaço latente necessárias para a síntese de vídeo. O nó lida com escalonamento espacial e dimensões temporais para gerar dados de condicionamento apropriados para modelos de vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positive` | Entrada de condicionamento positivo para orientar a geração de vídeo | CONDITIONING | Sim | - |
| `negative` | Entrada de condicionamento negativo para orientar a geração de vídeo | CONDITIONING | Sim | - |
| `vae` | Modelo VAE usado para codificar imagens no espaço latente | VAE | Sim | - |
| `width` | Largura do vídeo de saída em pixels (padrão: 832, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `height` | Altura do vídeo de saída em pixels (padrão: 480, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `length` | Número de quadros na sequência de vídeo (padrão: 81, passo: 4) | INT | Sim | 1 a MAX_RESOLUTION |
| `batch_size` | Número de sequências de vídeo a gerar (padrão: 1) | INT | Sim | 1 a 4096 |
| `ref_image` | Imagem de referência opcional para fornecer orientação visual | IMAGE | Não | - |
| `control_video` | Vídeo de controle opcional para orientar o processo de geração | IMAGE | Não | - |

**Nota:** O parâmetro `length` é processado em blocos de 4 quadros, e o nó lida automaticamente com o escalonamento temporal do espaço latente. Quando `ref_image` é fornecido, ele influencia o condicionamento por meio de latentes de referência. Quando `control_video` é fornecido, ele afeta diretamente a representação latente concatenada usada no condicionamento. O parâmetro `start_image` não é exposto como entrada no esquema deste nó, mas é referenciado na lógica de execução.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | Condicionamento positivo modificado com dados latentes específicos de vídeo, incluindo latente concatenado, máscara e latentes de referência opcionais | CONDITIONING |
| `negative` | Condicionamento negativo modificado com dados latentes específicos de vídeo, incluindo latente concatenado, máscara e latentes de referência opcionais | CONDITIONING |
| `latent` | Tensor latente vazio com dimensões apropriadas para geração de vídeo, com base no tamanho do lote, canais latentes e escalonamento espacial/temporal | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22FunControlToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `731b848f15c13ddc662f19230acb55d195f934bad7d9ae516a288e0ed8f8d899`
