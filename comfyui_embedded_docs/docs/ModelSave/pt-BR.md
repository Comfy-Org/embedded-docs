# ModelSave

O nó ModelSave salva um MODEL no armazenamento do seu computador como um arquivo de checkpoint `.safetensors`. Ele grava o arquivo no diretório de saída do ComfyUI usando o prefixo de nome de arquivo que você fornece e incorpora informações de prompt do fluxo de trabalho e metadados do modelo ao arquivo salvo quando disponíveis.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo a ser salvo em disco | MODEL | Sim | - |
| `prefixo_do_arquivo` | O prefixo de nome de arquivo e caminho para o arquivo de modelo salvo (padrão: "diffusion_models/ComfyUI") | STRING | Sim | - |
| `prompt` | Informações de prompt do fluxo de trabalho (fornecidas automaticamente) | PROMPT | Não | - |
| `extra_pnginfo` | Metadados adicionais do fluxo de trabalho (fornecidos automaticamente) | EXTRA_PNGINFO | Não | - |

Nota: O nome do arquivo salvo é construído a partir do valor de `filename_prefix` seguido por um contador de cinco dígitos (por exemplo, `diffusion_models/ComfyUI_00001_.safetensors`). Se um arquivo com o mesmo prefixo já existir, o contador é incrementado para que o novo arquivo receba um nome exclusivo. Quando disponíveis, o prompt do fluxo de trabalho, metadados adicionais e informações da arquitetura do modelo (por exemplo, Stable Diffusion XL, SDXL Refiner, Stable Video Diffusion ou Stable Diffusion 3) são incorporados ao arquivo salvo. Se o salvamento de metadados estiver desativado pelas configurações de linha de comando do ComfyUI, o prompt e os metadados extras não são gravados no arquivo.

## Saídas

| Nome de Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| *None* | Este nó não retorna nenhum valor de saída | - |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSave/pt-BR.md)

---
**Source fingerprint (SHA-256):** `943e60f2c596d9cbcaabe95029fd9d443df5b61c6137736a8b1b81ab78f200ea`
