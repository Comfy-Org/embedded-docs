> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LazyCache/pt-BR.md)

LazyCache é uma versão caseira do EasyCache que oferece uma implementação ainda mais simples. Ele funciona com qualquer modelo no ComfyUI e adiciona funcionalidade de cache para reduzir a computação durante a amostragem. Embora geralmente tenha desempenho inferior ao EasyCache, pode ser mais eficaz em alguns casos raros e oferece compatibilidade universal.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo ao qual adicionar o LazyCache. |
| `reuse_threshold` | FLOAT | Não | 0.0 - 3.0 | O limite para reutilizar etapas em cache (padrão: 0.2). |
| `start_percent` | FLOAT | Não | 0.0 - 1.0 | A etapa de amostragem relativa para começar a usar o LazyCache (padrão: 0.15). |
| `end_percent` | FLOAT | Não | 0.0 - 1.0 | A etapa de amostragem relativa para parar de usar o LazyCache (padrão: 0.95). |
| `verbose` | BOOLEAN | Não | - | Se deve registrar informações detalhadas (padrão: False). |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | O modelo com a funcionalidade LazyCache adicionada. |
