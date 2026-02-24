> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetDefaultAndCombine/pt-BR.md)

O nó PairConditioningSetDefaultAndCombine define valores de condicionamento padrão e os combina com os dados de condicionamento de entrada. Ele recebe entradas de condicionamento positivo e negativo, juntamente com suas contrapartes padrão, e então as processa através do sistema de *hooks* do ComfyUI para produzir saídas de condicionamento finais que incorporam os valores padrão.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sim | - | A entrada primária de condicionamento positivo a ser processada |
| `negative` | CONDITIONING | Sim | - | A entrada primária de condicionamento negativo a ser processada |
| `positive_DEFAULT` | CONDITIONING | Sim | - | Os valores padrão de condicionamento positivo a serem usados como *fallback* |
| `negative_DEFAULT` | CONDITIONING | Sim | - | Os valores padrão de condicionamento negativo a serem usados como *fallback* |
| `hooks` | HOOKS | Não | - | Grupo opcional de *hooks* para lógica de processamento personalizada |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | O condicionamento positivo processado com os valores padrão incorporados |
| `negative` | CONDITIONING | O condicionamento negativo processado com os valores padrão incorporados |
