# SamplingPercentToSigma

O nó SamplingPercentToSigma converte um valor de porcentagem de amostragem em um valor sigma correspondente, usando os parâmetros de amostragem do modelo. Ele recebe um valor percentual entre 0.0 e 1.0 e o mapeia para o valor sigma apropriado na programação de ruído do modelo, com opções para retornar o sigma calculado ou os valores sigma máximos/mínimos reais nos limites.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo que contém os parâmetros de amostragem usados para a conversão | MODEL | Sim | - |
| `sampling_percent` | A porcentagem de amostragem a ser convertida em sigma (padrão: 0.0) | FLOAT | Sim | 0.0 a 1.0 (passo: 0.0001) |
| `return_actual_sigma` | Retorna o valor sigma real em vez do valor usado para verificações de intervalo. Isso afeta apenas os resultados em 0.0 e 1.0. (padrão: False) | BOOLEAN | Sim | - |

Quando `return_actual_sigma` está habilitado, um `sampling_percent` de 0.0 retorna o valor sigma máximo do modelo (`sigma_max`), e um `sampling_percent` de 1.0 retorna o valor sigma mínimo (`sigma_min`). Para todas as outras porcentagens, o resultado é o mesmo independentemente de a opção estar habilitada ou não.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `sigma_value` | O valor sigma convertido correspondente à porcentagem de amostragem de entrada | FLOAT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplingPercentToSigma/pt-BR.md)

---
**Source fingerprint (SHA-256):** `30decf1d4804accbdf2a70eba1a773b41ef0e09cfb74f2a9388044dadf0a1ac1`
