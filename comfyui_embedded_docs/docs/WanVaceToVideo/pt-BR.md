# WanVaceToVideo

O nó WanVaceToVideo prepara dados de condicionamento de vídeo para modelos de geração de vídeo controlados por VACE. Ele combina condicionamento positivo e negativo com um vídeo de controle opcional, máscaras de controle e uma imagem de referência, codifica-os por meio de um VAE e produz como saída condicionamento atualizado, um tensor latente vazio e um valor de corte.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positivo` | Entrada de condicionamento positivo para guiar a geração | CONDITIONING | Sim | - |
| `negativo` | Entrada de condicionamento negativo para guiar a geração | CONDITIONING | Sim | - |
| `vae` | Modelo VAE usado para codificar imagens e frames de vídeo | VAE | Sim | - |
| `largura` | Largura do vídeo de saída em pixels (padrão: 832, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `altura` | Altura do vídeo de saída em pixels (padrão: 480, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `duração` | Número de frames no vídeo (padrão: 81, passo: 4) | INT | Sim | 1 a MAX_RESOLUTION |
| `tamanho_do_lote` | Número de vídeos a serem gerados simultaneamente (padrão: 1) | INT | Sim | 1 a 4096 |
| `força` | Força do condicionamento para controle VACE (padrão: 1.0, passo: 0.01). Esta não é uma força de LoRA. Os pesos de LoRA são aplicados por meio de nós LoRA separados. | FLOAT | Sim | 0.0 a 1000.0 |
| `control_video` | Vídeo de entrada opcional usado para condicionamento de controle. Se não for fornecido, um vídeo cinza neutro é criado automaticamente. | IMAGE | Não | - |
| `máscaras_de_controle` | Máscaras opcionais que determinam quais partes do vídeo de controle estão ativas. Se não forem fornecidas, uma máscara totalmente branca é usada. | MASK | Não | - |
| `imagem_de_referência` | Imagem de referência opcional para condicionamento adicional. Quando fornecida, ela é codificada e adicionada no início da sequência latente. Apenas a primeira imagem é usada. | IMAGE | Não | - |

**Nota:** Quando `control_video` é fornecido, ele é truncado para `length` frames e ampliado para a `width` e a `height` especificadas; se ele tiver menos frames que `length`, os frames ausentes são preenchidos com cinza neutro (valor 0.5). Quando ele não é fornecido, um vídeo cinza neutro de `length` frames é criado automaticamente. `control_masks` são ampliadas para a `width` e a `height` especificadas, truncadas para `length` frames e preenchidas com valor 1.0 se forem mais curtas. A máscara separa o vídeo de controle em partes inativa e reativa, cada uma codificada por VAE e concatenada ao longo da dimensão de canal; a máscara também é reduzida para a resolução latente. Quando `reference_image` é fornecida, sua primeira imagem é codificada por VAE e adicionada no início da sequência latente, e `trim_latent` reporta o número de frames latentes adicionados. A contagem de frames latentes é calculada como `((length - 1) // 4) + 1`, e as dimensões espaciais latentes são `height / 8` e `width / 8`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | Condicionamento positivo com dados de controle de vídeo (vace_frames, vace_mask, vace_strength) aplicados | CONDITIONING |
| `negative` | Condicionamento negativo com dados de controle de vídeo (vace_frames, vace_mask, vace_strength) aplicados | CONDITIONING |
| `latent` | Tensor latente vazio pronto para geração de vídeo com formato [batch_size, 16, latent_length, height/8, width/8] | LATENT |
| `trim_latent` | Número de frames latentes a serem cortados quando uma imagem de referência é usada; 0 se nenhuma imagem de referência for fornecida | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanVaceToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `2039b7509ce5b731e9e41d9cd2dad022d4c5004751f571a4cf88c1ba0cae405b`
