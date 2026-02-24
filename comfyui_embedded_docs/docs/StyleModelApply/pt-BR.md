> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StyleModelApply/pt-BR.md)

Este nó aplica um modelo de estilo a um condicionamento fornecido, aprimorando ou alterando seu estilo com base na saída de um modelo de visão CLIP. Ele integra o condicionamento do modelo de estilo ao condicionamento existente, permitindo uma fusão perfeita de estilos no processo de geração.

## Entradas

### Obrigatórias

| Parâmetro             | Tipo Comfy           | Descrição |
|-----------------------|-----------------------|-------------|
| `conditioning`        | `CONDITIONING`       | Os dados de condicionamento originais aos quais o condicionamento do modelo de estilo será aplicado. É crucial para definir o contexto ou estilo base que será aprimorado ou alterado. |
| `style_model`         | `STYLE_MODEL`        | O modelo de estilo usado para gerar um novo condicionamento com base na saída do modelo de visão CLIP. Tem um papel fundamental na definição do novo estilo a ser aplicado. |
| `clip_vision_output`  | `CLIP_VISION_OUTPUT` | A saída de um modelo de visão CLIP, que é usada pelo modelo de estilo para gerar um novo condicionamento. Fornece o contexto visual necessário para a aplicação do estilo. |

## Saídas

| Parâmetro            | Tipo Comfy           | Descrição |
|----------------------|-----------------------|-------------|
| `conditioning`       | `CONDITIONING`        | O condicionamento aprimorado ou alterado, incorporando a saída do modelo de estilo. Representa o condicionamento final, estilizado e pronto para processamento ou geração posterior. |
