# Pré-visualizar Mask

O nó MaskPreview exibe uma prévia visual dos dados de máscara diretamente na interface do ComfyUI, sem salvá-los no diretório de saída. Isso permite inspecionar os valores exatos da máscara em qualquer ponto do seu fluxo de trabalho.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-----------|--------------|-------------|-----------|
| `mask` | Os dados de máscara a serem pré-visualizados | MASK | Sim | - |
| `filename_prefix` | Prefixo para o nome do arquivo da prévia (padrão: "ComfyUI") | STRING | Não | - |
| `prompt` | Informações do prompt para metadados (fornecidas automaticamente) | PROMPT | Não | - |
| `extra_pnginfo` | Informações PNG adicionais para metadados (fornecidas automaticamente) | EXTRA_PNGINFO | Não | - |

As entradas `prompt` e `extra_pnginfo` são ocultas e fornecidas automaticamente pelo sistema do ComfyUI; você não precisa conectá-las manualmente.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-----------|--------------|
| `mask` | Os dados de máscara que foram pré-visualizados, retornados inalterados para uso posterior no fluxo de trabalho | MASK |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskPreview/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3d4ecb8cd90c3ecbe9d3cff8f782062c582c7190d9f0e0ed069cba114d4beac5`
