> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/unCLIPCheckpointLoader/pt-BR.md)

Este nó detectará modelos localizados na pasta `ComfyUI/models/checkpoints` e também lerá modelos de caminhos adicionais configurados no arquivo extra_model_paths.yaml. Às vezes, pode ser necessário **atualizar a interface do ComfyUI** para permitir que ela leia os arquivos de modelo da pasta correspondente.

O nó unCLIPCheckpointLoader é projetado para carregar checkpoints especificamente adaptados para modelos unCLIP. Ele facilita a recuperação e inicialização de modelos, módulos CLIP vision e VAEs a partir de um checkpoint especificado, agilizando o processo de configuração para operações ou análises posteriores.

## Entradas

| Campo       | Tipo Comfy     | Descrição                                                                       |
|-------------|----------------|-----------------------------------------------------------------------------------|
| `ckpt_name` | `COMBO[STRING]`| Especifica o nome do checkpoint a ser carregado, identificando e recuperando o arquivo de checkpoint correto de um diretório predefinido, determinando a inicialização dos modelos e configurações. |

## Saídas

| Campo        | Tipo Comfy    | Descrição                                                              | Tipo Python         |
|--------------|---------------|--------------------------------------------------------------------------|---------------------|
| `model`      | `MODEL`       | Representa o modelo principal carregado a partir do checkpoint.          | `torch.nn.Module`   |
| `clip`       | `CLIP`        | Representa o módulo CLIP carregado a partir do checkpoint, se disponível. | `torch.nn.Module`   |
| `vae`        | `VAE`         | Representa o módulo VAE carregado a partir do checkpoint, se disponível.  | `torch.nn.Module`   |
| `clip_vision`| `CLIP_VISION` | Representa o módulo CLIP vision carregado a partir do checkpoint, se disponível. | `torch.nn.Module`   |
