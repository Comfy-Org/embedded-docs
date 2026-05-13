> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointSave/pt-BR.md)

O nó `Save Checkpoint` foi projetado para salvar um modelo completo de Difusão Estável (incluindo componentes UNet, CLIP e VAE) como um arquivo de checkpoint no formato **.safetensors**.

O Save Checkpoint é usado principalmente em fluxos de trabalho de mesclagem de modelos. Após criar um novo modelo mesclado através de nós como `ModelMergeSimple`, `ModelMergeBlocks`, etc., você pode usar este nó para salvar o resultado como um arquivo de checkpoint reutilizável.

## Entradas

| Parâmetro | Tipo de Dado | Descrição |
|-----------|--------------|-----------|
| `modelo` | MODEL | O parâmetro `modelo` representa o modelo principal cujo estado será salvo. É essencial para capturar o estado atual do modelo para restauração ou análise futura. |
| `clip` | CLIP | O parâmetro `clip` é destinado ao modelo CLIP associado ao modelo principal, permitindo que seu estado seja salvo junto com o modelo principal. |
| `vae` | VAE | O parâmetro `vae` é para o modelo Autoencoder Variacional (VAE), permitindo que seu estado seja salvo para uso ou análise futura junto com o modelo principal e o CLIP. |
| `prefixo_nome_arquivo` | STRING | Este parâmetro especifica o prefixo para o nome do arquivo sob o qual o checkpoint será salvo. |

Além disso, o nó possui duas entradas ocultas para metadados:

**prompt (PROMPT)**: Informações do prompt do fluxo de trabalho
**extra_pnginfo (EXTRA_PNGINFO)**: Informações adicionais de PNG

## Saídas

Este nó irá gerar um arquivo de checkpoint, e o caminho do arquivo de saída correspondente é o diretório `output/checkpoints/`

## Compatibilidade de Arquitetura

- **Suporte total atualmente**: SDXL, SD3, SVD e outras arquiteturas principais, consulte o [código-fonte](https://github.com/comfyanonymous/ComfyUI/blob/master/comfy_extras/nodes_model_merging.py#L176-L189)
- **Suporte básico**: Outras arquiteturas podem ser salvas, mas sem informações padronizadas de metadados

## Links Relacionados

Código-fonte relacionado: [nodes_model_merging.py#L227](https://github.com/comfyanonymous/ComfyUI/blob/master/comfy_extras/nodes_model_merging.py#L227)