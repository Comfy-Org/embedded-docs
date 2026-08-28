# ModelSamplingContinuousV

O nó ModelSamplingContinuousV ajusta o comportamento de amostragem de um modelo aplicando amostragem contínua com previsão em V (V-prediction). Ele cria um clone do modelo de entrada e o configura com valores mínimo e máximo personalizados de sigma para um controle mais preciso sobre o processo de amostragem.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `modelo` | O modelo de entrada a ser modificado com amostragem contínua por previsão em V | MODEL | Sim | - |
| `amostragem` | O método de amostragem a ser aplicado; atualmente, a previsão em V é a única opção disponível (padrão: `"v_prediction"`) | COMBO | Sim | `"v_prediction"` |
| `sigma_máx` | O valor máximo de sigma para a amostragem (parâmetro avançado, padrão: 500.0) | FLOAT | Sim | 0.0 - 1000.0 |
| `sigma_mín` | O valor mínimo de sigma para a amostragem (parâmetro avançado, padrão: 0.03) | FLOAT | Sim | 0.0 - 1000.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `model` | O modelo modificado com amostragem contínua por previsão em V aplicada | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingContinuousV/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8549be9dd2375374c20da7c74a756a90285716db0e52fed8a1a2b753cd6d75fe`
