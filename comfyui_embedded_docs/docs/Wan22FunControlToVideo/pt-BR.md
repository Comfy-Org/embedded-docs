# Wan22FunControlToVideo

O nó Wan22FunControlToVideo prepara dados de condicionamento e um tensor latente vazio para geração de vídeo com o modelo de vídeo Wan. Ele codifica imagens de referência opcionais e vídeos de controle no espaço latente, anexa-os ao condicionamento positivo e negativo e cria um tensor latente preenchido com zeros com as dimensões espaciais e temporais corretas para o vídeo solicitado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positive` | Entrada de condicionamento positivo para guiar a geração de vídeo | CONDITIONING | Sim | - |
| `negative` | Entrada de condicionamento negativo para guiar a geração de vídeo | CONDITIONING | Sim | - |
| `vae` | Modelo VAE usado para codificar imagens no espaço latente | VAE | Sim | - |
| `width` | Largura do vídeo de saída em pixels (padrão: 832, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `height` | Altura do vídeo de saída em pixels (padrão: 480, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `length` | Número de quadros na sequência de vídeo (padrão: 81, passo: 4) | INT | Sim | 1 a MAX_RESOLUTION |
| `batch_size` | Número de sequências de vídeo a gerar (padrão: 1) | INT | Sim | 1 a 4096 |
| `ref_image` | Imagem de referência opcional que fornece orientação visual para a geração | IMAGE | Não | - |
| `control_video` | Vídeo de controle opcional que guia o processo de geração | IMAGE | Não | - |

**Nota:** O parâmetro `length` é processado em passos de 4 quadros, e o nó aplica automaticamente escala temporal ao construir o espaço latente. Quando `ref_image` é fornecido, apenas seu primeiro quadro é codificado (redimensionado para `width` x `height`) e anexado ao condicionamento como latentes de referência. Quando `control_video` é fornecido, ele é cortado para `length` quadros, redimensionado, codificado e colocado no latente concatenado usado pelo condicionamento. O latente concatenado é duplicado ao longo da dimensão de canais e seu layout de canais depende da contagem de canais latentes do VAE (48 canais usa o formato Wan 2.2, caso contrário, o formato Wan 2.1). O parâmetro `start_image` é referenciado na lógica de execução, mas não é exposto no esquema de entrada do nó, portanto, não pode ser definido pela interface do nó.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | Condicionamento positivo com dados latentes específicos de vídeo adicionados, incluindo o latente concatenado, máscara e latentes de referência opcionais | CONDITIONING |
| `negative` | Condicionamento negativo com dados latentes específicos de vídeo adicionados, incluindo o latente concatenado, máscara e latentes de referência opcionais | CONDITIONING |
| `latent` | Tensor latente vazio preparado para geração de vídeo, dimensionado de acordo com o tamanho do lote, canais latentes, comprimento, altura e largura | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22FunControlToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `731b848f15c13ddc662f19230acb55d195f934bad7d9ae516a288e0ed8f8d899`
