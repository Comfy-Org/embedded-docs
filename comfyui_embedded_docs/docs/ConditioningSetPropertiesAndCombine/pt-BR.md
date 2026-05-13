> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetPropertiesAndCombine/pt-BR.md)

O nó **ConditioningSetPropertiesAndCombine** modifica dados de condicionamento aplicando propriedades de uma nova entrada de condicionamento a uma entrada de condicionamento existente. Ele combina os dois conjuntos de condicionamento enquanto controla a intensidade do novo condicionamento e especifica como a área de condicionamento deve ser aplicada.

## Entradas

| Parâmetro | Tipo de Dado | Tipo de Entrada | Padrão | Faixa | Descrição |
|-----------|--------------|-----------------|--------|-------|-----------|
| `cond` | CONDITIONING | Obrigatório | - | - | Os dados de condicionamento originais a serem modificados |
| `cond_NEW` | CONDITIONING | Obrigatório | - | - | Os novos dados de condicionamento que fornecem as propriedades a serem aplicadas |
| `strength` | FLOAT | Obrigatório | 1.0 | 0.0 - 10.0 | Controla a intensidade das novas propriedades de condicionamento |
| `set_cond_area` | STRING | Obrigatório | default | ["default", "mask bounds"] | Determina como a área de condicionamento é aplicada |
| `mask` | MASK | Opcional | - | - | Máscara opcional para definir áreas específicas para condicionamento |
| `hooks` | HOOKS | Opcional | - | - | Funções de hook opcionais para processamento personalizado |
| `timesteps` | TIMESTEPS_RANGE | Opcional | - | - | Faixa de timesteps opcional para controlar quando o condicionamento é aplicado |

**Observação:** Quando `mask` é fornecida, o parâmetro `set_cond_area` pode usar "mask bounds" para restringir a aplicação do condicionamento às regiões mascaradas.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `CONDITIONING` | CONDITIONING | Os dados de condicionamento combinados com propriedades modificadas |

---
**Source fingerprint (SHA-256):** `da57eeae428a103cbad77af063419ed0e85aeaa0b8805c8c197df27613477fa8`
