# Aumentar Resolução Latent Por

O nó LatentUpscaleBy é projetado para aumentar a escala de representações latentes de imagens. Ele permite ajustar o fator de escala e o método de ampliação, oferecendo flexibilidade para melhorar a resolução de amostras latentes.

## Entradas

| Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `amostras` | A representação latente das imagens a serem ampliadas. Este parâmetro é essencial para determinar os dados de entrada que passarão pelo processo de aumento de escala. | `LATENT` |
| `método_de_upscale` | Especifica o método utilizado para ampliar as amostras latentes. A escolha do método pode afetar significativamente a qualidade e as características da saída ampliada. | COMBO[STRING] |
| `escalar_por` | Determina o fator pelo qual as amostras latentes são escaladas. Este parâmetro influencia diretamente a resolução da saída, permitindo controle preciso sobre o processo de ampliação. | `FLOAT` |

## Saídas

| Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `latent` | A representação latente ampliada, pronta para processamento adicional ou tarefas de geração. Esta saída é essencial para melhorar a resolução de imagens geradas ou para operações subsequentes do modelo. | `LATENT` |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscaleBy/pt-BR.md)
