# Pré-visualizar Mask

O nó MaskPreview exibe uma pré-visualização visual dos dados de máscara diretamente na interface do ComfyUI, sem salvá-los no diretório de saída. Isso permite inspecionar a máscara em qualquer ponto do seu fluxo de trabalho, enquanto a máscara também passa pelo nó sem alterações, para que possa continuar a ser usada nas etapas seguintes.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `mask` | Os dados de máscara a serem pré-visualizados | MASK | Sim | - |
| `filename_prefix` | Prefixo do nome de arquivo usado para a pré-visualização (padrão: "ComfyUI") | STRING | Não | - |
| `prompt` | Informações do prompt para metadados (fornecidas automaticamente) | PROMPT | Não | - |
| `extra_pnginfo` | Informações adicionais de PNG para metadados (fornecidas automaticamente) | EXTRA_PNGINFO | Não | - |

Apenas `mask` é uma entrada visível que precisa ser conectada. Os parâmetros `filename_prefix`, `prompt` e `extra_pnginfo` são fornecidos pelo sistema: `filename_prefix` usa seu valor padrão, enquanto `prompt` e `extra_pnginfo` são ocultos e fornecidos automaticamente pelo ambiente de execução do ComfyUI.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-----------|-----------|
| `mask` | Os mesmos dados de máscara que foram pré-visualizados, retornados sem alterações para que possam ser usados em outros pontos do fluxo de trabalho | MASK |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskPreview/pt-BR.md)

---
**Source fingerprint (SHA-256):** `fb7abe8cb6b5ac8a6a38e88ef90a146d16caf41d24c5de95309a94bc3c371d75`
