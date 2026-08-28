# LTXVScheduler

O nó LTXVScheduler gera valores de sigma para processos de amostragem personalizados. Ele calcula parâmetros de agendamento de ruído com base no número de tokens na entrada latente e aplica uma transformação sigmoide para criar o agendamento de amostragem. O nó pode opcionalmente esticar os sigmas resultantes para corresponder a um valor terminal especificado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `steps` | Número de passos de amostragem (padrão: 20) | INT | Sim | 1-10000 |
| `max_shift` | Valor máximo de deslocamento para o cálculo de sigma (padrão: 2.05) | FLOAT | Sim | 0.0-100.0 |
| `base_shift` | Valor base de deslocamento para o cálculo de sigma (padrão: 0.95) | FLOAT | Sim | 0.0-100.0 |
| `stretch` | Estica os sigmas para que fiquem no intervalo [terminal, 1] (padrão: True) | BOOLEAN | Sim | True/False |
| `terminal` | O valor terminal dos sigmas após o estiramento (padrão: 0.1) | FLOAT | Sim | 0.0-0.99 |
| `latent` | Entrada latente opcional usada para calcular a contagem de tokens para o ajuste de sigma | LATENT | Não | - |

**Observação:** O parâmetro `latent` é opcional. Quando não fornecido, o nó usa uma contagem padrão de 4096 tokens para os cálculos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `sigmas` | Valores de sigma gerados para o processo de amostragem | SIGMAS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVScheduler/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5b4907e905e27a951c332c400e24023ef089df7a5f4a17b1fc8ba42a41302399`
