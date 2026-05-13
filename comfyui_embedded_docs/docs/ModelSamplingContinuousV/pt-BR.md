> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingContinuousV/pt-BR.md)

O nó ModelSamplingContinuousV modifica o comportamento de amostragem de um modelo aplicando parâmetros de amostragem de previsão V contínua. Ele cria um clone do modelo de entrada e o configura com configurações personalizadas de faixa sigma para controle avançado de amostragem. Isso permite que os usuários ajustem o processo de amostragem com valores sigma mínimo e máximo específicos.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|-----------|----------|-------|-------------|
| `modelo` | MODEL | Sim | - | O modelo de entrada a ser modificado com amostragem de previsão V contínua |
| `amostragem` | STRING | Sim | `"v_prediction"` | O método de amostragem a ser aplicado (atualmente apenas previsão V é suportada) |
| `sigma_máx` | FLOAT | Sim | 0.0 - 1000.0 | O valor sigma máximo para amostragem (padrão: 500.0) |
| `sigma_mín` | FLOAT | Sim | 0.0 - 1000.0 | O valor sigma mínimo para amostragem (padrão: 0.03) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `modelo` | MODEL | O modelo modificado com amostragem de previsão V contínua aplicada |

---
**Source fingerprint (SHA-256):** `8095b5024c0d33011f6a81ed496cf1711981701e0f35f9527646b150f5033d45`
