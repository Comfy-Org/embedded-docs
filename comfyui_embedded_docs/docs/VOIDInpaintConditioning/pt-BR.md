# VOIDInpaintConditioning

O nó VOIDInpaintConditioning prepara os dados de condicionamento necessários para inpaint com modelos CogVideoX. Ele recebe um vídeo fonte e uma quadmask pré-processada, codifica-os através do VAE e os combina em um sinal de condicionamento de 32 canais que o modelo utiliza para preencher as áreas mascaradas.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `positive` | O condicionamento positivo a ser aumentado com as informações latentes de inpaint | CONDITIONING | Sim | - |
| `negative` | O condicionamento negativo a ser aumentado com as informações latentes de inpaint | CONDITIONING | Sim | - |
| `vae` | O modelo VAE usado para codificar a máscara e o vídeo mascarado no espaço latente | VAE | Sim | - |
| `video` | Quadros do vídeo fonte [T, H, W, 3] | IMAGE | Sim | - |
| `quadmask` | Quadmask pré-processada do VOIDQuadmaskPreprocess [T, H, W] | MASK | Sim | - |
| `width` | A largura para redimensionar o vídeo e a máscara (padrão: 672) | INT | Sim | 16 a MAX_RESOLUTION (passo: 8) |
| `height` | A altura para redimensionar o vídeo e a máscara (padrão: 384) | INT | Sim | 16 a MAX_RESOLUTION (passo: 8) |
| `length` | Número de quadros de pixel a processar. Para CogVideoX-Fun-V1.5 (patch_size_t=2), latent_t deve ser par — comprimentos que produzem latent_t ímpar são arredondados para baixo (ex.: 49 → 45) (padrão: 45) | INT | Sim | 1 a MAX_RESOLUTION (passo: 1) |
| `batch_size` | O tamanho do lote para o ruído latente de saída (padrão: 1) | INT | Sim | 1 a 64 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `positive` | O condicionamento positivo com as informações latentes de inpaint adicionadas | CONDITIONING |
| `negative` | O condicionamento negativo com as informações latentes de inpaint adicionadas | CONDITIONING |
| `latent` | Um tensor de ruído latente preenchido com zeros com formato [batch_size, 16, latent_t, latent_h, latent_w] | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDInpaintConditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a1fe36376d7930286c7a288f261dcf2961d6b13cc412d1a0d42af8a4f9ebeeaf`
