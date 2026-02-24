> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningTimestepsRange/pt-BR.md)

O nó ConditioningTimestepsRange cria três intervalos de timestep distintos para controlar quando os efeitos de condicionamento são aplicados durante o processo de geração. Ele recebe valores percentuais de início e fim e divide todo o intervalo de timestep (0.0 a 1.0) em três segmentos: o intervalo principal entre as porcentagens especificadas, o intervalo antes da porcentagem inicial e o intervalo após a porcentagem final.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `start_percent` | FLOAT | Sim | 0.0 - 1.0 | A porcentagem inicial do intervalo de timestep (padrão: 0.0) |
| `end_percent` | FLOAT | Sim | 0.0 - 1.0 | A porcentagem final do intervalo de timestep (padrão: 1.0) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `TIMESTEPS_RANGE` | TIMESTEPS_RANGE | O intervalo principal de timestep definido por `start_percent` e `end_percent` |
| `BEFORE_RANGE` | TIMESTEPS_RANGE | O intervalo de timestep de 0.0 até `start_percent` |
| `AFTER_RANGE` | TIMESTEPS_RANGE | O intervalo de timestep de `end_percent` até 1.0 |
