> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageOnlyCheckpointLoader/pt-BR.md)

Este nó detectará modelos localizados na pasta `ComfyUI/models/checkpoints` e também lerá modelos de caminhos adicionais configurados no arquivo extra_model_paths.yaml. Às vezes, pode ser necessário **atualizar a interface do ComfyUI** para permitir que ela leia os arquivos de modelo da pasta correspondente.

Este nó é especializado em carregar checkpoints especificamente para modelos baseados em imagem dentro de fluxos de trabalho de geração de vídeo. Ele recupera e configura de forma eficiente os componentes necessários de um checkpoint fornecido, com foco nos aspectos relacionados a imagem do modelo.

## Entradas

| Campo      | Tipo de Dados | Descrição                                                                       |
|------------|-------------|-----------------------------------------------------------------------------------|
| `ckpt_name`| COMBO[STRING] | Especifica o nome do checkpoint a ser carregado, crucial para identificar e recuperar o arquivo de checkpoint correto a partir de uma lista predefinida. |

## Saídas

| Campo     | Tipo de Dados | Descrição                                                                                   |
|-----------|-------------|-----------------------------------------------------------------------------------------------|
| `model`   | MODEL     | Retorna o modelo principal carregado do checkpoint, configurado para processamento de imagem em contextos de geração de vídeo. |
| `clip_vision` | `CLIP_VISION` | Fornece o componente de visão CLIP do checkpoint, adaptado para compreensão de imagem e extração de características. |
| `vae`     | VAE       | Fornece o componente de Autoencoder Variacional (VAE), essencial para tarefas de manipulação e geração de imagem. |
