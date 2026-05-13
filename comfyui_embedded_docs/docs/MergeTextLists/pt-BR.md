> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MergeTextLists/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MergeTextLists/en.md)

Este nó mescla múltiplas listas de texto em uma única lista combinada. Ele foi projetado para receber entradas de texto como listas e as concatena. O nó registra o número total de textos na lista mesclada.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `textos` | STRING | Sim | N/A | As listas de texto a serem mescladas. Múltiplas listas podem ser conectadas à entrada e serão concatenadas em uma única lista. |

**Observação:** Este nó é configurado como um processo de grupo (`is_group_process = True`), o que significa que ele gerencia automaticamente múltiplas entradas de lista, concatenando-as antes que a função principal de processamento seja executada.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `textos` | STRING | A única lista mesclada contendo todos os textos de entrada. |

---
**Source fingerprint (SHA-256):** `043a39a373d03f1ff79dd0746070171bab4d5d915c985e4e64fd35f802b09f69`
