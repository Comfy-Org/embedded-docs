# WanVaceToVideo

O nó WanVaceToVideo prepara dados de condicionamento de vídeo para modelos de geração de vídeo. Ele recebe entradas de condicionamento positivo e negativo, além de um vídeo de controle opcional, máscaras e uma imagem de referência, e as codifica em representações latentes que orientam a geração de vídeo. O nó lida com redimensionamento (upscaling), preenchimento (padding), mascaramento e codificação VAE para construir a estrutura de condicionamento adequada para modelos de vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `positivo` | Entrada de condicionamento positivo para orientar a geração | CONDITIONING | Sim | - |
| `negativo` | Entrada de condicionamento negativo para orientar a geração | CONDITIONING | Sim | - |
| `vae` | Modelo VAE usado para codificar imagens e quadros de vídeo | VAE | Sim | - |
| `largura` | Largura do vídeo de saída em pixels (padrão: 832, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `altura` | Altura do vídeo de saída em pixels (padrão: 480, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `duração` | Número de quadros no vídeo (padrão: 81, passo: 4) | INT | Sim | 1 a MAX_RESOLUTION |
| `tamanho_do_lote` | Número de vídeos a serem gerados simultaneamente (padrão: 1) | INT | Sim | 1 a 4096 |
| `força` | Força da condição para o controle VACE (padrão: 1.0, passo: 0.01). Não é uma força de LoRA. Os pesos LoRA são aplicados por meio de nós LoRA separados. | FLOAT | Sim | 0.0 a 1000.0 |
| `control_video` | Vídeo de entrada opcional usado para condicionamento de controle. Se não for fornecido, um vídeo em cinza neutro é criado automaticamente. | IMAGE | Não | - |
| `máscaras_de_controle` | Máscaras opcionais que determinam quais partes do vídeo de controle estão ativas. Se não forem fornecidas, uma máscara totalmente branca é usada. | MASK | Não | - |
| `imagem_de_referência` | Imagem de referência opcional para condicionamento adicional. Quando fornecida, ela é codificada e adicionada no início da sequência latente. | IMAGE | Não | - |

**Observação:** Quando `control_video` é fornecido, ele é truncado para `length` quadros e redimensionado para as `width` e `height` especificadas; se tiver menos quadros que `length`, os quadros ausentes são preenchidos com cinza neutro (valor 0.5). Quando não é fornecido, um vídeo em cinza neutro com `length` quadros é criado automaticamente. As `control_masks` são redimensionadas para as `width` e `height` especificadas, truncadas para `length` quadros e preenchidas com valor 1.0 se forem mais curtas. A máscara separa o vídeo de controle em partes inativas e reativas, cada uma codificada pelo VAE e concatenada ao longo da dimensão de canais; a máscara também é reduzida para a resolução latente. Quando `reference_image` é fornecida, ela é codificada pelo VAE e adicionada no início da sequência latente. A contagem de quadros latentes é calculada como `((length - 1) // 4) + 1`, e as dimensões espaciais latentes são `height / 8` e `width / 8`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positivo` | Condicionamento positivo com dados de controle de vídeo (`vace_frames`, `vace_mask`, `vace_strength`) aplicados | CONDITIONING |
| `negativo` | Condicionamento negativo com dados de controle de vídeo (`vace_frames`, `vace_mask`, `vace_strength`) aplicados | CONDITIONING |
| `latente` | Tensor latente vazio pronto para geração de vídeo com formato `[batch_size, 16, latent_length, height/8, width/8]` | LATENT |
| `latente_recortado` | Número de quadros latentes a remover quando uma imagem de referência é usada; 0 se nenhuma imagem de referência for fornecida | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanVaceToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `2039b7509ce5b731e9e41d9cd2dad022d4c5004751f571a4cf88c1ba0cae405b`
