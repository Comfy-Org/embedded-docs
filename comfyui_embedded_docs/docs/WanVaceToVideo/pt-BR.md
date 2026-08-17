# WanVaceToVideo

O nó WanVaceToVideo processa dados de condicionamento de vídeo para modelos de geração de vídeo. Ele recebe entradas de condicionamento positivo e negativo, juntamente com dados de controle de vídeo, e prepara representações latentes para a geração de vídeo. O nó lida com redimensionamento de vídeo, mascaramento e codificação VAE para criar a estrutura de condicionamento apropriada para modelos de vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positive` | Entrada de condicionamento positivo para orientar a geração | CONDITIONING | Sim | - |
| `negative` | Entrada de condicionamento negativo para orientar a geração | CONDITIONING | Sim | - |
| `vae` | Modelo VAE usado para codificar imagens e quadros de vídeo | VAE | Sim | - |
| `width` | Largura do vídeo de saída em pixels (padrão: 832, passo: 16) | INT | Sim | 16 to MAX_RESOLUTION |
| `height` | Altura do vídeo de saída em pixels (padrão: 480, passo: 16) | INT | Sim | 16 to MAX_RESOLUTION |
| `length` | Número de quadros no vídeo (padrão: 81, passo: 4) | INT | Sim | 1 to MAX_RESOLUTION |
| `batch_size` | Número de vídeos a serem gerados simultaneamente (padrão: 1) | INT | Sim | 1 to 4096 |
| `strength` | Força do condicionamento para controle VACE (padrão: 1.0, passo: 0.01). Este valor não é uma força LoRA. Os pesos LoRA são aplicados por meio de nós LoRA separados. | FLOAT | Sim | 0.0 to 1000.0 |
| `control_video` | Vídeo de entrada opcional para condicionamento de controle. Se não for fornecido, um vídeo cinza neutro é criado automaticamente. Quando fornecido, ele é redimensionado para `width` × `height` e limitado aos primeiros `length` quadros; se tiver menos quadros, os quadros ausentes são preenchidos com cinza neutro. | IMAGE | Não | - |
| `control_masks` | Máscaras opcionais para controlar quais partes do vídeo serão modificadas. Se não forem fornecidas, uma máscara totalmente branca é usada. Quando fornecidas, as máscaras são redimensionadas para `width` × `height`, limitadas a `length` quadros e preenchidas com branco se tiverem menos quadros. | MASK | Não | - |
| `reference_image` | Imagem de referência opcional para condicionamento adicional. Quando fornecida, ela é redimensionada para `width` × `height`, codificada pelo VAE e anexada ao início da sequência latente. | IMAGE | Não | - |

**Nota:** Quando `control_video` é fornecido, ele é redimensionado para os valores de `width` e `height` especificados. Se `control_masks` forem fornecidas, elas são redimensionadas para corresponder às mesmas dimensões. A `reference_image` é codificada pelo VAE e anexada ao início da sequência latente quando fornecida. O parâmetro `length` determina o número de quadros, e o comprimento latente é calculado como `((length - 1) // 4) + 1`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | Condicionamento positivo com dados de controle de vídeo (vace_frames, vace_mask, vace_strength) aplicados | CONDITIONING |
| `negative` | Condicionamento negativo com dados de controle de vídeo (vace_frames, vace_mask, vace_strength) aplicados | CONDITIONING |
| `latent` | Tensor latente vazio pronto para geração de vídeo com formato [batch_size, 16, latent_length, height/8, width/8] | LATENT |
| `trim_latent` | Número de quadros latentes a descartar quando a imagem de referência é usada (0 se nenhuma imagem de referência for fornecida) | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanVaceToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `2039b7509ce5b731e9e41d9cd2dad022d4c5004751f571a4cf88c1ba0cae405b`
