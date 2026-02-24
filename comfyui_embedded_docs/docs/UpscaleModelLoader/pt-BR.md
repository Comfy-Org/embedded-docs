> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UpscaleModelLoader/pt-BR.md)

Este nó detectará modelos localizados na pasta `ComfyUI/models/upscale_models` e também lerá modelos de caminhos adicionais configurados no arquivo extra_model_paths.yaml. Às vezes, pode ser necessário **atualizar a interface do ComfyUI** para permitir que ela leia os arquivos de modelo da pasta correspondente.

O nó UpscaleModelLoader é projetado para carregar modelos de super-resolução (upscale) de um diretório especificado. Ele facilita a recuperação e preparação de modelos de upscale para tarefas de aumento de resolução de imagem, garantindo que os modelos sejam carregados e configurados corretamente para avaliação.

## Entradas

| Campo          | Tipo Comfy         | Descrição                                                                       |
|----------------|-------------------|-----------------------------------------------------------------------------------|
| `model_name`   | `COMBO[STRING]`    | Especifica o nome do modelo de upscale a ser carregado, identificando e recuperando o arquivo de modelo correto do diretório de modelos de upscale. |

## Saídas

| Campo            | Tipo Comfy         | Descrição                                                              |
|-------------------|---------------------|--------------------------------------------------------------------------|
| `upscale_model`  | `UPSCALE_MODEL`     | Retorna o modelo de upscale carregado e preparado, pronto para uso em tarefas de aumento de resolução de imagem. |
