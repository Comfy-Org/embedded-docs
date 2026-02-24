> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SkipLayerGuidanceDiTSimple/pt-BR.md)

Versão simplificada do nó SkipLayerGuidanceDiT que modifica apenas a passagem incondicional durante o processo de remoção de ruído. Este nó aplica a orientação de camada de salto (skip layer guidance) a camadas específicas do transformador em modelos DiT (Diffusion Transformer), pulando seletivamente certas camadas durante a passagem incondicional com base em parâmetros de tempo e camada especificados.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo ao qual aplicar a orientação de camada de salto |
| `double_layers` | STRING | Sim | - | Lista separada por vírgulas dos índices das camadas de bloco duplo a serem puladas (padrão: "7, 8, 9") |
| `single_layers` | STRING | Sim | - | Lista separada por vírgulas dos índices das camadas de bloco simples a serem puladas (padrão: "7, 8, 9") |
| `start_percent` | FLOAT | Sim | 0.0 - 1.0 | A porcentagem inicial do processo de remoção de ruído quando a orientação de camada de salto começa (padrão: 0.0) |
| `end_percent` | FLOAT | Sim | 0.0 - 1.0 | A porcentagem final do processo de remoção de ruído quando a orientação de camada de salto para (padrão: 1.0) |

**Observação:** A orientação de camada de salto é aplicada apenas quando `double_layers` e `single_layers` contêm índices de camada válidos. Se ambos estiverem vazios, o nó retorna o modelo original inalterado.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | O modelo modificado com a orientação de camada de salto aplicada às camadas especificadas |
