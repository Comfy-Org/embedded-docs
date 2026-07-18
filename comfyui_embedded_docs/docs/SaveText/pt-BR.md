# SaveText

O nó Save Text escreve o conteúdo de texto em um arquivo no diretório de saída. Ele suporta a gravação em três formatos de arquivo diferentes: texto simples (.txt), Markdown (.md) e JSON (.json). Ao salvar como JSON, o nó tenta interpretar o texto de entrada como JSON válido e formatá-lo com indentação adequada.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|--------------|-------------|-------|
| `text` | O conteúdo de texto a ser salvo em um arquivo | STRING | Sim | |
| `filename_prefix` | Prefixo para o nome do arquivo de saída (padrão: "ComfyUI") | STRING | Não | |
| `format` | Formato do arquivo para salvar o texto (padrão: "txt") | STRING | Não | `"txt"`<br>`"md"`<br>`"json"` |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-------------|--------------|
| `text` | O conteúdo de texto original que foi salvo no arquivo | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveText/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5644d143f415773115b38d7af6d9afea20c9eadef2cea836b0384c15e0dcba6a`
