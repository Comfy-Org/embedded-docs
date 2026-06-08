Este nó aplica um modelo de estilo a um condicionamento fornecido, aprimorando ou alterando seu estilo com base na saída de um modelo de visão CLIP. Ele integra o condicionamento do modelo de estilo ao condicionamento existente, permitindo uma mesclagem perfeita de estilos no processo de geração.

## Entradas

### Obrigatórias

| Parâmetro | Descrição | Tipo Comfy |
| --- | --- | --- |
| `condicionamento` | Os dados de condicionamento originais aos quais o condicionamento do modelo de estilo será aplicado. É essencial para definir o contexto base ou estilo que será aprimorado ou alterado. | `CONDITIONING` |
| `style_model` | O modelo de estilo usado para gerar novo condicionamento com base na saída do modelo de visão CLIP. Ele desempenha um papel fundamental na definição do novo estilo a ser aplicado. | `STYLE_MODEL` |
| `clip_vision_output` | A saída de um modelo de visão CLIP, que é usada pelo modelo de estilo para gerar novo condicionamento. Ela fornece o contexto visual necessário para a aplicação do estilo. | `CLIP_VISION_OUTPUT` |

## Saídas

| Parâmetro | Descrição | Tipo Comfy |
| --- | --- | --- |
| `condicionamento` | O condicionamento aprimorado ou alterado, incorporando a saída do modelo de estilo. Representa o condicionamento final estilizado, pronto para processamento ou geração adicional. | `CONDITIONING` |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StyleModelApply/pt-BR.md)
