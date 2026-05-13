> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CaseConverter/pt-BR.md)

O nó Case Converter transforma strings de texto em diferentes formatos de capitalização. Ele recebe uma string de entrada e a converte com base no modo selecionado, produzindo uma string de saída com a formatação de capitalização especificada. O nó oferece suporte a quatro opções diferentes de conversão de capitalização para modificar a formatação de maiúsculas e minúsculas do seu texto.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `string` | STRING | Sim | - | A string de texto a ser convertida para um formato de capitalização diferente |
| `mode` | STRING | Sim | `"UPPERCASE"`<br>`"lowercase"`<br>`"Capitalize"`<br>`"Title Case"` | O modo de conversão de capitalização a ser aplicado (padrão: `"UPPERCASE"`) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | STRING | A string de entrada convertida para o formato de capitalização especificado |

---
**Source fingerprint (SHA-256):** `2493daccd5bdd86ce3fb24c6658057f5e50c2d6ed7616785f40806826f9a60dc`
