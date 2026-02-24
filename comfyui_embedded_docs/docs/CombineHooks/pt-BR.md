> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CombineHooks/pt-BR.md)

O nó Combine Hooks [2] mescla dois grupos de hooks em um único grupo de hooks combinado. Ele recebe duas entradas de hook opcionais e as combina usando a funcionalidade de combinação de hooks do ComfyUI. Isso permite consolidar múltiplas configurações de hooks para um processamento mais eficiente.

## Entradas

| Parâmetro | Tipo de Dados | Tipo de Entrada | Padrão | Intervalo | Descrição |
|-----------|-----------|------------|---------|-------|-------------|
| `hooks_A` | HOOKS | Opcional | Nenhum | - | Primeiro grupo de hooks a ser combinado |
| `hooks_B` | HOOKS | Opcional | Nenhum | - | Segundo grupo de hooks a ser combinado |

**Observação:** Ambas as entradas são opcionais, mas pelo menos um grupo de hooks deve ser fornecido para o nó funcionar. Se apenas um grupo de hooks for fornecido, ele será retornado inalterado.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `hooks` | HOOKS | Grupo de hooks combinado contendo todos os hooks de ambos os grupos de entrada |
