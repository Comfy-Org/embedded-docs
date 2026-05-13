> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningTimestepsRange/pt-BR.md)

O nó **ConditioningTimestepsRange** cria três faixas de timesteps distintas para controlar quando os efeitos de condicionamento são aplicados durante o processo de geração. Ele recebe valores percentuais de início e fim e divide toda a faixa de timesteps (0.0 a 1.0) em três segmentos: a faixa principal entre os percentuais especificados, a faixa anterior ao percentual inicial e a faixa posterior ao percentual final.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `start_percent` | FLOAT | Sim | 0.0 - 1.0 | Percentual inicial da faixa de timesteps (padrão: 0.0) |
| `end_percent` | FLOAT | Sim | 0.0 - 1.0 | Percentual final da faixa de timesteps (padrão: 1.0) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `TIMESTEPS_RANGE` | TIMESTEPS_RANGE | A faixa principal de timesteps definida por start_percent e end_percent |
| `BEFORE_RANGE` | TIMESTEPS_RANGE | A faixa de timesteps de 0.0 até start_percent |
| `AFTER_RANGE` | TIMESTEPS_RANGE | A faixa de timesteps de end_percent até 1.0 |

---
**Source fingerprint (SHA-256):** `dee21b5ac80fabdeacf3f4a985550fff795702e02911400ae49a97baae834e5e`
