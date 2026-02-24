> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CombineHooksEight/pt-BR.md)

O nó Combine Hooks [8] mescla até oito grupos de hooks diferentes em um único grupo de hooks combinado. Ele recebe múltiplas entradas de hooks e as combina usando a funcionalidade de combinação de hooks do ComfyUI. Isso permite consolidar múltiplas configurações de hooks para um processamento otimizado em fluxos de trabalho avançados.

## Entradas

| Parâmetro | Tipo de Dados | Tipo de Entrada | Padrão | Intervalo | Descrição |
|-----------|-----------|------------|---------|-------|-------------|
| `hooks_A` | HOOKS | opcional | None | - | Primeiro grupo de hooks a combinar |
| `hooks_B` | HOOKS | opcional | None | - | Segundo grupo de hooks a combinar |
| `hooks_C` | HOOKS | opcional | None | - | Terceiro grupo de hooks a combinar |
| `hooks_D` | HOOKS | opcional | None | - | Quarto grupo de hooks a combinar |
| `hooks_E` | HOOKS | opcional | None | - | Quinto grupo de hooks a combinar |
| `hooks_F` | HOOKS | opcional | None | - | Sexto grupo de hooks a combinar |
| `hooks_G` | HOOKS | opcional | None | - | Sétimo grupo de hooks a combinar |
| `hooks_H` | HOOKS | opcional | None | - | Oitavo grupo de hooks a combinar |

**Observação:** Todos os parâmetros de entrada são opcionais. O nó combinará apenas os grupos de hooks fornecidos, ignorando quaisquer que sejam deixados vazios. Você pode fornecer de um a oito grupos de hooks para combinação.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `HOOKS` | HOOKS | Um único grupo de hooks combinado contendo todas as configurações de hooks fornecidas |
