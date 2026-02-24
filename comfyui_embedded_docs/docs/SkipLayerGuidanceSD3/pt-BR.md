> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SkipLayerGuidanceSD3/pt-BR.md)

O nó SkipLayerGuidanceSD3 aprimora a orientação para uma estrutura detalhada aplicando um conjunto adicional de orientação livre de classificador com camadas ignoradas. Esta implementação experimental é inspirada na Perturbed Attention Guidance e funciona ao contornar seletivamente certas camadas durante o processo de condicionamento negativo para melhorar os detalhes estruturais na saída gerada.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo ao qual aplicar a orientação de camada ignorada |
| `layers` | STRING | Sim | - | Lista separada por vírgulas dos índices das camadas a serem ignoradas (padrão: "7, 8, 9") |
| `scale` | FLOAT | Sim | 0.0 - 10.0 | A intensidade do efeito de orientação de camada ignorada (padrão: 3.0) |
| `start_percent` | FLOAT | Sim | 0.0 - 1.0 | O ponto de início da aplicação da orientação como uma porcentagem do total de passos (padrão: 0.01) |
| `end_percent` | FLOAT | Sim | 0.0 - 1.0 | O ponto final da aplicação da orientação como uma porcentagem do total de passos (padrão: 0.15) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | O modelo modificado com a orientação de camada ignorada aplicada |
