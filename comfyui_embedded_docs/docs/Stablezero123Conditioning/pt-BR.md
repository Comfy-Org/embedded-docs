> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Stablezero123Conditioning/pt-BR.md)

Este nó foi projetado para processar e condicionar dados para uso em modelos StableZero123, focando na preparação da entrada em um formato específico que seja compatível e otimizado para esses modelos.

## Entradas

| Parâmetro             | Tipo Comfy        | Descrição |
|-----------------------|--------------------|-------------|
| `clip_vision`         | `CLIP_VISION`      | Processa dados visuais para alinhar com os requisitos do modelo, melhorando a compreensão do contexto visual. |
| `init_image`          | `IMAGE`            | Serve como a imagem inicial de entrada para o modelo, estabelecendo a linha de base para operações posteriores baseadas em imagem. |
| `vae`                 | `VAE`              | Integra saídas do autoencoder variacional, facilitando a capacidade do modelo de gerar ou modificar imagens. |
| `width`               | `INT`              | Especifica a largura da imagem de saída, permitindo redimensionamento dinâmico de acordo com as necessidades do modelo. |
| `height`              | `INT`              | Determina a altura da imagem de saída, possibilitando a personalização das dimensões de saída. |
| `batch_size`          | `INT`              | Controla o número de imagens processadas em um único lote, otimizando a eficiência computacional. |
| `elevation`           | `FLOAT`            | Ajusta o ângulo de elevação para renderização de modelos 3D, aprimorando a compreensão espacial do modelo. |
| `azimuth`             | `FLOAT`            | Modifica o ângulo azimutal para visualização de modelos 3D, melhorando a percepção de orientação do modelo. |

## Saídas

| Parâmetro     | Tipo de Dado | Descrição |
|---------------|--------------|-------------|
| `positive`    | `CONDITIONING` | Gera vetores de condicionamento positivo, auxiliando no reforço de características positivas do modelo. |
| `negative`    | `CONDITIONING` | Produz vetores de condicionamento negativo, auxiliando o modelo a evitar certas características. |
| `latent`      | `LATENT`     | Cria representações latentes, facilitando insights mais profundos do modelo sobre os dados. |