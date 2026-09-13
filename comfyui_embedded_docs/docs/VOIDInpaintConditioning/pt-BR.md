# VOIDInpaintConditioning

O nó VOIDInpaintConditioning prepara os dados de condicionamento necessários para inpainting com modelos CogVideoX. Ele recebe um vídeo de origem e uma quadmask pré-processada, codifica-os pelo VAE e os combina em um sinal de condicionamento de 32 canais (16 canais da máscara + 16 canais do vídeo mascarado) que o modelo usa para preencher as áreas mascaradas.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positive` | O condicionamento positivo a ser aumentado com a informação latente de inpainting | CONDITIONING | Sim | - |
| `negative` | O condicionamento negativo a ser aumentado com a informação latente de inpainting | CONDITIONING | Sim | - |
| `vae` | O modelo VAE usado para codificar a máscara e o vídeo mascarado no espaço latente | VAE | Sim | - |
| `video` | Quadros do vídeo de origem [T, H, W, 3] | IMAGE | Sim | - |
| `quadmask` | Quadmask pré-processada de VOIDQuadmaskPreprocess [T, H, W] | MASK | Sim | - |
| `width` | A largura para redimensionar o vídeo e a máscara (padrão: 672) | INT | Sim | 16 a MAX_RESOLUTION (passo: 8) |
| `height` | A altura para redimensionar o vídeo e a máscara (padrão: 384) | INT | Sim | 16 a MAX_RESOLUTION (passo: 8) |
| `length` | Número de quadros de pixel a processar. Para CogVideoX-Fun-V1.5 (patch_size_t=2), latent_t deve ser par — comprimentos que produzem latent_t ímpar são arredondados para baixo (ex.: 49 → 45) (padrão: 45) | INT | Sim | 1 a MAX_RESOLUTION (passo: 1) |
| `batch_size` | O tamanho do lote para o latente de ruído de saída (padrão: 1) | INT | Sim | 1 a 64 |

**Nota:** Como o CogVideoX-Fun-V1.5 usa `patch_size_t=2`, o latente codificado deve ter uma dimensão temporal par. Se `length` produzir um `latent_t` ímpar, o nó o arredonda automaticamente para baixo até o valor válido mais próximo e registra um aviso. Usar um `latent_t` ímpar corrompe o último quadro por meio de preenchimento circular, o que pode causar tremulação visível ou sujeitos que desaparecem perto do final do vídeo decodificado.

## Saídas

| Nome da Saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `positive` | O condicionamento positivo com a informação latente de inpainting adicionada | CONDITIONING |
| `negative` | O condicionamento negativo com a informação latente de inpainting adicionada | CONDITIONING |
| `latent` | Um tensor latente de ruído preenchido com zeros com formato [batch_size, 16, latent_t, latent_h, latent_w] | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDInpaintConditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `885e462c0f17a3e9610146a05ba3b9c879db0112d3961c95a83f63ba2cd511f1`
