Este nó foi projetado para aumentar a resolução de imagens usando um modelo de upscale específico. Ele gerencia eficientemente o processo de upscaling, ajustando a imagem ao dispositivo apropriado, otimizando o uso de memória e aplicando o modelo de upscale em blocos para evitar possíveis erros de falta de memória.

## Entradas

| Parâmetro | Descrição | Tipo Comfy |
| --- | --- | --- |
| `modelo_upscale` | O modelo de upscale a ser usado para aumentar a resolução da imagem. É crucial para definir o algoritmo de upscale e seus parâmetros. | `UPSCALE_MODEL` |
| `imagem` | A imagem a ser ampliada. Esta entrada é essencial para determinar o conteúdo de origem que passará pelo processo de upscale. | `IMAGE` |

## Saídas

| Parâmetro | Descrição | Tipo de Dados |
| --- | --- | --- |
| `imagem` | A imagem ampliada, processada pelo modelo de upscale. Esta saída é o resultado da operação de upscale, exibindo a resolução ou qualidade aprimorada. | `IMAGE` |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageUpscaleWithModel/pt-BR.md)
