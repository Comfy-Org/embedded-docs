Este nó detectará modelos localizados na pasta `ComfyUI/models/checkpoints` e também lerá modelos de caminhos adicionais configurados no arquivo extra_model_paths.yaml. Às vezes, pode ser necessário **atualizar a interface do ComfyUI** para que ele leia os arquivos de modelo da pasta correspondente.

O nó unCLIPCheckpointLoader foi projetado para carregar checkpoints especificamente adaptados para modelos unCLIP. Ele facilita a recuperação e inicialização de modelos, módulos CLIP vision e VAEs a partir de um checkpoint especificado, simplificando o processo de configuração para operações ou análises posteriores.

## Entradas

| Campo | Descrição | Tipo Comfy |
| --- | --- | --- |
| `ckpt_name` | Especifica o nome do checkpoint a ser carregado, identificando e recuperando o arquivo de checkpoint correto de um diretório predefinido, determinando a inicialização dos modelos e configurações. | `COMBO[STRING]` |

## Saídas

| Campo | Descrição | Tipo Comfy | Tipo Python |
| --- | --- | --- | --- |
| `model` | Representa o modelo principal carregado do checkpoint. | `MODEL` | `torch.nn.Module` |
| `clip` | Representa o módulo CLIP carregado do checkpoint, se disponível. | `CLIP` | `torch.nn.Module` |
| `vae` | Representa o módulo VAE carregado do checkpoint, se disponível. | `VAE` | `torch.nn.Module` |
| `clip_vision` | Representa o módulo CLIP vision carregado do checkpoint, se disponível. | `CLIP_VISION` | `torch.nn.Module` |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/unCLIPCheckpointLoader/pt-BR.md)
