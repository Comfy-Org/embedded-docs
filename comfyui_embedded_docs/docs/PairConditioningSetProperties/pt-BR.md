> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetProperties/pt-BR.md)

O nó **PairConditioningSetProperties** permite modificar propriedades de pares de condicionamento positivo e negativo simultaneamente. Ele aplica ajustes de intensidade, configurações de área de condicionamento e controles opcionais de máscara ou temporização a ambas as entradas de condicionamento, retornando os dados de condicionamento positivo e negativo modificados.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `positive_NEW` | CONDITIONING | Sim | - | A entrada de condicionamento positivo a ser modificada |
| `negative_NEW` | CONDITIONING | Sim | - | A entrada de condicionamento negativo a ser modificada |
| `strength` | FLOAT | Sim | 0.0 a 10.0 | O multiplicador de intensidade aplicado ao condicionamento (padrão: 1.0) |
| `set_cond_area` | STRING | Sim | "default"<br>"mask bounds" | Determina como a área de condicionamento é calculada (padrão: "default") |
| `mask` | MASK | Não | - | Máscara opcional para restringir a área de condicionamento |
| `hooks` | HOOKS | Não | - | Grupo opcional de hooks para modificações avançadas de condicionamento |
| `timesteps` | TIMESTEPS_RANGE | Não | - | Faixa opcional de timesteps para limitar quando o condicionamento é aplicado |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `positive` | CONDITIONING | O condicionamento positivo modificado com as propriedades aplicadas |
| `negative` | CONDITIONING | O condicionamento negativo modificado com as propriedades aplicadas |

---
**Source fingerprint (SHA-256):** `3f750c270665b4f3567790ab1ae0bdbfa176527d4f8d96cf10570a5c5deb9636`
