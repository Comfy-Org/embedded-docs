# LTXVAddGuide

O nó LTXVAddGuide codifica imagens ou vídeos de entrada através de um codificador VAE e os adiciona como keyframes de guia a uma sequência de vídeo latente. Ele atualiza tanto o condicionamento positivo quanto o negativo e retorna o latente modificado, com opções para definir o quadro inicial, a força de condicionamento, uma máscara de atenção opcional e parâmetros IC-LoRA opcionais.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `positive` | Entrada de condicionamento positivo a ser modificada com orientação de keyframe. | CONDITIONING | Sim | - |
| `negative` | Entrada de condicionamento negativo a ser modificada com orientação de keyframe. | CONDITIONING | Sim | - |
| `vae` | Modelo VAE usado para codificar os quadros da imagem/vídeo de entrada. | VAE | Sim | - |
| `latent` | Sequência latente de entrada que receberá os quadros de condicionamento. | LATENT | Sim | - |
| `image` | Imagem ou vídeo para condicionar o vídeo latente. Deve ter 8*n + 1 quadros. Se o vídeo não tiver 8*n + 1 quadros, ele será cortado para os 8*n + 1 quadros mais próximos. | IMAGE | Sim | - |
| `frame_idx` | Índice do quadro para iniciar o condicionamento. Para imagens de quadro único ou vídeos com 1-8 quadros, qualquer valor de frame_idx é aceitável. Para vídeos com 9+ quadros, frame_idx deve ser divisível por 8, caso contrário, será arredondado para baixo para o múltiplo de 8 mais próximo. Valores negativos são contados a partir do final do vídeo. Padrão: 0. | INT | Sim | -9999 a 9999 |
| `strength` | Força da influência do condicionamento, onde 1.0 aplica condicionamento total e 0.0 não aplica condicionamento. Padrão: 1.0. | FLOAT | Sim | 0.0 a 10.0 |
| `attention_mask` | Máscara espacial opcional no espaço de pixels. Controla a influência do condicionamento por região via autoatenção, multiplicada pela força. | MASK | Não | - |
| `iclora_parameters` | Parâmetros IC-LoRA opcionais de um nó Get IC-LoRA Parameters. Usados para ajustar o processamento de guia conforme exigido por certos IC-LoRAs (por exemplo, aqueles com um reference_downscale_factor > 1). Quando encadeados, cada LTXVAddGuide usa apenas os parâmetros conectados a ele. | IC_LORA_PARAMETERS | Não | - |

**Nota:** A imagem/vídeo de entrada deve ter uma contagem de quadros seguindo o padrão 8*n + 1 (por exemplo, 1, 9, 17, 25 quadros). Se a entrada exceder esse padrão, ela será automaticamente cortada para a contagem de quadros válida mais próxima.

**Nota sobre `iclora_parameters`:** Ao usar parâmetros IC-LoRA com um `reference_downscale_factor` maior que 1, as dimensões espaciais latentes (largura e altura) devem ser divisíveis por esse fator. O nó gerará um erro se esta condição não for atendida.

**Nota:** Os quadros de guia codificados devem caber dentro da sequência latente na posição de quadro selecionada. Se os quadros condicionados excederem o comprimento da sequência latente, o nó gerará um erro.

**Nota:** Adicionar um guia a um latente que combina canais de áudio e vídeo não é suportado e gerará um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `positive` | Condicionamento positivo atualizado com informações de orientação de keyframe. | CONDITIONING |
| `negative` | Condicionamento negativo atualizado com informações de orientação de keyframe. | CONDITIONING |
| `latent` | Sequência latente com quadros de condicionamento incorporados e máscara de ruído atualizada. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddGuide/pt-BR.md)

---
**Source fingerprint (SHA-256):** `031bc9030dafed85b5ff1cbceae36234e9d5f77f7f4b040267067ecd16a27929`
