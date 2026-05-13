> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplingPercentToSigma/pt-BR.md)

O nó SamplingPercentToSigma converte um valor percentual de amostragem para um valor sigma correspondente usando os parâmetros de amostragem do modelo. Ele recebe um valor percentual entre 0.0 e 1.0 e o mapeia para o valor sigma apropriado na programação de ruído do modelo, com opções para retornar o sigma calculado ou os valores sigma máximo/mínimo reais nos limites.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `model` | MODEL | Sim | - | O modelo contendo os parâmetros de amostragem usados para a conversão |
| `sampling_percent` | FLOAT | Sim | 0.0 a 1.0 | O percentual de amostragem a ser convertido para sigma (padrão: 0.0) |
| `return_actual_sigma` | BOOLEAN | Sim | - | Retorna o valor sigma real em vez do valor usado para verificações de intervalo. Isso afeta apenas resultados em 0.0 e 1.0. (padrão: Falso) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `sigma_value` | FLOAT | O valor sigma convertido correspondente ao percentual de amostragem de entrada |

---
**Source fingerprint (SHA-256):** `88ecea0528dfeff75248a8dfee8381e1f73d1a2d9ee3e7f8e37fef0f2b2499ec`
