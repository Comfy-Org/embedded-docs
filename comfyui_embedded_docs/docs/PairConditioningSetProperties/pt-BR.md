O nó **PairConditioningSetProperties** permite modificar propriedades de pares de condicionamento positivo e negativo simultaneamente. Ele aplica ajustes de intensidade, configurações de área de condicionamento e controles opcionais de máscara ou temporização a ambas as entradas de condicionamento, retornando os dados de condicionamento positivo e negativo modificados.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `positivo_NOVO` | A entrada de condicionamento positivo a ser modificada | CONDITIONING | Sim | - |
| `negativo_NOVO` | A entrada de condicionamento negativo a ser modificada | CONDITIONING | Sim | - |
| `força` | O multiplicador de intensidade aplicado ao condicionamento (padrão: 1.0) | FLOAT | Sim | 0.0 a 10.0 |
| `definir_área_cond` | Determina como a área de condicionamento é calculada (padrão: "default") | STRING | Sim | "default"<br>"mask bounds" |
| `máscara` | Máscara opcional para restringir a área de condicionamento | MASK | Não | - |
| `ganchos` | Grupo opcional de hooks para modificações avançadas de condicionamento | HOOKS | Não | - |
| `etapas` | Faixa opcional de timesteps para limitar quando o condicionamento é aplicado | TIMESTEPS_RANGE | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `positive` | O condicionamento positivo modificado com as propriedades aplicadas | CONDITIONING |
| `negative` | O condicionamento negativo modificado com as propriedades aplicadas | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetProperties/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3f750c270665b4f3567790ab1ae0bdbfa176527d4f8d96cf10570a5c5deb9636`
