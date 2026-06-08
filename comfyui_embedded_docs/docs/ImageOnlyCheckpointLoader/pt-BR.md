Este nó detecta modelos localizados na pasta `ComfyUI/models/checkpoints` e também lê modelos de caminhos adicionais configurados no arquivo extra_model_paths.yaml. Às vezes, pode ser necessário **atualizar a interface do ComfyUI** para que ele leia os arquivos de modelo da pasta correspondente.

Este nó é especializado em carregar checkpoints especificamente para modelos baseados em imagem em fluxos de trabalho de geração de vídeo. Ele recupera e configura eficientemente os componentes necessários de um determinado checkpoint, focando nos aspectos relacionados à imagem do modelo.

## Entradas

| Campo | Descrição | Tipo de Dado |
| --- | --- | --- |
| `nome_do_ckpt` | Especifica o nome do checkpoint a ser carregado, crucial para identificar e recuperar o arquivo de checkpoint correto de uma lista predefinida. | COMBO[STRING] |

## Saídas

| Campo | Descrição | Tipo de Dado |
| --- | --- | --- |
| `model` | Retorna o modelo principal carregado do checkpoint, configurado para processamento de imagem em contextos de geração de vídeo. | MODEL |
| `clip_vision` | Fornece o componente de visão CLIP do checkpoint, adaptado para compreensão de imagem e extração de características. | `CLIP_VISION` |
| `vae` | Entrega o componente do Autoencoder Variacional (VAE), essencial para tarefas de manipulação e geração de imagens. | VAE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageOnlyCheckpointLoader/pt-BR.md)
