> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringConcatenate/pt-BR.md)

Esta documentação foi gerada por IA. Se encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringConcatenate/en.md)

O nó StringConcatenate combina duas strings de texto em uma só, unindo-as com um delimitador especificado. Ele recebe duas strings de entrada e um caractere ou string delimitador, e então gera uma única string onde as duas entradas são conectadas com o delimitador inserido entre elas.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `string_a` | STRING | Sim | - | A primeira string de texto a ser concatenada |
| `string_b` | STRING | Sim | - | A segunda string de texto a ser concatenada |
| `delimitador` | STRING | Não | - | O caractere ou string a ser inserido entre as duas strings de entrada (padrão: string vazia) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `output` | STRING | A string combinada com o delimitador inserido entre string_a e string_b |

---
**Source fingerprint (SHA-256):** `8e33665fb14a53f6c3bbfb6a4553ac7effa96d7d16d9ab2a9d4a1249abfc62e4`
