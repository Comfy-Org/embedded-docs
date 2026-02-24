> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SkipLayerGuidanceDiT/pt-BR.md)

Melhora a orientação para estruturas detalhadas usando outro conjunto de CFG negativo com camadas ignoradas. Esta versão genérica do SkipLayerGuidance pode ser usada em todos os modelos DiT e é inspirada no Perturbed Attention Guidance. A implementação experimental original foi criada para o SD3.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo ao qual aplicar a orientação de camada ignorada |
| `double_layers` | STRING | Sim | - | Números das camadas separados por vírgula para blocos duplos a serem ignorados (padrão: "7, 8, 9") |
| `single_layers` | STRING | Sim | - | Números das camadas separados por vírgula para blocos simples a serem ignorados (padrão: "7, 8, 9") |
| `scale` | FLOAT | Sim | 0.0 - 10.0 | Fator de escala da orientação (padrão: 3.0) |
| `start_percent` | FLOAT | Sim | 0.0 - 1.0 | Percentual inicial para aplicação da orientação (padrão: 0.01) |
| `end_percent` | FLOAT | Sim | 0.0 - 1.0 | Percentual final para aplicação da orientação (padrão: 0.15) |
| `rescaling_scale` | FLOAT | Sim | 0.0 - 10.0 | Fator de escala de reescalonamento (padrão: 0.0) |

**Observação:** Se tanto `double_layers` quanto `single_layers` estiverem vazios (não contiverem números de camada), o nó retorna o modelo original sem aplicar nenhuma orientação.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | O modelo modificado com a orientação de camada ignorada aplicada |
