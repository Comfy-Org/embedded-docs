O nó UNetTemporalAttentionMultiply aplica fatores de multiplicação a diferentes tipos de mecanismos de atenção em um modelo UNet temporal. Ele modifica o modelo ajustando os pesos das camadas de autoatenção e atenção cruzada, distinguindo entre componentes estruturais e temporais. Isso permite ajustar finamente o quanto cada tipo de atenção influencia a saída do modelo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo de entrada a ser modificado com multiplicadores de atenção | MODEL | Sim | - |
| `auto_estrutural` | Multiplicador para componentes estruturais de autoatenção (padrão: 1.0) | FLOAT | Não | 0.0 - 10.0 |
| `auto_temporal` | Multiplicador para componentes temporais de autoatenção (padrão: 1.0) | FLOAT | Não | 0.0 - 10.0 |
| `cruzado_estrutural` | Multiplicador para componentes estruturais de atenção cruzada (padrão: 1.0) | FLOAT | Não | 0.0 - 10.0 |
| `cruzado_temporal` | Multiplicador para componentes temporais de atenção cruzada (padrão: 1.0) | FLOAT | Não | 0.0 - 10.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `modelo` | O modelo modificado com pesos de atenção ajustados | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNetTemporalAttentionMultiply/pt-BR.md)

---
**Source fingerprint (SHA-256):** `98d62fb28a0cdf62154ae4e0b672b3a7bcb9ed61186a164a43992263c1f9439a`
