> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDInpaintConditioning/pt-BR.md)

O nó VOIDInpaintConditioning prepara os dados de condicionamento necessários para inpaint com modelos CogVideoX. Ele recebe um vídeo fonte e uma quadmask pré-processada, codifica-os através do VAE e os combina em um sinal de condicionamento de 32 canais que o modelo utiliza para preencher as áreas mascaradas.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sim | - | O condicionamento positivo a ser aumentado com as informações latentes de inpaint |
| `negative` | CONDITIONING | Sim | - | O condicionamento negativo a ser aumentado com as informações latentes de inpaint |
| `vae` | VAE | Sim | - | O modelo VAE usado para codificar a máscara e o vídeo mascarado no espaço latente |
| `video` | IMAGE | Sim | - | Quadros do vídeo fonte no formato [T, H, W, 3] |
| `quadmask` | MASK | Sim | - | Quadmask pré-processada do VOIDQuadmaskPreprocess no formato [T, H, W] |
| `width` | INT | Sim | 16 a MAX_RESOLUTION (passo: 8) | A largura para redimensionar o vídeo e a máscara (padrão: 672) |
| `height` | INT | Sim | 16 a MAX_RESOLUTION (passo: 8) | A altura para redimensionar o vídeo e a máscara (padrão: 384) |
| `length` | INT | Sim | 1 a MAX_RESOLUTION (passo: 1) | Número de quadros de pixel a processar. Para CogVideoX-Fun-V1.5 (patch_size_t=2), latent_t deve ser par — comprimentos que produzem latent_t ímpar são arredondados para baixo (ex.: 49 → 45) (padrão: 45) |
| `batch_size` | INT | Sim | 1 a 64 | O tamanho do lote para o ruído latente de saída (padrão: 1) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | O condicionamento positivo com as informações latentes de inpaint adicionadas |
| `negative` | CONDITIONING | O condicionamento negativo com as informações latentes de inpaint adicionadas |
| `latent` | LATENT | Um tensor de ruído latente preenchido com zeros com formato [batch_size, 16, latent_t, latent_h, latent_w] |