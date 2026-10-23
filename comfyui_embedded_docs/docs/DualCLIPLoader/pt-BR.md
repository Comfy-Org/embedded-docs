# Carregador DualCLIP

O nó DualCLIPLoader foi projetado para carregar dois modelos CLIP simultaneamente, facilitando operações que exigem a integração ou comparação de características de ambos os modelos.

Este nó detectará modelos localizados na pasta `ComfyUI/models/text_encoders`.

## Entradas

| Parâmetro | Descrição | Tipo Comfy |
| --- | --- | --- |
| `clip_nome1` | Especifica o nome do primeiro modelo CLIP a ser carregado. Este parâmetro é crucial para identificar e recuperar o modelo correto de uma lista predefinida de modelos CLIP disponíveis. | COMBO[STRING] |
| `clip_nome2` | Especifica o nome do segundo modelo CLIP a ser carregado. Este parâmetro permite o carregamento de um segundo modelo CLIP distinto para análise comparativa ou integrativa junto ao primeiro. | COMBO[STRING] |
| `tipo` | Escolha entre "sdxl", "sd3", "flux" para se adaptar a diferentes modelos. | `option` |

* A ordem de carregamento não afeta o resultado final

## Saídas

| Parâmetro | Descrição | Tipo de Dados |
| --- | --- | --- |
| `clip` | A saída é um modelo CLIP combinado que integra as características ou funcionalidades dos dois modelos CLIP especificados. | CLIP |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCLIPLoader/pt-BR.md)
