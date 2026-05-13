> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DiffControlNetLoader/pt-BR.md)

Este nó detecta modelos localizados na pasta `ComfyUI/models/controlnet` e também lê modelos de caminhos adicionais configurados no arquivo extra_model_paths.yaml. Às vezes, pode ser necessário **atualizar a interface do ComfyUI** para que ele leia os arquivos de modelo da pasta correspondente.

O nó DiffControlNetLoader foi projetado para carregar redes de controle diferenciais, que são modelos especializados capazes de modificar o comportamento de outro modelo com base em especificações de rede de controle. Este nó permite o ajuste dinâmico de comportamentos de modelos ao aplicar redes de controle diferenciais, facilitando a criação de saídas de modelo personalizadas.

## Entradas

| Campo              | Tipo Comfy        | Descrição                                                                                 |
|--------------------|-------------------|-------------------------------------------------------------------------------------------|
| `modelo`            | `MODEL`           | O modelo base ao qual a rede de controle diferencial será aplicada, permitindo a personalização do comportamento do modelo. |
| `control_net_name` | `COMBO[STRING]`   | Identifica a rede de controle diferencial específica a ser carregada e aplicada ao modelo base para modificar seu comportamento. |

## Saídas

| Campo         | Tipo Comfy    | Descrição                                                                   |
|---------------|---------------|-----------------------------------------------------------------------------|
| `control_net` | `CONTROL_NET` | Uma rede de controle diferencial que foi carregada e está pronta para ser aplicada a um modelo base para modificação de comportamento. |