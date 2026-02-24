> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Sd4xupscaleConditioning/pt-BR.md)

Este nó é especializado em aprimorar a resolução de imagens por meio de um processo de super-resolução 4x, incorporando elementos de condicionamento para refinar a saída. Ele utiliza técnicas de difusão para aumentar a escala das imagens, permitindo o ajuste da razão de escala e da amplificação de ruído para afinar o processo de aprimoramento.

## Entradas

| Parâmetro            | Tipo Comfy         | Descrição |
|----------------------|--------------------|-------------|
| `images`             | `IMAGE`            | As imagens de entrada a serem ampliadas. Este parâmetro é crucial, pois influencia diretamente a qualidade e a resolução das imagens de saída. |
| `positive`           | `CONDITIONING`     | Elementos de condicionamento positivo que orientam o processo de ampliação em direção a atributos ou características desejadas nas imagens de saída. |
| `negative`           | `CONDITIONING`     | Elementos de condicionamento negativo que o processo de ampliação deve evitar, ajudando a direcionar a saída para longe de atributos ou características indesejadas. |
| `scale_ratio`        | `FLOAT`            | Determina o fator pelo qual a resolução da imagem é aumentada. Uma razão de escala maior resulta em uma imagem de saída maior, permitindo maior detalhe e clareza. |
| `noise_augmentation` | `FLOAT`            | Controla o nível de amplificação de ruído aplicado durante o processo de ampliação. Isso pode ser usado para introduzir variabilidade e melhorar a robustez das imagens de saída. |

## Saídas

| Parâmetro     | Tipo de Dados | Descrição |
|---------------|--------------|-------------|
| `positive`    | `CONDITIONING` | Os elementos de condicionamento positivo refinados resultantes do processo de ampliação. |
| `negative`    | `CONDITIONING` | Os elementos de condicionamento negativo refinados resultantes do processo de ampliação. |
| `latent`      | `LATENT`     | Uma representação latente gerada durante o processo de ampliação, que pode ser utilizada em processamentos posteriores ou no treinamento de modelos. |
