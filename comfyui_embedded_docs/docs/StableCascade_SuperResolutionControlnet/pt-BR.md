> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_SuperResolutionControlnet/pt-BR.md)

O nó StableCascade_SuperResolutionControlnet prepara as entradas para o processamento de super-resolução do Stable Cascade. Ele recebe uma imagem de entrada e a codifica usando um VAE para criar a entrada do controlnet, enquanto também gera representações latentes de espaço reservado para o estágio C e o estágio B do pipeline do Stable Cascade.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sim | - | A imagem de entrada a ser processada para super-resolução |
| `vae` | VAE | Sim | - | O modelo VAE usado para codificar a imagem de entrada |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `controlnet_input` | IMAGE | A representação da imagem codificada adequada para a entrada do controlnet |
| `stage_c` | LATENT | Representação latente de espaço reservado para o estágio C do processamento do Stable Cascade |
| `stage_b` | LATENT | Representação latente de espaço reservado para o estágio B do processamento do Stable Cascade |
