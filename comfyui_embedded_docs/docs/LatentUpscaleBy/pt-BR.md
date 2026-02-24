> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscaleBy/pt-BR.md)

O nó LatentUpscaleBy é projetado para aumentar a escala (upscaling) de representações latentes de imagens. Ele permite ajustar o fator de escala e o método de aumento, oferecendo flexibilidade para aprimorar a resolução de amostras latentes.

## Entradas

| Parâmetro     | Tipo de Dados | Descrição |
|---------------|--------------|-------------|
| `samples`     | `LATENT`     | A representação latente das imagens a serem aumentadas. Este parâmetro é crucial para determinar os dados de entrada que passarão pelo processo de aumento de escala. |
| `upscale_method` | COMBO[STRING] | Especifica o método usado para aumentar a escala das amostras latentes. A escolha do método pode afetar significativamente a qualidade e as características da saída resultante. |
| `scale_by`    | `FLOAT`      | Determina o fator pelo qual as amostras latentes são dimensionadas. Este parâmetro influencia diretamente a resolução da saída, permitindo um controle preciso sobre o processo de aumento de escala. |

## Saídas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | A representação latente com a escala aumentada, pronta para processamento adicional ou tarefas de geração. Esta saída é essencial para aprimorar a resolução de imagens geradas ou para operações subsequentes do modelo. |
