> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderModelOnly/pt-BR.md)

Este nó detectará modelos localizados na pasta `ComfyUI/models/loras` e também lerá modelos de caminhos adicionais configurados no arquivo extra_model_paths.yaml. Às vezes, pode ser necessário **atualizar a interface do ComfyUI** para permitir que ela leia os arquivos de modelo da pasta correspondente.

Este nó é especializado em carregar um modelo LoRA sem exigir um modelo CLIP, focando em aprimorar ou modificar um determinado modelo com base em parâmetros LoRA. Ele permite o ajuste dinâmico da intensidade do modelo por meio dos parâmetros LoRA, facilitando o controle refinado sobre o comportamento do modelo.

## Entradas

| Campo             | Tipo Comfy        | Descrição                                                                                   |
|-------------------|-------------------|-----------------------------------------------------------------------------------------------|
| `model`           | `MODEL`           | O modelo base para modificações, ao qual os ajustes LoRA serão aplicados.                   |
| `lora_name`       | `COMBO[STRING]`   | O nome do arquivo LoRA a ser carregado, especificando os ajustes a aplicar ao modelo.      |
| `strength_model`  | `FLOAT`           | Determina a intensidade dos ajustes LoRA, com valores mais altos indicando modificações mais fortes. |

## Saídas

| Campo   | Tipo de Dados | Descrição                                                              |
|---------|-------------|--------------------------------------------------------------------------|
| `model` | `MODEL`     | O modelo modificado com os ajustes LoRA aplicados, refletindo mudanças no comportamento ou capacidades do modelo. |
