> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MergeTextLists/pt-BR.md)

Este nó mescla várias listas de texto em uma única lista combinada. Ele foi projetado para receber entradas de texto como listas e concatená-las. O nó registra o número total de textos na lista mesclada.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `texts` | STRING | Sim | N/A | As listas de texto a serem mescladas. Várias listas podem ser conectadas à entrada e serão concatenadas em uma única. |

**Observação:** Este nó está configurado como um processo de grupo (`is_group_process = True`), o que significa que ele lida automaticamente com múltiplas entradas de lista concatenando-as antes que a função principal de processamento seja executada.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `texts` | STRING | A lista única e mesclada contendo todos os textos de entrada. |
