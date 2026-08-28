# Salvar Texto

O nó Save Text grava conteúdo de texto em um arquivo no diretório de saída. Ele oferece suporte a salvar nos formatos .txt, .csv, .md ou .json e lida automaticamente com a formatação JSON (pretty-printing) quando um JSON válido é fornecido.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-----------|---------------|-------------|-----------|
| `text` | O conteúdo de texto a ser salvo em um arquivo. Esta entrada deve ser conectada a partir de outro nó. | STRING | Sim | - |
| `filename_prefix` | Prefixo para o nome do arquivo de saída. Um contador de 5 dígitos é acrescentado para evitar a sobrescrita de arquivos existentes (padrão: "ComfyUI"). | STRING | Não | - |
| `format` | O formato de arquivo no qual salvar o texto (padrão: "txt"). Quando "json" é selecionado, texto JSON válido é formatado com indentação de 2 espaços; caso contrário, o texto é salvo como está. | COMBO | Não | `"txt"`<br>`"csv"`<br>`"md"`<br>`"json"` |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-----------|---------------|
| `text` | O conteúdo de texto original que foi salvo no arquivo | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveText/pt-BR.md)

---
**Source fingerprint (SHA-256):** `09bd896cab770358132834892c1b37efd2ffa0cb0aa7b02b7ef91163331dc9b1`
