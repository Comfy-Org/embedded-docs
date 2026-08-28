# Agendador de Amostragem Beta

O nó BetaSamplingScheduler gera uma sequência de níveis de ruído (sigmas) para o processo de amostragem usando um algoritmo de agendamento beta. Ele recebe um modelo e parâmetros de configuração para criar um agendamento de ruído personalizado que controla o processo de remoção de ruído durante a geração de imagens. Este agendador permite ajuste fino da trajetória de redução de ruído por meio dos parâmetros alpha e beta.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo usado para amostragem, que fornece o objeto de amostragem do modelo | MODEL | Sim | - |
| `etapas` | O número de etapas de amostragem para gerar sigmas (padrão: 20) | INT | Sim | 1 a 10000 |
| `alfa` | Parâmetro alfa para o agendador beta, controlando a curva de agendamento (padrão: 0.6, parâmetro avançado) | FLOAT | Sim | 0.0 a 50.0 |
| `beta` | Parâmetro beta para o agendador beta, controlando a curva de agendamento (padrão: 0.6, parâmetro avançado) | FLOAT | Sim | 0.0 a 50.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `SIGMAS` | Uma sequência de níveis de ruído (sigmas) usados no processo de amostragem | SIGMAS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BetaSamplingScheduler/pt-BR.md)

---
**Source fingerprint (SHA-256):** `80adae3cbedff7fe544a1fbcf638af7965f1216e422931063ecf67da53ddff95`
