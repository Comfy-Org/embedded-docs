# ModelSave

O nó ModelSave salva modelos treinados ou modificados no armazenamento do seu computador. Ele recebe um modelo como entrada e o grava em um arquivo de checkpoint safetensors na pasta de saída, usando o prefixo de nome de arquivo que você especificar. As informações de prompt do fluxo de trabalho e os metadados são incorporados ao arquivo salvo quando disponíveis.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model` | O modelo a ser salvo no disco | MODEL | Sim | - |
| `filename_prefix` | O prefixo de nome de arquivo e caminho para o arquivo de modelo salvo (padrão: "diffusion_models/ComfyUI"). Um contador é anexado ao nome ao salvar (por exemplo, `ComfyUI_00000_.safetensors`). | STRING | Sim | - |
| `prompt` | Informações de prompt do fluxo de trabalho (fornecidas automaticamente) | PROMPT | Não | - |
| `extra_pnginfo` | Metadados adicionais do fluxo de trabalho (fornecidos automaticamente) | EXTRA_PNGINFO | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| *Nenhum* | Este nó não retorna nenhum valor de saída | - |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSave/pt-BR.md)

---
**Source fingerprint (SHA-256):** `943e60f2c596d9cbcaabe95029fd9d443df5b61c6137736a8b1b81ab78f200ea`
