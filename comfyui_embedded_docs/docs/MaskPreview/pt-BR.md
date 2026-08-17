# Pré-visualizar Mask

O nó MaskPreview mostra uma prévia visual dos dados de máscara diretamente na interface do ComfyUI, para que você possa inspecionar máscaras durante seu fluxo de trabalho. Ele exibe a prévia sem salvá-la no diretório de saída do ComfyUI e repassa a máscara como saída.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `mask` | Os dados de máscara a serem pré-visualizados | MASK | Sim | - |
| `filename_prefix` | Prefixo para o nome do arquivo de saída (padrão: "ComfyUI") | STRING | Não | - |
| `prompt` | Informações do prompt para metadados (fornecidas automaticamente) | PROMPT | Não | - |
| `extra_pnginfo` | Informações PNG adicionais para metadados (fornecidas automaticamente) | EXTRA_PNGINFO | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `mask` | Os dados de máscara que foram pré-visualizados, repassados inalterados | MASK |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskPreview/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3d4ecb8cd90c3ecbe9d3cff8f782062c582c7190d9f0e0ed069cba114d4beac5`
