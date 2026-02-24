> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15SuperResolution/pt-BR.md)

O nó HunyuanVideo15SuperResolution prepara dados de condicionamento para um processo de super-resolução de vídeo. Ele recebe uma representação latente de um vídeo e, opcionalmente, uma imagem inicial, e os empacota juntamente com dados de aumento de ruído e visão CLIP em um formato que pode ser usado por um modelo para gerar uma saída de maior resolução.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sim | N/A | A entrada de condicionamento positivo a ser modificada com dados latentes e de aumento. |
| `negative` | CONDITIONING | Sim | N/A | A entrada de condicionamento negativo a ser modificada com dados latentes e de aumento. |
| `vae` | VAE | Não | N/A | O VAE usado para codificar a `start_image` opcional. Obrigatório se `start_image` for fornecida. |
| `start_image` | IMAGE | Não | N/A | Uma imagem inicial opcional para orientar a super-resolução. Se fornecida, será ampliada e codificada no latente de condicionamento. |
| `clip_vision_output` | CLIP_VISION_OUTPUT | Não | N/A | Incorporações de visão CLIP opcionais para adicionar ao condicionamento. |
| `latent` | LATENT | Sim | N/A | A representação latente do vídeo de entrada que será incorporada ao condicionamento. |
| `noise_augmentation` | FLOAT | Não | 0.0 - 1.0 | A intensidade do aumento de ruído a ser aplicado ao condicionamento (padrão: 0.70). |

**Observação:** Se você fornecer uma `start_image`, também deverá conectar um `vae` para que ela seja codificada. A `start_image` será automaticamente ampliada para corresponder às dimensões implícitas do `latent` de entrada.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | O condicionamento positivo modificado, agora contendo o latente concatenado, o aumento de ruído e os dados opcionais de visão CLIP. |
| `negative` | CONDITIONING | O condicionamento negativo modificado, agora contendo o latente concatenado, o aumento de ruído e os dados opcionais de visão CLIP. |
| `latent` | LATENT | O latente de entrada é passado inalterado. |
