> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CombineHooksFour/pt-BR.md)

O nó Combine Hooks [4] mescla até quatro grupos de hooks separados em um único grupo de hooks combinado. Ele aceita qualquer combinação das quatro entradas de hooks disponíveis e as combina usando o sistema de combinação de hooks do ComfyUI. Isso permite que você consolide múltiplas configurações de hooks para um processamento otimizado em fluxos de trabalho avançados.

## Entradas

| Parâmetro | Tipo de Dados | Tipo de Entrada | Padrão | Intervalo | Descrição |
|-----------|-----------|------------|---------|-------|-------------|
| `hooks_A` | HOOKS | opcional | None | - | Primeiro grupo de hooks a combinar |
| `hooks_B` | HOOKS | opcional | None | - | Segundo grupo de hooks a combinar |
| `hooks_C` | HOOKS | opcional | None | - | Terceiro grupo de hooks a combinar |
| `hooks_D` | HOOKS | opcional | None | - | Quarto grupo de hooks a combinar |

**Observação:** Todas as quatro entradas de hooks são opcionais. O nó combinará apenas os grupos de hooks que forem fornecidos e retornará um grupo de hooks vazio se nenhuma entrada estiver conectada.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `HOOKS` | HOOKS | Grupo de hooks combinado contendo todas as configurações de hooks fornecidas |
