O nó **ConditioningSetPropertiesAndCombine** modifica dados de condicionamento aplicando propriedades de uma nova entrada de condicionamento a uma entrada de condicionamento existente. Ele combina os dois conjuntos de condicionamento enquanto controla a intensidade do novo condicionamento e especifica como a área de condicionamento deve ser aplicada.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Tipo de Entrada | Padrão | Faixa |
| --- | --- | --- | --- | --- | --- |
| `cond` | Os dados de condicionamento originais a serem modificados | CONDITIONING | Obrigatório | - | - |
| `cond_NOVO` | Os novos dados de condicionamento que fornecem as propriedades a serem aplicadas | CONDITIONING | Obrigatório | - | - |
| `força` | Controla a intensidade das novas propriedades de condicionamento | FLOAT | Obrigatório | 1.0 | 0.0 - 10.0 |
| `definir_área_cond` | Determina como a área de condicionamento é aplicada | STRING | Obrigatório | default | ["default", "mask bounds"] |
| `mask` | Máscara opcional para definir áreas específicas para condicionamento | MASK | Opcional | - | - |
| `ganchos` | Funções de hook opcionais para processamento personalizado | HOOKS | Opcional | - | - |
| `etapas_de_tempo` | Faixa de timesteps opcional para controlar quando o condicionamento é aplicado | TIMESTEPS_RANGE | Opcional | - | - |

**Observação:** Quando `mask` é fornecida, o parâmetro `set_cond_area` pode usar "mask bounds" para restringir a aplicação do condicionamento às regiões mascaradas.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `CONDITIONING` | Os dados de condicionamento combinados com propriedades modificadas | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetPropertiesAndCombine/pt-BR.md)

---
**Source fingerprint (SHA-256):** `da57eeae428a103cbad77af063419ed0e85aeaa0b8805c8c197df27613477fa8`
