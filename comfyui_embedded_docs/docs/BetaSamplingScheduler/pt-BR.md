# Agendador de Amostragem Beta

O nó BetaSamplingScheduler cria uma sequência de níveis de ruído (sigmas) que controlam como o ruído é removido durante o processo de amostragem na geração de imagens. Ele usa um algoritmo de agendamento beta, e as configurações `alpha` e `beta` ajustam a forma do agendamento de ruído. Os sigmas gerados são passados para um amostrador para orientar o processo de remoção de ruído.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo usado para amostragem, que fornece o objeto de amostragem do modelo. | MODEL | Sim | - |
| `steps` | O número de etapas de amostragem para gerar sigmas (padrão: 20). | INT | Sim | 1 a 10000 |
| `alpha` | Parâmetro alfa para o agendador beta, controlando a curva de agendamento (padrão: 0.6). Parâmetro avançado. | FLOAT | Sim | 0.0 a 50.0 |
| `beta` | Parâmetro beta para o agendador beta, controlando a curva de agendamento (padrão: 0.6). Parâmetro avançado. | FLOAT | Sim | 0.0 a 50.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `SIGMAS` | Uma sequência de níveis de ruído (sigmas) usada para o processo de amostragem. | SIGMAS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BetaSamplingScheduler/pt-BR.md)

---
**Source fingerprint (SHA-256):** `80adae3cbedff7fe544a1fbcf638af7965f1216e422931063ecf67da53ddff95`
