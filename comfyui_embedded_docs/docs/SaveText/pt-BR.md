# SaveText

O nó Save Text grava o conteúdo de texto em um arquivo no diretório de saída. Ele suporta salvamento nos formatos .txt, .md ou .json e lida automaticamente com a formatação JSON pretty-printing quando um JSON válido é fornecido.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|--------------|-------------|-------|
| `text` | O conteúdo de texto a ser salvo em um arquivo | STRING | Sim | - |
| `filename_prefix` | Prefixo para o nome do arquivo de saída (padrão: "ComfyUI") | STRING | Não | - |
| `format` | O formato do arquivo para salvar o texto (padrão: "txt") | STRING | Não | `"txt"`<br>`"md"`<br>`"json"` |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-----------|--------------|
| `text` | O conteúdo de texto original que foi salvo no arquivo | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveText/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5644d143f415773115b38d7af6d9afea20c9eadef2cea836b0384c15e0dcba6a`
