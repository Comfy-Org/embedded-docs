Este nó foi projetado para processar e condicionar dados para uso em modelos StableZero123, focando na preparação da entrada em um formato específico que seja compatível e otimizado para esses modelos.

## Entradas

| Parâmetro | Descrição | Tipo Comfy |
| --- | --- | --- |
| `clip_vision` | Processa dados visuais para alinhar com os requisitos do modelo, melhorando a compreensão do contexto visual. | `CLIP_VISION` |
| `init_image` | Serve como a imagem inicial de entrada para o modelo, estabelecendo a linha de base para operações posteriores baseadas em imagem. | `IMAGE` |
| `vae` | Integra saídas do autoencoder variacional, facilitando a capacidade do modelo de gerar ou modificar imagens. | `VAE` |
| `width` | Especifica a largura da imagem de saída, permitindo redimensionamento dinâmico de acordo com as necessidades do modelo. | `INT` |
| `height` | Determina a altura da imagem de saída, possibilitando a personalização das dimensões de saída. | `INT` |
| `batch_size` | Controla o número de imagens processadas em um único lote, otimizando a eficiência computacional. | `INT` |
| `elevation` | Ajusta o ângulo de elevação para renderização de modelos 3D, aprimorando a compreensão espacial do modelo. | `FLOAT` |
| `azimuth` | Modifica o ângulo azimutal para visualização de modelos 3D, melhorando a percepção de orientação do modelo. | `FLOAT` |

## Saídas

| Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `positive` | Gera vetores de condicionamento positivo, auxiliando no reforço de características positivas do modelo. | `CONDITIONING` |
| `negative` | Produz vetores de condicionamento negativo, auxiliando o modelo a evitar certas características. | `CONDITIONING` |
| `latent` | Cria representações latentes, facilitando insights mais profundos do modelo sobre os dados. | `LATENT` |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Stablezero123Conditioning/pt-BR.md)
