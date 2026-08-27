# ModelSave

O nó ModelSave salva um modelo no armazenamento do seu computador como um arquivo de checkpoint `.safetensors`. Ele recebe um modelo como entrada e o grava no diretório de saída usando o prefixo de nome de arquivo que você especificar. Quando disponível, ele também incorpora informações do prompt do fluxo de trabalho e metadados adicionais no arquivo salvo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo a ser salvo no disco | MODEL | Sim | - |
| `prefixo_do_arquivo` | O prefixo do nome do arquivo e do caminho para o arquivo de modelo salvo (padrão: "diffusion_models/ComfyUI") | STRING | Sim | - |
| `prompt` | Informações do prompt do fluxo de trabalho (fornecidas automaticamente) | PROMPT | Não | - |
| `extra_pnginfo` | Metadados adicionais do fluxo de trabalho (fornecidos automaticamente) | EXTRA_PNGINFO | Não | - |

Nota: O nome do arquivo salvo é composto pelo valor de `filename_prefix` seguido por um contador de cinco dígitos (por exemplo, `diffusion_models/ComfyUI_00001_.safetensors`). Se já existir um arquivo com o mesmo prefixo, o contador é incrementado para que o novo arquivo tenha um nome exclusivo. Quando disponível, o prompt do fluxo de trabalho, os metadados adicionais e as informações de arquitetura do modelo são incorporados ao arquivo salvo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| *None* | Este nó não retorna nenhum valor de saída | - |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSave/pt-BR.md)

---
**Source fingerprint (SHA-256):** `943e60f2c596d9cbcaabe95029fd9d443df5b61c6137736a8b1b81ab78f200ea`
