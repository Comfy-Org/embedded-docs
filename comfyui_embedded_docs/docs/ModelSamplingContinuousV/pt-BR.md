# ModelSamplingContinuousV

O nó ModelSamplingContinuousV modifica o comportamento de amostragem de um modelo ao aplicar parâmetros contínuos de amostragem V-prediction. Ele cria um clone do modelo de entrada e o configura com configurações personalizadas de faixa sigma para controle avançado de amostragem. Isso permite que os usuários ajustem finamente o processo de amostragem com valores sigma mínimos e máximos específicos.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model` | O modelo de entrada a ser modificado com amostragem contínua V-prediction | MODEL | Sim | - |
| `sampling` | O método de amostragem a ser aplicado. Apenas V-prediction é suportado atualmente. | COMBO | Sim | `"v_prediction"` |
| `sigma_max` | O valor sigma máximo para amostragem (padrão: 500.0) | FLOAT | Sim | 0.0 – 1000.0 (passo 0.001) |
| `sigma_min` | O valor sigma mínimo para amostragem (padrão: 0.03) | FLOAT | Sim | 0.0 – 1000.0 (passo 0.001) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo modificado com amostragem contínua V-prediction aplicada | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingContinuousV/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8549be9dd2375374c20da7c74a756a90285716db0e52fed8a1a2b753cd6d75fe`
