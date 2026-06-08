O nó ModelSamplingContinuousV modifica o comportamento de amostragem de um modelo aplicando parâmetros de amostragem de previsão V contínua. Ele cria um clone do modelo de entrada e o configura com configurações personalizadas de faixa sigma para controle avançado de amostragem. Isso permite que os usuários ajustem o processo de amostragem com valores sigma mínimo e máximo específicos.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo de entrada a ser modificado com amostragem de previsão V contínua | MODEL | Sim | - |
| `amostragem` | O método de amostragem a ser aplicado (atualmente apenas previsão V é suportada) | STRING | Sim | `"v_prediction"` |
| `sigma_máx` | O valor sigma máximo para amostragem (padrão: 500.0) | FLOAT | Sim | 0.0 - 1000.0 |
| `sigma_mín` | O valor sigma mínimo para amostragem (padrão: 0.03) | FLOAT | Sim | 0.0 - 1000.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `modelo` | O modelo modificado com amostragem de previsão V contínua aplicada | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingContinuousV/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8095b5024c0d33011f6a81ed496cf1711981701e0f35f9527646b150f5033d45`
