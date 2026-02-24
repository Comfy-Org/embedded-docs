> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EasyCache/pt-BR.md)

O nó EasyCache implementa um sistema de cache nativo para modelos, visando melhorar o desempenho ao reutilizar etapas previamente calculadas durante o processo de amostragem. Ele adiciona a funcionalidade EasyCache a um modelo com limites configuráveis para definir quando iniciar e parar de usar o cache durante a linha do tempo de amostragem.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo ao qual o EasyCache será adicionado. |
| `reuse_threshold` | FLOAT | Não | 0.0 - 3.0 | O limite para reutilizar etapas em cache (padrão: 0.2). |
| `start_percent` | FLOAT | Não | 0.0 - 1.0 | A etapa de amostragem relativa para iniciar o uso do EasyCache (padrão: 0.15). |
| `end_percent` | FLOAT | Não | 0.0 - 1.0 | A etapa de amostragem relativa para encerrar o uso do EasyCache (padrão: 0.95). |
| `verbose` | BOOLEAN | Não | - | Se deve registrar informações detalhadas (padrão: False). |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | O modelo com a funcionalidade EasyCache adicionada. |
