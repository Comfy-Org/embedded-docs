> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNetTemporalAttentionMultiply/pt-BR.md)

O nó UNetTemporalAttentionMultiply aplica fatores de multiplicação a diferentes tipos de mecanismos de atenção em um modelo UNet temporal. Ele modifica o modelo ajustando os pesos das camadas de auto-atenção e atenção cruzada, distinguindo entre componentes estruturais e temporais. Isso permite um ajuste fino de quanto influência cada tipo de atenção tem na saída do modelo.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo de entrada a ser modificado com os multiplicadores de atenção |
| `self_structural` | FLOAT | Não | 0.0 - 10.0 | Multiplicador para os componentes estruturais da auto-atenção (padrão: 1.0) |
| `self_temporal` | FLOAT | Não | 0.0 - 10.0 | Multiplicador para os componentes temporais da auto-atenção (padrão: 1.0) |
| `cross_structural` | FLOAT | Não | 0.0 - 10.0 | Multiplicador para os componentes estruturais da atenção cruzada (padrão: 1.0) |
| `cross_temporal` | FLOAT | Não | 0.0 - 10.0 | Multiplicador para os componentes temporais da atenção cruzada (padrão: 1.0) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | O modelo modificado com os pesos de atenção ajustados |
