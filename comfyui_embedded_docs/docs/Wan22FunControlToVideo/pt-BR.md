# Wan22FunControlToVideo

O nó Wan22FunControlToVideo prepara dados de condicionamento e um tensor latente vazio para geração de vídeo com o modelo de vídeo Wan. Ele codifica imagens de referência opcionais e vídeos de controle no espaço latente, anexa-os ao condicionamento positivo e negativo e cria um tensor latente preenchido com zeros com as dimensões espaciais e temporais corretas para o vídeo solicitado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `positivo` | Entrada de condicionamento positivo para orientar a geração de vídeo | CONDITIONING | Sim | - |
| `negativo` | Entrada de condicionamento negativo para orientar a geração de vídeo | CONDITIONING | Sim | - |
| `vae` | Modelo VAE usado para codificar imagens no espaço latente | VAE | Sim | - |
| `largura` | Largura do vídeo de saída em pixels (padrão: 832, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `altura` | Altura do vídeo de saída em pixels (padrão: 480, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `duração` | Número de frames na sequência de vídeo (padrão: 81, passo: 4) | INT | Sim | 1 a MAX_RESOLUTION |
| `tamanho_do_lote` | Número de sequências de vídeo a serem geradas (padrão: 1) | INT | Sim | 1 a 4096 |
| `imagem_de_referência` | Imagem de referência opcional que fornece orientação visual para a geração | IMAGE | Não | - |
| `vídeo_de_controle` | Vídeo de controle opcional que orienta o processo de geração | IMAGE | Não | - |

**Nota:** O parâmetro `length` é processado em passos de 4 frames, e o nó aplica automaticamente a escala temporal ao construir o espaço latente. Quando `ref_image` é fornecido, apenas o primeiro frame é codificado e anexado ao condicionamento como latentes de referência. Quando `control_video` é fornecido, ele é ajustado para `length` frames, codificado e colocado no latente concatenado usado pelo condicionamento. O parâmetro `start_image` é referenciado na lógica de execução, mas não está exposto no esquema de entradas do nó.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positivo` | Condicionamento positivo com dados latentes específicos de vídeo adicionados, incluindo o latente concatenado, a máscara e os latentes de referência opcionais | CONDITIONING |
| `negativo` | Condicionamento negativo com dados latentes específicos de vídeo adicionados, incluindo o latente concatenado, a máscara e os latentes de referência opcionais | CONDITIONING |
| `latente` | Tensor latente vazio preparado para geração de vídeo, dimensionado de acordo com o tamanho do lote, canais latentes, comprimento, altura e largura | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22FunControlToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `731b848f15c13ddc662f19230acb55d195f934bad7d9ae516a288e0ed8f8d899`
