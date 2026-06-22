# Carregar Modelo de Upscale

Este nó detecta modelos localizados na pasta `ComfyUI/models/upscale_models` e também lê modelos de caminhos adicionais configurados no arquivo extra_model_paths.yaml. Às vezes, pode ser necessário **atualizar a interface do ComfyUI** para permitir que ele leia os arquivos de modelo da pasta correspondente.

O nó UpscaleModelLoader foi projetado para carregar modelos de upscale de um diretório especificado. Ele facilita a recuperação e preparação de modelos de upscale para tarefas de redimensionamento de imagens, garantindo que os modelos sejam carregados e configurados corretamente para avaliação.

## Entradas

| Campo | Descrição | Tipo Comfy |
| --- | --- | --- |
| `nome_modelo` | Especifica o nome do modelo de upscale a ser carregado, identificando e recuperando o arquivo de modelo correto do diretório de modelos de upscale. | `COMBO[STRING]` |

## Saídas

| Campo | Descrição | Tipo Comfy |
| --- | --- | --- |
| `upscale_model` | Retorna o modelo de upscale carregado e preparado, pronto para uso em tarefas de redimensionamento de imagens. | `UPSCALE_MODEL` |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UpscaleModelLoader/pt-BR.md)
