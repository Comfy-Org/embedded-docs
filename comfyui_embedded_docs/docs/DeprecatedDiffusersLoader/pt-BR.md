O nó **DiffusersLoader** é projetado para carregar modelos da biblioteca diffusers, lidando especificamente com o carregamento de modelos UNet, CLIP e VAE com base nos caminhos fornecidos. Ele facilita a integração desses modelos no framework ComfyUI, permitindo funcionalidades avançadas como geração de texto para imagem, manipulação de imagens e muito mais.

## Entradas

| Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `model_path` | Especifica o caminho para o modelo a ser carregado. Este caminho é crucial, pois determina qual modelo será utilizado nas operações subsequentes, afetando a saída e as capacidades do nó. | COMBO[STRING] |

## Saídas

| Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `model` | O modelo UNet carregado, que faz parte da tupla de saída. Este modelo é essencial para tarefas de síntese e manipulação de imagens no framework ComfyUI. | MODEL |
| `clip` | O modelo CLIP carregado, incluído na tupla de saída se solicitado. Este modelo permite capacidades avançadas de compreensão e manipulação de texto e imagem. | CLIP |
| `vae` | O modelo VAE carregado, incluído na tupla de saída se solicitado. Este modelo é crucial para tarefas que envolvem manipulação do espaço latente e geração de imagens. | VAE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DeprecatedDiffusersLoader/pt-BR.md)
