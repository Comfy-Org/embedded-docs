# Salvar Texto

O nó Save Text grava conteúdo de texto em um arquivo no diretório de saída. Ele oferece suporte para salvar nos formatos .txt, .csv, .md ou .json e lida automaticamente com a formatação legível de JSON quando um JSON válido é fornecido.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `text` | O conteúdo de texto a ser salvo em um arquivo. Esta entrada deve ser conectada a partir de outro nó. | STRING | Sim | - |
| `filename_prefix` | Prefixo para o nome do arquivo de saída. Um contador de 5 dígitos é anexado para evitar sobrescrever arquivos existentes (padrão: "ComfyUI"). | STRING | Não | - |
| `format` | O formato de arquivo no qual salvar o texto (padrão: "txt"). Quando `"json"` é selecionado, texto JSON válido é formatado de forma legível com indentação de 2 espaços; caso contrário, o texto é salvo como está. | COMBO | Não | `"txt"`<br>`"csv"`<br>`"md"`<br>`"json"` |

### Notas

- `text` é uma entrada forçada e deve ser conectada a outro nó; não pode ser digitado diretamente.
- O arquivo salvo é nomeado `<filename_prefix>_<5-digit counter>.<extension>` e é gravado no diretório de saída do ComfyUI (em uma subpasta derivada do prefixo).
- Selecionar o formato `"json"` tenta analisar o texto como JSON. Se a análise for bem-sucedida, o conteúdo é gravado com formatação legível e indentação de 2 espaços; se a análise falhar, o texto bruto é gravado sem alterações.
- O nó reporta o arquivo salvo de volta à interface para que ele apareça junto com os outros arquivos de saída gerados.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-----------|-----------|
| `text` | O conteúdo de texto original que foi salvo no arquivo | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveText/pt-BR.md)

---
**Source fingerprint (SHA-256):** `09bd896cab770358132834892c1b37efd2ffa0cb0aa7b02b7ef91163331dc9b1`
